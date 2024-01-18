import csv
import os.path

class repository:
    def __init__(self, full_file_Path):
        self.full_file_Path = full_file_Path
    
    def add(self ,contact):
        headers = [h for h in contact]
        headers.sort()
        write_headers = not os.path.isfile(self.full_file_Path)
        with open(self.full_file_Path, "a+") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            if write_headers:
                writer.writeheader()
            writer.writerow(contact)

    def names(self):
        with open(self.full_file_Path, "r+") as file:
            names = list(map(lambda r: r["name"], csv.DictReader(file)))
            return names
        
    def full_contact(self, name):
        with open(self.full_file_Path, "r+") as file:
            for contact in list(csv.DictReader(file)):
                if contact["name"] == name:
                    return contact
            return
        

class main:

    def __init__(self, contact_name):
        self.repo = repository(contact_name)

    def create(self):
        name = input("Name: ")
        number = input("Number: ")
        contact = { "name": name, "number" : number}
        self.repo.add(contact)

    def names(self):
        names = self.repo.names()
        if len(names) > 0:
            for n in names:
                print("- {}".format(n))
        else:
            print("no contacts were found")

    def full_contact(self):
        name = input("name: ")
        contact = self.repo.full_contact(name)
        if contact is not None:
            print("name: {}".format(contact["name"]))
            print("number: {}".format(contact["number"]))
        else:
            print("contact not found.")

    def menu(self):
        actions = {"1": self.create, "2": self.names, "3": self.full_contact}
        options = ["1) Create Contact", "2) All Contacts", "3) Detail of a contact", "0) Exit"]
        for o in options:
            print(o)
        selected = input("What do you want to do? ")
        if selected in actions:
            actions[selected]()
            self.menu()


main("contacts.csv").menu()