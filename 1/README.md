
> 👨‍💻 A repository for my solutions submitted for problems on LeetCode.

---

### Problem 1:

- [py](1/solution.py)
```
# Runtime: 44 ms
# Memory Usage: 15.2 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in p:
                p[num] = i
            else:
                return [p[n], i]

```

- [js](1/solution.js)
```
// Runtime: 112 ms
// Memory Usage: 34.9 MB

var twoSum = function(nums, target) {
        var p = nums.length;
        for(var i = 0; i < p; i++){
            for(var j = i + 1; j < p; j++){
                if (nums[i] + nums[j] == target){
                    return [i, j];
            }
        }
    }
};

```

- [java](1/solution.java)
```
// Runtime: 50 ms
// Memory Usage: 39.3 MB

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int p = nums.length;
        for(int i = 0; i < p; i++){
            for(int j = i + 1; j < p; j++){
                if (nums[i] + nums[j] == target){
                    int[] res = {i, j};
                    return res;
                }
            }
        }
        return null;
    }
}

```

