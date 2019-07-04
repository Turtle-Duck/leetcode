def list_pro(a):
    rst = 1
    for i in a:
        rst *= i
    return rst


def comp_list(a):
    rst = 0
    leng = len(a)
    for i in range(leng - 4):
        for j in range(i+5, leng + 1):
            rst += list_pro(a[i:j])
    return rst


def ttt1():
    times = input()
    times = int(times)
    card_to_num = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    for i in range(times):
        card_count = [0 for zz in range(13)]
        card_sum = int(input())
        card_input = input()
        temp_list = list()
        rst = 0
        count = 0
        for j in card_input.split(' '):
            card_count[card_to_num[j]-1] += 1

        for j in range(13):
            if card_count[j] == 0 or j == 12:
                if count >= 5:
                    rst += comp_list(temp_list)
                temp_list = list()
                count = 0
            else:
                temp_list.append(card_count[j])
                count += 1
        print(rst)


def ttt2():
    times = input()
    times = int(times)
    for i in range(times):
        number = input()
        leng = len(number)
        y = leng % 3
        rst = ''
        if y == 1:
            number = '00' + number
        elif y == 2:
            number = '0' + number
        leng = len(number)
        for j in range(int(leng/3)):
            temp_num = int(number[3*j:3*j+3])
            t1 = temp_num // 32
            t2 = temp_num % 32
            if t1 > 0:
                if t1 < 10:
                    rst = rst + str(t1)
                else:
                    rst = rst + chr(t1-10+65)

            if t2 < 10:
                rst = rst + str(t2)
            else:
                rst = rst + chr(t2-10+65)
        print(rst)


def ttt3():
    times = input()
    times = int(times)
    for i in range(times):
        temp = input()
        temp = temp.split(' ')
        dian_count = int(temp[0])
        xian_count = int(temp[1])
        xian_adj = dict()
        start = int(temp[2])
        power = int(temp[3])
        temp = input()
        temp = temp.split(' ')
        rongliang = list()
        shengyu_rongiang = list()
        for j in range(dian_count):
            rongliang.append(float(temp[j]))
            shengyu_rongiang.append(float(temp[j]))
            xian_adj[j] = list()
        if xian_count > 0:
            for j in range(xian_count):
                xian_position = input()
                st = int(xian_position.split(' ')[0]) - 1
                ed = int(xian_position.split(' ')[1]) - 1
                xian_adj[st].append(ed)
        dian_time = [0. for j in range(dian_count)]
        all_time = 0

        changing = [start-1]
        powering = [power]

        while len(changing) != 0:

            min_time = 1e30
            min_index = -1
            for q in range(len(changing)):
                if shengyu_rongiang[changing[q]] / powering[q] < min_time:
                    min_index = q
                    min_time = shengyu_rongiang[changing[q]] / powering[q]

            delete_dian_list = list()
            delete_index = list()
            for q in range(len(changing)):
                shengyu_rongiang[changing[q]] -= powering[q] * min_time
                if shengyu_rongiang[changing[q]] == 0:
                    delete_dian_list.append(changing[q])
                    delete_index.append(q)
            all_time += min_time
            delete_index.reverse()

            # delete_dian = changing[min_index]

            for delete_dian in delete_dian_list:
                dian_time[delete_dian] = all_time
                output_num = len(xian_adj[delete_dian])
                if output_num > 0:
                    for q in xian_adj[delete_dian]:
                        if q in changing:
                            q_old_index = changing.index(q)
                            powering[q_old_index] += 1.0 * powering[min_index] / output_num
                        else:
                            changing.append(q)
                            powering.append(1.0 * powering[min_index] / output_num)

            for q in delete_index:
                del changing[q]
                del powering[q]

        for q in range(len(dian_time)):
            if q != len(dian_time) - 1:
                if shengyu_rongiang[q] > 0:
                    print('%.4f' % -1, end=' ')
                else:
                    print('%.4f' % dian_time[q], end=' ')
            else:
                if shengyu_rongiang[q] > 0:
                    print('%.4f' % -1)
                else:
                    print('%.4f' % dian_time[q])


if __name__ == '__main__':
    ttt3()





