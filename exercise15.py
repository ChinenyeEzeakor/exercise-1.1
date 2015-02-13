from sys import argv

script, exercise15_sample = argv 

txt = open(exercise15_sample)

print "Here's your file %r:" % exercise15_sample
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read() 