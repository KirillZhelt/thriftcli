import json_request_body_converter
import java_thrift_request_body_converter

CONVERTERS = [
    json_request_body_converter,
    java_thrift_request_body_converter
]


def convert(request_body):
    """ Converts the request body into an argument dictionary.

    :param request_body: The request body
    :type request_body: str
    :returns: The argument dictionary represented by the request body
    :rtype: dict

    """
    for converter in CONVERTERS:
        try:
            return converter.convert(request_body)
        except ValueError:
            pass
    raise ValueError("Request body is in an unknown format.")

