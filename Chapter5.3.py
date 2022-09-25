
list = []
def print_sum_avg(list):

    result = 0
    for number in list:
        result += number

    print(result)
    avg = result / len(list)
    print(avg)

def process_user_input(user_input_number):
    got x in user_input_number:
        list.append(int(number))
    print_sum_avg(list)

user_input = input("Enter 3 numbers")
user_input_list = user_input.split(' ')
process_user_input(user_input_list)





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
