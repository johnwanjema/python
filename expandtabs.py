# Sometimes, there is a need of specifying the space in the string, but the amount of space to be left
# is uncertain and depending upon the environment and conditions. For these cases, the need to modify 
# the string, again and again, is a tedious task. Hence python in its library
# has “expandtabs()” which specifies the amount of space to be substituted with the “\t” symbol in the string.

# initializing string 
str = "i\tlove\tgfg"


# using expandtabs to insert spacing
print("Modified string using default spacing: ", end ="")
print(str.expandtabs())
  
print("\r")
  
# using expandtabs to insert spacing
print("Modified string using less spacing: ", end ="")
print(str.expandtabs(2))
  
print("\r")
  
# using expandtabs to insert spacing
print("Modified string using more spacing: ", end ="")
print(str.expandtabs(12))
  
print("\r")