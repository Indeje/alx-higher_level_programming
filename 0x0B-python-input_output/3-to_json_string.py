#!/usr/bin/python3

""" Convert Python object (string) to JSON string """


import json

def to_json_string(my_obj):

    """
        Returns JSON string representation of an object (string)
    """

    return json.dumps(my_obj)
