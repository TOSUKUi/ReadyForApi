# make this until 2017/5/30
from . import *
from .core import ReadyForObject, ReadyForConnection
from cached_property import cached_property


class User(ReadyForObject):

    def __init__(self, user_id, user_url):
        if user_id is None:
            raise ValueError('no one of argument which must be supplied')
        elif user_id is not None:
            self._id = user_id
        elif user_url is not None:
            self.user_url = user_url

    @cached_property
    def __from_user_page(self):
        user_identifier = ""
        if self._id is not None:
            user_identifier = self._id
        elif self.user_url is not None:
            user_identifier = self.user_url.split("/").get(2)
        response = ReadyForConnection.call(object_name="users", object_id=user_identifier, param=None, method="GET")
        return html_parser.UserPageParser(response.read()).parse()

    @property
    def name(self):
        return self.__from_user_page.name

    @property
    def biography(self):
        return self.__from_user_page.biography

    @property
    def backed_projects(self):
        return self.__convert_to_projects(self.__from_user_page.backed_projects)

    @property
    def created_projects(self):
        return self.__convert_to_projects(self.__from_user_page.created_projects)

    @property
    def sns_links(self):
        return self.__from_user_page.sns_links

    def __convert_to_projects(self, projects):
        return [project.Project(project_url) for project_url in projects]
