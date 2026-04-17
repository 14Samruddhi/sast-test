# BAD CODE SAMPLE — DO NOT USE IN REAL PROJECTS

import os, sys, time, random

globalVar = "password123"   # hardcoded sensitive data

def doStuff(a, b, c, d, e, f, g, h):  # too many parameters
    print("Doing stuff...")  # debug print left in production
    
    if a == True:  # bad boolean check
        if b == True:
            if c == True:
                print("Nested hell")  # deep nesting

    x = 0
    while x < 10:
        x += 1
        if x == 5:
            pass  # useless statement

    try:
        risky = 10 / 0  # division by zero
    except:
        pass  # swallowing exception

    query = "SELECT * FROM users WHERE username = '" + a + "';"  # SQL injection risk
    print(query)

    os.system("echo " + a)  # command injection risk

    file = open("data.txt", "w")  # file not closed properly
    file.write("Some data")

    for i in range(0, 1000000):  # inefficient loop
        temp = i * random.random()

    if a == "admin":
        print("Welcome admin")
    elif a == "admin":  # duplicate condition
        print("Still admin?")

    unused_var = 12345  # unused variable

    return None  # unnecessary return


def duplicateFunction():
    print("This function is duplicated")

def duplicateFunction():  # duplicate definition
    print("Overwritten function")


class bad_class_name:  # bad naming convention
    def __init__(self):
        self.Value = 10  # inconsistent naming

    def getValue(self):
        return self.Value

    def setValue(self, v):
        self.Value = v


if __name__ == "__main__":
    user_input = input("Enter username: ")  # no validation
    doStuff(user_input, True, True, False, None, None, None, None)

    password = input("Enter password: ")  # insecure input handling
    if password == globalVar:
        print("Access granted")
    else:
        print("Access denied")

    # Infinite loop risk
    while True:
        time.sleep(1)
