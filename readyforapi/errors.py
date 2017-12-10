__author__ = 'TOSUKUi'
from requests.exceptions import *


class APIException(Exception):
    """
    Base class for all API exception
    """
    pass


class ProjectPageEndException(APIException):
    """
    An error caused by crawl ended and hided project page
    """
    pass


class ProjectPageNotPublishedException(APIException):
    """
    An error caused by crawl when project is not published 
    """
    pass


class APIProjectError(APIException):
    """
    An API error caused by a project error, like a html format is changed or html
    """
    pass


class HtmlParseException(APIException):
    """
    An Api error caused by parser error
    """
    pass


class ProjectPageTabParseException(HtmlParseException):
    """
    An html parse error caused by parser error of project tab.
    """
    pass


class ProjectNotFoundError(APIProjectError):
    """
    The specified project aws not found on the readyfor. (Bad vanity URL? Non-existent ID?)
    """
    pass


class ProjectCommentsPageBackersZeroException(APIProjectError):
    """
    An error cause when comments page backers count is 0 
    """


class AccessException(RequestException):
    """
    An error caused by page access error, like access denied by readyfor.
    """
    pass


class PageAccessException(AccessException):
    """
    An error caused by 4** error, for example, page not found.
    """