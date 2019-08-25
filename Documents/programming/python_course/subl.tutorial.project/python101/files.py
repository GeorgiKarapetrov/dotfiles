#files.py
import os
path = os.getcwd()
for entry in os.scandir(path):
   if not entry.name.startswith('.') and entry.is_file():
       print(entry.name)

with open("new_test_file.py", "w") as f:
    f.write("def a(): pass")

f = open("new_test_file.py", "r")
f.read()
f.close()

f = open("new_test_file.py", "r")
f.readlines()

with open("new_test_file.py", "a") as f:
    f.write("print(a())")

if __name__ == "__main__":
    print("In {0} module".format(__name__))
