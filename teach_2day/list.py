#
# list
#   : 수정 가능한 데이터 집합, 데이터 저장
#   : sequence 자료형( 순서가 존재한다. )
#   : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   : 공통 연산을 적용할 수 있다.
# list 생성
l = [] # 빈 list
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

l = [ 1, 2, 'python' ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

colors = [ 'red', 'blue', 'green' ]
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

# 생성( 변환 ) 함수 이용한 list 생성
l = list( range( 10 ) )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

l = list( range( 1, 11, 2  ) )
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

# list 내용 포함 확인
print( "red" in colors )
print( "purple" in colors, '\n' )

# list 인덱싱
print( colors[ 0 ] )
print( colors[ 2 ] )
print( colors[ -2 ], '\n' )

# list 슬라이싱
print( colors[ 0:3 ] )
print( colors[ 1:3 ] )
print( colors[ 2: ] )
print( colors[ :2 ] )
print( colors[ ::2 ], '\n' )

# list 결합
print( colors + colors, '\n' )

# list 반복
print( colors * 3, '\n' )

# list 내용 변경
# list 일부 값 변경
l = [ 'spam', 'eggs', 100, 2020 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 2 ] = l[ 2 ] + 59
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

# list 일부 값 치환
l[ 0:2 ] = [ 1, 12 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 0:2 ] = [ 1 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# list 일부 값 삭제
l = [ 1, 12, 123, 1234 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 0:2 ] = []
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

#list 일부 값 추가
l = [ 123, 1234 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 1:1 ]= [ 'spam', 'ham' ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# del 명령을 이용한 삭제
del l[ 0 ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

del l[ 1: ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

l = list( range( 4 ) )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( 'l : {}\tlen( l ) : {}'.format( l[ ::2 ], len( l ) ) )
del l[ ::2 ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

# list 함수
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.append( 'white' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.extend( [ 'black', 'yellow' ] )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.insert( 3, 'purple' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.insert( 0, 'orange' )
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

colors.append( 'white' )
print( colors.count( 'white') )
print( colors.index( 'white' ), '\n' )

colors.reverse()
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

colors.sort()
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

colors.sort( reverse = True )
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

l = 'Python is a Programming Language'.split()
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.sort()
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.sort( key = str.lower )
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

l = [ 1, 6, 3, 8, 6, 2, 9 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.sort()            # 메소드( method )
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

l = [ 1, 6, 3, 8, 6, 2, 9 ]
new = sorted( l )   # 함수( function )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( 'new2 : {}\tlen( new2 ) : {}\n'.format( new, len( new ) ) )

print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )
colors.remove( 'red' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )
del colors[ : ]
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

l = []

l.append( 5 )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.append( 10 )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.append( 15 )
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

print( l.pop() )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( l.pop() )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( l.pop() )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

# 중첩 list( 2차원 )
korScore = [ 59, 99, 79 ]
engScore = [ 57, 97, 77 ]
midterm = [ korScore, engScore ]
print( 'midterm : {}\nlen( midterm ) :{}'.format( midterm, len( midterm ) ) )

print( '\n', midterm[ 0 ] )
print( midterm[ 0 ][ 1 ] )
print( midterm[ 0 ][ 1: ] )

# list의 패킹/언패킹
t = [ 1, 2, 3 ]     # 패킹
a, b, c = t         # 언패킹
print( t )
print( a, b, c )














