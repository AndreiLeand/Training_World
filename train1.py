def remove_duplicates(lst):

    seen = []       # List to keep track of items we've already added
    result = []     # List to store the final unique items
    
    for item in lst:
        if item not in seen:
            seen.append(item)
            result.append(item)
            
    return result
my_list = [1,2,3,1,2,5,6,3,4,5,6,7,7,8,10,11,10,2,11,10]
output = remove_duplicates(my_list)
print(output)