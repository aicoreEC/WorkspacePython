#
# tuple
#
print( 'tuple' )
t = ( 1, 2, 3 )
print( t, '\n' )

t = 1, 2, 3
print( t, '\n' )

t2 = ( 1, )
print( t2, '\n' )

t3 = 1,
print( t3, '\n' )

print( 'tuple 길이' )
print( len( t ), '\n' )

print( 'tuple 인덱싱' )
print( t[ 0 ] )
print( t[ -1 ], '\n' )

print( 'tuple 슬라이싱' )
print( t[ 0:2 ] )
print( t[ -1: ] )
print( t[ : ], '\n' )

print( 'tuple 연산' )
print( '+( 결합 ) 연산' )
print( t + t, '\n' )

print( '*( 반복 ) 연산' )
print( t * 2, '\n' )

print( 'in( 포함 여부 ) 연산' )
print( 2 in t )
