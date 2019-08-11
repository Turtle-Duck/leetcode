
def num_1(num):
    count = 0
    while num != 0:
        num = num & (num - 1)
        count += 1
    return count


# 二进制表示中1个数相同则为一类。输入某序列，一共有几类？
def f1():
    times = int(input())
    # print(times)
    for i in range(times):
        m = dict()
        num_sum = int(input())
        nums = input().split(' ')
        for n in nums:
            m[num_1(int(n))] = True
        print(len(m))


# m1入水，t1分钟一换
# m2出水，t2分钟一换
# m容量，t分钟有多少水？
# 5
# 10 2 1 5 2 5
# 10 2 10 5 2 5
# 10 2 3 5 2 5
# 100 100 3 4 4 3
# 10000 1000 10 5 5 3
def f2():
    times = int(input())
    # print(times)
    for i in range(times):
        inpp = input().split(' ')
        m = int(inpp[0])
        t = int(inpp[1])
        m1 = int(inpp[2])
        t1 = int(inpp[3])
        m2 = int(inpp[4])
        t2 = int(inpp[5])
        water = 0
        for tt in range(t):
            s1 = tt % (2*t1) < t1
            s2 = tt % (2*t2) < t2
            if s1 and s2:
                if m1 - m2 > 0:
                    water = min(m, water + m1 - m2)
                else:
                    water = max(0, water + m1 - m2)
            elif s1:
                water = min(m, water + m1)
            elif s2:
                water = max(0, water - m2)
            #     water += m1
            # if t % (2*t2) < t2:
            #     water -= m2
            # if water > m:
            #     water = m
            # if water < 0:
            #     water = 0
        print(water)


# 3
# NNTN
# NNNNGGNNNN
# NGNNNNGNNNNNNNNSNNNN
# 可以修改至多两个非N为N，求N最长序列
def f3():
    times = int(input())
    # print(times)
    for i in range(times):
        inpp = input()
        old_is_N = False
        count = 0
        value = list()
        bad_count = 0
        for t in inpp:
            if old_is_N:
                if t == "N":
                    count += 1
                else:
                    value.append(count)
                    value.append(0)
                    count = 0
                    old_is_N = False
                    bad_count += 1
            else:
                if t == "N":
                    count = 1
                    old_is_N = True
                else:
                    value.append(0)
                    value.append(0)
                    bad_count += 1
        if count != 0:
            value.append(count)
        if bad_count <= 2 or len(value)<5:
            print(sum(value)+bad_count)
        else:
            win_sum = 0
            # print(value)
            for i in range(5):
                win_sum += value[i]
            max_sum = win_sum
            for i in range(5, len(value)):
                win_sum += (value[i] - value[i-5])
                if win_sum > max_sum:
                    max_sum = win_sum
            print(max_sum+2)


if __name__ == "__main__":
    f2()

















