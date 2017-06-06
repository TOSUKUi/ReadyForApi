from .core import ReadyForObject, ReadyForConnection, FacebookGraphConnection
from cached_property import cached_property
from . import html_parser, user
from secrets.settings import Settings


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
            self.project_url = self.project_url
            self.project_key = None

    @cached_property
    def __project_identifier(self):
        if self.project_key is not None:
            return self.project_key
        elif self.__id is not None:
            return self.__id
        elif self.project_url is not None:
            return self.project_url.split('/').get(2)

    @cached_property
    def summary(self):
        response = ReadyForConnection.call(object_name="projects", object_id=self.__project_identifier, param=None, method="GET")
        return html_parser.ProjectPageParser(response.text).parse()


    @cached_property
    def name(self):
        if self.project_key is not None:
            return self.project_key
        else:
            return self.summary.keyword

    @cached_property
    def _id(self):
        if self.__id is None:
            return self.summary.id
        else:
            return self.__id

    @cached_property
    def amount(self):
        return self.summary.amount

    @property
    def anticipative_amount(self):
        return self.summary.anticipative_amount

    @property
    def achievement_amount(self):
        return self.summary.achievement_amount

    @property
    def degree(self):
        """
        :return: end time of project
         :rtype: Datetime
        """
        return self.summary.degree

    @property
    def expired_at_year(self):
        """
        this parameter appear of project were end.
        :return: the year when project end.
        :rtype: string
        """
        return self.summary.expired_at_year

    @property
    def funding_percent(self):
        return self.amount/self.goal_amount

    @property
    def goal_amount(self):
        return self.summary.goal_amount

    @property
    def image(self):
        return self.summary.image

    @property
    def is_accomplish_report_republished(self):
        return self.summary.is_accomplish_report_republished

    @cached_property
    def is_expired(self):
        return True if self.summary.is_expired is "終了日" else False

    @property
    def is_matching_complete(self):
        return self.summary.is_matching_complete

    @property
    def keep_it_all(self):
        return self.summary.keep_it_all

    @property
    def label_type(self):
        return self.summary.label_type

    @property
    def matching(self):
        return self.summary.matching

    @property
    def favorite_count(self):
        return self.summary.watchilist_count

    @property
    def project_type(self):
        """
        :return: project type. e.g. "charity" , "normal" 
        """
        return self.summary.project_type

    @property
    def tags(self):
        return self.summary.tags

    @cached_property
    def author(self):
        url = self.summary.user_profile_url
        return user.User(user_url=url)

    @cached_property
    def __facebook_graph(self):
        """
        
        :return: Facebook_Like 
        """
        object_id = "{{domain}}/{{name}}".format(domain=Settings.readyfor_domain, name=self.name)
        return html_parser.FaceBookLikeParser(FacebookGraphConnection.call(object_id=object_id, v="v2.8")).parse()

    @property
    def facebook_likes(self):
        return self.__facebook_graph.share.share_count

    @property
    def facebook_comment_count(self):
        return self.__facebook_graph.share.comment_count

    @property
    def category(self):
        pass

    @cached_property
    def __comments_summary(self):
        response = ReadyForConnection.call(object_name="project", object_id=self.__project_identifier, sub_object="comment")
        return html_parser.ProjectCommentsPageParser(response.text).parse()

    @property
    def backers(self):
        return self.__comments_summary.backers


