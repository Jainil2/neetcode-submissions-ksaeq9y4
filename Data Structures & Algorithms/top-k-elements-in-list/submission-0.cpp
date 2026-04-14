class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> answer;
        unordered_map<int, int> count;
        for(auto num : nums) {
            count[num]++;
        }
        vector<pair<int,int>> arr;
        for(const auto& p: count) {
            arr.push_back(make_pair(p.second,p.first));
        }
        sort(arr.rbegin(), arr.rend());
        for(int i = 0; i < k; i++) {
            answer.push_back(arr[i].second);
        }
        return answer;
    }
};
