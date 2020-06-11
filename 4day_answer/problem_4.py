#
# 4) 3명 학생의 이름, 과목1 점수, 과목2 점수, 과목3 점수를 입력받아 dict에 이름을 key로
#    저장하고 출력 결과와 같이 성적 일람표를 출력하고 ‘end’가 입력될 때 까지 이름으로
#    검색하여 결과를 출력하는 파이썬 스크립트
#
#    - 90점이상은 excellent, 60점미만은 fail, 나머지는 공백
#    - 평균을 이용하여 석차를 계산하여 출력
#    - 이름은 중복되지 않는다.
#
# 	[ 출력 결과 ]
# 	hong		50	50	50	150	50.00		3	fail
# 	kim		90	90	90	270	90.00		1	excellent
# 	lee		70 	70	70 	210	70.00		2
#
# 	검색할 이름 입력 : hong
# 	hong		50	50	50	150	50.00		3	fail
#
# 	검색할 이름 입력 : kim
# 	kim		90	90	90	270	90.00		1	excellent
#
# 	검색할 이름 입력 : end
#
# 	*** 스크립트 종료 ***
# symbolic constant
MAX_STUDENT = 3
MAX_SUBJECT = 3
EXCELLENT = 90.0
FAIL = 60.0

# 0. 과목수 상수와 3명 학생 저장 list 생성
students = {}

# 1. 3명 학생 정보 입력
for i in range( MAX_STUDENT ):
    student = []
    name = input( "Input student[ %2d ] - name : " % ( i + 1 ) )

    total = 0
    for i in range( MAX_SUBJECT ):
        subject = int( input( "\tInput subject[ %2d ] : " % ( i + 1 ) ) )
        student.append( subject )
        total += subject
    student.append( total )

    average = total / MAX_SUBJECT
    student.append( average )

    if average >= EXCELLENT:
        student.append( "excellent" )
    elif average < FAIL:
        student.append( "fail" )
    else:
        student.append( "" )

    students[ name ] = student
    print()

# 2. 석차 계산
for i in range( len( students ) ):
    rank = 1
    for j in range( len( students ) ):
        if students[ i ][ 5 ] < students[ j ][ 5 ]:
            rank += 1
    students[ i ].append( rank )

# 3. 결과 출력
for i in range( MAX_STUDENT ):
    print( '{:<20s}\t{:3d}\t{:3d}\t{:3d}\t{:5d}\t{:6.2f}\t{:2d}\t{:<10s}'.format( students[ i ][ 0 ],
                                                                                  students[ i ][ 1 ],
                                                                                  students[ i ][ 2 ],
                                                                                  students[ i ][ 3 ],
                                                                                  students[ i ][ 4 ],
                                                                                  students[ i ][ 5 ],
                                                                                  students[ i ][ 7 ],
                                                                                  students[ i ][ 6 ] ) )