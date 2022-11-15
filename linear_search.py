def linear_search(list, target):
    """
    Return index position of target else returns NONE
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    else:
        return None
    
def verify(index):
    if index is not None:
        print('target foound at index ', index)
    else:
        print('target not fount in the list')
        
        
numbers =[1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 11)
verify(result)

result = linear_search(numbers, 3)
verify(result)