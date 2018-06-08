class Solution {
public:
    void combinationSum2Helper(std::vector<int>& candidates,
            int target, std::vector<int> candidate,
            int index, std::vector<std::vector<int>>& result) {
        if (target == 0) {
            result.push_back(candidate);
            return;
        }
        for (int i = index; i < candidates.size() && candidates[i] <= target; ++i) {
            if (i != index && candidates[i] == candidates[i-1]) {
                continue;
            }
            candidate.push_back(candidates[i]);
            combinationSum2Helper(candidates, target - candidates[i], candidate, i + 1, result);
            candidate.pop_back();
        }
    }

    std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
        std::vector<std::vector<int>> result;
        std::sort(candidates.begin(), candidates.end());
        std::vector<int> candidate;
        int index = 0;
        combinationSum2Helper(candidates, target, candidate, index, result);
        return result;
    }
};
