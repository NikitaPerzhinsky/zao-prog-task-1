def sum_of_two(nums -> list , target -> int)
    n = len(nums)
    if type(nums) is not list or type(target) is not int:
        return 'Nums or target - invalid Type'
    else:
        n = len(nums)    
        for i in range(n)
            for j in range(i + 1, n)
            if nums[i] + nums[j] == target
            return [i, j]
        return [] 
           
