from requests import request
from .errors import *
from secrets.settings import Settings
from datetime import datetime, timedelta
import time
from inflector import Inflector

class ReadyForConnection(object):
    queried_at = datetime.now()
    inflicter = Inflector()

    @classmethod
    def call(cls, object_name=None, object_id=None, sub_object=None, method="GET", test=None, **kwargs):

        """
        Call an A
        :param object_name: the readyfor object name such like tags, projects, users...etc
        :param object_id: id of project or others
        :param method: http method.
        :param param: specify to get more information such like comments, news , from object page
        :param kwargs   : kwargs of page. e.g. page...etc
        :return: response
        """

        delta = datetime.now() - cls.queried_at
        time_to_sleep = timedelta(seconds=1.3) - delta
        if delta < timedelta(seconds=1.3):
            time.sleep(time_to_sleep.seconds)
        try:
            # User double curly-braces to tell python
            objects_name = cls.inflicter.pluralize(object_name)
            query = "{domain}/{objects_name}/{id}/{sub_object}".format(domain=Settings.readyfor_domain, objects_name=objects_name, id=object_id, sub_object=sub_object)
            if sub_object is None:
                query = "{domain}/{objects_name}/{id}".format(domain=Settings.readyfor_domain,
                                                              objects_name=objects_name,
                                                              id=object_id)
            cls.queried_at = datetime.now()
            response = request(method=method, url=query, params=kwargs)
            if response.status_code % 400 < 100:
                raise AccessException("4** error")
            return response
        except:
            raise AccessException("some problem occurred when access")


class FacebookGraphConnection(object):
    queried_at = datetime.now()
    QUERY_DOMAIN = "http://graph.facebook.com"


    @classmethod
    def call(cls, object_id, v, method="GET", **kwargs):

        """
        Call an A
        :param object_name: the readyfor object name such like tags, projects, users...etc
        :param object_id: id of project or others
        :param method: http method.
        :param param: specify to get more information such like comments, news , from object page
        :param kwargs   : kwargs of page. e.g. page...etc
        :return: response
        """

        delta = datetime.now() - cls.queried_at
        time_to_sleep = timedelta(seconds=1) - delta
        if delta < timedelta(seconds=1):
            time.sleep(time_to_sleep.seconds)
        try:
            # User double curly-braces to tell python
            query = "{domain}/{id}".\
                format(domain=cls.QUERY_DOMAIN, v=v, id=object_id)
            cls.queried_at = datetime.now()
            return request(method=method, url=query, params=kwargs)
        except:
            raise AccessException("some problem occurred when access")


class ReadyForObject(object):
    """
    A base class for all rich ReadyFor objects.
    """

    @property
    def id(self):
        # "_id" is set by the child class
        return self._id

    def __repr__(self):
        try:
            return '<{clsname} "{name}" ({id})>'.format(
                clsname=self.__class__.__name__,
                name=self.name,
                id=self.id
            )
        except (AttributeError, APIException):
            return '<{clsname} ({id})>'.format(
                clsname=self.__class__.__name__,
                id=self._id
            )

    def __eq__(self, other):
        """
        :param other: ReadyForObject
        :return: boolean
        """
        # Use a "hash" of each object to prevent cases where derivative classes sharing the
        # same ID.
        return hash(self) == hash(other)

    def __ne__(self, other):
        """
        :param other: ReadyForObject
        :return: boolean
        """
        return not self == other

    def __hash__(self):
        return hash(self.id)

