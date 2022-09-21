#Write a loop that prints each of the numbers on a new line.
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for x in xs:
    print(x)

#Write a loop that prints each number and its square on a new line.

for x in xs:
print(x*x)

#Write a loop that adds all the numbers from the list into a variable called total.
#You should set the total variable to have the value 0 before you start
#adding them up, and print the value in total after the loop has completed.

total = 0

for x in xs:
    total += x
print(total)

#Print the product of all the numbers in the list. (product means all multiplied together)
product = 1
for x in xs:
    product *= x

print(product)
