 mini = nums[0]
        profit = 0
        for i in range(1, len(nums)):
            cost = nums[i] - mini
            if cost > profit:  # Compare cost with profit
                profit = cost
            if nums[i] < mini:  # Update mini if nums[i] is smaller
                mini = nums[i]
        return profit



#cost=total cost matlab ki sell karrne ke baad kitna bacha terea paas
#mini= min ccost at which you buy,always we buy stock at low price 