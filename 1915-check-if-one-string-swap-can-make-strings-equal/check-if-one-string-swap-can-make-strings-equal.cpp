class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.size();
        int p1 = 0;
        int p2 = n-1;

        while(p1 <= p2){
            if(s1[p1] == s2[p1]) p1++;
            else if(s1[p2] == s2[p2]) p2--;
            else{
                char temp = s2[p1];
                s2[p1] = s2[p2];
                s2[p2] = temp;
                p1++;
                p2--;
                break; 
            }
        }
        return s1 == s2;
    }
};