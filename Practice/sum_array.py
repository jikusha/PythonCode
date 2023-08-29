def sum_array(arr):
    sum = 0
    for i in arr:
        sum+=i
    print(sum)

sum_array([12, 3, 4, 15])

def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    print(max)

largest([12, 3, 4, 15])