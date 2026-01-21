public class Solution {
    public int HammingWeight(int n) {
        string s = Convert.ToString(n, 2);
        int count=0;
        foreach(char ch in s){
            if(ch== '1'){
                count++;
            }
        }
        return count;
    }
}