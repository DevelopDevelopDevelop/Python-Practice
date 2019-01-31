# Generate Circumference and Area of Circles
# With Radius from 1" to 36"

import time
start = time.time()

radius = range(1,37)
for r in radius:
    print("A Circle with a Radius of",r, "\"\nwill have an Area of:")
    area= 2.14*r**2
    feet= area/12
    print(feet,"\'\nor")
    print(2.14*r**2,"\"\n")

# Measure run time
stop = time.time()
print(stop-start,"secs to exe")
