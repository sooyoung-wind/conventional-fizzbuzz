def do_fizzbuzz(num):
    """
    fizzbuzz 기능을 수행합니다.
    정해진 숫자에 대해,
    3의 배수는 'fizz'
    5의 배수는 'buzz'
    15의 배수는 'fizzbuzz'
    나머지는 숫자 그대로를 출력합니다.
    """
    for i in range(1,num+1):
        if i%3==0 or i%5==0:
            print('fizz'*(i%3==0)+'buzz'*(i%5==0))
        else:
            print(i)

if __name__=='__main__':
    do_fizzbuzz(16)
