from datetime import datetime


def format_timestamp(timestamp_str):
    timestamp = datetime.fromisoformat(timestamp_str[:-1])  # Remove the 'Z' character
    formatted_timestamp = timestamp.strftime('%-m/%-d/%y at %-I:%M:%S %p')
    return formatted_timestamp
