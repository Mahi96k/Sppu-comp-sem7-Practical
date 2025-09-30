import re
def matchre(data, *args):
  for regstr in args:
    matchObj = re.search(regstr + '.*', data, re.M | re.I)
    if matchObj:
      print(matchObj.group(0).lstrip().rstrip())
    else:
      print("No" , regstr, "found")
print("Email Header Program by Mahesh Chelekar")
filename = input("Enter path for email header file\n")
try:
  with open(filename, "r" ) as fo:
    data = fo.read()
    matchre(data, "MIME-version", "Date:", "Subject:", "delivered-to;", "From:", "^to:")
except FileNotFoundError:
  print(f"Error: The File '{filename}' was not found.")
except Exception as e:
  print(f"An Error occurred : {e}")
