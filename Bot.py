class Bot:
    def __init__(self, id, name, type, cookie, headers, filter):
        """Constructor"""
        self.filter = filter
        self.headers = headers
        self.cookie = cookie
        self.id = id
        self.name = name
        self.type = type

