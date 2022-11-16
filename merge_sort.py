def merge_sort(list):
    '''sort list in ascendine order with merge sort
       using divide and conquer 
       Divide - Find the midpoint of the list and divide list in sublists
       Conquer - Recursively sort the sublists created in the previous 
       Combine - Combine the sorted sublists created in previous step
       big-O = O(split()) * O(merge()) = o(log n) * O(n) = O(n log n)
    '''
    
    if len(list) <= 1:
        return list
    
    left, right = split(list)
    left_side = merge_sort(left)
    right_side = merge_sort(right)
    
    return merge(left, right)

def split(list):
    '''
        Divide the unsorted list at midpoint into sublists
        returns two unsorted sublists - left and right
        O(log n)
    '''
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    '''
        Sorts two sublists and merges them in the process
        returns new sorted merged list
        O(n)
    '''
    
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
            
    while i < len(left):
        l.append(left[i])
        
    while j < len(right):
        l.append(right[j])
        j += 1
    return l
        
        
a_list = [22,3,53,2,1,78,334,78,0,66]
x = merge_sort(a_list)

print(x)
    
    
