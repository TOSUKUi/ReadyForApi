import unittest
from readyforapi.html_parser import *
import tests.test_resources.dicts_for_tests as pps


class TestProjectPageParserMethods(unittest.TestCase):

    f = open("tests/test_resources/project_page.html", "r")
    test_html = f.read()
    f.close()

    def test_parse(self):
        self.assertEqual(ProjectPageParser(self.test_html).parse(), pps.project_summary_dict["project"])


class TestProjectCommentsPageParserMethods(unittest.TestCase):

    def test_parse(self):

        f = open("tests/test_resources/project_comments_page.html", "r")
        test_html = f.read()
        f.close()
        self.assertEqual(ProjectCommentsPageParser(test_html).parse(), pps.backers)




class TestFacebookLikesParserMethods(unittest.TestCase):

    f = open("tests/test_resources/facebook_likes.json", "r")
    test_facebook = f.read()
    f.close()

    def test_parse(self):
        self.assertEqual(FaceBookLikeParser(self.test_facebook).parse(), pps.facebook_likes_dict)

if __name__ == '__main__':
    unittest.main()
