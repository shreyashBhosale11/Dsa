
# resursions functions
# time complexity : o(logn )
def binarySearch(arr , i , j , x):
    while i <= j:
        mid = i + (j -i)//2
        if(arr[mid]== x):
            return mid 
        elif arr[mid] < x:
            return binarySearch(arr , mid + 1 , j , x )
        else:
            return binarySearch(arr , i , mid - 1, x )
    return -1

def binarySearchBychange(arr , i , j , x):
    while i <= j:
        mid = i + (j -i)//2
        if(arr[mid]== x):
            return mid 
        elif arr[mid] < x:
            #  update the i parameter
            i = mid + 1
        else:
            #  update the j parameter
            j = mid - 1
    return -1




# driver code 
# sorted array 
arr = [2, 5, 10, 14, 18 , 22 , 27 , 35 , 40 , 59  ]
x = 40 
i = 0 
j = len(arr) - 1

# function call 
result = binarySearch(arr , i , j , x)
rs = binarySearchBychange(arr , i , j , x)
print("Searching element is present at the index ", result)