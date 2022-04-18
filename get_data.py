import json


def get_data(filename: str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    data = open(filename, encoding='utf-8')
    return json.load(data)


print(get_data("randomuser_data.json"))
