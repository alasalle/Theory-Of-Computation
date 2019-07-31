import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# Read HTML file
html_file = open(filename, 'r')
source_code = html_file.read() 


# Set up regex
matches = re.findall('[\"\'](http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)[\"\']', source_code)

# for item in matches:
#   print(item)


# Find links using regex, save in list called 'matches'


# Check matches, print results
# Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'

answer_data = list()
with open('answers.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
      for link in row:
        # if link not in matches:
        #   print(f"Link not found in matches: {link}")
        answer_data.append(link)

for item in answer_data:
  print(item)

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )