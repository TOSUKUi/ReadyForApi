# make this until 2017/5/30
from . import *
from . import project
from .core import ReadyForObject, ReadyForConnection
from cached_property import cached_property


class User(ReadyForObject):

    def __init__(self, user_id=None, user_url=None, backed_at=None, name=None):
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
        self.setted_name = name

    @cached_property
    def from_user_page(self):
        user_identifier = ""
        if self.__id is not None:
            user_identifier = self.__id
        elif self.user_url is not None:
            user_identifier = self.user_url.split("/")[4]
        response = ReadyForConnection.call(objects_kind="users", object_id=user_identifier, param=None, method="GET")
        return html_parser.UserPageParser(response.text).parse()

    @cached_property
    def _id(self):
        if self.__id is not None:
            return self.__id
        elif self.user_url is not None:
            return self.user_url.split("/")[4]

    @property
    def name(self):
        if self.setted_name is not None:
            return self.setted_name
        else:
            return self.from_user_page["name"]

    @property
    def url(self):
        if self.user_url is not None:
            return self.user_url
        else:
            return "{domain}/{users}/{id}".format(
                domain="https://readyfor.jp",
                users="users",
                id=self.id
            )

    @property
    def biography(self):
        return self.from_user_page["biography"]

    @property
    def sns_links(self):
        return self.from_user_page["sns_links"]
