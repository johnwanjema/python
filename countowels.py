
# Python code to count and display number of vowels
# Simply using for and comparing it with a
# string containing all vowels
def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    #print length
    print(len(final))
    print(final)
     


def Main():
   # Driver Code
    string = "Geeks for Geeks"
    vowels = "AaEeIiOoUu"
    Check_Vow(string, vowels)
    

if __name__=="__main__":
    Main()

