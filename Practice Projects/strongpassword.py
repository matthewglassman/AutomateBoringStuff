#!/usr/bin/python3

#A function to use regular expressions to check whether a password inputted from user is considered strong

'''Password is strong if it is at least 8 characters long, 
contains both upper and lower cases, 1 digit
and one special character'''

#Import Necessary Modules
import re

#TODO: Take in user input and assign to a variable
password = input("Please type in a strong password ")

#TODO: Start a function to handle password and check strength
def passwordStrength(text):
#	eightOrMore = re.compile(r'[\w]{8,}')
##TODO: Check input for length equal to or greater than 8.
#	if eightOrMore.findall(text) == []:
#		print("The password you entered does not meet the requirement of having at least 8 characters")
#	else:
#		print("Looks like the password has at least 8 characters")
		

#TODO: Check input for at least one number.
#	hasADigit = re.compile(r'[\d{1,}]')
#	if hasADigit.findall(text) == []:
#		print("The password does not meet the requirement of having at least 1 number")
#	else:
#		print("Looks like this password has at least 1 number")

#TODO: Check input for at least one special character.
	#specialCharacter = re.compile(r'[^a-zA-z0-9_ ]{1,}')
#	if specialCharacter.findall(text) == []:
#		print("The password must contain at least 1 special character")
#	else:
#		print("Looks like this password has at least 1 special character")

#TODO: Check input for at least 1 upper case letter
	#lowerCaseCheck = re.compile(r'[a-z]+')
#	if lowerCaseCheck.findall(text) == []:
#		print("The password must contain at least 1 lowercase character")
#	else:
#		print("Looks like this has at least 1 lowercase letter")

#TODO: Check input for at least 1 lower case alpha character.
	upperCaseCheck = re.compile(r'[A-Z]+')
	if upperCaseCheck.findall(text) == []:
		print("The password must contain at least 1 uppercase character")
	else:
		print("Looks like this has at least 1 uppercase letter")

#TODO: If input passes all checks send message to user that password is strong.

passwordStrength(password)