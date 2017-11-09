"""
These classes are parser for scraping each pages.
I recommend to naming follow the pattern of {object_name}{sub_object}PageParser
for easy to use.
"""
import lxml.html
from lxml.html import tostring
import html
import json
import re
from . import errors


class Parser(object):
    """
    Parent class for PageParsers.
    """
    def __init__(self, html_text):
        self.html_text = html_text
        if self.__detect_end():
            raise errors.ProjectPageEndException("プロジェクトが終わってます")
        elif self.__detect_will_be_published():
            raise errors.ProjectPageNotPublishedException("プロジェクトがまだ公開されていません")

    def parse(self):
        """
        :return: Attribute object of page information.
        :rtype: AttrDict
        """

        page_dict = self.page_parser()
        return page_dict

    def page_parser(self):
        pass

    def __detect_end(self):
        title_pattern = r"<title>\n(.*)\n</title>"
        error_title_pattern = '    こちらのプロジェクトの掲載は終了いたしました - クラウドファンディング - Readyfor（レディーフォー）'
        matches = re.finditer(title_pattern, self.html_text)
        title = ""
        for match in matches:
            title = match.groups()[0]
        if title == error_title_pattern:
            return True
        else:
            return False

    def __detect_will_be_published(self):
        will_be_published_text = "COMING SOON!"
        message_text = ""
        message_pattern = r'<div class="message">\n.*<h2>(.*)</h2>\n'
        text_matches = re.finditer(message_pattern, self.html_text)
        for match in text_matches:
            message_text = match.groups()[0]
        if message_text == will_be_published_text:
            return True
        else:
            return False


class ProjectPageParser(Parser):

    def page_parser(self):
        project_dict = self.__project_json_getter()
        project_dict["project"].update(self.__project_tab_parser())
        project_dict["project"].update(self.__project_deadline_parser())
        project_dict["project"].update(self.__project_text_parser())
        return project_dict["project"]

    def __project_json_getter(self):
        react_props_pattern = r'<div data-react-class="PcLikeBtn" data-react-props="(.*)"></div></div><section>'
        props_matches = re.finditer(react_props_pattern, self.html_text)
        project_json = ""
        for match in props_matches:
            project_json = match.groups()[0].replace('&quot;', '"')
        return json.loads(project_json)

    def __project_tab_parser(self):
        html = lxml.html.fromstring(self.html_text)

        root = html.body.xpath('/*')[0]
        _site_container = "div[@class='Site-container']"
        _article = 'article'
        _project_visual_container = "div[@class='Project-visual Container u-mb_20 u-clrfix']"
        _tab_wrapper = 'div[@class="tab-wrapper"]'
        _tab_menu = 'div[@class="Tab__menu tabnav-tabs"]'
        _tabnav_tabs = 'nav[@class="tabnav-tabs"]'
        tab_menus = ""
        try:
            tab_menus = \
                root. \
                body. \
                find(_site_container).\
                find(_article). \
                find(_project_visual_container).\
                find(_tab_wrapper).\
                find(_tab_menu).\
                find(_tabnav_tabs).\
                findall("a")
        except:
            return {"news_update_count": -1, "comments_count": -1}

        tab_items = {}
        for tab_menu in tab_menus:
            if tab_menu.find("span") is not None:
                if tab_menu.find("span").text == "新着情報":
                    update_count = tab_menu.find("span[@class='Tab__menu-icon Icon-num']").text
                    tab_items.update({"news_update_count": int(update_count)})
                elif tab_menu.find("span").text == "応援コメント":
                    comments_count = tab_menu.find("span[@class='Tab__menu-icon Icon-num']").text
                    tab_items.update({"comments_count": int(comments_count)})
        return tab_items

    def __project_deadline_parser(self):
        regexp_time_suc = r'<div class="Project-visual__alert is-complete u-mt_15 u-mb_20"><span class="u-fs_18 u-font_b">プロジェクトが成立しました！<\/span><br \/><span class="u-fs_14">このプロジェクトは<br \/> (.+?)年(.+?)月(.+?)日\((.+?)\)(.+?):(.+?) に成立しました。<\/span><\/div>'
        regexp_time_fail = r'<div class="Project-visual__alert is-miss u-mt_15 u-mb_20"><span class="u-fs_14">このプロジェクトは<br \/> (.+?)年(.+?)月(.+?)日\((.+?)\) (.+?):(.+?) に支援募集を締め切りました。<\/span><\/div>'
        success_page_matches = re.finditer(regexp_time_suc, self.html_text)
        failed_page_matches = re.finditer(regexp_time_fail, self.html_text)
        success_date = None
        failed_date = None

        for match in success_page_matches:
            if len(match.groups()) < 1:
                break
            success_date = '-'.join(match.groups()[0:3])
        for match in failed_page_matches:
            if len(match.groups()) < 1:
                break
            failed_date = '-'.join(match.groups()[0:3])

        dead_line = None
        if success_date is not None:
            dead_line = success_date
        elif failed_date is not None:
            dead_line = failed_date
        return {"deadline": dead_line}

    def __project_text_parser(self):
        project_text = ""
        text_pattern = r'<section class="Project-outline Tab__content">((\s|\S)*)</aside>\n\s*</section>'
        text_matches = re.finditer(text_pattern, self.html_text)
        for match in text_matches:
            project_text = match.groups()[0]
        img_pattern = r'<img.*src="(.*)".*/>'
        text_matches = re.finditer(img_pattern, project_text)
        images = [match.groups()[0] for match in text_matches]
        return {'project_text': project_text, 'project_images': images}


