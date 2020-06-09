#
# 문자열( string )
#   : 문자 집합
#   : sequence 자료형( 순서가 존재 한다. )
#   : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#   : 공통 연산을 적용할 수 있다.
# 문자열 생성
str = ''            #  빈 문자열 생성
str2 = 'hello'
print( 'type( str ) : ', type( str ), end = '' )
print( '\ttype( str2 ) : ', type( str2 ) )
print( 'str : {}\tstr2 : {}\n'.format( str, str2 ) )

str = 'Don\'t walk. "Run"'
print( str )

str = 'This is a rather long string \
containing back slash and new line.\nGood!'
print( str )

str = '''
Python is great!\nYes, it is.
'''
print( str, '\n' )

str = 'This is a rather long string ' + \
      'containing back slash and new line.\nGood!'
print( str, '\n' )

# 문자열 길이 계산
str = "Python is grate!!!"
print( "str : {}\tlength : {}\n".format( str, len( str ) ) )

# 문자열 내용 포함 확인
print( "P" in str )
print( 'p' in str )
print( 'Python' in str )
print( 'is' in str )
print( 'th' in str, '\n' )

# 문자열 인덱싱 : 파이썬에서 인덱싱 시작은 [ 0 ]부터 마지막은 [ 길이 - 1 ]
#   : 문자열의 원하는 문자에 접근하는 방법
print( str[ 0 ] )
print( str[ 7 ] )
print( str[ -1 ] )
print( str[ -8 ], '\n' )

# 문자열 슬라이싱 : 문자열에 대하여 부분 문자를 지정할 때 사용
print( str[ 0:6 ] )
print( str[ 8:10 ] )
print( str[ 7:12:3 ] )
print( str[ :6 ] )
print( str[ 11: ] )
print( str[ ::2 ] )
print( str[ ::-1 ] )
print( str[ : ] )
print( str[ -50:50], '\n' )

# 문자열은 변경 불가 자료형
#str[ 0 ] = 'p'
print( str, '\n' )

# 문자열 결합( + )
s1 = 'first'
s2 = 'second'
s3 = s1 + ' ' + s2
print( "s1 : [ {} ] s2 : [ {} ] s3 : [ {} ]\n".format( s1, s2, s3 ) )

# 문자열 반복( * )
print( s1 * 3, '\n' )

s = 'spam and egg'
print( s )
s = s[ :5 ] + ' cheese ' + s[ 5: ]
print( s )

# 문자열 함수
str = 'i like programming. i like swimming'
print( '\n' + str.upper() )
print( str.lower() )
print( str.capitalize() )
print( str.title() )
print( str.count( 'like' ) )
print( str.find( 'like' ) )
print( str.rfind( 'like' ) )

str = ' spam and egg '
print( str.strip() )
print( str.rstrip() )
print( str.split() )
print( str.split( 'and' ), '\n' )

l = str.split()
print( ':'.join( l ) )
print( '\n'.join( l ), '\n' )
print( str.center( 60 ) )
print( str.ljust( 60 ) )
print( str.rjust( 60 ) )
print( str.center( 60, '-' ) )

print( ord( 'A' ) )
print( chr( 0x0041 ) )




