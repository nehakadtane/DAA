# non recursive
# Get the number of terms from the user
nterms = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        # Calculate the next term
        nth = n1 + n2
        # Update the previous two terms
        n1, n2 = n2, nth
        count += 1

# Recursive function to calculate Fibonacci sequence
def recur_fibo(n): 
   if n <= 1:
       return n
   else:
       return recur_fibo(n - 1) + recur_fibo(n - 2)

# Number of terms in the sequence
nterms = 10

# Check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
