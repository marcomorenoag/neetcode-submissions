class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def _backtracking(idx: int, cur: List[int], total: int) -> None:
            # BASE CONDITIONS
            if target == total:
                res.append(cur.copy()) # Store a copy
                return
            if idx >= len(candidates) or total > target:
                return

            # LEFT PATH
            ## W/o picking new candidate
            cur.append(candidates[idx])
            _backtracking(idx, cur, total + candidates[idx])
            
            # RIGHT PATH
            ## Backtrack and explore right path
            cur.pop()
            _backtracking(idx+1, cur, total)

        _backtracking(0, [], 0)
        return res