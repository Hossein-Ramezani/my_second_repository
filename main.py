# This is a program that gets and manages date coming from the thermal controller (tcw122B-CM_R1)
from Classes.FileManager import FileManager
import functions as func
from os import system
import sched, time

system("cls")


file_manager = FileManager()


# Value initialization:


# controller_id / controller_address
controllers = {
    "controller_1": "http://192.168.1.252/status.xml.kjgjh",
    "controller_2": "http://192.168.1.252/status.xml",
    "controller_3": "http://192.168.1.252/status.xml",
}


def get_sensor_info(
    controllers_addresses: dict, requested_controllers: tuple = (), all=False
):
    """
    this function will get the sensor information with help of other functions within the functions module
    steps:
    1- Checking for "all" value and making a tuple of all controllers if equalled to True
    2- Calling each URL and getting the resualt as a tuple containing XML file and error status
    3- Trying to get the temperature value out of the XML value and making records of succesion of the operation
    4- Trying to get the humidity value out of the XML value and making records of succesion of the operation
    5- returning a tuple of un-successful operations in case of falier
    """
    if all == True:
        controller_list = list()
        for controller_id, controller_address in controllers_addresses.items():
            controller_list.append((controller_id, True, True))
        requested_controllers = tuple(controller_list)

    status_list = []
    controller_id = None
    controller_address = None

    for (
        controller_id,
        requested_temperature,
        requested_humidity,
    ) in requested_controllers:
        confirm_temperature = requested_temperature
        confirm_humidity = requested_humidity
        temp_humidity = None
        temperature_calling_result = None

        if (xml := func.url_catch(controllers_addresses.get(controller_id)))[0]:
            func.print_error(xml[1], xml[2])
            status_list.append((controller_id, confirm_temperature, confirm_humidity))
            continue

        if requested_temperature:
            if not (temperature_calling_result := func.temperature_separator(xml[1]))[
                0
            ]:
                if status := file_manager.store(
                    "temperature", temperature_calling_result[1]
                )[0]:
                    func.print_error(status[1], status[2])
                else:
                    confirm_temperature = False
                    print(temperature_calling_result[1])
            else:
                func.print_error(
                    temperature_calling_result[1], temperature_calling_result[2]
                )

        if requested_humidity and (
            status := file_manager.store(
                "humidity", temp_humidity := func.humidity_separator(xml[1])
            )[0]
        ):
            func.print_error(status[1], status[2])
        else:
            confirm_humidity = False
            print(temp_humidity)

        if confirm_humidity or confirm_temperature:
            status_list.append((controller_id, confirm_temperature, confirm_humidity))

    return tuple(status_list)


if failed_controllers := get_sensor_info(controllers, all=True):
    print(failed_controllers)


# ===============================================================
# NOTES:

# # Trying to get the temperature value out of the HTML string
# try:
#     file_manager.store(func.temperature_separator(html))
# except Exception as error_description:
#     print(error_description)
#     # func.print_error(error_description, "exception occured!")


# # try and except for sepearation and storing of the temperature and humidity values
# try:
#     file_manager.store("temperature", temperature_calling_result := func.temperature_separator(xml[1]))
# except Exception as error_description:
#     func.print_error(
#         error_description,
#         f'an unexpected exception occured while getting temperature from controller: "{controller_id}"',
#     )
# else:
#     confirm_temperature = 0
#     print(temperature_calling_result)

# try:
#     file_manager.store("humidity", temp_humidity := func.humidity_separator(xml[1]))
# except Exception as error_description:
#     func.print_error(
#         error_description,
#         f'an unexpected exception occured while getting humidity from controller: "{controller_id}"',
#     )
# else:
#     confirm_humidity = 0
#     print(temp_humidity)
