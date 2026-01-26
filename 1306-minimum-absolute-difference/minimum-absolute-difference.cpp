static constexpr int N=2048, MASK=2047, bshift=11;
static int freq[N];

void radix_sort(int* nums, int n) {// 2 rounds
    int* buf=(int*)alloca(n * sizeof(int));

    const int bias=*min_element(nums, nums+n);
    // normalize! 
    // auto-vectorized (SIMD)
    for (int i=0; i<n; i++) nums[i]-=bias;

    int* in=nums;
    int* out=buf;

    //1st round
    memset(freq, 0, sizeof(freq));

    for (int i=0; i<n; i++) 
        freq[in[i] & MASK]++;

    partial_sum(freq, freq+N, freq);

    for (int i=n-1; i>=0; i--) {
        const int v=in[i];
        out[--freq[v & MASK]]=v;
    }

    // 2nd round
    memset(freq, 0, sizeof(freq));

    for (int i=0; i<n; i++)
        freq[(out[i]>>bshift) & MASK]++;

    partial_sum(freq, freq+N, freq);

    for (int i=n-1; i>= 0; i--) {
        const int v=out[i];
        in[--freq[(v>>bshift) & MASK]]=v;
    }

    // restore! auto-vectorized (SIMD)
    for (int i=0; i<n; i++) nums[i]+=bias;
}

class Solution {
public:
    static vector<vector<int>> minimumAbsDifference(vector<int>& arr){
        const int n=arr.size();
        int* a=arr.data();
        radix_sort(a, n);
        
        int minD=1e9+7;
        for(int i=1; i<n; i++){
            minD=min(minD, a[i]-a[i-1]);
        }
        vector<vector<int>> ans;
        for(int i=1; i<n; i++){
            if (a[i]-a[i-1]==minD)
                ans.push_back({a[i-1], a[i]});
        }
        return ans;
    }
};
auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();