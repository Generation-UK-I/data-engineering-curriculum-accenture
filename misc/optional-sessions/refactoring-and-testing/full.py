running = True
result = 0
a = 3
b = 4

while running: #1

    check = input ("What do I do? ") #2

    if check == "quit": #3
        print("Current result is ", result)
        break

    if check == "math": #4
        test = input ("What next? ") #5
        if test == "add": #6
            result = result + ( a + b) #7
            print("Current result is ", result)
        elif test == "minus": #8
            result = result + ( a - b ) #9
            print("Current result is ", result)
        elif test == "mult": #8
            result = result + ( a * b ) #9
            print("Current result is ", result)
        elif test == "mix": #10
            result = result + ( a**b ) #11
            print("Current result is ", result)
        elif test == "addmult": #12
            result = result + ( a + b) + ( a * b ) #14
            print("Current result is ", result)
        elif test == "addmix": #15
            result = result + ( a + b) + ( a**b ) #17
            print("Current result is ", result)
        else: #18
            print("No operation")
            print("Current result is ", result)

    print("Round we go...")

print("Final result is ", result)
