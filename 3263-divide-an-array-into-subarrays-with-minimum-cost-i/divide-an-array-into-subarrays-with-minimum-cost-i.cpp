class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int n=nums.size();
        int x1=INT_MAX, x2=INT_MAX;
        for (int i=1; i<n; i++){
            int x=nums[i];
            bool is_min=(x<x1), is_sec=((!is_min)&(x<x2)), neither=(!(is_min|is_sec));
            x2=(-is_min & x1)+(-is_sec & x)+(-neither & x2);
            x1=(-is_min & x)+(-!is_min & x1);
        }
        return nums[0]+x1+x2;
    }
};

auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();