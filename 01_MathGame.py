'''
1 + 4 = 5
3 * 3 = 9
'''

import random

# Generate number
def gen_number():
    return random.randint(0,9)

# Generate operation:
def gen_ops():
    operations = ["+", "-", "*", "/"]
    return operations[random.randint(0, 3)]

# Use Strategy Pattern to calculate
def calculate(x, ops, y):
    expression = "%d %s %d" %(x, ops, y)
    return expression, int(eval(expression))


# MAIN
point = 0
while point <= 20:

    # Initiate number and operator
    x = gen_number()
    y = gen_number()
    ops = gen_ops()

    # Get the expression and the result
    expression, expected = calculate(x, ops, y)

    # For the player: get the question and answer
    question = "%s = " %(expression)

    try:
        answer = int(input(question).strip())   # input will return a String, use Strip to remove space and then convert to Int

        # Check result and print out message
        if answer == expected:
            print("Correct!")
            point += 1
        else:
            print("Incorrect! The correct answer is %s" %(expected))
            point -= 1
    except ValueError:
        print("Don't leave it blank")

print("Bye!")


    
