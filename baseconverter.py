'''
	  Program:  binaryconverter.py
	  Author:     Elayna Ridley
	  Based on a program written by Dr. Meyer
	  Purpose:   to convert a binary number to its decimal equivalent
	  Input:        a string of 1s and 0s that represents a binary number
	  Output:     the equivalent decimal number

	Algorithm:
	     get a binary number from the user that is a string
	     reverse it so that the least significant bit is first
	     initialize the decimal final resulting number to 0
	     initialize the exponent of 2
	     
	     for each character in the reversed input string  do the following:
			convert that character to 1 or 0 and multiply by the power of 2
			add that to the ongoing decimal number
			bump up the power of 2
	     
	     print the final result
'''
import sys

base = input("What is your base? (2-9):")

for digit in base:
        base = int(base)
        if base > 9:
                print("Your base cannot exceed 9")
                sys.exit()
                # otherwise continue with loop
        if base < 2:
                print("Your base cannot be less than 2")
                sys.exit()

                # otherwise continue with the loop body
                
original_number = input("Enter your number:")

decimal_result = 0
power = 0

reversed = original_number[::-1]
               
for digit in reversed:
        base = int(base)
        digit = int(digit)
        if digit > base-1:
                print('Illegal input number for base', base)
                sys.exit
                # otherwise continue with the loop body
        xdigit = int(digit) * base**power
        decimal_result += xdigit
        power += 1


print (original_number, '(base', base, ') =', decimal_result, '(base 10)')
