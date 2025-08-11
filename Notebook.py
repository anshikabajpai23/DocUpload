
class Notebook():

    def __init__(self,
                 name,
                 description):
        self.name = name
        self.description = description

    def print_all(self):
        return (f"name: {self.name} and description: {self.description}")
