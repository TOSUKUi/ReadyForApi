"""
These classes name should be {{object_name}}{{sub_object}}PageParser with Camel case
e.g When object name is project and param is None, ProjectPageParser.
    When object name is project and param is Comments, ProjectCommentPageParser
"""
import lxml.html
import json
import re
from attrdict import AttrDict


class ProjectPageParser(object):

    def __init__(self, html_text):
        self.html_text = html_text
        self.success = self.__error_detection()

    def parse(self):
        return self.__project_json_getter()

    def __project_json_getter(self):
        _body = "body"
        _site_container = "div[@class='Site-container']"
        _article = 'article'
        _container = "div[@class='Container']"
        _sidebar = "div[@class='Sidebar is-type0 u-fl_r']"
        _u_em = "div[@class='u-em u-fs_18 u-font_b u-align_c u-mt_20 u-mb_20']"

        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        project_json = root.body.\
            find(_site_container).\
            find(_article).\
            find(_container).\
            find(_sidebar).\
            find(_u_em).\
            find('div')
        return AttrDict(project_json.attrib['data-react-props'])


    def __error_detection(self):
        html = lxml.html.fromstring(self.html_text)
        root = html.body.xpath('/*')[0]
        error_pattern = r".*[400-499].*"
        if re.match(root.find('head/title').text, error_pattern):
            return False
        else:
            return True





class UserPageParser(object):
    pass


if __name__=="__main__":
    f = open("tests/test_html/project_page.html", "r")
    ProjectPageParser(f.read()).parse()
