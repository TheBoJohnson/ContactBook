import Circle

# class is what holds the list of circles together to become a contact book
class ContactBook:
    # the only instace field id the list holding the circles
    def __init__(self):
        self.list_of_circles = []

    # each of the following methods are pretty self explanatory and nake up most of the functionality
    # you see in Main.py
        
    def create_circle(self, n, d):
        self.list_of_circles.append(Circle.Circle(n, d))

    def delete_circle(self, n):
        for circle in self.list_of_circles:
            if circle.name == n:
                self.list_of_circles.remove(circle)

    def list_circles(self):
        for circle in self.list_of_circles:
            circle.print_circle()

    # get circle returns a reference to a specific circle in the contactbook which is useful for many operations
    def get_circle(self, name):
        for circle in self.list_of_circles:
            if circle.name == name:
                return circle

        return None


