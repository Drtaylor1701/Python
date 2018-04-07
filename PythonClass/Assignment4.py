#! python3

Sum = 0
NumberOfNumbers = 0

Number = eval(input("Enter a number."))

if Number != -1:
    NumberOfNumbers + 1
    for count in range (NumberOfNumbers):
        Sum = Sum + Number
        Average = Sum / NumberOfNumbers
        NumberOfNumbers = NumberOfNumbers + 1
    

print(Sum)
print(Average)
