import get_data


def get_users_data(data: dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    res = []
    for r in data['results']:
        info = {
            "first_name": r['name']['first'],
            "last_name": r['name']['last'],
            "phone_number": r['phone']
        }
        res.append(info)

    return res


print(get_users_data(get_data.get_data("randomuser_data.json")))
