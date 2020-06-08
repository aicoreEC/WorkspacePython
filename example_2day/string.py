#
# 문자열( string )
#
print( '문자열' )
str = "abcde"
print( str, '\n' )

print( '문자열 길이' )
print( len( str ), '\n' )

print( '문자열 인덱싱' )
print( str[ 0 ], str[ 4 ] )
print( str[ -1 ], str[ -5 ], '\n' )

print( '문자열 슬라이싱' )
str = 'TEAMLAB MOOC, AWESOME Python'
print( str )
print( str[ 0:6 ], " AND ", str[ -9: ], '\n' )

print( str[ : ] )
print( str[ -50:50 ] )
print( str[ ::2 ], " AND ", str[ ::-1 ], '\n' )

print( '문자열 연산' )
str1 = 'TEAM'
str2 = 'LAB'

print( '+( 결합 ) 연산' )
print( str1 + ' ' + str2 )
print( str1 * 2 + ' ' + str2 * 2, '\n' )

print( '*( 반복 ) 연산' )
print( str1 * 2, '\n' )

print( 'in( 포함 여부 ) 연산' )
print( 'A' in str1, '\n' )

print( '문자열 함수' )
title = 'TEAMLAB X Inflearn'
print( title.upper() )
print( title.lower(), '\n' )

print( title.title() )
print( title.capitalize(), '\n' )

print( title.count( 'a' ) )
print( title.upper().count( 'a' ) )
print( title.isdigit() )
print( title.startswith( 'a' ), '\n' )
