def with_cache(func):
    _cache: dict[tuple, int] = {}
    def _wrapper(*args):
        print(f'{args=} | {_cache=}')
        if args in _cache:
            return _cache[args]
        res = func(*args)
        _cache[args] = res
        return res
    return _wrapper

class Solution:
    def climbStairs(self, n: int) -> int:
        @with_cache
        def _backtrack(total: int) -> int:
            # Base Cases
            if total > n:
                return 0

            if total == n:
                return 1

            # Recurrence Relation
            return _backtrack(total + 1) + _backtrack(total + 2)
            
        res = _backtrack(0)
        return res