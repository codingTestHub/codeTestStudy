# [BOJ] 4673_셀프넘버_실버5

limit = 10000


# 셀프 넘버 아닌 숫자
def d(n):
    return n + sum(map(int, str(n)))


# 셀프 넘버인 숫자
def find_self_numbers(limit):
    all_numbers = set(range(1, limit))  #모든 숫자 집합 (1~10001)
    non_self_numbers = set()            #셀프 넘버 아닌 숫자 집합

    for n in range(1, limit):
        non_self_numbers.add(d(n))      #셀프 넘버 아닌 숫자 집합에 d(n) 추가

    self_numbers = all_numbers - non_self_numbers   #셀프넘버 = 모든숫자집합-셀프넘버아닌집합
    return sorted(self_numbers)


self_numbers = find_self_numbers(limit)

for num in self_numbers:
    print(num)
