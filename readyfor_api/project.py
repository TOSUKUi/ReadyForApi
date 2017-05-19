from .core import ReadyForObject, ReadyForConnection, FacebookGraphConnection
from cached_property import cached_property
from . import html_parser, user
from attrdict import AttrDict
from requests import request
from secrets.settings import Settings


class Project(ReadyForObject):

    def __init__(self, project_id=None, project_key=None, project_url=None):
        if project_id is None and project_key is None and project_url is None:
            raise ValueError('one of argument must be supplied')
        elif project_key is not None:
            if '/' in project_key:
                raise ValueError("\"project_key\" must be the *ending* of a vanity URL, not the entire URL!")
            self.project_key = project_key
        elif project_id is not None:
            self._id = project_id
        elif project_url is not None:
            self.project_url = self.project_url

    @cached_property
    def __summary(self):
        project_identifier = ""
        if self.project_key is not None:
            project_identifier = self.project_key
        elif self._id is not None:
            project_identifier = self._id
        elif self.project_url is not None:
            project_identifier = self.project_url.split('/').get(2)
        response = ReadyForConnection.call(object_name="projects", object_id=project_identifier, param=None, method="GET")
        return html_parser.ProjectPageParser(response).parse()

    @cached_property
    def name(self):
        if self.project_key is not None:
            return self.project_key
        else:
            return self.__summary.keyword

    @cached_property
    def id(self):
        if self._id is None:
            return self.__summary.id
        else:
            return self._id

    @property
    def amount(self):
        return self.__summary.amount

    @property
    def anticipative_amount(self):
        return self.__summary.anticipative_amount

    @property
    def achievement_amount(self):
        return self.__summary.achievement_amount

    @property
    def degree(self):
        """
        :return: end time of project
         :rtype: Datetime
        """
        return self.__summary.degree

    @property
    def expired_at_year(self):
        """
        this parameter appear of project were end.
        :return: the year when project end.
        :rtype: string
        """
        return self.__summary.expired_at_year

    @property
    def funding_percent(self):
        return self.amount/self.goal_amount

    @property
    def goal_amount(self):
        return self.__summary.goal_amount

    @property
    def image(self):
        return self.__summary.image

    @property
    def is_accomplish_report_republished(self):
        return self.__summary.is_accomplish_report_republished

    @cached_property
    def is_expired(self):
        return True if self.__summary.is_expired is "終了日" else False

    @property
    def is_matching_complete(self):
        return self.__summary.is_matching_complete

    @property
    def keep_it_all(self):
        return self.__summary.keep_it_all

    @property
    def label_type(self):
        return self.__summary.label_type

    @property
    def matching(self):
        return self.__summary.matching

    @property
    def favorite_count(self):
        return self.__summary.watchilist_count

    @property
    def project_type(self):
        """
        :return: project type. e.g. "charity" , "normal" 
        """
        return self.__summary.project_type

    @property
    def tags(self):
        return self.__summary.tags

    @cached_property
    def author(self):
        url = self.__summary.user_profile_url
        return user.User(url)

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

    #----------プロパティをすべて書こう[amount, anticipative_amount, achivement_amount, degree, expired_at_year, funding_model, goal_amount, image, is_accombilish_report_published]


