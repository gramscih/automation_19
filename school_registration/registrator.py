class Registrator:
    def __init__(self, data_handler, name="Development"):
        self.name = name
        self.data_handler = data_handler
        self.students = []

    def register(self, student):
        # txt = TxtHandler()
        # txt.save_data(student)

        # csv = CsvHandler()
        # csv.save_data(str(student))
        self.data_handler.save_data(str(student))

    def get_data(self, data_handler, id):
        pass

