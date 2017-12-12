"""
These classes are parser for scraping each pages.
I recommend to naming follow the pattern of {object_name}{sub_object}PageParser
for easy to use.
"""
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
        """
        detect project page publishing is end or not
        :return: 
        """
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
        """
        detect is project page shows it will published massage or not 
        :return: 
        """
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
    """
    A parser which parse project page. 
    It is used when project object properties are called.
    """
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
        project_tab_pattern = r'<nav class="tabnav-tabs">(.*)</nav></div></div></div><div class="Container">'
        project_tab = re.search(project_tab_pattern, self.html_text).group(1)
        self.project_tab = project_tab
        tab = self.__project_tab_splitter()
        return {"news_update_count": tab["news_update_count"], "comments_count": tab["comments_count"]}

    def __project_tab_splitter(self):
        project_tab_units = re.finditer(r'<a class="tabnav-tab(.*?)</a>', self.project_tab)
        nums = {"news_update_count": None, "comments_count": None}

        for project_tab_unit in project_tab_units:
            tab_unit = project_tab_unit.group(1)
            tab_name = re.search(r'href="/projects/.*?"><span>(.*?)</span>', tab_unit)
            if tab_name is None:
                break
            num = re.search(r'<span class="Tab__menu-icon Icon-num">(\d*?)</span>', tab_unit)
            if tab_name.group(1) == "新着情報":
                nums["news_update_count"] = num.group(1)
            elif tab_name.group(1) == "応援コメント":
                nums["comments_count"] = num.group(1)
        return nums


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
        img_pattern = r'<img.*?src="(.*?)".*?/>'
        text_matches = re.finditer(img_pattern, project_text)
        images = [match.groups()[0] for match in text_matches]
        return {'project_text': project_text, 'project_images': images}


class ProjectCommentsPageParser(Parser):

    def page_parser(self):
        temp = {"backers": self.__comment_getter()}
        return temp

    def __comment_getter(self):
        comment_unit_pattern = r'<article style="border-bottom: 1px solid #ebebeb">((\s|\S)*?)</article>'
        comment_units = re.finditer(comment_unit_pattern, self.html_text)
        backer_info = []
        for comment_unit in comment_units:
            date, name, uid = self.__extract(comment_unit.group(1))
            backer_info.append({"backer_name": name, "backer_id": uid, "backed_at": date})
        if len(backer_info) == 0:
            raise errors.ProjectCommentsPageBackersZeroException("このページには支援者がいません")
        return backer_info

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
            uid = "NoID"
            name = link.group(1)

        return date, name, uid


class UserPageParser(Parser):

    def page_parser(self):
        user_dict = self.__profile_parser()
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