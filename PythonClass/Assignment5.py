#! python3

def convert_to_farenheit(Celsius):
    Farenheit = 9.0/5.0 * Celsius + 32
    return Farenheit

for i in (0, 101, 10):
    print(i, convert_to_farenheit(i))
