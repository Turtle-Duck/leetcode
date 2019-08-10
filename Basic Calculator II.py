class Solution:
    def calculate(self, s: str) -> int:
        data_list = list()
        oper_list = list()
        s_l = len(s)
        data_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        op_1 = ["+", "-"]
        op_2 = ["*", "/"]
        temp = 0
        for i in range(s_l):
            if s[i] in data_set:
                temp = 10 * temp + int(s[i])
                if i+1<s_l and s[i+1] in data_set:
                    continue

            if s[i] == ' ':
                continue
            if s[i] in data_set:
                if len(oper_list) > 0 and oper_list[-1] in op_2:
                    op = oper_list.pop()
                    d1 = data_list.pop()
                    if op == "*":
                        data_list.append(d1 * temp)
                    else:
                        data_list.append(d1 // temp)
                else:
                    data_list.append(temp)
            elif s[i] in op_1:
                if len(oper_list) > 0 and oper_list[-1] in op_1:
                    op = oper_list.pop()
                    d2 = data_list.pop()
                    d1 = data_list.pop()
                    if op == "+":
                        data_list.append(d1 + d2)
                    else:
                        data_list.append(d1 - d2)
                oper_list.append(s[i])
            elif s[i] in op_2:
                oper_list.append(s[i])

            temp = 0

        if len(oper_list) > 0:
            op = oper_list.pop()
            d2 = data_list.pop()
            d1 = data_list.pop()
            if op == "+":
                return d1 + d2
            elif op == "-":
                return d1 - d2
            elif op == "*":
                return d1 * d2
            else:
                return d1 // d2

        return data_list[0]


if __name__ == '__main__':
    a = Solution()
    rst = a.calculate("1+1+1")
    print(rst)