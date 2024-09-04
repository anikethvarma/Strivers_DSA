class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        set<pair<int,int>> s;
        for(auto elem: obstacles){
            s.insert({elem[0],elem[1]});
        }
            
        int direction = 0;
        int xi = 0;
        int yi = 0;
        int ans = 0;

        for(auto command: commands){
            if (command == -1) direction = (direction+1)%4;
            else if(command == -2) direction = (direction+3)%4;
            else{
                if (direction == 0){
                    while(command > 0 and s.find({xi,yi+1}) == s.end()){
                        yi++;
                        command -= 1;
                    }
                        
                }
                else if(direction == 1){
                    while(command > 0 and s.find({xi+1,yi}) == s.end()){
                        xi++;
                        command -= 1;
                    }
                }
                else if(direction == 2){
                    while(command > 0 and s.find({xi,yi-1}) == s.end()){
                        yi--;
                        command -= 1;
                    }
                }
                else if(direction == 3){
                    while(command > 0 and s.find({xi-1,yi}) == s.end()){
                        xi--;
                        command -= 1;
                    }
                }
                    
                ans = max(ans,xi*xi + yi*yi);
            }
            cout << xi << ' ' << yi << direction << endl;
        }
            
                
        return ans;

    }
};