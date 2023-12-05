'''
#initialising class
class Demo:
    #def a constructor
    def __init__(self,name):
        self.name = name
        print("Initialised value is",self.name)
#Driver code
obj1 = Demo("Hello")
obj1 = Demo("World")
obj1 = Demo("Hello World")
#sum of object
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
class Sum:
    def abc(obj,a,b):
        c = a+b
        print("Sum of a and b = ",c)
obj=Sum()
obj.abc(a,b)

#init fn
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
class Sum:
    def __init__(self,a,b):
        c = a+b
        print("Sum of a and b = ",c)
a=Sum(a,b)

a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
class Sum:
    def __init__(self,a,b):
        c = a+b
        self.a=a
        self.b=b
        print(a)
        print(b)
        print("Sum of a and b = ",c)
a=Sum(a,b)

#write a Python Program to Create a circle and calculate the perimeter and  area with the class and object?
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Create a Circle object
circle = Circle(radius)

# Calculate and display the area and perimeter
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print(f"Circle Area: {area:.2f}")
print(f"Circle Perimeter: {perimeter:.2f}")
'''
#Inheritance
class A:
    def first(obj):
        print("This is Base Class")
class B(A):
    def second(obj):
        print("This is Child Class")
class C(B):
    def third(obj):
        print("This is Derved Class")
obj=C()
obj.first()
obj.second()
obj.third()

''' QUESTION :- Write a Python Program create a circle as a parent class and 
 calculate area and circum pharanse and show the attributes and another 
 take a sphere as a child class and calculate volume and surface area'''
'''class Circle:
    def cal_circle(obj):
        obj.r=float("Enter the radius = ")
        area_c=3.14*obj.r*obj.r
        circum_c=2*3.14*obj.r
        print("Area and circumference of circle",area_c,circum_c)
class Sphere(Circle):
    def cal_sphere(obj):
        area_s=4*3.14*obj.r*obj.r
        volume_s=(4/3)*3.14*obj.r*obj.r*obj.r
        print("surface area and volume of sphere",area_s,volume_s)
obj=Sphere()
obj.cal_circle()
obj.cal_sphere() '''

''' QUESTION:- ankit is a competitive person and always try to compare him to other ,
he has got five subject in his course and he wants to make a list of total marks and 
average,marks of the student in his class with their roll numbers and he wants to use
concept of the multilevel inheritance and the contents are roll no should be 0 to 100 
marks also to be 0 to 100.'''
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] = max(0, self.items[item] - quantity)
            if self.items[item] == 0:
                del self.items[item]

    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            # Assuming price is provided for each item
            # You might want to extend this to include a dictionary of prices for different items
            total += quantity * self.get_item_price(item)
        return total

    def get_item_price(self, item):
        # In a real-world scenario, you might fetch the price from a database or another source
        # For simplicity, we'll assume a fixed price for each item here
        prices = {"item1": 10, "item2": 15, "item3": 20}  # You can extend this dictionary as needed
        return prices.get(item, 0)

# Example of using the ShoppingCart class
def main():
    cart = ShoppingCart()

    cart.add_item("item1", 2)  # Adding 2 quantities of item1
    cart.add_item("item2", 1)  # Adding 1 quantity of item2

    print("Current Items in Cart:", cart.items)
    print("Total Price:", cart.calculate_total())

    cart.remove_item("item1", 1)  # Removing 1 quantity of item1
    print("Updated Items in Cart:", cart.items)
    print("Total Price:", cart.calculate_total())

if __name__ == "__main__":
    main()
