# A class for a course


class Course:
    def __init__(self, code, name, description, prerequisite, restricition, link):
        self.code = code
        self.name = name
        self.description = description
        self.prerequisite = prerequisite
        self.restriction = restricition
        self.link = link

    def getCode(self):
        return '{}'.format(self.code)
    
    def getName(self):
        return '{}'.format(self.name)

    def getDecription(self):
        return '{}'.format(self.description)

    def getPrerequisite(self):
        return '{}'.format(self.prerequisite)


