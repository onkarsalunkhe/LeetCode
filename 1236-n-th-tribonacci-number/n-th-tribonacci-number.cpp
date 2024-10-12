class Solution {
public:
    int tribonacci(int n) {
        /*
        Recursion
        if (n==0) return 0;
        else if (n==1) return 1;
        else if (n==2) return 1;
        else {
            return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3);
        }
        */
        if (n==0) return 0;
        else if (n==1 || n==2) return 1;

        int T0 = 0;
        int T1 = 1;
        int T2 = 1;
        int ans = 0;
        for (int i=3; i<=n;i++){
            ans = T0 + T1 + T2; 
            T0 = T1;
            T1 = T2;
            T2 = ans;
        }
        return ans;
    }
};