import os


# A class for creating objects for managing files containing logging data
class FileManager:
    def store(self, value_type, value):
        """
        This Function is one of the FileManager class functions
        parameters:
        value: it gets some input from from Main module as a value
        value_type: askes
        """
        folder_path = (os.path.dirname(__file__)).replace("Classes", "Data\\{}")
        print(folder_path)
        writing_format = "\n{}"

        if value_type == "temperature":
            try:
                with open(folder_path.format("temperature_data.txt"), "a") as file:
                    file.write(writing_format.format(value))

            except FileNotFoundError as error_description:
                return True, error_description, "That file was not found"

            except Exception as error_description:
                return True, error_description, "un-expected exception"

            else:
                return False, "temperature saved"

        if value_type == "humidity":
            try:
                with open(folder_path.format("humidity_data.txt"), "a") as file:
                    file.write(writing_format.format(value))

            except FileNotFoundError as error_description:
                return True, error_description, "That file was not found"

            except Exception as error_description:
                return True, error_description, "un-expected exception"

            else:
                return False, "humidity saved"


# -------------------------------------------------------------------------
# Notes:
# folder_path = "C:\\Users\\h.ramezani.MBACO.000\\Desktop\\python practice\\python termal controller project\\Data\\{}"
