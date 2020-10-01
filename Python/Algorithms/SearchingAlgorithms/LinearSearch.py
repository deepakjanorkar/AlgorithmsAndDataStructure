#Implementation of LinearSearch in python

# Python3 code to linearly search x in arr[]. 
# If x is present then return its location, 
# otherwise return -1 


def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['p','y','t','h','o','n']
x = 'o'
print("element found at index "+str(linearsearch(arr,x)))


#output: element found at index 4
