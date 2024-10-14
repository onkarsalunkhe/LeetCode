class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int len = nums.size();

        for (int i=0,j=i+1; i<len-1,j<len;){
            if (nums[i]!=0) {
                i++;
                j++;
            }
            else if (nums[j]==0) {
                j++;
            }
            else if(nums[j]!=0){
                nums[i]=nums[j];
                nums[j]=0;
                i++;
                j++;
            }
        }
    }
};