import sys


def com(count, real_p_l):
    if count == 98:
        return real_p_l[count]
    return real_p_l[count] + (1 - real_p_l[count]) * (1 - real_p_l[count + 1]) * com(count + 2, real_p_l)



p_l = list()
real_p_l = list()
a = int(input())
for i in range(a):
    p_l.append(float(input()))
if a > 100:
    real_p_l = p_l[:100]
else:
    while True:
        if len(real_p_l) > 100:
            real_p_l = real_p_l[:100]
            break
        else:
            real_p_l = real_p_l + p_l

rst = com(0, real_p_l)

print('%.4f' % rst)
# sys.stdout.write(str(rst))


