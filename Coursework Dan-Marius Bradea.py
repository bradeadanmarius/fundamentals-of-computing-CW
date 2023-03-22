# CS4051 - Individual Coursework

# Student: Dan-Marius Bradea
# Student ID: 20044497

# DATE: 09/05/2022

"""
This is a program is a binary adder and it works by taking two integers between 0 and 255 from the user. 

These inputs are stored in to their individual variables and then coverted in to binary using a python built-in function.

After the conversion the converted input is stored in to a list and the "0b" from the conversion is removed while the rest of the binary number is stored in the list each individual digit with its own index.

After the each list contains the required number if digits each digit, from each individual list, starting with the lastdigit is passed thru the logic gates of the full 8 bit adder and the result is stroed in to the variable called output.

Due to the fact that the operation has started from the last digit in the list the output needs to be reversed in order for it to be displayed correctly on the console.
"""

# * Definition of AND gate
def AND(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


# * Definition of OR gate
def OR(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


# * Definition of XOR gate
def XOR(a, b):
    if a ^ b:
        return 1
    else:
        return 0


# * Definition of NOT gate
def NOT(a):
    return not a


choice = input(
    "This is a program that takes user from you, the user and then simulates the use of logic gates in order to add these numbers \nthat you as the user will input when promted to do so. Both of these numbers must be positive integers from 0 to 256 inclusive.\nWould you like to procede? Y/N : "
)

# ! Definition of a function that validates the input that will get used this was the first attempt at writing a function to obtain and validate input from the user

"""def rangechecker():
    the_input = int(input("Please enter a number between 0 and 255 inclusive: "))
    while the_input not in range(-255, 256):
        the_input = int(input("Please enter a valid number from the suggested range: "))
    if the_input in range(-255, 256):
        inputX = the_input
        return inputX
        # print(inputX)
"""

# * Defining the function that obtains and validates the input from the user
def getInput():
    x = int(input("Please enter a number between 0 and 256 inclusive: "))
    if x not in range(257):  # * Does not include negatives
        return getInput()
    else:
        return x


if choice == "Y" or choice == "y":
    getInput()
elif choice == "N" or choice == "n":
    print("Have a good day")
    exit()

# * Calling the getInput() function for the first input and storing the input in it's designated variable
numOne = getInput()
# ! print(numOne)

# * Calling the getInput() function for the first input and storing the input in it's designated variable
numTwo = getInput()
# ! print(numTwo)

# TODO: Convert inputs to binary

# * Store the value of the binary counterpart of the integer in to a list
numOneBin = bin(numOne)
# * Store the value of the binary counterpart of the integer in to a list
numTwoBin = bin(numTwo)

# TODO: Store binary conterpart of the integers in to separate lits or arrays

# * Store the binary number in to a list while removing the '0b' from the begining of the list and then using '.zfill' push zeros till the list has 8 elements representing the 8 bits required
numOneList = list(numOneBin[2:].zfill(8))

# * Store the binary number in to a list while removing the '0b' from the begining of the list and then using '.zfill' push zeros till the list has 8 elements representing the 8 bits required
numTwoList = list(numTwoBin[2:].zfill(8))

print("        ")
print("Number ", numOne, " has been converted to : ")
print(numOneList)
print("        ")
print("Number ", numTwo, " has been converted to: ")
print(numTwoList)


# TODO: Take each individual bit of the inputs and pass them through the logic gates of the circuit don't forget the cary-in


# * Defining a full bit adder
def full_bit_adder(upper, lower, carry_in):
    output1 = AND(upper, lower)
    output2 = XOR(upper, lower)
    output3 = AND(output2, carry_in)
    sum = XOR(output2, carry_in)
    carry_out = OR(output1, output3)
    return sum, carry_out


# * Declaring the carry in as 0 for the begining as there is no previous execution from which we can bring a carry-in from
carry_in = 0
# * Declaring the empty list to store our result
output = []
i = 7
while i >= 0:
    bit_a = int(numOneList[i])
    bit_b = int(numTwoList[i])
    sum, carry_out = full_bit_adder(bit_a, bit_b, carry_in)
    output.append(sum)
    carry_in = carry_out
    # ! print(bit_a, bit_b)
    i = i - 1

# * print(output)
output.reverse()
output.insert(0, carry_out)
# ! print(output)

# TODO: Store the results in to a temporary list or array and recompose the binary number from that list and turn the binary number in to base 10 number

# * After storing the output in to the output variable and adding the "carry_out" on the first position of the output list, in order to account for binary numbers with more then 8 bits we use built in functions from python to convert the list in to a string and then convert the string into an integer in case other operations must be done using this result.
print("The result of the addition is as follows: ", (int("".join(map(str, output)), 2)))
