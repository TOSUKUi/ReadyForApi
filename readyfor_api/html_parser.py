"""
These classes are parser for scraping each pages.
I recommend to naming follow the pattern of {object_name}{sub_object}PageParser
for easy to use.
"""
import lxml.html
import json
import re
from attrdict import AttrDict
from . import errors


class Parser(object):
    """
    Parent class for PageParsers.
    """
    def __init__(self, html_text):
        self.html_text = html_text
        self.__error_detection()

    def __error_detection(self):
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        title_text = root.head.find('title').text
        error_pattern = r'(404 error - クラウドファンディング Readyfor)'
        is_error = list(map(lambda x: x.groups(), re.finditer(error_pattern, title_text)))
        if len(is_error) > 0:
            raise errors.PageAccessException("Get 4** error, Page not found")
        else:
            pass

    def parse(self):
        """
        :return: Attribute object of page information.
        :rtype: AttrDict
        """
        page_dict = self.page_parser()
        return AttrDict(page_dict)

    def page_parser(self):
        pass


class ProjectPageParser(Parser):

    def page_parser(self):
        project_dict = self.__project_json_getter()
        project_dict["project"].update({"news_update_count": self.__project_news_count_parser()})
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

    def __project_news_count_parser(self):
        pattern = r'<span class="Tab__menu-icon Icon-num">(.*)</span>'
        matches = re.finditer(pattern, self.html_text)
        for match in matches:
            return int(match.groups()[0])


class ProjectCommentsPageParser(Parser):

    def page_parser(self):
        return {"backers": self.__comment_getter()}

    def __comment_getter(self):
        comments_pattern = r'<div class="Cheer-comment"><div class="Cheer-comment__image"><a href="/users/([0-9]*)"'
        comments_matches = re.finditer(comments_pattern, self.html_text)
        backed_at_pattern = r'<time class="Cheer-comment__status__date" pubdate="(.*)">.*</time></div><p class="Cheer-comment__text">'
        backed_at_matches = re.finditer(backed_at_pattern, self.html_text)
        return [{"backer_id": comment.groups()[0], "backed_at": backed_at.groups()[0]} for comment, backed_at in zip(comments_matches, backed_at_matches)]


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
        _tab_pan = 'div[@class="Tab-pan"]'
        _tab_contents = 'div[@class="Tab-contents"]'
        _tab_contents__item = 'div[@class="Tab-contents__item"]'
        _article = "article"
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        try:
            backed_projects = \
                root.\
                body.\
                find(_site_container).\
                find(_profile_container).\
                find(_tab_pan).\
                find(_tab_contents).\
                findall(_tab_contents__item)
        except AttributeError:
            return []
        return [backed_project.find(_article).find("a").attrib["href"].split("/")[2] for backed_project in backed_projects]

    def __created_projects_parser(self):
        _site_container = "div[@class='Site-container']"
        _profile_container = 'div[@class="Profile-container"]'
        _tab_pan = 'div[@class="Tab-pan"]'
        _tab_contents = 'div[@class="Tab-contents active"]'
        _tab_contents__item = 'div[@class="Tab-contents__item"]'
        _article = "article"
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        try:
            backed_projects = \
                root. \
                body. \
                find(_site_container). \
                find(_profile_container). \
                find(_tab_pan). \
                find(_tab_contents). \
                findall(_tab_contents__item)
        except AttributeError:
            return []
        return [backed_project.find(_article).find("a").attrib["href"].split("/")[2] for backed_project in backed_projects]

    def __regexp_match_group(self, pattern):
        matches = re.finditer(pattern, self.html_text)
        for match in matches:
            return match.groups()[0]


class FaceBookLikeParser(object):

    def __init__(self, api_response):
        self.api_response = api_response

    def parse(self):
        return AttrDict(self.__page_parser())

    def __page_parser(self):
        return json.loads(self.api_response.text)


if __name__ == "__main__":
    f = open("tests/test_resources/project_page.html", "r")
    print(ProjectPageParser(f.read()).parse())

