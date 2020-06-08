# 표준 입/출력
result = None

number1 = int( input( "Input number1 : " ) )
number2 = int( input( "Input number2 : " ) )

result = number1 + number2

print( number1, '\t', number2, '\t', result )
# % [전체자릿수] d : ( Decimal number ) -> 출력 형식
# python 2에서 사용하는 방식
print( '%5d + %5d = %10d' % ( number1, number2, result ) )

# python 3에서 사용하는 방식
print( '{0:5} + {1:5} = {2:10}'.format( number1,
                                        number2,
                                        result ) )