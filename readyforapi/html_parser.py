"""
These classes are parser for scraping each pages.
I recommend to naming follow the pattern of {object_name}{sub_object}PageParser
for easy to use.
"""
import lxml.html
import json
import re
from . import errors


class Parser(object):
    """
    Parent class for PageParsers.
    """
    def __init__(self, html_text):
        self.html_text = html_text

    def parse(self):
        """
        :return: Attribute object of page information.
        :rtype: AttrDict
        """
        page_dict = self.page_parser()
        return page_dict

    def page_parser(self):
        pass


class ProjectPageParser(Parser):

    def page_parser(self):
        project_dict = self.__project_json_getter()
        project_dict["project"].update(self.__project_tab_parser())
        project_dict["project"].update(self.__project_deadline_parser())
        return project_dict["project"]

    def __project_json_getter(self):
        _site_container = "div[@class='Site-container']"
        _article = 'article'
        _container = "div[@class='Container']"
        _sidebar = "div[@class='Sidebar is-type0 u-fl_r']"
        _u_em = "div[@class='u-em u-fs_18 u-font_b u-align_c u-mt_20 u-mb_20']"

        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        project_json = \
            root.\
            body.\
            find(_site_container).\
            find(_article).\
            find(_container).\
            find(_sidebar).\
            find(_u_em).\
            find('div')
        return json.loads(str(project_json.attrib['data-react-props']))

    def __project_tab_parser(self):
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        _site_container = "div[@class='Site-container']"
        _article = 'article'
        _project_visual_container = "div[@class='Project-visual Container u-mb_20 u-clrfix']"
        _tab_wrapper = 'div[@class="tab-wrapper"]'
        _tab_menu = 'div[@class="Tab__menu tabnav-tabs"]'
        _tabnav_tabs = 'nav[@class="tabnav-tabs"]'
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

    def __project_comments_count_parser(self):
        pattern = r''


class ProjectCommentsPageParser(Parser):

    def page_parser(self):
        temp = {"backers": self.__comment_getter(), "max_page": self.__max_page()}
        return temp

    def __comment_getter(self):
        #print(f"222{self.html_text}\n----------------------------------")
        comments_pattern = r'<div class="Cheer-comment"><div class="Cheer-comment__image"><a href="/users/([0-9]*)"'
        comments_matches = re.finditer(comments_pattern, self.html_text)
        backed_at_pattern = r'<time class="Cheer-comment__status__date" pubdate="(\d{4}\-\d{2}\-\d{2})">.*</time></div><div class="Cheer-comment__text">'
        backed_at_matches = re.finditer(backed_at_pattern, self.html_text)
        return [{"backer_id": comment.groups()[0], "backed_at": backed_at.groups()[0]} for comment, backed_at in zip(comments_matches, backed_at_matches)]

    def __max_page(self):
        page_pattern = r'<span class="page">\n.*<a href=".*">(\d+)</a>\n</span>'
        page_matches = re.finditer(page_pattern, self.html_text)
        pages = [page.groups()[0] for page in page_matches]
        if len(pages) > 0:
            return pages[-1]
        else:
            return 1



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