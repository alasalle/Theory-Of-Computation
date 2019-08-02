import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# Define your regex

while line != "exit":
    # Find matches
    match = re.finditer(r'(?:\(?(?:(?P<areacode>[0-9]{3})\)?))(-| ?)(?:(?P<prefix>[0-9]{3})(-| ?)(?P<suffix>[0-9]{4}))', line)
    
    # If no match found, print that no number was found
    if not match:
        print("No number found!")
   
    
    # Else, break number up into area code, prefix, and suffic
    else:
        for m in match:
             print(f"Area Code: {m.group('areacode')}\nPrefix: {m.group('prefix')}\nSuffix: {m.group('suffix')}")
    
    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")