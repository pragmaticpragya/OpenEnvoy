from exceptions.custom_exception import CustomException


class Validations:
    @staticmethod
    def check_file_path(filepath):
        print("filepath", filepath)
        if filepath is None:
            raise CustomException("Please provide the file path in the arguments.")

    @staticmethod
    def check_language(language):
        print("language", language)
        if language is None:
            raise CustomException("Language with extension {} is not supported".format(language))

    @staticmethod
    def not_file_or_directory(filepath):
        print("filepath", filepath)
        raise CustomException("{} is neither a valid file nor a directory.".format(filepath))

    @staticmethod
    def check_syntax(language):
        print("language", language)
        raise CustomException("{} is not a valid language.".format(language))





