
> 👨‍💻 A repository for my solutions submitted for problems on LeetCode.

---

### Problem 1:

- [md](1/README.md)
```
> 👨‍💻 A repository for my solutions submitted for problems on LeetCode.

---

### Problem 1:

- [md](1/README.md)
```
> 👨‍💻 A repository for my solutions submitted for problems on LeetCode.

---

### Problem 1:

- [java](1/solution.java)
```// Runtime: 50 ms
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

- [py](1/solution.py)
```# Runtime: 5920 ms
# Memory Usage: 14.8 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = len(nums)
        for i in range(p):
            n = i + 1
            for j in range(n, p):
                if nums[i] + nums[j] == target:
                    return [i, j]
```


```

- [py](1/solution.py)
```# Runtime: 5920 ms
# Memory Usage: 14.8 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = len(nums)
        for i in range(p):
            n = i + 1
            for j in range(n, p):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

- [java](1/solution.java)
```// Runtime: 50 ms
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


```

- [py](1/solution.py)
```# Runtime: 5920 ms
# Memory Usage: 14.8 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = len(nums)
        for i in range(p):
            n = i + 1
            for j in range(n, p):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

- [java](1/solution.java)
```// Runtime: 50 ms
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


