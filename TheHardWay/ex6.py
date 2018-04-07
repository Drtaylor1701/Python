#prints line "There are 10 types of people"
x = "There are %d types of people." % 10
#defines variable binary as binary
binary = "binary"
#defines variable do_not as don't
do_not = "don't"

#defines y as "those who know binary and those who don't
y = "Those who know %s and those who %s." % (binary, do_not)

#prints out There are 10 types of people
print x
#prints out "Those who know binary and those who don't.
print y

#prints out "I said there are 10 types of people
print "I said %r." % x
#prints out "Those who know binary and those who don't
print "I also said '%s'." % y

#sets hilarious as false
hilarious = False
#sets value of joke_evaluation as "isn't that joke so funny? 
joke_evaluation = "Isn't that joke so funny? %r"

#prints out "isn't that joke so funny? False"
print joke_evaluation % hilarious
#sets w to "This is hte left side
w = "This is the left side of..."
#sets e to "a string with a right side
e = "a string with a right side."

#prints "this is the left side of a string with a right side
print w + e