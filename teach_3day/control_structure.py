#
# 제어 구조
#  : 프로그램의 실행 구조를 결정
#  1. 순차 구조 : 위에서 아래로 차례대로 명령을 실행 하는 구조
#  2. 선택 구조 : 조건 판단의 결과에 따라 실행 방향을 결정하는 구조
#  3. 반복 구조 : 정해진 횟수나 조건에 따라 일정한 명령 집합( 코드 블록 )을
#                 반복해서 실행하는 구조
#
#  프로그램은 자료형, 연산자, 제어문을 활용하여 문제에서 요구하는 사항을
#  해결하는 명령 집합( 코드 블록 )이다.
#
# 선택 구조( if ~ elif ~ else )
#   if < 조건식1 >:
#       < 명령문 1 >    -> 조건식1이 참일 때 수행
#  [elif < 조건식2 >:]
#       < 명령문 2 >    -> 조건식2가 참일 때 수행
#  [else:]
#       < 명령문 3 >    -> 모든 조건이 만족하지 않을 때 수행
#
# 선택 구조 형태
# 1. 단순 선택 구조 -> if만 사용
# 2. 양자 택일 구조 -> if ~ else
# 3. 다중 선택 구조 -> if ~ [elif ... ] ~ else
#
# 1. 단순 선택 구조
number = 10
if number > 0:
    print( "Yes, sir!!!\n" )

if number != 0 and number > 0:
    print( "Yes, sir!!!" )
    print( "number : {}\n".format( number ) )

number = -10
if number != 0 and number > 0:
    print( "Yes, sir!!!" )
print( "number : {}\n".format( number ) )

# 3. 다중 선택
if number != 0 and number > 0:
    print( "Positive" )
elif number != 0 and number < 0:
    print( "Negative" )
else:
    print( "zero" )
print( "number : {}\n".format( number ) )

order = 'spagetti'
if order == 'spam':
    price = 500
elif order == 'ham':
    price = 700
elif order == 'egg':
    price = 100
elif order == 'spagetti':
    price = 1000
else:
    price = 0
print( "Order : {}\tprice : {}\n".format( order, price ) )

# 2. 양자 택일 구조
lunch = '먹는다'
if lunch == '먹는다':
    print( "살찌겠군!!!\n" )
else:
    print( "몸 망가지겠군!!!\n" )

# 선택구조 대신에 dict를 사용하는 것이 더 편리할 때도 있다.
# 이 형태가 Python스러운 code
order = 'spam'
menu = { 'spam':500, 'ham':700, 'egg':100, 'spagetti':1000 }
price = menu.get( order, 0 )
print( "Order : {}\tprice : {}\n".format( order, price ) )

# 삼항 연산자를 이용한 선택
if price >= 500:
    message = "VIP"
else:
    message = "non VIP"
print( "Order : {}\tprice : {}\t{}\n".format( order, price, message ) )

# 삼항 연산자( 양자 택일일 경우에 사용 )
#          참        조건            거짓
message = "VIP" if price >= 500 else "non VIP"
print( "Order : {}\tprice : {}\t{}\n".format( order, price, message ) )

#
# 반복구조
# 1. for문 : 반복 횟수가 일정한 경우 사용
# 2. while문 : 반복 횟수가 일정하지 않은 경우 사용
#
# 1. for문
# for < 반복제어변수 > in < 반복을 횟수를 결정하는 객체( sequence 형 ) >:
#   < 반복 수행 내용 >
#
l = [ 'cat', 'cow', 'tiger' ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

for value in l:
    print( 'value : {}( {} )'.format( value, len( value ) ) )

print()
for i in range( 0, len( l ), 2 ):
    print( i, end = '\t' )
    print( 'value : {}( {} )'.format( l[ i ], len( l[ i ] ) ) )


print()
for i in range( 1, 11, 1 ):
    print( i, end = ' ' )
print()

str = 'Python is great!!!'
for value in str:
    print( value, end = ' ' )
print()

for i in range( len( str ) ):
    print( str[ i ], end = ' ' )
print()

t = ( 100, 'hello', True, 'Hong' )
print( '\nt : {}( {} )\n'.format( t, len( t ) ) )

for value in t:
    print( value, end = ' ' )
print()

for i in range( len( t ) ):
    print( t[ i ], end = ' ' )
print()

# enumerate() : 요소의 값과 인덱스를 제공하는 함수
#               ( 인덱스, 요소값 )형식으로 tuple로 제공
print()
for i, value in enumerate( l ):
    print( 'i : {}\tvalue : {}'.format( i, value ) )
print()

# break : 반복을 탈출할 때 사용
# continue : 반복 조건 검사 수행
print()
for i in range( 1, 101, 1 ):
    if ( i % 10 ) == 0:
        continue
    if ( i >= 20 ):
        break
    print( '{:5d}'.format( i ), end = '' )

#
# 2. while문
# 반복 제어 변수 초기화
# while < 반복 탈출 조건 >:   -> 참인동안 반복
#   < 반복 수행 내용>
#   반복 제어 변수 변화
#
print()
i = 1                       # 반복 제어 변수 초기화
while i <= 10:              # 반복 탈출 조건 검사
    print( i, end = ' ' )
    i += 1                  # 반복 제어 변수 변화
print()

i = 1
while True:
    if ( i > 10 ):
        break;
    print( i, end = ' ' )
    i += 1
print()

# 2-read 기법
i = 1;
str = input( 'Input string ( quit : "end" ) : ' )
while str.lower() != 'end':
    print( '[{:3d}] : {}'.format( i, str ) )
    i += 1
    str = input('Input string ( quit : "end" ) : ')



