def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                print(arr[i], arr[j])
                count += 1
    return count

sequence = [3, 2, 4, 6, 12, 11, 10, 9, 8, 7, 13, 14, 5, 1, 15]
print(count_inversions(sequence))
