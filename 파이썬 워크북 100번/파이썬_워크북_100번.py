#연습 100번
def determine_leap(year):
    if year%400==0:
        if year%100!=0:
            return 29
    elif year%4==0:
        if year%100!=0:
            return 29
    else:
         return 28

def determine_lastday(month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30

year=int(input("연도를 입력해주세요: "))
month=int(input("달 을 입력해주세요: "))
if month ==2:
    print("{}년 {}월의 마지막 날은 {}입니다.".format(year,month,determine_leap(year)))
else:
    print("{}년 {}월의 마지막 날은 {}입니다.".format(year,month,determint_lastday(month)))


#연습 101번
#최대공약수 구하는 문제인 75번을 참고.
#분자 분모를 각각 받은 다음, 분자와 분모의 관계가 소수
def max_div(m,n):
    if m<=n:
        d=n
    else:
        d=m
    for i in range(2,d+1):
        if m%i==0 and n%i==0:
            max_div=i
    return max_div
m=int(input("분자의 값을 입력해주세요: "))
n=int(input("분모의 값을 입력해주세요: "))
max_div=max_div(m,n)
m=m//(max_div)
n=n//(max_div)
print("약분 된 결과값은 {}/{}입니다.".format(m,n))

#연습 102번
#계량에 대한 문제 (컵,테이블 스푼(큰 숟가락), 티스푼(작은 숟가락))
#돈으로 따지면, 15500원을 만원 지폐 1장 5천원 지폐 1장, 500원 1개 이런식
#1컵=16테이블 스푼, 1테이블 스푼=3티스푼
#1컵=48티스푼, 1테이블 스푼=3티스푼

def measures(teaspoon):
    tablespoon=0
    cup=0
    cup=teaspoon//48
    teaspoon=teaspoon%48
    tablespoon=teaspoon//3
    teaspoon=teaspoon%3
    measure=[cup,tablespoon,teaspoon]
    return measure

teaspoon=int(input("몇 티스푼인지 입력해주세요: "))
measure=measures(teaspoon)
print("{} 컵 {} 테이블 스푼 {} 티스푼과 같은 계량입니다.".format(measure[0],measure[1],measure[2]))