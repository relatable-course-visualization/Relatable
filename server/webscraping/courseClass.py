# A class for a course


class Course:
    def __init__(self, code, name, description, prerequisite, restricition, link):
        self.name = name
        self.code = code
        self.description = description
        self.prerequisite = prerequisite
        self.restriction = restricition
        self.link = link

