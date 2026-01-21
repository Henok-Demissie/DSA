class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans=nums[0];
        for(int i=0;i<nums.size()-1;i++){
            ans=ans^nums[i+1];
        }
        return ans;
    }
};