from requests import request
from .errors import *
from datetime import datetime, timedelta
import time
from inflector import Inflector


def set_tokens(_facebook_token=None):
    FacebookGraphConnection.facebook_token = _facebook_token


def set_readyfor_sleep_time(sleep_time=2.0):
    ReadyForConnection.sleep_time = timedelta(sleep_time)


class ReadyForConnection(object):
    queried_at = datetime.now()
    inflicter = Inflector()
    sleep_time = timedelta(2.0)

    @classmethod
    def call(cls, objects_kind=None, object_id=None, sub_object_kind=None, method="GET", test=None, **kwargs):

        """
        Call an A
        :param objects_kind: the readyfor object name. e.g. tags, projects, users...etc
        :param object_id: id of object which is include in object_name category
        :param method: http method.
        :param param: specify to get more information such like comments, news , from object page
        :param kwargs   : kwargs of page. e.g. page...etc
        :return: response
        """
        domain = "https://readyfor.jp"
        delta = datetime.now() - cls.queried_at
        if delta < cls.sleep_time:
            time_to_sleep = cls.sleep_time - delta
            time.sleep(time_to_sleep.seconds + time_to_sleep.microseconds*10e-7)
        query = "{domain}/{objects_name}/{id}/{sub_object}".format(domain=domain, objects_name=objects_kind, id=object_id, sub_object=sub_object_kind)
        if sub_object_kind is None:
            query = "{domain}/{objects_name}/{id}".format(domain=domain,
                                                          objects_name=objects_kind,
                                                          id=object_id)
        response = request(method=method, url=query, params=kwargs)
        cls.queried_at = datetime.now()
        if 400 < response.status_code:
            raise AccessException("{code} error".format(code=response.status_code))
        return response


class FacebookGraphConnection(object):
    queried_at = datetime.now()
    QUERY_DOMAIN = "https://graph.facebook.com"
    facebook_token = ""

    def set_token(self, token):
        self.facebook_token = token


    @classmethod
    def call(cls, object_id, v, method="GET"):

        """
        Call an A
        :param object_name: the readyfor object name such like tags, projects, users...etc
        :param object_id: id of project or others
        :param v: api version (e.g. 'v2.8'
        :param method: http method.
        :param param: specify to get more information such like comments, news , from object page
        :param kwargs   : kwargs of page. e.g. page...etc
        :return: response
        """

        delta = datetime.now() - cls.queried_at
        time_to_sleep = timedelta(seconds=2.0) - delta
        params = {"fields": "engagement", "access_token": cls.facebook_token}
        params.update({"id": object_id})
        if delta < timedelta(seconds=2.0):
            time.sleep(time_to_sleep.seconds + time_to_sleep.microseconds * 10e-7)
        try:
            # User double curly-braces to tell python
            query = "{domain}/{v}".\
                format(domain=cls.QUERY_DOMAIN, v=v)
            cls.queried_at = datetime.now()
            return request(method=method, url=query, params=params)
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

