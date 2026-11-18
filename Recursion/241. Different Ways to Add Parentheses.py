class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:

        op = set("+-*")

        def solve(expression):
            result = []

            for i in range(len(expression)):
                if expression[i] in op :
                    left = solve(expression[:i])
                    right = solve(expression[i+1:])

                    for l in left:
                        for r in right:
                            if expression[i] == "*":
                                result.append(l*r)
                            if expression[i] == "+":
                                result.append(l+r)
                            if expression[i] == "-":
                                result.append(l-r)

            if not result :
                return [int(expression)]
            
            return result

        return solve(expression)