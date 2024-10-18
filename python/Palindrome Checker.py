#Python
#Palindrome checker for String

def is_palindrome(s):
  s = s.replace(" ", "").lower()
  return s == s[::-1]

input_string = input("Enter a string:")
if is_palindrome(input_string):
  print(f'"{input_string}" is a palindrome.')
else:
  print(f'"{input_string}" is not a palindrome.')


#Palindrome checker for Integer

def is_palindrome(num):
  str_num = str(num)
  return str_num == str_num[::-1]

input_num = int(input("Enter an integer:"))
if is_palindrome(input_num):
  print(f"{input_num} is a palindrome")
else:
  print(f"{input_num} is not a palindrome")
