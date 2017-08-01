# class holds the information for individual contacts and is the most basic block of the entire program
class Contact:
    def __init__(self, fN, lN, pN, eM):
        self.first_name = fN
        self.last_name = lN
        self.phone_num = pN
        self.email = eM

    def print_contact(self):
        print("Name: " + self.first_name + " " + self.last_name)
        print("Phone: " + self.phone_num)
        print("Email: " + self.email)
