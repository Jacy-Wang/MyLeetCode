class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.nums = []
        self.signs = []
        val = ""
        sign = False
        for i in xrange(len(s)):
            if '0' <= s[i] <= '9':
                val += s[i]
            else:
                if val:
                    self.nums.append(int(val))
                val = ""
                if s[i] == ' ':
                    continue
                if sign:
                    sign = self.compute()
                if s[i] in ['+', '-', '*', '/']:
                    self.signs.append(s[i])
                    if s[i] == '*' or s[i] == '/':
                        sign = True
        if val:
            self.nums.append(int(val))
        if sign:
            sign = self.compute()
        while self.signs:
            cal = self.signs.pop(0)
            first = self.nums.pop(0)
            second = self.nums[0]
            if cal == '-':
                self.nums[0] = first - second
            elif cal == '+':
                self.nums[0] = first + second
        return self.nums[0]

    def compute(self):
        second = self.nums.pop()
        first = self.nums.pop()
        cal = self.signs.pop()
        print first, cal, second
        if cal == '*':
            self.nums.append(first * second)
        elif cal == '/':
            self.nums.append(first / second)
        return False
