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
