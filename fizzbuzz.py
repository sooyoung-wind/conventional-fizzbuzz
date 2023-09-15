def do_fizzbuzz():
    """
    fizzbuzz 기능을 수행합니다.
    정해진 숫자에 대해,
    3의 배수는 'fizz'
    5의 배수는 'buzz'
    15의 배수는 'fizzbuzz'
    나머지는 숫자 그래도를 출력합니다.
    """
    for i in range(1,20+1):
        if i%3==0:
            print('fizz')
        else:
            print(i)

if __name__ == '__main__':
    do_fizzbuzz()
