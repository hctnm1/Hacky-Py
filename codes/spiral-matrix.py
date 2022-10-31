class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        pos = [0, 0]
        move = (0, 1)
        for index in range(1, n * n + 1):
            res[pos[0]][pos[1]] = index
            if res[(pos[0] + move[0]) % n][(pos[1] + move[1]) % n] > 0:
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                move = (move[1], -1 * move[0])
            pos[0] = pos[0] + move[0]
            pos[1] = pos[1] + move[1]
        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.generateMatrix(2)
