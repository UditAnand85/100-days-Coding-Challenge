class Solution:
    def toggleBits(self, N, L, R):
        for i in range(L, R + 1):
            bit = (N >> (i - 1)) & 1

            if bit == 1:
                N = N & ~(1 << (i - 1))
            else:
                N = N | (1 << (i - 1))

        return N
            
            