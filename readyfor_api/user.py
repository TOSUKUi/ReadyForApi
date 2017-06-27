# make this until 2017/5/30
from . import *
from secrets.settings import Settings
from . import project
from .core import ReadyForObject, ReadyForConnection
from cached_property import cached_property


class User(ReadyForObject):

    def __init__(self, user_id=None, user_url=None, backed_at=None):
        if user_id is None and user_url is None:
            raise ValueError('no one of argument which must be supplied')
        elif user_id is not None:
            self.__id = user_id
            self.user_url = None
        elif user_url is not None:
            self.user_url = user_url
            self.__id = None
        # This property activate when this user is gotten from comment page of project.
        self.backed_at = backed_at

    @cached_property
    def from_user_page(self):
        user_identifier = ""
        if self.__id is not None:
            user_identifier = self.__id
        elif self.user_url is not None:
            user_identifier = self.user_url.split("/")[4]
        response = ReadyForConnection.call(object_name="users", object_id=user_identifier, param=None, method="GET")
        return html_parser.UserPageParser(response.text).parse()

    @cached_property
    def _id(self):
        if self.__id is not None:
            return self.__id
        elif self.user_url is not None:
            return self.user_url.split("/")[4]

    @property
    def name(self):
        return self.from_user_page.name

    @property
    def url(self):
        if self.user_url is not None:
            return self.user_url
        else:
            return "{domain}/{users}/{id}".format(
                domain=Settings.readyfor_domain,
                users=Settings.user_domain,
                id=self.id
            )

    @property
    def biography(self):
        return self.from_user_page.biography

    @cached_property
    def backed_projects(self):
        return [project.Project(project_key=project_key) for project_key in self.from_user_page.backed_projects]

    @cached_property
    def created_projects(self):
        return [project.Project(project_key=project_key) for project_key in self.from_user_page.created_projects]

    @property
    def sns_links(self):
        return self.from_user_page.sns_links




