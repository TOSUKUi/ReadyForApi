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


class APIProjectError(APIException):
    """
    An API error caused by a project error, like a html format is changed or html
    """
    pass


class ProjectNotFoundError(APIProjectError):
    """
    The specified project aws not found on the readyfor. (Bad vanity URL? Non-existent ID?)
    """
    pass


class AccessException(RequestException):
    """
    An error caused by page access error, like access denied by readyfor.
    """
    pass

class PageAccessException(AccessException):
    """
    An error caused by 4** error, for example, page not found.
    """