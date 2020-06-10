import math

l = [ i for i in range( 2, 101, 2 ) ]
l2 = [ i for i in range( 101 ) if i % 2 == 0 ]
print( len( l ), len( l2 ) )
print( l )
print( l2 )
print( sum( l ), sum( l2 ) )
