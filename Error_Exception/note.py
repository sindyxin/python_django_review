try:
  f = open("simple.txt", "w")
  f.write("Test write to simple text!")
except IOError:
  print("Error: Could not find file or read data!")
else:
  print("Success!")
  f.close()

try:
  f = open("simple.txt", "r")
  f.write("Test write to simple text!")
except IOError:
  print("Error: Could not find file or read data!")
finally:
  print("I always work no matter what!")
  f.close()