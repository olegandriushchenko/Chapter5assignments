#Write a loop that prints each of the numbers on a new line.
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for x in xs:
    print(x)

#Write a loop that prints each number and its square on a new line.
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
ys = [144, 100, 1024, 9, 4356, 289, 1764, 9801, 400]
for x in xs:
    for y in ys:
        print(x, y)

#Write a loop that adds all the numbers from the list into a variable called total.
#You should set the total variable to have the value 0 before you start
#adding them up, and print the value in total after the loop has completed.

total = 0
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for x in xs:
    total = iter(xs)
    print(total)

#Print the product of all the numbers in the list. (product means all multiplied together)
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
ys = xs * xs
for x in xs:
    for y in ys:
        print(xs, ys)
