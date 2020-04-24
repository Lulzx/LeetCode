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
