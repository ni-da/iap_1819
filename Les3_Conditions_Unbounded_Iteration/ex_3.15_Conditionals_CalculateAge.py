dob_d = int(input())
dob_m = int(input())
dob_y = int(input())

cur_d = int(input())
cur_m = int(input())
cur_y = int(input())

y = cur_y - dob_y

if cur_m < dob_m or cur_d < dob_d:
    y -= 1

print(y)
