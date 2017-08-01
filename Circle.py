import Contact

# this class holds a group of contacts together into a circle. The contact book is then made of a list of instances of this class
class Circle:
    def __init__(self, n, d):
        # each circle will have a name, a short description, and then the list that holds all of the contacts in the circle
        self.name = n
        self.descrip = d
        self.list_of_contacts = []
    # method adds a contact with a simple call to the contact constructor then appends the contact to the end of the list
    def add_contact(self, fN, lN, pN, eM):
        self.list_of_contacts.append(Contact.Contact(fN, lN, pN, eM))

    # method deletes a contact from the circle based on the first and last names
    def delete_contact(self, fN, lN):
        for contact in self.list_of_contacts:
            if contact.first_name == fN and contact.last_name == lN:
                self.list_of_contacts.remove(contact)

    # method allows you to search for a contact based on a query
    def search_contact(self, query):
        hit_list = []
        for contact in self.list_of_contacts:
            if contact.first_name.find(query) != -1 or contact.last_name.find(query) != -1:
                hit_list.append(contact)
        return hit_list

    # method allows you to print a quick overview of the circle (the circle's name, description, and the number of contacts in that circle)
    def print_circle(self):
        print(self.name + "\n" + self.descrip + "\n" + str(len(self.list_of_contacts)))
        
    # method lists all the contacts that are currently in the circle 
    def list_contacts(self):
        for contact in self.list_of_contacts:
            contact.print_contact()
            print()
