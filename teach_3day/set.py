#
# set( 집합 )
#  : 순서 없이 중복 없이 저장하는 set 자료형
#  : 변경 가능한 자료형
#
# set 생성
s = set()
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( [ 1, 2, 3, 1, 2, 3 ] )
print( "s : {}( {} )".format( s, len( s ) ) )
s = { 1, 2, 3, 1, 2, 3 }
print( "s : {}( {} )\n".format( s, len( s ) ) )

s = set( ( 1, 2, 3, 1, 2, 3 ) ) # tuple 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( 'hello' )              # str 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( [ 1, 2, 3 ] )          # list 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( { 'one':1, 'two': 2 } )# dict 이용 set 생성
print( "s : {}( {} )\n".format( s, len( s ) ) )

l1 = [ 1, 2, 3 ]
l2 = [ 3, 4, 5 ]
#s = { l1, l2 }  # set의 원소에는 변경 불가능한 자료형만 가능
print( "s : {}( {} )".format( s, len( s ) ) )

# set 함수( 연산, 메서드 )
s = { 1, 2, 3, 1, 2, 3 }
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.add( 1 )      # 원소 추가
print( "s : {}( {} )".format( s, len( s ) ) )
s.add( 5 )
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.remove( 1 )   # 원소 삭제
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.update( [ 1, 4, 5, 6, 7 ] ) # 해당 set에 대한 합집합
print( "s : {}( {} )".format( s, len( s ) ) )

s.discard( 3 ) # 해당 원소 제거, 해당 원소가 없으면 무시
print( "s : {}( {} )".format( s, len( s ) ) )
s.discard( 3 )
print( "s : {}( {} )".format( s, len( s ) ) )
#s.remove( 3 ) # 해당 원소 제거, 해당 원소가 없으면 예외( exception ) 발생
#print( "s : {}( {} )\n".format( s, len( s ) ) )

s.clear()
print( "s : {}( {} )\n".format( s, len( s ) ) )

# set 집합 연산
s1 = { 1, 2, 3, 4, 5 }
s2 = { 3, 4, 5, 6, 7 }

print( "합집합" )
print( s1.union( s2 ) )
print( s1 | s2, '\n' )

print( "교집합" )
print( s1.intersection( s2 ) )
print( s1 & s2, '\n' )

print( "차집합" )
print( s1.difference( s2 ) )
print( s1 - s2, '\n' )




