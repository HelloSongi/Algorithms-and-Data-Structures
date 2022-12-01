#binart search algorithm
def binary_search(list, target):
    first = 0 #Bid-O == O(1)
    last = len(list) - 1  #Big-O for len(list) == O(1)
    
    while first <= last:
        midpoint = (first + last ) //2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None

def verify(index):
    if index is not None:
        print('target foound at index ', index)
    else:
        print('target not fount in the list')
        
        
numbers =[1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 1)
verify(result)

result = binary_search(numbers, 3)
verify(result)

