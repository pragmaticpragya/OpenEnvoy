class Config:

    PYTHON = "python"
    JAVA = "java"

    def __init__(self):
        self.language_comments_map = {
                        "java": {"comments": ['//', '/*']},
                        "python": {"comments": ['#']}
        }

