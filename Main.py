import ContactBook as cb

# this is the main object for the whole contactbook
contacts = cb.ContactBook()

# String that holds the main menu for the program with the corresponding buttons for each command
main_menu = "C: Create Circle\nL: List Circles\nD: Delete Circle\nA: Add Contact\nR: Remove Contact\nV: View Contacts\nS: Search Contacts\nI: Import Circle\nE: Export Circle\nQ: Quit\n"

# each of the methods corresponds to an option in the main menu

# this method creates a circle of contacts
def create_circle():
    print("Enter the name of the circle:")
    name = input()

    print()
    
    print("Enter a brief desciption of the circle:")
    descrip = input()

    print()
    
    contacts.create_circle(name, descrip)

    print(name + " has successfully been created\n")
    
# this method simply lists out the circles that are in the contact list
def list_circles():
    contacts.list_circles()

# this routine deletes a given circle
def delete_circle():
    print("Enter the name of the circle you want to delete")
    name = input()

    print()
    
    contacts.delete_circle(name)

    print(name + " has been deleted")

# this method adds a contact to the circle that the user has chosen
def add_contact():
    list_circles() # here the circles are displayed so that the user can see all the circles they can add a condtact to

    print("Enter the name of the Circle you want to add a contact to:")
    name = input()

    target = contacts.get_circle(name)

    if target == None:
        print("That circle does not exist")
        return
    
    print("Enter the first name of the new contact:")
    first_name = input()
    
    if first_name == "":
        print("All contacts must have a first name.")
        return
    
    print("Enter the last name of the new contact:")
    last_name = input()

    # I decided to use a N/A placeholder for any empty fields that the user may leave but the first name field must be filled out
    if last_name == "":
        last_name = "N/A"
    
    print("Enter the phone number of the new contact:")
    phone = input()

    if phone == "":
        phone = "N/A"

    print("Enter the email of the new contact")
    email = input()

    if email == "":
        email = "N/A"
    
    target.add_contact(first_name, last_name, phone, email)
    print(first_name + " was added to " + name)

# this method simply removes a contact from the circle of the users choosing
def remove_contact():
    list_circles()

    print("Enter the name of the circle the contact is in:")
    name = input()

    target = contacts.get_circle(name)

    if target == None:
        print("The target was not found")
        return

    
    print("Enter the first name of the contact to delete:")
    first_name = input()

    if first_name == "":
        print("The contact must have a first name")
        return
    
    print("Enter the last name of the contact to delete:")
    last_name = input()

    if last_name == "":
        last_name == "N/A"
    
    target.delete_contact(first_name, last_name)
    print(first_name + " has been removed from " + name)

# this method displays every contact in the contactbook by dumping the contacts in each of the circles
def view_contacts():
    for circle in contacts.list_of_circles:
        circle.print_circle()
        circle.list_contacts()
        
# this method allows the user to search for a contact in the book based on their first or last name
# the searching will get multiple hits of contacts not just one and a query with only part of a name will yield acurate results
def search_contacts():
    print("Enter your search query:")
    query = input()

    if query == "":
        return

    for circle in contacts.list_of_circles:
        hit_list = circle.search_contact(query) 
        if len(hit_list) > 0:
            print(circle.name)
        for contact in hit_list:
            contact.print_contact()
            print()

# the following methods will be for the start up and shut down of the program

# this method reads the data from the circles from a textfile when the program starts up
def initalize_circles():
    the_file = open("circles.txt", "rt")
    lines = the_file.read().split("\n")

    for line in lines:
        if len(line) == 0:
            break
        info = line.split(":")
        contacts.create_circle(info[0], info[1])

    the_file.close()    

# this mehtod is just like initalize_circles but for the individual contacts that will be saved in their own textfile
def initalize_contacts():
    the_file = open("contacts.txt", "rt")
    lines = the_file.read().split("\n")

    index = 0

    for line in lines:
        if len(line) == 0:
            index += 1
            continue

        elif line == "pass":
            continue
        
        else:
            info = line.split(":")
            contacts.list_of_circles[index].add_contact(info[0], info[1], info[2], info[3])
    the_file.close()
    
# this method just calls initalize_circles and initalize_contacts consecutuivly 
def initalize():
    initalize_circles()
    initalize_contacts()    

# this method saves both the circles and the contacts into circles.txt and contacts.txt respectivly
# these two textfiles will be read when the program starts up again to get the data back into the program
def save():
    # save the list of circles
    the_file = open("circles.txt", "wt")

    for circle in contacts.list_of_circles:
        print(circle.name + ":" + circle.descrip, file=the_file)
    
    the_file.close()

    #save the list of contacts 
    the_file = open("contacts.txt", "wt")

    for circle in contacts.list_of_circles:
        if len(circle.list_of_contacts) == 0:
            print("pass\n", file=the_file)
        else:
            for contact in circle.list_of_contacts:
                print(contact.first_name + ":" + contact.last_name + ":" + contact.phone_num + ":" + contact.email, file=the_file)
            print(file=the_file)
            

    the_file.close()
    
# this is the main routine of the program where the user input is translated into the respective commands
    
initalize() # first we initalize the program reading in any of the users data from the other two textfiles
print(main_menu) # we then print the main menu for the user to see the commands

user_input = input().lower() # we then take in the user input and make it lower case

# this while loop takes care of all the operations that the user wants to do with the methods above
while True:
    if user_input == "c":
        create_circle()
    elif user_input == "l":
        list_circles()
    elif user_input == "d":
        delete_circle()
    elif user_input == "a":
        add_contact()
    elif user_input == "r":
        remove_contact()
    elif user_input == "v":
        view_contacts()
    elif user_input == "s":
        search_contacts()
    elif user_input == "q":
        save()
        break
        
    else:
        print("Invalid input")
    user_input = input().lower()
