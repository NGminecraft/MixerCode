
names = ["Jim", "Jane", "Joe", "Jill"]

nums = sorted([1,2,3,4,5,6,7,8,9,19])

search_name = 8

def binary_search(list, item, index = 0):
    print(list, index)
    if len(list) > 2:
        peek = list[len(list)//2]
        if peek == item:
            return peek, index+len(list)//2
        elif peek < item:
            return binary_search(list[len(list)//2+1:], item, index+len(list)//2)
        elif peek > item:
            return binary_search(list[0:len(list)//2], item, index)
    elif len(list) == 1 or list[0] == item:
        return list[0], index
    elif list[1] == item:
        return list[1], index+1
    else:
        return None, index

def linear_search(list, item):
    for x in range(len(list)):
        if nums[x] == item:
            print(item, x)
            
            
print(binary_search(nums, search_name))
print(nums.index(search_name))