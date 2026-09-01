class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque

        m, n = len(classroom), len(classroom[0])
        litter = {}
        sx = sy = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)
        if k == 0:
            return 0

        full = (1 << k) - 1
        total = m * n
        best = [[-1] * (1 << k) for _ in range(total)]

        start = sx * n + sy
        best[start][0] = energy

        q = deque([(sx, sy, energy, 0, 0)])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            x, y, e, mask, moves = q.popleft()

            if mask == full:
                return moves

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if classroom[nx][ny] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nm = mask

                if classroom[nx][ny] == 'R':
                    ne = energy

                if (nx, ny) in litter:
                    nm |= 1 << litter[(nx, ny)]

                pos = nx * n + ny

                if ne > best[pos][nm]:
                    best[pos][nm] = ne
                    q.append((nx, ny, ne, nm, moves + 1))

        return -1