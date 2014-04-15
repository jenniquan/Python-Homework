number1 = int(raw_input ("1st number: "))
number2 = int(raw_input ("2nd number: "))


if number2 == 0 or number1 == 0:
    print "Total: 0"
elif number2 == 1:
    print "Total: ", number1
elif number2 == -1:
    print "Total: ", - number1
elif number2 < -1:
    total = number2
    times = number1 - 1
    while times > 0:
        total = total + number2
        times = times - 1
    if times == 0:
        print "Total: ", total
    
    
elif number2 > 1:
    total = number1
    times = number2 - 1
    while times > 0:
        total = total + number1
        times = times - 1
    if times == 0:
        print "Total: ", total
    
