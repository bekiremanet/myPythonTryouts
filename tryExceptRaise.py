def turnOver(s):
    if(type(s) != str):
        raise ValueError("Please enter a string array.")
    else:
        return s[::-1]


try:
    turnOver("bekiremanet")
except ValueError:
    print("MISTAKE.")


print(turnOver("bekiremanet"))
print(turnOver(11))