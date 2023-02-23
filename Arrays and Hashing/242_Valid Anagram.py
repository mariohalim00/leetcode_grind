class Solution:
    def convertToDictionaryCounter(self, string: str):
        ret_val = {}
        for i in string:
            if i not in ret_val:
                ret_val[i] = 1
            else:
                ret_val[i] = ret_val[i] + 1
        return ret_val

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict_count = self.convertToDictionaryCounter(s)
        t_dict_count = self.convertToDictionaryCounter(t)
        print(s_dict_count)
        print(t_dict_count)
        for key in s_dict_count:
            if key not in t_dict_count: 
                return False
            if s_dict_count[key] != t_dict_count[key]:
                return False
            else:
                continue
        return True