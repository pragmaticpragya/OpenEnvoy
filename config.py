class Config:

    def __init__(self):
        self.language_comments_map = {
            "java": {"comments": ['//', '/*'], "import_vars": ["import"], "extension": ".py"},
            "python": {"comments": ['#'], "import_vars": ["import", "from"], "extension": ".java"}
        }
