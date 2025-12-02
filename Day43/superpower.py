class Solution(object):
    def mod_pow(self,a, k):
        result = 1
        MOD = 1337
        a %= MOD
        while k > 0:
            if k & 1:
                result = (result * a) % MOD
            a = (a * a) % MOD
            k >>= 1
        return result

    def superPow(self,a, b):
        MOD = 1337
        if not b:
            return 1
        
        last_digit = b.pop()
        
        part1 = self.mod_pow(self.superPow(a, b), 10)
        part2 = self.mod_pow(a, last_digit)
        
        return (part1 * part2) % MOD
            