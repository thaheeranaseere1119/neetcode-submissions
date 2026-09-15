class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Word completely matched
            if i == len(word):
                return True

            # Invalid cell
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore 4 directions
            res = (
                dfs(r + 1, c, i + 1)  # down
                or dfs(r - 1, c, i + 1)  # up
                or dfs(r, c + 1, i + 1)  # right
                or dfs(r, c - 1, i + 1)  # left
            )

            # Backtrack
            path.remove((r, c))

            return res

        # Try starting from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False