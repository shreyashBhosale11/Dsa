arr = [2, 1, 8 , 9, 12 , 15, 11, 19 ]
# random access 

print(arr[4])

## search for an element "15 " and if it prent return index;
x = 15

# function defination
def linearSearch(arr , x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i
    return -1   

# funcrion calling 
result = linearSearch(arr , x)

print("element is present at index ", result)


# insert on element 5 at index 2
arr.insert(2 , 5)
print(arr)

# remove element 
arr.remove(8)

#count number accorence 
print(arr.count(2))

# delete element with index
arr.pop(4)

# sort the array 
arr.sort()
print(arr)

# to extracrt the index of any give elemt 
arr.index(11)

# to extend orignal arr
arr.extend([2,3, 4,5 ])

# reverse the entire list 
arr.reverse()