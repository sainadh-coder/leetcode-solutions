class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # state:
        # 0..m-1      => ending at value i, last move was DOWN
        # m..2m-1     => ending at value i, last move was UP
        S = 2 * m

        def mat_mul(A, B):
            rows = len(A)
            cols = len(B[0])
            mid = len(B)

            C = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for k in range(mid):
                    if A[i][k] == 0:
                        continue
                    a = A[i][k]

                    for j in range(cols):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            sz = len(M)

            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(M, R)

                M = mat_mul(M, M)
                p >>= 1

            return R

        # n = 2 special case
        if n == 2:
            return m * (m - 1) % MOD

        # transition matrix
        T = [[0] * S for _ in range(S)]

        for x in range(m):

            # DOWN -> UP
            for y in range(x + 1, m):
                T[m + y][x] = 1

            # UP -> DOWN
            for y in range(x):
                T[y][m + x] = 1

        # initial vector for length = 2
        V = [[0] for _ in range(S)]

        for a in range(m):
            for b in range(m):
                if a == b:
                    continue

                if b > a:
                    V[m + b][0] += 1      # UP
                else:
                    V[b][0] += 1          # DOWN

        P = mat_pow(T, n - 2)

        V = mat_mul(P, V)

        ans = 0
        for i in range(S):
            ans = (ans + V[i][0]) % MOD

        return ans