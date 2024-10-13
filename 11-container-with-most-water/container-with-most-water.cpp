class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int len = height.size();
        for (int i=0,j=len-1; i<j;)
        {
            int area = 0;
            if (height[i]<=height[j]){
                area = (j-i)*height[i];
                i++;
            }else {
                area = (j-i)*height[j];
                j--;
            }
            if (area > maxArea){
                maxArea = area;
            }
        }
        return maxArea;
    }
};