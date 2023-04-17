print("Hello world!")


# 기본 입출력 

""" side1 = float(input('한 변의 길이 입력 : '))
side2 = float(input('다른 한 변의 길이 입력 : '))

hyp = (side1 * side1 + side2 * side2) ** 0.5

print('빗변의 길이 = ' , hyp) """

# 함수 정의 

def main():
    side1 = float(input('한 변의 길이 입력 : '))
    side2 = float(input('다른 한 변의 길이 입력 : '))
    hyp = (side1 * side1 + side2 * side2) ** 0.5
    print('빗변의 길이 = ' , hyp)
    
# if문 

age = int(input('나이: '))

if age < 13 : 
    print('초등학생입니다.')
elif age < 20 : 
    print('중고등학생 입니다.')
elif age < 30 : 
    print('20대 입니다.')
else : 
    print('이상')
    
# while문 - 조건문 만족하는 동안 계속 반복함 
#           조건문을 만족하지 않는다면 반복 중단

def print_nums(n) : 
    i = 1 
    while i <= n:
        print(i, end = ' ')
        i += 1

# 예제1 - 피보나치 수열 함수 (매개변수 보다 작은 모든 수열 값 구하기)

def pr_fibo(n) :
    a, b = 1, 0 # 튜플 대입 
    while a < n:
        print(a, sep = ' ')
        a, b = a + b, a # 보이는 그대로 a에는 a+b를 b에는 a를 대입하는 코드
        
# 에제2 - up & down 게임 

from random import randint 
n = randint(1, 50) # 1 ~ 50의 임의의 숫자 

while True: 
    ans = int(input('어떤 숫자인지 맞춰봐라. '))
    if ans > n : print('down')
    
    elif ans < n : print('up')
    
    else :
        print('정답입니다!')
        break
    
    
        
        