from sys import argv

script, filename = argv
txt = open(filename)
print(txt.read())

filename_again = input("filename: ")
txt_again = open(filename_again)
print(txt_again.read())
