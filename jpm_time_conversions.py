import numpy as np
import datetime

__author__ = "James Paul Mason"
__contact__ = "jmason86@gmail.com"


def sod_to_hhmmss(sod):
    """Convert seconds of day to 'hh:mm:ss'.

    Inputs:
        sod [np.array]: The array of seconds of day to convert.

    Optional Inputs:
        None.

    Outputs:
        hhmmss [np chararray]: Array of strings of the form 'hh:mm:ss'.

    Optional Outputs:
        None.

    Example:
        hhmmss = sod_to_hhmmss(sod)
    """

    # Parse seconds of day into hours, minutes, and seconds
    time = sod % (24 * 3600)
    time = time.astype(int)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    # Convert to string type and add leading zeros
    hours_str = hours.astype(str)
    small_hour_indices = hours < 10
    hours_str[small_hour_indices] = np.core.defchararray.zfill(hours_str[small_hour_indices], 2)

    minutes_str = minutes.astype(str)
    small_minute_indices = minutes < 10
    minutes_str[small_minute_indices] = np.core.defchararray.zfill(minutes_str[small_minute_indices], 2)

    seconds_str = seconds.astype(str)
    small_second_indices = seconds < 10
    seconds_str[small_second_indices] = np.core.defchararray.zfill(seconds_str[small_second_indices], 2)

    return np.char.array(hours_str) + ':' + np.char.array(minutes_str) + ':' + np.char.array(seconds_str)


def yyyydoy_to_datetime(yyyydoy):
    """Convert yyyydoy (e.g., 2017013) date to datetime (e.g., datetime.datetime(2017, 1, 13, 0, 0)).

    Inputs:
        yyyydoy [np.array]: The array of dates to convert.

    Optional Inputs:
        None.

    Outputs:
        dt_array [np.array]: Array of datetimes.

    Optional Outputs:
        None.

    Example:
        dt_array = yyyydoy_to_yyyymmdd(yyyydoy)
    """

    # Parse year and doy
    parsed_date = np.modf(yyyydoy / 1000)  # Divide to get yyyy.doy

    # Convert to array of yyyymmdd datetimes and return
    return np.array([datetime.datetime(int(parsed_date[1][i]), 1, 1) +           # base year (yyyy-01-01)
                     datetime.timedelta(days=int(parsed_date[0][i] * 1000) - 1)  # doy -> mm-dd
                     for i in range(len(yyyydoy))])                              # loop over input array
