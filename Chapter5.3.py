
list = []
def print_sum_avg(list):

    result = 0
    for x in list:
    result += x
print(result)

    result = 0
    for x in list:
    result /= len(list)
print(result)

list = user_input()
print(print_sum_avg(list))

user_input = input('Add 3 numbers\n'):
print("Thank you")

list = int(user_input):

#Exercise 2
def print_sum_avg_arg(*args):

    result = 0
    for x in args:
        result += x
    return result
print(print_sum_avg_arg(list))


#Exercise 4
"""
Create any program of your choice that will take the user's input 
and will perform any action with it (for example greeting program,
program that calculates the factorial of the number, program that prints the word from the back and etc.)
"""

user_input = input("What you studying?\n")
print("I am studying " + user_input)

user_answer = str(user_input)
