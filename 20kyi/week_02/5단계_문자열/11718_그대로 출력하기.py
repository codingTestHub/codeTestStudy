# ???
# input()과 sys.stdin.readline()의 차이점이 나온다.
# input()은 EOF를 받을 때 EOFError를 일으키지만 sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴을 한다.
# 따라서 오류가 발생하지 않고 틀리게 되는 것이다.

while True:
    try:
        print(input())
    except EOFError:
        break
