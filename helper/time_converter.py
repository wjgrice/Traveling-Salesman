def timestamp_to_seconds(timestamp: str) -> int:
    """
    Converts a timestamp in the format "HH:MM" to seconds from 8:00 am.

    :time complexity: O(1)
    :param timestamp: A timestamp in the format "HH:MM"
    :return: The number of seconds from 8:00 am

    """
    hours, minutes = timestamp.split(":")
    total_minutes = int(hours) * 60 + int(minutes)
    seconds_from_8am = (total_minutes - 480) * 60
    return seconds_from_8am


def seconds_to_time(seconds: int) -> str:
    """
    Converts an integer representing the number of seconds from 8:00 am to a string in the format "HH:MM".

    :time complexity: O(1)
    :param seconds: The number of seconds from 8:00 am
    :return: A timestamp in the format "HH:MM"

    """
    hours = seconds // 3600  # 3600 seconds in an hour
    minutes = (seconds % 3600) // 60  # 60 minutes in an hour
    return "{:02d}:{:02d}".format(hours + 8, minutes)
