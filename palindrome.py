my_str= input("Enter the name\:")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("this is palindrome")
else:
    print("this string is not a palindrome")