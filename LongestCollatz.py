# https://projecteuler.net/problem=14
# Collatz sequence defined in above URL
# Which starting number below 1 million produces the longest chain?

# Function to generate the sequence
def CollatzGen(startnum):
    x = startnum
    print "The starting number is: %d" % x
    while x > 1:
        if x % 2 == 0:
            x = x/2
            print x
        elif x % 2 != 0:
            x = 3*x + 1
            print x
        else:
            print "Error"
            
# Now what? Could iterate for every i in range [1,1000000] but this will just produce a lot of results and then need to sift thru
# Write each set of results to a list, perform len on each list, looking to max len 
# really need an array that has startnum and chain length

# Create list of possible starting numbers
startnums = []
for i in range(1,1000000):
    startnums.append(i)
