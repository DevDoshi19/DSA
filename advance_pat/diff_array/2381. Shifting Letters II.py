class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * n
        for start,end,shift in shifts :
            if shift == 0 :
                diff[start] += -1
                if end +1 < n :
                    diff[end+1] += 1 
            else :
                diff[start] += 1 
                if end +1 < n :
                    diff[end+1] += -1 

        running_sum = 0
        s_list = list(s)

        for i in range(n):
            running_sum += diff[i]
            original_pos = ord(s_list[i]) - ord('a')
            new_pos = (original_pos + running_sum) % 26
            s_list[i] = chr(new_pos + ord('a'))

        return "".join(s_list)