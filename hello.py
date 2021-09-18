
# importing date class from datetime module
from datetime import date

# creating the date object of today's date
todays_date = date.today()

print("Hello Python")

# List is the most basic Data Structure in python.
# List is a mutable data structure i.e items can be added to list later after the list creation.

# creates a empty list
nums = [] 
  
# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")
  
# print(nums)

# Python program to illustrate
# functions
def hello():
    name = input("Enter your name: ")
    result = int(input("Enter year of birth: "))
    print("Hello", name)
    print("your are", todays_date.year -result,"years old" )

def countSubstrings():
    # string in which occurrence will be checked
    string = "geeks for geeks" 
    
    # counts the number of times substring occurs in 
    # the given string and returns an integer
    print(string.count("geeks"))

def Main():
    hello()
    

if __name__=="__main__":
    Main()