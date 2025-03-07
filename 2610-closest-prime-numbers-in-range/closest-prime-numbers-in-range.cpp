class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<int> sieve(right + 1,1);
        sieve[0] = sieve[1] = 0;

        for(int i=2;i*i<=right;i++){
            if(sieve[i]){
                for(long long j=i*i;j <=right;j+=i){
                    sieve[j] = 0;
                }
            }
        }

        vector<int> primes;
        for(int i=left;i<=right;i++){
            if(sieve[i]) primes.push_back(i);
        }

        if(primes.size() < 2) return {-1,-1};

        int start = primes[0];
        int gap = primes[1] - primes[0];
        for(int i=1;i<primes.size();i++){
            if(gap > primes[i] - primes[i-1]){
                gap = primes[i] - primes[i-1];
                start = primes[i-1];
            }
        }
        return {start, start+gap};
    }
};