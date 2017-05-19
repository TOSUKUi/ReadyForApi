import unittest
from readyfor_api.html_parser import *
import tests.test_resources.dicts_for_tests as pps


class TestProjectPageParserMethods(unittest.TestCase):

    test_html = open("tests/test_resources/project_page.html", "r")

    def test_parse(self):
        self.assertEqual(ProjectPageParser(self.test_html.read()).parse(), pps.project_summary_dict)


class TestFacebookLikesParserMethods(unittest.TestCase):

    test_facebook = open("tests/test_resources/facebook_likes.json", "r")

    def test_parse(self):
        self.assertEqual(FaceBookLikeParser(self.test_facebook.read()).parse(), pps.facebook_likes_dict)

if __name__ == '__main__':
    unittest.main()
