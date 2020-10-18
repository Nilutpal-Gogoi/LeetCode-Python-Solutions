def maxSlidingWindow(nums, k):
    # Base conditions
    if not nums or k<1 or k>len(nums):
        return []
    output = []
    dq = []

    # Rules:
    # Length of dq <= k
    # values stored are indexes (because it will give us the way to reference and
    #                            understand where our maximum value lie under)
    # This is somewhat like priorty queue implementation but not a priority queue
    # max contained in deque dq[0]

    for i, num in enumerate(nums):
        if dq and dq[0] < i-k+1:
            dq.pop(0)

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k-1:
            output.append(nums[dq[0]])

    return output


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

