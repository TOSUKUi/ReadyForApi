import unittest
from readyforapi.project import Project
from readyforapi.user import User
from datetime import datetime


class TestProject(unittest.TestCase):
    """
       型チェック
    """
    test_p_key = Project(project_key='solarboat')
    test_p_id = Project(project_id=12194)
    test_p_proce = Project(project_key="bushland-house")

    def test_name(self):
        self.assertEqual(type(self.test_p_key.name), str)
        self.assertEqual(self.test_p_key.name, self.test_p_id.name)

    def test_url(self):
        self.assertEqual(type(self.test_p_key.url), str)
        self.assertEqual(self.test_p_key.url, self.test_p_id.url)

    def test_amount(self):
        self.assertEqual(type(self.test_p_key.amount), int)
        self.assertEqual(self.test_p_key.amount, self.test_p_id.amount)

    def test_anticipative_amount(self):
        self.assertIsNone(self.test_p_proce.anticipative_amount)
        self.assertIsNone(self.test_p_key.anticipative_amount)
        self.assertEqual(self.test_p_id.anticipative_amount, self.test_p_key.anticipative_amount)

    def test_news_update_count(self):
        self.assertEqual(type(self.test_p_key.news_update_count), int)
        self.assertEqual(self.test_p_key.news_update_count, self.test_p_id.news_update_count)

    def test_achivement_amount(self):
        self.assertIsNone(self.test_p_proce.achievement_amount)
        self.assertIsNone(self.test_p_key.achievement_amount)
        self.assertEqual(self.test_p_id.achievement_amount, self.test_p_key.achievement_amount)

    def test_degree(self):
        self.assertEqual(type(self.test_p_proce.degree), str)
        self.assertEqual(self.test_p_key.degree, self.test_p_id.degree)

    def test_expired_at_year(self):
        self.assertIsNone(self.test_p_proce.expired_at_year)
        self.assertEqual(type(self.test_p_key.expired_at_year), str)
        self.assertEqual(self.test_p_key.expired_at_year, self.test_p_id.expired_at_year)

    def test_funding_percent(self):
        self.assertEqual(type(self.test_p_key.funding_percent), int)
        self.assertEqual(self.test_p_key.funding_percent, self.test_p_id.funding_percent)

    def test_goal_amount(self):
        self.assertEqual(type(self.test_p_key.goal_amount), int)
        self.assertEqual(self.test_p_key.goal_amount, self.test_p_id.goal_amount)

    def test_deadline(self):
        self.assertEqual(type(self.test_p_proce.deadline), datetime)
        self.assertEqual(type(self.test_p_key.deadline), datetime)
        self.assertEqual(self.test_p_key.deadline, self.test_p_id.deadline)

    def test_author(self):
        self.assertEqual(self.test_p_key.author.__class__.__name__, User.__name__)
        self.assertEqual(self.test_p_key.author, self.test_p_id.author)

    def test_facebook_likes(self):
        self.assertEqual(type(self.test_p_id.facebook_likes), int)
        self.assertEqual(self.test_p_key.facebook_likes, self.test_p_id.facebook_likes)

    def test_comments_count(self):
        self.assertEqual(type(self.test_p_key.comments_count), int)
        self.assertEqual(self.test_p_key.comments_count, self.test_p_id.comments_count)
