# numbers = [1,1,2,3,5,8,13,21]

# target = 13
 
# def binary_search(arr, target, left, right):
#     if left > right:
#         return -1
#     mid = (left+right) // 2 # lesson learnt. to find the middle we add the left and right and integer divide by two
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid+1, right)
#     else:
#         return binary_search(arr,target, left, mid-1)
    
# answer = binary_search(numbers, target, 0, len(numbers)-1)
# print(answer)

numbers = [1,1,2,3,5,6,13,21]

target = 13

def binary_search(arr,target, left, right):
    if left > right:
        return -1
    mid = (left+right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1, right)
    else:
        return binary_search(arr,target,left,mid-1)
    
answer = binary_search(numbers, target, 0, len(numbers)-1)
print(answer)
