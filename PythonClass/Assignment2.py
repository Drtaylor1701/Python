#! python3

#input a word or phrase
phrase = input("Please enter a word or phrase. ")

#input an index to start slicing
start = input("Where would you like to start slicing? ")

#input an index to stop slicing
stop = input("Where would you like to stop slicing? ")

#convert start, and stop to a numeric datatype

eval(start)
eval(stop)

#output the clipped section of phrase
print(phrase[int(start):int(stop)])
