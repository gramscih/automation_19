from data_handler import DataHandler

class CsvHandler(DataHandler):
    def __init__(self):
        super().__init__()
        self.file = 'Students.csv'
        
    def save_data(self, data):
        with open(self.file, 'w') as txt_file:
            txt_file.write(str(data))