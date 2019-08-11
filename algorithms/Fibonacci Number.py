class Solution:
    def fib(self, N: int) -> int:
        log = {0:0, 1:1}
        for x in range(2, N + 1):
            log[x] = log[x - 1] + log[x - 2]
        return log[N]
        