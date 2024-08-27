class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int,double>>> adj_list(n);
        for(int i=0;i<edges.size();i++){
            adj_list[edges[i][0]].push_back({edges[i][1], succProb[i]});
            adj_list[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }
        
        vector<double> prob(n,0.0);
        priority_queue<pair<double,int>> pq;
        prob[start_node] = 1.0;
        pq.push({1.0,start_node});
        while(!pq.empty()){
            auto elem = pq.top();
            pq.pop();
            double source_prob = elem.first;
            int curr = elem.second;
            if(curr == end_node) return source_prob;
            for(auto k:adj_list[curr]){
                int neighbour = k.first;
                double new_prob = k.second;
                if(prob[neighbour] < prob[curr]*new_prob){
                    prob[neighbour] = prob[curr]*new_prob;
                    pq.push({prob[neighbour],neighbour});
                }
            }
        }

        return 0.0;
    }
};