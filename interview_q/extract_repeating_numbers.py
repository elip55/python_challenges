
# 1: Extract repeating integers from an arr
# 2: Write a .txt document displaying those numbers

from make_random_list import make_a_random_list # Imported a function I made to generate a random list

"""NEEDS OPTIMIZATION"""
def extract_numbers(arr):
    # first initialize the lists
    l1 = []
    l2 = []
    # bubble up the list so that the numbers are in ascending order
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # then compare each element to extract the repeating numbers
    for k in range(len(arr)-1):
        if arr[k] == arr[k+1]:
            l1.append(arr[k])
    # finally, append the final list without any repeated numbers
    for l in l1:
        if l not in l2:
            l2.append(l)
    return l2

def build_txt(arr):
    # simply build the .txt file
    buildit = f'The repeating numbers are:\n'
    for i in arr:
        buildit += f'{i}\n'
    with open('repeating number.txt', 'w') as writer:
        writer.write(buildit)

"""TO TEST THE CODE PRINT INSTEAD OF RETURN"""
def print_extracted_numbers(arr):
    # first initialize the lists
    l1 = []
    l2 = []
    # bubble up the list so that the numbers are in ascending order
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # then compare each element to extract the repeating numbers
    for k in range(len(arr)-1):
        if arr[k] == arr[k+1]:
            l1.append(arr[k])
    # finally, append the final list without any repeated numbers
    for l in l1:
        if l not in l2:
            l2.append(l)
    print(l2)
