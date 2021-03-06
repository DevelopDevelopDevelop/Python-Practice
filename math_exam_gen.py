
import random
import time
start1 = time.time()

key = []
i = range(1,6)
for n in i:

# Generate 3 random values
# 3 digits each    
    x = random.randint(100,999)
    y = random.randint(100,999)
    z = random.randint(100,999)
    ans = (x-y-z)
    key.append(ans)
# Generate 5 problems for Subtraction    
    print(n,"\n   ",x)
    print("   ",y)
    print("  -",z)
    print("  ------\n")
    
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

# Measure and show execution time of block
stop = time.time()
print("\n", stop-start1,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
    
# Generate 3 random values
# 3 digits each
    x = random.randint(100,999)
    y = random.randint(100,999)
    z = random.randint(100,999)
    ans = (x+y+z)
    key.append(ans)

# Generate 5 problems for Addition  
    print(n,"\n   ",x)
    print("   ",y)
    print("  +",z)
    print("  ------\n")
    
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
    
# Generate random values for x and y
    x = random.randint(100,999)
    y = random.randint(10,99)
   
    ans = (x*y)
    key.append(ans)
# Generate 5 problems for Multiplication    
    print(n,"\n   ",x)   
    print("   *",y)
    print("  ------\n")
    
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
# Generate random values for x and y
    x = random.randint(100,999)
    y = random.randint(10,99)   
    ans = (x/y)
    key.append(ans)

# Generate 5 problems for Division    
    print(n,"\n   ",x)
    print("  ------ =")
    print("    ",y, "\n")

# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
# Generate 3 random values
# 2 digits each    
    x = random.randint(10,99)
    y = random.randint(10,99)
    z = random.randint(10,99)
    ans = (x+y-z)
    key.append(ans)

# Generate 5 problems    
    print(n,"\n  ",x, "+", y, "-", z, "=\n")
   
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()


key = []
i = range(1,6)
for n in i:
# Generate 3 random values    
    x = random.randint(10,99)
    y = random.randint(1,12)
    z = random.randint(1,10)
    ans = (x-y*z)
    key.append(ans)

# Generate 5 problems    
    print(n,"\n   ",x, "-", y, "*", z, "=\n")
   
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
    
# Generate 3 random values
    x = random.randint(10,99)
    y = random.randint(1,12)
    z = random.randint(1,10)
    ans = (x-y/z)
    key.append(ans)

# Generate 5 problems    
    print(n,"\n   ",x, "-", y, "/", z, "=\n")
   
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
    d = random.randint(1,100)
    r = d/2
    ans = 2*3.14*r
    key.append(ans)

# Generate 5 problems
    print(n,"\n     A Circle with a Diameter of", d, "\n  has a Circumference of\n")
   
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n\n")


start = time.time()

key = []
i = range(1,6)
for n in i:
    d = random.randint(1,100)
    r = d/2
    ans = 3.14*r**2
    key.append(ans)

# Generate 5 problems
    print(n,"\n   A Circle with a Diameter of", d, "has an\n Area of\n")
   
# Generate answer key
print("\nAnswer Key:\n")    
i = range(0,5)
for n in i:
    print(n+1, "= ", key[n])

stop = time.time()
print("\n", stop-start,"secs to exe\n")

# Measure and show total execution time
print(stop-start1, 'total secs to exe')
