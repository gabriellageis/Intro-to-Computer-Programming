
# get dimensions of two rectangles
r1_width = int(input("R1 width: "))
r1_length = int(input("R1 length: "))
r2_width = int(input("R2 width: "))
r2_length = int(input("R2 length: "))

# compute area of two rectangles
r1_area = r1_width * r1_length
r2_area = r2_width * r2_length
print()
print("R1 Area:", r1_area)
print("r2 Area:", r2_area)

# see which one is bigger and report
print()
if r1_area > r2_area:
    print("R1 is bigger!")
elif r1_area == r2_area:
    print("They are the same size!")
else:
    print("R2 is bigger!")

# see if either is a square
if r1_width == r1_length:
    print("R1 is a square!")
if r2_width == r2_length:
    print("R2 is a square!")
