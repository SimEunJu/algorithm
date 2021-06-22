class Solution:
    stack = []
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def findDfs(openCnt, closeCnt, path):
            if openCnt == 0:
                for i in range(0, closeCnt):
                    path += ")"
                for i in range(0, len(path)):
                    if path[i] == "(":
                        self.stack.append("(")
                    elif len(self.stack) != 0:
                        self.stack.pop()
                    else:
                        return
                if len(self.stack) == 0:
                    result.append(path)
                self.stack = []
                return
            if closeCnt == 0:
                return
            
            findDfs(openCnt-1, closeCnt, path+"(")
            findDfs(openCnt, closeCnt-1, path+")")
        print(result)
        findDfs(n-1, n, "(")
        return result
