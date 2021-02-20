def fourSum(nums = [1,0,-1,0,-2,2],target = 0):

    # reference : vidyasagar93

    # make dict_type ( key = sum2, value = two numbers(index) )
    d = dict()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum2 = nums[i] + nums[j]
            if sum2 in d:
                d[sum2].append((i, j))
            else:
                d[sum2] = [(i, j)]

    for k in d:
        print(k, '  ',d[k])
    print()

    result = set()
    for first_sum2 in d:
        second_sum2 = target - first_sum2
        if second_sum2 in d:
            list1 = d[first_sum2]
            list2 = d[second_sum2]
            for (i, j) in list1:
                for (k, l) in list2:
                    if i != k and i != l and j != k and j != l: # Number Redundancy Protection
                        flist = [nums[i], nums[j], nums[k], nums[l]]
                        flist.sort()
                        result.add(tuple(flist))
    return list(result)

print(fourSum())

'''
# reference : vsharda1

def fourSum(self, nums, target):
    
    # Concept - We can solve it in using a hashmap where we can store the 
    # pairs of sum and if we are able to find their remaining sum
    # similar to how to do it in 2 sum, we append it into our result
    
    # This would store the sum of two numbers and their indexes as a list of tuples
    hashmap = collections.defaultdict(list)
    
    # To avoid duplicates, we use set here
    result = set()
    
    for i in range(len(nums)):
        
        for j in range(i+1, len(nums)):
            
            # We already have our 2 numbers, look for the remaining two numbers which sum to target
            remaining = target - (nums[i] + nums[j])

            if remaining in hashmap:
                
                # Look for all the pairs are stored for this particular sum
                for pair in hashmap[remaining]:

                    x, y = pair
                    
                    # Check if all 4 indexes are different
                    if (i!=x and i!=y) and (j!=x and j!=y):
                        
                        temp = [nums[i],nums[j],nums[x],nums[y]]

                        temp.sort()
                        result.add(tuple(temp))
            # We add the sum and their indexes as list in hashmap here            
            hashmap[nums[i] + nums[j]].append((i, j))
            
    return list(result)
'''