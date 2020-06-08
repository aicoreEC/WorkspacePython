#
# dict
#
print( 'dict' )
student_info = { 20140012:'Hong', 20140059:'kim', 20140058:'Lee' }
print( student_info, '\n' )

print( 'dict 길이' )
print( len( student_info ), '\n' )

print( 'dict 인덱싱' )
print( student_info[ 20140012 ], '\n' )

print( 'dict 내용 추가' )
student_info[ 20140012 ] = 'Park'
print( student_info )
print( student_info[ 20140012 ] )

student_info[ 20140039 ] = 'Nam'
print( student_info )
print( student_info[ 20140039 ], '\n' )

print( 'dict 함수' )
country_code = {}
print( country_code )

country_code = { 'America':1, 'Korea':82, 'China':86, 'Japan':81 }
print( country_code )
print( country_code.keys() )

country_code[ 'German' ] = 49
print( country_code )
print( country_code.values() )

print( country_code.items() )