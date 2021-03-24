#!/usr/bin/python3

#A function to use regular expressions to check whether a password input from user is considered valid

'''Password is valid if it is at least 8 characters long, 
contains both upper and lower cases, 1 digit
and one special character'''

#Import Necessary Modules
import re

#TODO: Take in user input and assign to a variable
password = input("Please type in a strong password ")

#TODO: Start a function to handle password and check strength
def passwordStrength(text):
	eightOrMore = re.compile(r'[\w]{8,}')
	hasADigit = re.compile(r'[\d{1,}]')
	specialCharacter = re.compile(r'[^a-zA-z0-9_ ]{1,}')
	lowerCaseCheck = re.compile(r'[a-z]+')
	upperCaseCheck = re.compile(r'[A-Z]+')
	spaceCheck = re.compile(r'^[\S]+$')

	if eightOrMore.findall(text) == []:
		print("The password is invalid because it requires at least 8 characters.")
	elif hasADigit.findall(text) == []:
		print("The password is invalid because it requires at least 1 digit.")
	elif specialCharacter.findall(text) == []:
		print("The password is invalid because it requires at least 1 special character.")
	elif lowerCaseCheck.findall(text) == []:
		print("The password is invalid because it requires at least 1 lowercaser letter.")
	elif upperCaseCheck.findall(text) == []:
		print("The password is invalid because it requires at least 1 uppercase letter")
	elif spaceCheck.findall(text) == []:
		print("The password is invalid because it may not contain spaces.")
	else:
		print("Looks like all password requirements pass.  This password is valid!")



passwordStrength(password)