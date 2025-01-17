class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int res = 0;
        for(auto k: derived) res = res ^ k;
        return !res;
    }
};