# Strategy

from abc import ABC, abstractmethod

class DataHandler(ABC):
    # CRUD
    # C - Create
    # R - Read
    # U - Update
    # D - Delete

    @abstractmethod
    def save_data(self, data):
        pass
    
    # @abstractmethod
    # def read_data(self, id):
    #     pass
    
    # @abstractmethod
    # def update_data(self, id):
    #     pass
    
    # @abstractmethod
    # def delete_data(self, id):
    #     pass