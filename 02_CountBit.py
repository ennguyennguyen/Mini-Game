'''
pow(2,3) = 8
pow(2,2) = 4
pow(2,8) = 256
'''

import random
import numpy

def gen_num():
    return random.randint(0,16)

def gen_strategy(num, powerOf):
    expression = "pow(%d, %d)" % (num, powerOf)
    return expression, pow(num, powerOf)

point = 0
while point <= 20:

    # Initial variables
    num = 2
    powerOf = gen_num()
    expression, expected = gen_strategy(num, powerOf)

    # Display expression and let user input
    question = "%s is: " %(expression)
    try:
        answer = int(input(question).strip())
        
        # Check answer with result
        if answer == expected:
            point += 1
            print("Correct! Your point is %d" %(point))
        else:
            point -= 1
            print("Incorrect! The answer is %d. Your point is %d" %(expected, point))
    except ValueError:
        print("Try harder")
print("Bye")

