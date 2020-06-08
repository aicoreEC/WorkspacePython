#
# set
#
print( 'set' )
s = set( [ 1, 2, 3, 1, 2, 3 ] )
print( s, '\n' )

print( 'set 연산' )
s.add( 1 )
print( s )

s.remove( 1 )
print( s )

s.update( [ 1, 4, 5, 6, 7 ] )
print( s )

s.discard( 3 )
print( s )

s.clear()
print( s, '\n' )

print( 'set 집합 연산' )
s1 = set( [ 1, 2, 3, 4, 5 ] )
s2 = set( [ 3, 4, 5, 6, 7 ] )

print( '합집합' )
print( s1.union( s2 ) )
print( s1 | s2, '\n' )

print( '교집합' )
print( s1.intersection( s2 ) )
print( s1 & s2, '\n' )

print( '차집합' )
print( s1.difference( s2 ) )
print( s1 - s2 )
