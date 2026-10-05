"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
Note: The characters in the array beyond the returned length do not matter and should be ignored.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].
"""

"""
notes :
- create two pointers read and write
- read pointer iterates through the array
- write pointer keeps track of the position to write the compressed characters
- for each group of consecutive repeating characters, write the character and its count (if greater than 1) to the write position
- return the length of the compressed array (write pointer)

"""

class Solution:
    def compress(self, chars: list[str]) -> int:
        # two pointer read-write apporch 
        read = 0
        write = 0
        n = len(chars)
        while read < n:
            ch = chars[read]
            start = read
            while read < n and chars[read] == ch:
                read += 1
                
            count = read-start
            chars[write] = ch
            write+=1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write+=1

        return len(chars[:write])