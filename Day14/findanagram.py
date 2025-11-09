class Solution:
    def findAnagrams(self, s, p):
        res = []
        p_len, s_len = len(p), len(s)
        if p_len > s_len:
            return res

        p_dict = {}
        for ch in p:
            p_dict[ch] = p_dict.get(ch, 0) + 1

      
        window_dict = {}
        for i in range(s_len):

            window_dict[s[i]] = window_dict.get(s[i], 0) + 1

   
            if i >= p_len:
                left_char = s[i - p_len]
                if window_dict[left_char] == 1:
                    del window_dict[left_char]
                else:
                    window_dict[left_char] -= 1

            if window_dict == p_dict:
                res.append(i - p_len + 1)

        return res
