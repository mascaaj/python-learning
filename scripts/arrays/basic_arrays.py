print("arrays")

# array definition
arr = [18,36,12,433,32,19,3,43,54]

# initialization operation
max = arr[0]

for num in arr:
    if num < max:
        max = num

print(max)