class YTViewsTrackerException(Exception):
    """Base exception for YouTube Views Tracker"""


class UrlFileDoesNotExistError(YTViewsTrackerException):
    """Not existing url file exception"""


class UnsupportedUrlFileError(YTViewsTrackerException):
    """Unsupported file extension for url file"""


class EmptyUrlListError(YTViewsTrackerException):
    """Empty url list exception"""


class UnsupportedOutputFileError(YTViewsTrackerException):
    """Unsupported output file exception"""


class MissingShareMailError(YTViewsTrackerException):
    """Missing share mail exception"""


class UnsupportedConfigFileError(YTViewsTrackerException):
    """Unsupported config file exception"""


class UnsupportedScheduleOptionError(YTViewsTrackerException):
    """Unsupported schedule option exception"""
