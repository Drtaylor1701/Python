#! python3

#Inputs the hurricane's windspeed
WindSpeed = int(input("Please enter the hurricane's windspeed. "))

#Determines the category of the hurricane
if WindSpeed < 74:
    Category = "nothing, because this is not a hurricane"
elif WindSpeed >=74 and WindSpeed <= 95:
    Category = "1"
elif WindSpeed >= 96 and WindSpeed <= 110:
    Category = "2"
elif WindSpeed >= 111 and WindSpeed <= 130:
    Category = "3"
elif WindSpeed >= 131 and WindSpeed <= 155:
    Category = "4"
elif WindSpeed >= 156:
    Category = "5"
else:
    Category = "not calculable"

#outputs the result

print("The category of the hurricane is " + Category + ".")
