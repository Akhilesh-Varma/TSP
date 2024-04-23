def temp_conv(n, conv:str):
    if conv == 'F':
        x = (n*(9/5))  + 32 
        return  f"{x:.{1}f}" + "F"
    elif conv == 'C':
        x = (n-32)*(5/9)
        return  f"{x:.{1}f}" + "C"
    else:
        print("Please enter F-for Fahrenheit conversion or C for Celsius convesion")

print(temp_conv(100,'F'))
print(temp_conv(100,'C'))