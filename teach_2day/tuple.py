#
# tuple
#   : 수정 불가능한 데이터 집합, 데이터 저장
#   : sequence 자료형( 순서가 존재한다. )
#   : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   : 공통 연산을 적용할 수 있다.
# tuple 생성
t = () # 빈 튜플
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = ( 1, 2, 3 )
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = 1, 2, 3
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = ( 1, )
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = 1,
print( 't : {}\tlen( t ) : {}\n'.format( t, len( t ) ) )

# 튜플 내용 포함 확인
t = ( 1, 2, 3 )
print( 1 in t )
print( 5 in t, '\n' )

# 튜플 인덱싱
print( t[ 0 ] )
print( t[ 2 ] )
print( t[ -2 ], '\n' )

# 튜플 슬라이싱
print( t[ 0:3 ] )
print( t[ 1:3 ] )
print( t[ 2: ] )
print( t[ :2 ] )
print( t[ ::2 ], '\n' )

# 튜플 결합
print( t + t, '\n' )

# 튜플 반복
print( t * 2, '\n' )

# 튜플 함수
t = ( 1, 2, 3, 2, 5, 1, 4, 3 )
print( t.count( 2 ) )
print( t.index( 2 ) )
print( t.index( 2, 2 ) )

# 튜플 중첩
t1 = ( 1, 2, 3 )
t2 = ( "hello", 2020, 'world' )
t = t1, t2
print( t )
print( t[ 0 ][ 1 ], '\n' )

t = ( 1, 2, 3), ( 'hello', 2020, 'world' ), 10
print( t )
print( t[ 0 ] )
print( t[ 0 ][ : 2 ] )
print( t[ 2 ], '\n' )

# 튜플을 이용한 데이터 치환
x, y, z = 1, 2, 3
print( x, y, z )
( x1, x2 ), ( y1, y2 ) = ( 1, 2 ), ( 3, 4 )
print( x1, x2, y1, y2, '\n' )

x, y = 1, 2
print( x, y )
t = x
x = y
y = t
print( x, y, '\n' )

x, y = 1, 2
print( x, y )
x, y = y, x
print( x, y, '\n' )

# 패킹( Packing ) : 한 공간에 여러개의 데이터를 넣는 행위
# 언패킹( Unpacking ) : 데이터 집합의 내용을 꺼오는 행위
t = 1, 2, 'python'  # 패킹
print( t )
x, y, z = t         # 언패킹
print( x, y, z, '\n' )

# 확장된 언패킹
# 확장된 언패킹에서 *의 의미는 전부라는 뜻
t = ( 1, 2, 3, 4, 5 )
print( t )
a, *b = t
print( a, b )
*a, b = t
print( a, b )
a, b, *c = t
print( a, b, c )

# 튜플이 활용되는 경우
# 1. 함수에서 하나 이상의 값을 반환( return 값 ) 할 때 활용
# 2. 함수의 인수로 활용
# 3. 파이썬 2형식의 print() 형식 지정 출력에 사용



