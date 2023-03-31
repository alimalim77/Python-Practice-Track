def helper(costs,total,k,candidates):
        if k == 0:
            return total
        if 2*candidates > len(costs):
            ans = min(costs)
            p = costs.index(ans)
            del costs[p]
            return helper(costs,total+ans,k-1,candidates)
        else:
            ans = min(min(costs[:candidates]),min(costs[-candidates:]))
            p = costs.index(ans)
            del costs[p]
            return helper(costs,total+ans,k-1,candidates)

print(helper([17,12,10,2,7,2,11,20,8],0,3,4))
print(helper([1,2,4,1],0,3,3))

