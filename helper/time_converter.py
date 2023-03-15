from datetime import datetime, timedelta


def timestamp_to_seconds(timestamp: str) -> int:
    """
    Converts a timestamp in various formats to seconds from 8:00 am.

    Args:
        timestamp (str): A timestamp in various formats (e.g., "HH:MM", "HH:MM:SS", "HH:MM AM/PM", "HHMM")

    Returns:
        int: The number of seconds from 8:00 am

    Time complexity: O(1)
    Space complexity: O(1)
    """
    # Define the possible timestamp formats
    formats = ["%H:%M", "%H:%M:%S", "%I:%M %p", "%I:%M:%S %p", "%H%M"]
    # Iterate through the formats and try to parse the input timestamp
    for fmt in formats:
        try:
            # Parse the timestamp using the current format
            dt = datetime.strptime(timestamp, fmt)
            # Calculate the total number of seconds in the timestamp
            total_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second
            # Calculate the number of seconds from 8:00 am
            seconds_from_8am = total_seconds - 8 * 3600
            return seconds_from_8am
        except ValueError:
            # If parsing fails, try the next format
            continue
    # If none of the formats match, raise an error
    raise ValueError("Invalid timestamp format")


def seconds_to_time(seconds: int) -> str:
    """
    Converts an integer representing the number of seconds from 8:00 am to a string in the format "HH:MM AM/PM".

    Args:
        seconds (int): The number of seconds from 8:00 am

    Returns:
        str: A timestamp in the format "HH:MM AM/PM"

    Time complexity: O(1)
    Space complexity: O(1)
    """
    # Create a datetime object for 8:00 am
    base_time = datetime.strptime("08:00:00", "%H:%M:%S")
    # Calculate the time passed since 8:00 am using the input seconds
    time_passed = timedelta(seconds=seconds)
    # Add the time passed to the base time (8:00 am) to get the new time
    new_time = base_time + time_passed
    # Return the new time formatted as "HH:MM AM/PM"
    return new_time.strftime("%I:%M %p")
