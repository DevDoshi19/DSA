from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids :
            if n > 0 :
                stack.append(n)
            if n < 0 :
                distroyed = False
                while stack and stack[-1] > 0: 
                    if stack[-1] < (n*-1) :
                        stack.pop()
                    elif stack[-1] > (n*-1):
                        distroyed = True
                        break
                    else :
                        distroyed = True
                        stack.pop()
                        break
                if not distroyed:
                    stack.append(n)

        return stack

                        