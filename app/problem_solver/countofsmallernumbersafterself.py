def count_Smaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    counts = [0] * len(nums)
        
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                counts[i] += 1
        
    return counts