__author__ = "James Paul Mason"
__contact__ = "jmason86@gmail.com"


def sod_to_hhmmss(sod):
    """Convert seconds of day to 'hh:mm:ss'

    Inputs:
        sod [np.array]: The array of seconds of day to convert.

    Optional Inputs:
        None

    Outputs:
        hhmmss [list]: List of strings of the form 'hh:mm:ss'

    Optional Outputs:
        None

    Example:
        hhmmss = sod_to_hhmmss(sod)
    """
    time = sod % (24 * 3600)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    hour_str = []
    for hour in hours:
        if hour < 10:
            hour_str.append('0' + str(int(hour)))
        else:
            hour_str.append(str(int(hour)))

    minute_str = []
    for minute in minutes:
        if minute < 10:
            minute_str.append('0' + str(int(minute)))
        else:
            minute_str.append(str(int(minute)))

    second_str = []
    for second in seconds:
        if second < 10:
            second_str.append('0' + str(int(second)))
        else:
            second_str.append(str(int(second)))

    return hour_str + ':' + minute_str + ':' + second_str
