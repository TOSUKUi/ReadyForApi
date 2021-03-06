from .core import ReadyForObject, ReadyForConnection, FacebookGraphConnection
from cached_property import cached_property
from . import user
from .errors import ProjectCommentsPageBackersZeroException
from .html_parser import ProjectCommentsPageParser, ProjectPageParser, FaceBookLikeParser
from datetime import datetime, timedelta
import itertools


class Project(ReadyForObject):

    def __init__(self, project_id=None, project_key=None, project_url=None):
        if project_id is None and project_key is None and project_url is None:
            raise ValueError('one of argument must be supplied')
        elif project_key is not None:
            if '/' in project_key:
                raise ValueError("\"project_key\" must be the *ending* of a vanity URL, not the entire URL!")
            self.project_key = project_key
            self.__id = None
            self.project_url = None
        elif project_id is not None:
            self.__id = project_id
            self.project_url = None
            self.project_key = None
        elif project_url is not None:
            self.__id = None
            self.project_url = project_url
            self.project_key = None

    @cached_property
    def __project_identifier(self):
        """
        this method return porject identifier for summary request.
        :return: project_key: if project_key or project_url is exist. project_id: if self.__id is exist. 
        """
        if self.project_key is not None:
            return self.project_key
        elif self.__id is not None:
            return self.__id
        elif self.project_url is not None:
            return self.project_url.split('/')[4]

    # ----------------------------------------------
    # related summary
    # ----------------------------------------------
    @cached_property
    def summary(self):
        """
        this method return almost of property of project object
        :return: 
        """
        response = ReadyForConnection.call(objects_kind="projects", object_id=self.__project_identifier, param=None, method="GET")
        return ProjectPageParser(response.text).parse()

    @cached_property
    def name(self):
        if self.project_key is not None:
            return self.project_key
        else:
            return self.summary["keyword"]

    @cached_property
    def _id(self):
        if self.__id is None:
            return self.summary["id"]
        else:
            return self.__id

    @cached_property
    def url(self):
        if self.project_url is not None:
            return self.project_url
        else:
            return "{domain}/{object}/{key}".format(domain="https://readyfor.jp", object="projects", key=self.name)

    @cached_property
    def amount(self):
        """
        :return: amount of money
        """
        amount = self.summary["amount"].replace(",", "")
        return int(amount)

    @property
    def anticipative_amount(self):
        """
        It is past goal amount of this project but not appear.
        :return: None
        """
        try:
            anticipative_amount = self.summary["anticipative_amount"].replace(",", "")
            return int(anticipative_amount)
        except:
            return None

    @property
    def is_2nd_stage(self):
        """
        :return: if 2nd stage , true else false 
        """
        return self.anticipative_amount is not None

    @property
    def news_update_count(self):
        """
        新着情報の更新回数
        :return: 新着情報の更新回数
        """
        return int(self.summary["news_update_count"]) if self.summary["news_update_count"] is not None else None

    @property
    def achievement_amount(self):
        """
        Goal amount of past it appears when this project is setten 2nd goal.
        readyfor typo this property
        :return: goal amount of past.
        """
        return self.summary["achivement_amount"] if "achivement_amount" in self.summary else None

    @property
    def degree(self):
        """
        :return: end time of project
         :rtype: Datetime
        """
        return self.summary["degree"]

    @property
    def expired_at_year(self):
        """
        this parameter appear of project wes end.
        :return: the year when project end.
        :rtype: string
        """
        return self.summary["expired_at_year"] if "expired_at_year" in self.summary else None

    @property
    def funding_percent(self):
        return self.summary["funded_percent"]

    @property
    def goal_amount(self):
        goal_amount = self.summary["goal_amount"].replace(",", "")
        return int(goal_amount)

    @property
    def image(self):
        return self.summary["image"]

    @property
    def is_accomplish_report_published(self):
        return self.summary["is_accomplish_report_published"]

    @cached_property
    def is_expired(self):
        return True if self.summary["is_expired"] == "終了日" else False

    @property
    def is_matching_complete(self):
        return self.summary["is_matching_complete"]

    @property
    def keep_it_all(self):
        return self.summary["keep_it_all"]

    @property
    def deadline(self):
        if self.summary["deadline"] is not None:
            return datetime.strptime(self.summary["deadline"], "%Y-%m-%d")
        else:
            return datetime.today() + timedelta(days=3)

    @cached_property
    def is_succeed(self):
        return True if self.funding_percent >= 100 else False

    @property
    def label_type(self):
        return self.summary["label_type"]

    @property
    def matching(self):
        return self.summary["matching"]

    @property
    def favorite_count(self):
        return int(self.summary["watchlists_count"]) if self.summary["watchlists_count"] is not None else None

    @property
    def project_type(self):
        """
        :return: project type. e.g. "charity" , "normal"
        """
        return self.summary["project_type"]

    @property
    def tags(self):
        return self.summary["tags"]

    @cached_property
    def author(self):
        return user.User(user_url=self.summary["user_profile_url"], name=self.summary["user"]["name"])

    @property
    def comments_count(self):
        return int(self.summary["comments_count"]) if self.summary["comments_count"] is not None else None

    @property
    def project_text(self):
        return self.summary["project_text"]

    @property
    def project_images(self):
        return self.summary["project_images"]

    @property
    def num_project_images(self):
        return len(self.project_images)

    @cached_property
    def category(self):
        for tag in self.tags:
            if tag["tag_type"] == "category":
                return tag["name"]

    @cached_property
    def comments_summary(self):
        """
        :return: Backers which back to this project
        :rtype: user.User
        """
        comments_summary = {"backers": []}
        for page in itertools.count(start=1, step=1):
            try:
                response = ReadyForConnection.call(objects_kind="projects", object_id=self.__project_identifier,
                                                   sub_object_kind="comments", page=page)
                comments_summary["backers"].extend(ProjectCommentsPageParser(response.text).parse()["backers"])
            except ProjectCommentsPageBackersZeroException as e:
                break

        return [
            user.User(
                user_id=backer["backer_id"],
                backed_at=backer["backed_at"],
                name=backer["backer_name"]
            )
            for backer in comments_summary["backers"]
        ]

    @cached_property
    def backers(self):
        return self.comments_summary

    # ----------------------------------------
    # related facebook
    # ----------------------------------------
    @cached_property
    def __facebook_graph(self):
        """
        :return: Facebook_Like
        """
        domain = "https://readyfor.jp"
        object_id = "{domain}/{object}/{name}".format(domain=domain, object="projects", name=self.name)
        return FaceBookLikeParser(FacebookGraphConnection.call(object_id=object_id, v="v2.10").text).parse()

    @property
    def facebook_reaction_count(self):
        return self.__facebook_graph["engagement"]["reaction_count"]

    @property
    def facebook_share_count(self):
        return self.__facebook_graph["engagement"]["share_count"]

    @property
    def facebook_comment_count(self):
        return self.__facebook_graph["share"]["comment_count"]



