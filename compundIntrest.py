# a = p(1 + r/n) ** nt

print("You are going to recieve several prompts, fill them out as acoording.")

print("We are going to solve for compound intrest.")

print("Input all numbers as decimals with no spaces")

print("What is the initial ammount?")

iamount = input("> ")

print("What is the intrest rate, convert the percent to a decimal.")

intrest = input("> ")

print("How many times is the intrest compunded per year?")

compound = input("> ")

print("How long will you be collecting intrest for?")

time = input("> ")

step1 = (intrest / compound) + 1

step2 = coumpound * time

step3 = step1 ** step2

step4 = step3 * iamount

print(step4)