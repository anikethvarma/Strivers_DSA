class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count = 0;
        unordered_set<char> s;

        for(auto k:allowed){
            s.insert(k);
        }

        for(auto word:words){
            bool flag = true;
            for(auto letter:word){
                if(s.find(letter) == s.end()){
                    flag = false;
                    break;
                }
            }
            if(flag) count++;
        }
        return count;
    }
};