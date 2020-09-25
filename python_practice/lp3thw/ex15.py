from sys import argv

#unpacks arguments to be given to script.
script, filename = argv

#opens file named {filename} and sets it to variable named txt.
txt = open(filename)

print(f"Here's your file {filename}:")
#reads the txt and prints on screen.
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
