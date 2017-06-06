from requests import request
from .errors import *
from datetime import datetime, timedelta
import time
from inflector import Inflector

class ReadyForConnection(object):
    queried_at = datetime.now()
    inflicter = Inflector()
    QUERY_DOMAIN = "http://readyfor.jp"

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
        time_to_sleep = timedelta(seconds=1) - delta
        if delta < timedelta(seconds=1):
            time.sleep(time_to_sleep.seconds)
        try:
            # User double curly-braces to tell python
            objects_name = cls.inflicter.pluralize(object_name)
            query = "{domain}/{objects_name}/{id}/{sub_object}".format(domain=cls.QUERY_DOMAIN, objects_name=objects_name, id=object_id, sub_object=sub_object)
            if sub_object is None:
                query = "{domain}/{objects_name}/{id}".format(domain=cls.QUERY_DOMAIN,
                                                              objects_name=objects_name,
                                                              id=object_id)
            cls.queried_at = datetime.now()
            return request(method=method, url=query, params=kwargs)
        except:
            raise AccessException("some problem occurred when access")


class FacebookGraphConnection(object):
    queried_at = None
    QUERY_DOMAIN = "https://graph.facebook.com"

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
            query = "{domain}/{{v}}/{{id}}".\
                format(domain=cls.QUERY_DOMAIN, v=v, id=object_id)
            cls.queried_at = datetime.now()
            return request(method=method, url=query, params=kwargs)
        except:
            raise AccessException("some problem occurred when access")



class ReadyForResponse(object):
    inflicter = Inflector()

    def __init__(self, father_html, object_name, sub_object):
        parser_class_snake = "{{object_name}}_{{sub_object}}_page_parser". \
            format(object_name=object_name, sub_object=sub_object)
        parser_class_camel = self.inflicter.camelize(word=parser_class_snake)
        self.str_to_cls(parser_class_camel)(father_html)


    @classmethod
    def str_to_cls(cls, class_name):
        global_symbol_table = globals()
        return global_symbol_table[class_name]


class ReadyForObject(object):
    """
    A base class for all rich ReadyFor objects.
    """

    @property
    def id(self):
        return self._id #"_id" is set by the child class

    def __repr__(self):
        try:
            return '<{clsname} "{name}" ({id})>'.format(
                clsname=self.__class__.__name__,
                name=self.name,
                id=self._id
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

