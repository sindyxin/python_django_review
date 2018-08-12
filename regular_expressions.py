import re #regular expression module

patterns = ['term1', 'term2']

text = "This is a string with term1, not the other"

for pattern in patterns:
  print(pattern)
  print("I'm searching for: "+ pattern)
  if re.search(pattern, text):
    print("Match")
  else:
    print("No Match")

# more example maybe add later

