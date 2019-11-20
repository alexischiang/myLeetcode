/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// 利用数组做映射
var twoSum = function(nums, target) {
  let temp = [];
  for (let i = 0; i < nums.length; i++) {
    a = target - nums[i];
    if (temp[a] != undefined) {
      return [temp[a], i];
    } else {
      temp[nums[i]] = i;
    }
  }
};
