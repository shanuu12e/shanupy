import re                                   #Importing regex module
print("Magic calculator")
print("'quit' to exit\n")                   #Method to exit

previous=0
run=True

def calc():                                 #Defining function calc for calculations
    global run
    global previous
    equation=""

    if previous==0:
        equation=input("Enter the equation")
    else:
        equation=input(str(previous))

    if equation == "quit":
        print("Goodbye")
        run = False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous==0:
           previous=eval(equation)
        else:
           previous=eval(str(previous)+equation)

while run:
    calc()
