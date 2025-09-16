def luhn_check(number):
    s = number.replace(" ", "")
    if  len(s) != 16:
        return False

    digit = int(s[-1])         
    c = s[:-1][::-1]               
    total = 0
    for i in range(len(core)):
        d = int(c[i])
        if i % 2 == 0:                 
            d *= 2
            if d > 9:
                d -= 9
        total += d
    print(total)
    total += digit
    print(total)
    return total % 10 == 0

#print(luhn_check("5893804115457289"))
#print(luhn_check("1234567812345670"))

print(luhn_check("1234567812345678"))  # Invalid
