def merge(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        merge(left)
        merge(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
             
              myList[k] = left[i]
              
              i += 1
            else:
                myList[k] = right[j]
                j += 1
           
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

list = [54,26,93,17,77,31,44,55,20]
merge(list)
print(list)