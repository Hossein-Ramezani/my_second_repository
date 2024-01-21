import urllib.request
import re


def temperature_separator(xml):
    """
    Getting the XML string and separating the temperature value from it
    """
    try:
        value = re.search("<Temperature1>([^<]*)&#176;C</Temperature1>", xml)[1]
    except Exception as error_description:
        return (
            True,
            error_description,
            "there was an error while separating temperature value",
        )
    else:
        return False, value


def humidity_separator(xml):
    """
    Getting the XML string and separating the humidity value from it
    """
    return re.search("<Humidity1>([^<]*)%RH</Humidity1>", xml)[1]


def url_catch(url_):
    """
    Function for calling the controller URL and returning a tuple
    containing error report
    if no error: (False, xml_file)
    if there was an error: (True, error_exception, message)
    """
    try:
        with urllib.request.urlopen(url_) as response:
            xml = str(response.read())

    except Exception as error_description:
        return True, error_description, 'There was an error in function "url_catch"'

    else:
        return False, xml


def print_error(exception_description, message):
    """
    Getting both message and exception description and printing iformation in the desired format
    """
    print(message, "exception error: ", exception_description, sep="\n", end="\n\n")


# ----------------------------------------------------------------------------------------
# NOTES:
# temp_elem_tags = "<Temperature1>", "</Temperature1>"
# y = html[html.find(temp_elem_tags[0]) + 14 : html.find(temp_elem_tags[1])].replace(
#     "&#176;C", ""
# )

# opening_tag_location = html.find(temp_elem_tags[0]) + 14
# closing_tag_location = html.find(temp_elem_tags[1])
# temperature = html[opening_tag_location : closing_tag_location]
# temperature = temperature.replace("&#176;C", "")
# return temperature


# humdt_elem_tags = "<Humidity1>", "</Humidity1>"
# return xml[
#     xml.find(humdt_elem_tags[0]) + 11 : xml.find(humdt_elem_tags[1])
# ].replace("%RH", "")
