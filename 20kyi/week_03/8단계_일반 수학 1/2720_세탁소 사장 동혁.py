T = int(input())  # 테스트 케이스 수

quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(T):
    coin = int(input())  # 거스름돈
    print(coin // quarter, coin % quarter // dime, coin % quarter % dime // nickel, coin % quarter % dime % nickel // penny)