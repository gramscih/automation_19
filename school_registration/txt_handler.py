# Concrete Strategy

from data_handler import DataHandler

class TxtHandler(DataHandler):
    def __init__(self):
        super().__init__()
        self.file = 'Students.txt'
    
    def save_data(self, data):
        with open(self.file, 'w') as txt_file:
            txt_file.write(str(data))