class ProjectCommentsPageParser(Parser):

    def page_parser(self):
        temp = {"backers": self.__comment_getter(), "max_page": self.__max_page()}
        return temp

    def __comment_getter(self):
        comment_unit_pattern = r'<article style="border-bottom: 1px solid #ebebeb">(.+?)</article>'
        comment_units = re.finditer(comment_unit_pattern, self.html_text)
        backer_info = []
        for comment_unit in comment_units:
            date, name, uid = self.__extract(comment_unit.groups()[0])
            backer_info.append({"backer_name": name, "backer_id": uid, "backed_at": date})
        return backer_info

    def __max_page(self):
        page_pattern = r'<span class="page">\n.*<a href=".*">(\d+)</a>\n</span>'
        page_matches = re.finditer(page_pattern, self.html_text)
        pages = [page.groups()[0] for page in page_matches]
        if len(pages) > 0:
            return pages[-1]
        else:
            return 1

    def __extract(self, text):
        date = re.search(r'pubdate="(.*?)"', text).group(1)
        link = re.search(r'<div class="Cheer-comment__name"><b>(.*?)</b>', text)
        names = re.search(r'<a href="/users/(\d+?)">(.*?)</a>', link.group())

        name = ''
        uid = ''

        if names != None:
            uid = names.group(1)
            name = names.group(2)
        else:
            uid = 'NoID'
            name = link.group(1)

        return date, name, uid


class UserPageParser(Parser):

    def page_parser(self):
        user_dict = {
            "backed_projects":  self.__backed_projects_parser(),
            "created_projects": self.__created_projects_parser(),
        }
        user_dict.update(self.__profile_parser())
        return user_dict

    def __profile_parser(self):
        name_pattern = r'<div class="Profile__body__header__name">(.*)</div><div class="Profile__body__header__SNS-links">'
        biography_pattern = r'<div class="Profile__body__desc__main"><p>(.*)</p></div><div class="Profile__body__desc__more">'
        sns_pattern = r'<div class="Profile__body__header__SNS-links">(.*)</div></div><div class="Profile__body__desc">'
        return {
            "name":      self.__regexp_match_group(name_pattern),
            "biography": self.__regexp_match_group(biography_pattern),
            "sns_links": self.__regexp_match_group(sns_pattern),
        }

    def __backed_projects_parser(self):
        _site_container = "div[@class='Site-container']"
        _profile_container = 'div[@class="Profile-container"]'
        _ul_tab_menu = "ul[@class='Tab-menu']"
        _li_active = "li[@class='active']"
        _tab_pan = 'div[@class="Tab-pan"]'
        _tab_contents = 'div[@class="Tab-contents"]'
        _tab_contents_active = 'div[@class="Tab-contents active"]'
        _tab_contents__item = 'div[@class="Tab-contents__item"]'
        _article = "article"
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        try:
            backed_projects = None
            projects_profile = \
                root.\
                body.\
                find(_site_container).\
                find(_profile_container)
            if projects_profile.find(_ul_tab_menu).find(_li_active).text == "支援したプロジェクト":
                backed_projects = \
                    projects_profile.\
                    find(_tab_pan).\
                    find(_tab_contents_active).\
                    findall(_tab_contents__item)
            else:
                backed_projects = \
                    projects_profile. \
                    find(_tab_pan). \
                    find(_tab_contents). \
                    findall(_tab_contents__item)
        except AttributeError:
            return []
        return [backed_project.find(_article).find("a").attrib["href"].split("/")[2] for backed_project in backed_projects]

    def __created_projects_parser(self):
        _site_container = "div[@class='Site-container']"
        _profile_container = 'div[@class="Profile-container"]'
        _ul_tab_menu = "ul[@class='Tab-menu']"
        _li_active = "li[@class='active']"
        _tab_pan = 'div[@class="Tab-pan"]'
        _tab_contents = 'div[@class="Tab-contents"]'
        _tab_contents_active = 'div[@class="Tab-contents active"]'
        _tab_contents__item = 'div[@class="Tab-contents__item"]'
        _article = "article"
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        try:
            created_projects = None
            projects_profile = \
                root. \
                body. \
                find(_site_container). \
                find(_profile_container)
            if projects_profile.find(_ul_tab_menu).find(_li_active).text == "公開したプロジェクト":
                created_projects = \
                    projects_profile. \
                    find(_tab_pan). \
                    find(_tab_contents_active). \
                    findall(_tab_contents__item)
            else:
                created_projects = \
                    projects_profile. \
                    find(_tab_pan). \
                    find(_tab_contents). \
                    findall(_tab_contents__item)
        except AttributeError:
            return []
        return [created_project.find(_article).find("a").attrib["href"].split("/")[2] for created_project in created_projects]

    def __regexp_match_group(self, pattern):
        matches = re.finditer(pattern, self.html_text)
        for match in matches:
            return match.groups()[0]


class FaceBookLikeParser(object):

    def __init__(self, api_response):
        self.api_response = api_response

    def parse(self):
        return self.__page_parser()

    def __page_parser(self):
        return json.loads(self.api_response)


if __name__ == "__main__":
    f = open("tests/test_resources/project_page.html", "r")
    print(ProjectPageParser(f.read()).parse())