
names = ["Jim", "Jane", "Joe", "Jill"]

nums = sorted([2,5,3,7,9,10])

search_name = 9

def binary_search(list, item):
    if len(list) > 2:
        return binary_search(list[0:len(list)//2], item)
    elif len(list) == 1 or list[0] == item:
        return list[0]
    elif list[1] == item:
        return list[1]
    else:
        return None

def linear_search(list, item):
    for x in range(len(list)):
        if nums[x] == item:
            print(item, x)
            
            
print(binary_search(nums))