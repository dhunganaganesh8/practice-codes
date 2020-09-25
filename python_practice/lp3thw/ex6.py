#Assign value to variable "types_of_people".
types_of_people = 10

#Assign formatted string as value to variable "x"
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# "y" is also a variable with formatted string as its value.
y = f"Those who know {binary} and those who {do_not}."

#prints value of both variables x and y on screen.
print(x)
print(y)

#prints formatted string containing another formatted string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

#sets boolean value to variable "hilarious".
hilarious = False

#"joke_evaluation" is again another variable containing formatted string.
joke_evaluation = "Isn't that joke so funny?! {}"

#Use of .format() with variable that puts value of hilarious in curly brackets.
print(joke_evaluation.format(hilarious))

#String concatenation using '+' operator.
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
