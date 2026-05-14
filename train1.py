def remove_duplicates(lst):

    seen = []       # List to keep track of items we've already added
    result = []     # List to store the final unique items
    
    for item in lst:
        if item not in seen:
            seen.append(item)
            result.append(item)
            
    return result
my_list = [1,2,3,1,2,5,6,3]
output = remove_duplicates(my_list)
print(output)