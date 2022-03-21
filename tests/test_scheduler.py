import pytest
import schedule

from exceptions import UnsupportedScheduleOptionError
from scheduler import ScheduleInterval, convert_interval, setup_schedule


def test_scheduler_fail_with_invalid_value():

    with pytest.raises(UnsupportedScheduleOptionError):
        setup_schedule("13:333", lambda: None, None)


def test_scheduler_with_unsupported_option():

    with pytest.raises(UnsupportedScheduleOptionError):
        setup_schedule("HOUR13", lambda: None, None)


@pytest.mark.parametrize(
    "interval,resulting_enum",
    [
        ("MIN10", ScheduleInterval.MIN10),
        ("MIN15", ScheduleInterval.MIN15),
        ("MIN30", ScheduleInterval.MIN30),
        ("HOUR1", ScheduleInterval.HOUR1),
        ("HOUR3", ScheduleInterval.HOUR3),
        ("HOUR6", ScheduleInterval.HOUR6),
        ("HOUR8", ScheduleInterval.HOUR8),
        ("HOUR12", ScheduleInterval.HOUR12),
        ("13:42", ScheduleInterval.HHMM),
    ],
)
def test_scheduler_convert_interval_with_supported_option(interval, resulting_enum):

    assert convert_interval(interval) == resulting_enum


@pytest.mark.parametrize("interval", ["MIN10", "HOUR3", "13:42"])
def test_scheduler_with_supported_option(capfd, interval):

    setup_schedule(interval, lambda: True, None)

    _, err = capfd.readouterr()

    assert "Setting scheduler to run" in err
    assert len(schedule.jobs) == 1

    schedule.clear()
