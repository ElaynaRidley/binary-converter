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

original_number = input("Enter your binary number:")

decimal_result = 0
power_of_2 = 0

reversed = original_number[::-1]

for digit in reversed:
        n = int(digit)
        if n > 1:
                print("Illegal input numberfor base 2")
                sys.exit()
                # otherwise continue with the loop body
        xdigit = int(digit) * 2**power_of_2
        decimal_result += xdigit
        power_of_2 += 1

print (original_number, '(base 2) =', decimal_result, '(base 10)')
