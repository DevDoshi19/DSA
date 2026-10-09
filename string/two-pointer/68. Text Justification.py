class Solution:

    """
    - (N) = number of words.
    - (W) = maximum width of a line.
    - (C) = total number of characters across all words.
    - Complexity	     \   Your solution
        Time	         \     (O(C + NW))
        Auxiliary space	 \    (O(W)) per constructed line, excluding the output
        Output space	 \    (O(LW)), where (L) is the number of output lines
    """

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        n = len(words)
        # if n == 1 :
        #     return [words[0] + " "* (maxWidth - n)]

        ans = []
        i = 0
        while i < n :
            letter = 0
            j = i 

            while j < n and (j-i) + len(words[j]) + letter <= maxWidth :
                letter += len(words[j]) 
                j += 1

            gaps = j - i - 1
            
            if j == n or gaps == 0 :
                txt = " ".join(words[i:j])
                txt += " "*(maxWidth - len(txt))

            else :
                totalSpace = maxWidth - letter 
                space = totalSpace // gaps
                extra = totalSpace % gaps

                path = []
                for k in range(i,j-1):
                    path.append(words[k])

                    spaces = space 
                    if k-i < extra:
                        spaces += 1
                    
                    path.append(" "* spaces)

                path.append(words[j-1])
                txt = "".join(path)

            ans.append(txt)

            i = j

        return ans 