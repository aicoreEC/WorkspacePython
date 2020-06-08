#
# list
#
print( 'list' )
colors = [ 'red', 'blue', 'green' ]
print( colors, '\n' )

print( 'list 길이' )
print( len( colors ), '\n' )

print( 'list 인덱싱' )
print( colors[ 0 ] )
print( colors[ 2 ], '\n' )

print( 'list 슬라이싱' )
cities = [ '서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원' ]
print( cities[ 0:6 ] )
print( cities[ 0:5 ] )
print( cities[ 5: ], '\n' )

print( cities[ -8: ] )

# 범위를 넘는 슬라이싱
print( cities[ : ] )
print( cities[ -50:50 ], '\n' )

print( cities[ ::2 ] )
print( cities[ ::-1 ], '\n' )

print( 'list 연산' )
color1 = [ 'red', 'blue', 'green' ]
color2 = [ 'orange', 'black', 'white' ]

print( '+( 결합 ) 연산' )
print( color1 + color2 )
print( len( color1 ) )
total_color = color1 + color2
print( total_color, '\n' )

print( '*( 반복 ) 연산' )
print( color1 * 2, '\n' )

print( 'in( 포함 여부 ) 연산' )
print( 'blue' in color2, '\n' )

print( 'list 함수' )
color = [ 'red', 'blue', 'green' ]
print( color )

color.append( 'white' )
print( color, '\n' )

color.extend( [ 'black', 'purple' ] )
print( color, '\n' )

color.insert( 0, 'orange' )
print( color, '\n' )

color.remove( 'red' )
print( color, '\n' )

del color[ 0 ]
print( color, '\n' )

print( 'list 패킹과 언패킹' )
t = [ 1, 2, 3 ]
a, b, c = t
print( t, a, b, c, '\n' )

print( '2차원 list' )
korScore = [ 49, 79, 20, 100, 80 ]
mathScore = [ 43, 59, 85, 30, 90 ]
engScore = [ 49, 79, 48, 60, 100 ]
midtermScore = [ korScore, mathScore, engScore ]
print( midtermScore, '\n' )

print( midtermScore[ 0 ][ 2 ] )
