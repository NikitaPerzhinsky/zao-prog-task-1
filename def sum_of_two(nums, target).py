def sum_of_two(nums, target)
    n = len(nums)
    for i in range(n)
        for j in range(i + 1, n)
        if nums[i] + nums[j] == target
            return [i, j]
    return [] 
           
