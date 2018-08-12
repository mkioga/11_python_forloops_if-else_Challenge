# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment
#
# An IP address consist of 4 numbers, separated from each other with a full stop.
# But your program shoud just count however many are entered
# Examples of input are
# 127.0.0.1
# .192.168.0.1
# 10.0.123456.255
# 172.16
# 255
#
# Your program should work even with invalid IP addresses. We are just interested in
# the number if segments and how long each one is.
# Once you have a working program, use these invalid inputs to test
# .123.45.678.91
# 123.4567.8.9
# 123.156.289.10123456
# 10.10t.10.10
# 12.9.34.6.12.90
# " - that is, press enter without typing anything
#
# This challenge is intended to practice "for loops" and "if/else" statements
# Although there are other techniques such as splitting the sting up, that
# is not the approach we are looking for here

# =====================================================================================

# This is my first code
# I assumed they don't want any printout if we are starting with a .
# I used range


# segment = 0  # initialize
# segmentLenth = 0  # initialize
# ipAddress = input("Please enter an IP address: ")  # Request IP address
# for i in range(0, len(ipAddress)): # test for range from 0 to length of input
#     if ipAddress[i] in '0123456789': # Test if input is in these numbers
#         segmentLenth += 1 # If it is, add 1 to segmentLength
#
#     elif segmentLenth > 0: # When no match (ipAddress[i] not in '0123456789') and segmentLength is > 0, do following
#         segment += 1
#         print("Segment {0}'s Length is {1}".format(segment, segmentLenth))
#         segmentLenth = 0 # reinitialize segmentLength for next iteration
#
# print("-"*20)
# if segmentLenth > 0: # For last input where there is no . after it.
#     segment += 1
#     print("Segment {0}'s Length is {1}".format(segment, segmentLenth))

# ======================================================================================

# This is my second code showing initial segment even if starting with .

# segment = 0  # initialize
# segmentLenth = 0  # initialize
# ipAddress = input("Please enter an IP address: ")  # Request IP address
# for i in range(0, len(ipAddress)): # test for range from 0 to length of input
#     if ipAddress[i] in '0123456789': # Test if input is in these numbers
#         segmentLenth += 1 # If it is, add 1 to segmentLength
#
#     else:
#         segment += 1
#         print("Segment {0}'s Length is {1}".format(segment, segmentLenth))
#         segmentLenth = 0 # reinitialize segmentLength for next iteration
#
# if segmentLenth > 0: # For last input where there is no . after it.
#     segment += 1
#     print("Segment {0}'s Length is {1}".format(segment, segmentLenth))



# ======================================================================================


# Trainers code_1
# Trainer did not use range


# ipAddress = input("Please enter an IP address: ")
# segment = 1
# segmentLength = 0
# character = '' # initialize this so if you enter nothing, there is no error
#
# for character in ipAddress:
#     if character == '.':
#         print("Segment {0}'s length is {1}".format(segment, segmentLength))
#         segment += 1
#         segmentLength = 0
#     else:
#         segmentLength += 1  # increment segment length if character is not period (.)
#
# if character != '.': # This test the last character if its not .
#     print("Segment {0}'s length is {1}".format(segment, segmentLength))


# ======================================================================================


# Trainers code_2
# Another way to do so as not to have the last two lines of code to test .
# In this code, if you enter a number ending with a ., result will have two periods
# And it will give a last result showing 0 length
# This may not be what you want
# So you can add code to check that input does not end with period
# See that in code after this.

# ipAddress = input("Please enter an IP address: ")
# ipAddress += '.' # Here we append a . to the input
# segment = 1
# segmentLength = 0
# # character = ''
#
# for character in ipAddress:
#     if character == '.':
#         print("Segment {0}'s length is {1}".format(segment, segmentLength))
#         segment += 1
#         segmentLength = 0
#     else:
#         segmentLength += 1
#
# if character != '.': # This test the last character if its not .
#     print("Segment {0}'s length is {1}".format(segment, segmentLength))
#

# ======================================================================================

# Trainers code_3
# In this code, we test to see if there is no period at the end of input
# if no period, we add one, if there is already one, we don't add


ipAddress = input("Please enter an IP address: ")
if ipAddress[-1] != '.': # if no period at end, then add/concatenate period
    ipAddress += '.' # Here we append a . to the input
segment = 1
segmentLength = 0
# character = ''

for character in ipAddress:
    if character == '.':
        print("Segment {0}'s length is {1}".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1


# ======================================================================================


# splitting a line that is too long. Python likes only 120 or less characters per line
# line length and breaking long line into two lines using double quotes
# if you put the cursor at the place you want to split the line and hit enter
# it will separate the line and add the double quotes

# print()
# print("this is a very long line. I am going to print a very long line. "
#       "I am going to print a very long line. I am going to print a very long line")


# Splitting a line with a forward cursor
# When you hit enter at the place you want to split the line,
# it splits it and adds a " and a \

# inputPrompt = "This is the input prompt that we want to split using forward slash " \
#               "at this point in the line to make it shorter"
# print()
# print(inputPrompt)


# Splitting a line using parenthesis
# This is usually the prefered method

# inputPrompt1 = ("I am going to split this line into two lines using parenthesis. "
#                 "Make sure the second line is alligned with the first one")
#
# print()
# print(inputPrompt1)

