import unittest
from readyfor_api.html_parser import *
import tests.test_html as test_html


class TestProjectPageParserMethods(unittest.TestCase):

    test_html = open("test_html/project_page.html", "r")

    def test_parse(self):
        self.assertEqual(ProjectPageParser(self.test_html.read()), test_html.project_page_summary.project_summary_hash)


if __name__ == '__main__':
    unittest.main()
