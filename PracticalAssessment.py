
PhNumber = input("Enter your Phone number: ")
numeric_filter = filter(str.isdigit, PhNumber)
numeric_string = "".join(numeric_filter)
print(numeric_string.zfill(10))
add_zero = numeric_string.zfill(10)
length = len(numeric_string)
if length == 10 \
        and numeric_string[:3].isdigit() \
        and numeric_string[4:7].isdigit() \
        and numeric_string[8:].isdigit():
    print("Valid Phone Number")
else:
    print("Invalid Phone Number" )
print(add_zero)



#Questions 1b. b.Add an initial zero if it is missing.



