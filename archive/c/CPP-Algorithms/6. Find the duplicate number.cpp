// Find the duplicate number
// Input: nums = [3,1,3,4,2]
// Output: 3

int findDuplicate(vector<int>& nums) {
    // Floyd's Cycle-Finding Algorithm
    int slow = nums[0];
    int fast = nums[0];
    do{
        slow = nums[slow];
        fast = nums[nums[fast]];
    }while(slow != fast);

    fast = nums[0];
    while(slow != fast){
        slow = nums[slow];
        fast = nums[fast];
    }

    return slow;
}
