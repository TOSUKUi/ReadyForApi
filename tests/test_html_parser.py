import unittest
from readyfor_api.html_parser import *
import tests.test_resources.dicts_for_tests as pps


class TestProjectPageParserMethods(unittest.TestCase):

    test_html = open("tests/test_resources/project_page.html", "r").read()

    def test_parse(self):
        self.assertEqual(ProjectPageParser(self.test_html).parse(), pps.project_summary_dict["project"])


class TestProjectCommentsPageParserMethods(unittest.TestCase):

    def test_parse(self):
        test_html = open("tests/test_resources/project_comments_page.html", "r").read()
        self.assertEqual(ProjectCommentsPageParser(test_html).parse(), pps.backers)

    def test_parse_exception(self):
        test_html = open("tests/test_resources/404error.html", "r").read()
        self.assertRaises(
            errors.PageAccessException,
            ProjectCommentsPageParser,
            test_html
        )


class TestFacebookLikesParserMethods(unittest.TestCase):

    test_facebook = open("tests/test_resources/facebook_likes.json", "r").read()

    def test_parse(self):
        self.assertEqual(FaceBookLikeParser(self.test_facebook).parse(), pps.facebook_likes_dict)

if __name__ == '__main__':
    unittest.main()
