from exceptions import CustomException


class Validations:
    @staticmethod
    def check_file_path(filepath):
        if filepath is None:
            raise CustomException("Please provide the file path in the arguments.")

    @staticmethod
    def check_language(language):
        if language is None:
            raise CustomException("Language with extension {} is not supported".format(language))

    @staticmethod
    def not_file_or_directory(path):
        if path is None:
            raise CustomException("{} is neither a valid file nor a directory.".format(path))



