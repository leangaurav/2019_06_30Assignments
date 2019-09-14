from contact import Contact
from sql_handler import SQLHandler
import copy

class ContactManager:
    def __init__(self):
        self.sql_mgr = SQLHandler('contact.db')
        self.contacts = self.sql_mgr.get_contacts()
    
    def __get_index_by_name(self, name):
    
        for i, data in enumerate(self.contacts):
            if data.name.lower() == name.lower():
                return i
                
        return -1
                
        
    def find_by_name(self, name):
        # TODO: write logic
        pass
        
    def search_contacts(self, pattern):
        # TODO: write logic
        pass
    
    def get_contacts(self):
        # TODO: write logic
        pass
    
    def add_contact(self, contact_data):
        res = self.sql_mgr.add_contact(contact_data)
        
        if res:
            self.contacts.append(contact_data)
            
        return res
    
    def delete_contact(self, contact_name):
        res = self.sql_mgr.delete_contact(contact_name)
        
        if res:
            idx = self.__get_index_by_name(contact_name)
            if idx != -1:
                self.contacts.pop(idx)

        return res
    
    def update_name(self, name, new_name):
        # TODO: write logic
        pass

    def update_phone(self, name, new_phone):
        # TODO: write logic
        pass

    def update_email(self, name, new_email):
        # TODO: write logic
        pass