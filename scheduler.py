from enum import Enum, auto
from typing import Callable

import schedule

from exceptions import UnsupportedScheduleOptionError
from utils import logger


class ScheduleInterval(Enum):

    MIN10 = auto()
    MIN15 = auto()
    MIN30 = auto()
    HOUR1 = auto()
    HOUR3 = auto()
    HOUR6 = auto()
    HOUR8 = auto()
    HOUR12 = auto()
    HHMM = auto()


def convert_interval(interval: str) -> ScheduleInterval:
    """Convert interval argument to enum value

    Raises UnsupportedScheduleOptionError if an unsupported option is given.

    :type interval: str
    :param interval: Interval to run script
    :rtype: ScheduleInterval
    :returns: ScheduleInterval enum value
    """

    scheduled_interval = None

    if interval == "MIN10":
        scheduled_interval = ScheduleInterval.MIN10
    elif interval == "MIN15":
        scheduled_interval = ScheduleInterval.MIN15
    elif interval == "MIN30":
        scheduled_interval = ScheduleInterval.MIN30
    elif interval == "HOUR1":
        scheduled_interval = ScheduleInterval.HOUR1
    elif interval == "HOUR3":
        scheduled_interval = ScheduleInterval.HOUR3
    elif interval == "HOUR6":
        scheduled_interval = ScheduleInterval.HOUR6
    elif interval == "HOUR8":
        scheduled_interval = ScheduleInterval.HOUR8
    elif interval == "HOUR12":
        scheduled_interval = ScheduleInterval.HOUR12
    elif ":" in interval:
        scheduled_interval = ScheduleInterval.HHMM
    else:
        raise UnsupportedScheduleOptionError("Unsupported schedule option!")

    return scheduled_interval


def setup_schedule(interval: str, task: Callable, task_args: "Namespace") -> None:  # noqa: F821
    """Setup schedule for the script

    Raises UnsupportedScheduleOptionError if schedule setting fails.

    :type interval: str
    :param interval: Interval to run script
    :type task: Callable
    :param task: Task to run
    :type task_args: Namespace
    :param task_args: Command line args returned by ArgumentParser
    """

    scheduled_interval = convert_interval(interval)

    try:
        if scheduled_interval in (
            ScheduleInterval.MIN10,
            ScheduleInterval.MIN15,
            ScheduleInterval.MIN30,
        ):
            minute = int(interval[3:])
            logger.info(f"Setting scheduler to run in every {minute} minutes...")
            schedule.every(minute).minutes.do(task, task_args)

        elif scheduled_interval in (
            ScheduleInterval.HOUR1,
            ScheduleInterval.HOUR3,
            ScheduleInterval.HOUR6,
            ScheduleInterval.HOUR8,
            ScheduleInterval.HOUR12,
        ):
            hour = int(interval[4:])
            logger.info(f"Setting scheduler to run in every {hour} hours...")
            schedule.every(hour).hours.do(task, task_args)

        else:
            hour_minute = interval
            logger.info(f"Setting scheduler to run every day at {hour_minute}...")
            schedule.every().day.at(hour_minute).do(task, task_args)

    except schedule.ScheduleError:
        raise UnsupportedScheduleOptionError("Failed to set schedule!")
