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
        return {"backers": list(map(lambda x: int(x.split("/")[2]), self.__comment_getter()))}

    def __comment_getter(self):
        pattern = r'<div class="Cheer-comment"><div class="Cheer-comment__image"><a href="(/users/[0-9]*)"'
        matches = re.finditer(pattern, self.html_text)
        return [match.groups()[0] for match in matches]


class UserPageParser(Parser):
    pass


class FaceBookLikeParser(object):
    pass


if __name__ == "__main__":
    f = open("tests/test_resources/project_page.html", "r")
    print(ProjectPageParser(f.read()).parse())

