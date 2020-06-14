#!/usr/bin/env python
# coding: utf-8

# # NumPy( Numerical Python )

# https://numpy.org/

# - 조밀한 데이터 버퍼에서 저장하고 처리하는 효과적인 인터페이스를 제공
# - NumPy 배열은 파이썬의 내장 타입인 list와 비슷하지만 배열의 규모가 커질수록 데이터 저장 및 처리에 훨씬 더 효율적이다.
# - NumPy 배열은 파이썬의 데이터 과학 도구로 구성된 전체 생태계의 핵심을 이루고 있다.

# In[5]:


import numpy as np


# In[6]:


numpy.__version__


# In[7]:


np? # NumPy 내장 문서 표시


# - 파이썬은 데이터를 효율적인 고정 타입 데이터 버퍼에 저장하는 다양한 방식을 제공
# - 내장 array 모듈은 단일 타입의 조밀한 배열( dense array )을 만드는데 사용할 수 있다.

# In[8]:


import array


# In[9]:


L = list( range( 10 ) )
A = array.array( 'i', L )
A


# - 'i'는 내용이 정수임을 가리키는 타입 코드이다.   
# - 훨씬 더 유용한 것은 NumPy 패키지의 ndarray 객체이다.
# - 파이썬의 array 객체는 배열 기반의 데이터에 효율적인 저장소를 제공하는 반면, NumPy는 그 데이터의 효율적인 연산을 추가한다.

# ## 파이썬 리스트에서 배열 만들기

# In[11]:


# np.array를 사용하여 파이썬 리스트에서 배열을 만들 수 있다.
np.array( [ 1, 4, 2, 5, 3 ] )


# - 파이썬 리스트와 달리 NumPy는 배열의 모든 요소가 같은 타입이어야 한다.
# - 타입이 일치하지 않으면 NumPy는 가능한 경우 상위 타입을 취하게 된다.

# In[12]:


np.array( [ 3.14, 4, 2,3 ] )


# - 명시적으로 결과 배령의 데이터 타입을 설정하려면 dtype 키워드를 사용하면 된다.

# In[13]:


np.array( [ 1, 2, 3, 4 ], dtype = 'float32' )


# - 파이썬 리스트와는 달리 NumPy 배열은 명시적으로 다차원이 가능하다.

# In[14]:


# 리스트를 중첩하면 다차원 배열이 됨
# 내부 리스트는 결과로 얻은 이차원 배열의 행으로 취급된다.
np.array( [ range( i, i + 3 ) for i in [ 2, 4, 6 ] ] )


# ## 처음부터 배열 만들기

# https://numpy.org/doc/stable/user/basics.creation.html

# - 규모가 큰 배열의 경우에는 NumPy에 내장된 루틴을 사용해 처음부터 배열을 생성하는 것이 더 효율적이다.

# In[15]:


# 0으로 채운 길이 10의 정수 배열
np.zeros( 10, dtype = int )


# In[16]:


# 1로 채운 3 x 5 부동 소수점 배열
np.ones( ( 3, 5 ), dtype = float )


# In[17]:


# 3.14로 채운 3 x 5 배열 만들기
np.full( ( 3, 5 ), 3.14 )


# In[18]:


# 선형 수열로 채운 배열 만들기
# 0에서 시작해 2씩 더해 20까지 채움
# ( 내장 함수인 range()와 유사함 )
np.arange( 0, 20, 2 )


# In[19]:


# 0과 1사이에 일정하 간격을 가진 다섯 개의 값으로 채운 배열 만들기
np.linspace( 0, 1, 5 )


# In[20]:


# 균등하게 분포된 3 x 3 배열 만들기
# 0과 1사이의 난수로 채움
np.random.random( ( 3, 3 ) )


# In[21]:


# 정규 분포( 평균 = 0, 표준 편차 = 1 )의 난수로 채운 3 x 3 배열 만들기
np.random.normal( 0, 1, ( 3, 3 ) )


# In[22]:


# [ 0, 10 ] 구간의 임의의 정수를 채운 3 x 3 배열 만들기
np.random.randint( 0, 10, ( 3, 3 ) )


# In[23]:


# 3 x 3 단위 행렬 만들기
np.eye( 3 )


# In[24]:


# 세 개의 정수를 가지는 초기화되지 않은 배열 만들기
# 값은 해당 메모리 위치에 이미 존재하고 있는 값으로 채움
np.empty( 3 )


# ## NumPy 표준 데이터 타입

# https://numpy.org/doc/stable/user/basics.types.html

# - NumPy 배열은 한 가지 타입의 값을 담고 있으므로 해당 타입과 그 타입의 제약 사항을 자세히 아는 것이 중요하다.
# - NumPy는 C로 구현되어 있어 NumPy 데이터 타입은 C언어와 유사하다.

# In[25]:


# 배열을 구성할 때 데이터 타입은 문자열을 이용해 지정할 수 있다.
np.zeros( 10, dtype = 'int16' )


# In[26]:


# 해당 데이터 타입과 관련된 NumPy 객체를 사용해 지정한다.
np.zeros( 10, dtype = np.int16 )


# ## NumPy 배열 기초

# - 파이썬에서 데이터 처리는 NumPy 배열 처리와 거의 비슷하다.
# - Pandas도 NumPy 배열을 기반으로 만들어 졌다.

# ### 기본 배열 조작
#    
#    - 배열 속성 지정
#        - 배열의 크기, 모양, 메모리 소비량, 데이터 타입을 결정한다.
#        
#       
#    - 배열 인덱싱
#        - 개별 배열 요소값을 가져오고 설정한다.
#        
#       
#    - 배열 슬라이싱
#        - 큰 배열 내에 있는 작은 하위 배열을 가져오고 설정한다.
#        
#       
#    - 배열 재구조화
#        - 해당 배열의 형상을 변경한다.
#        
#           
#    - 배열 결합 및 분활
#        - 여러 배열을 하나로 결합하고 하나의 배열을 여러 개로 분할한다.

# ### 배열 속성 지정 : 배열의 크기, 모양, 메모리 소비량, 데이터 타입을 결정한다.

# In[27]:


np.random.seed( 0 ) # 재현 가능성을 위한 시드 값


# In[29]:


x1 = np.random.randint( 10, size = 6 ) # 1차원 배열
x2 = np.random.randint( 10, size = ( 3, 4 ) ) # 2차원 배열
x3 = np.random.randint( 10, size = ( 3, 4, 5 ) ) # 3차원 배열


# In[30]:


x1


# In[31]:


x2


# In[32]:


x3


# - 각 배열은 속성으로 ndim( 차원의 개수 ), shape( 각 차원의 크기 ), size( 전체 배열의 크기 )를 가지고 있다.

# In[33]:


print( 'x3 ndim: ', x3.ndim ) # 차원의 개수
print( 'x3 shape: ', x3.shape ) # 차원의 크기
print( 'x3 size: ', x3.size ) # 전체 배열의 크기


# In[34]:


print( 'dtype : ', x3.dtype ) # 배열의 데이터 타입


# - itemsize : 각 배열의요소의 크기를 바이트 단위로 보여줌
# - nbytes : 배열 전체 크기를 바이트 단위로 보여준다. itemsize를 size로 곱한 값과 같다

# In[35]:


print( 'itemsize : ', x3.itemsize, 'bytes' )
print( 'nbytes : ', x3.nbytes, 'bytes' )


# ## 배열 인덱싱 : 단일 요소에 접근하기

# https://numpy.org/doc/stable/user/basics.indexing.html

# - 1차원 배열에서 i번째( 0부터 시작 ) 값에 접근하려면 파이썬 리스트에서와 같이 꺽쇄괄호 안에 원하는 인덱스를 지정하면 된다.

# In[36]:


x1


# In[37]:


x1[ 0 ]


# In[38]:


x1[ 4 ]


# - 배열의 끝에서부터 인덱싱하려면 음수 인덱스를 사용하면 된다.

# In[39]:


x1[ -1 ]


# In[40]:


x1[ -2 ]


# - 다차원 배열에서는 콤마로 구분된 인데스 튜플을 이용해 배열 항목에 접근할 수 있다.

# In[41]:


x2


# In[42]:


x2[ 0, 0 ]


# In[43]:


x2[ 2, 0 ]


# In[44]:


x2[ 2, -1 ]


# - 인덱스 표기법을 사용해 값을 수정할 수도 있다.

# In[45]:


x2[ 0, 0 ] = 12
x2


# - 파이썬 리스트와 달리 NumPy 배열은 고정 타입을 가진다는 점을 명심
# - 가령 정수 배열에 부동 소수점 값을 삽입하면 그 값으 소수점 이하를 잘라버린다.

# In[47]:


x1[ 0 ] = 3.14159 # 이 값의 소수점 이하는 잘릴 것이다
x1


# ## 배열 슬라이싱 : 하위 배열에 접근하기

# - 꺽쇠괄호를 사용해 개별 배열 요소에 접근할 수 있는 것처럼 : 기호로 표시되는 슬라이스( slice ) 표기법으로 하위 배열에 접근할 수 있다.
# - NumPy 슬라이싱 구문은 표준 파이썬 리스트의 구문을 따른다
# - 배열 x 의 슬라이스에 접근하려면 다음 구문을 사용하면 된다.   
# 
# x[ start : stop : step ]   
# 
# - 이 가운데 하나라도 지정되지 않으면 기본으로 start = 0, stop = 차원 크기, step = 1로 값이 설정된다.

# ### 1차원 하위 배열

# In[48]:


x = np.arange( 10 )
x


# In[49]:


x[ :5 ] # 첫 다섯 개 요소


# In[50]:


x[ 5: ] # 인덱스 5 다음 요소들


# In[51]:


x[ 4:7 ] # 중간 하위 배열


# In[52]:


x[ ::2 ] # 하나 걸러 하나씩의 요소로 구성된 배열


# In[53]:


x[ 1::2 ] # 인덱스 1에서 시작해 하나 걸러 하나씩 요소로 구성된 배열


# - 혼동을 줄 수 있는 경우는 step값이 음수일 때다. 이 경우에는 start와 stop의 기본값이 서로 바뀐다.
# - 이는 배열을 꺼꾸로 만드는 편리한 방법이 될 수 있다.

# In[54]:


x[ ::-1 ] # 모든 요소를 꺼꾸로 나열


# In[55]:


x[ 5::-2 ] # 인덱스 5부터 하나 걸러 하나씩 요소를 거꾸로 나열


# ### 다차원 하위 배열

# - 다차원 슬라이싱도 콤마로 구분된 다중 슬라이스를 사용해 똑같은 방식으로 동작한다.

# In[57]:


x2


# In[58]:


x2[ :2, :3 ] # 두 개의 행, 세 개의 열


# In[59]:


x2[ :3, ::2 ] # 모든 행, 한 열 걸러 하나씩


# - 하위 배열 차원도 함께 역으로 변환할 수 있다.

# In[60]:


x2[ ::-1, ::-1 ]


# #### 배열의 행과 열에 접근하기   
# 
# - 한 가지 공통으로 필요한 루틴은 배열의 단일 행이나 열에 접근하는 것이다.
# - 이것은 단일 콜론으로 표시된 빈 슬라이스를 사용해 인덱싱과 슬라이싱을 결합함으로써 할 수 있다.

# In[61]:


print( x2[ :, 0 ] ) # x2의 첫 번째 열


# In[62]:


print( x2[ 0, : ] ) # x2의 첫 번째 열


# - 행에 접근하는 경우 더 간결한 구문을 위해 빈 슬라이스를 생략할 수 있다.

# In[63]:


print( x2[ 0 ] ) # x2[ 0, : ] 와 동일


# #### 사본이 아닌 뷰로서의 하위 배열
# 
# - 배열 슬라이스에 대해 알아야 할 중요하고 매우 유용한 사실 하나는 배열 슬라이스가 배열 데이터의 사본( copy )가 이니라 뷰( view )를 반환한다는 점이다.
# 
# - 이는 NumPy 배열 슬라이싱이 파이썬 리스트 슬라이싱과 다른 점 주 하나다.
# - 리스트에서 슬라이스는 사본이다.

# In[64]:


print( x2 )


# In[65]:


x2_sub = x2[ :2, :2 ] # 2 x 2 하위 배열 추출
print( x2_sub )


# In[66]:


x2_sub[ 0, 0 ] = 99 # 이 하위 배열을 수정하면 원래 배녈이 변경된다.
print( x2_sub )


# In[67]:


print( x2 )


# - 이 기본 행위는 실제로 매우 유용하다.
# - 이것은 큰 데이터세트를 다룰 때 기반 데이터 버퍼를 복사하지 않아도 이 데이터의 일부에 접근하고 처리할 수 있다는 뜻이다.

# #### 배열의 사본 만들기
# 
# - 배열 뷰의 훌륭한 기능에도 불구하고 때로는 배열이나 하위 배열 내의 데이터를 명시적으로 복사하는 것이 더 유용할 때가 있다.
# - 그 작업은 copy() 메서드로 가장 쉽게 할 수 있다.

# In[68]:


x2_sub_copy = x2[ :2, :2 ].copy()
print( x2_sub_copy )


# In[69]:


x2_sub_copy[ 0, 0 ] = 42 # 하위 배열을 수정해도 원래 배열이 그대로 유지된다.
print( x2_sub_copy )


# In[70]:


print( x2 )


# ### 배열 재구조화

# - 다른 유용한 조작 유형은 배열의 형상을 변경하는 것이다.
# - 이를 가장 유연하게 하는 방법은 reshape() 메서드를 사용하는 것이다.

# In[71]:


grid = np.arange( 1, 10 ).reshape( ( 3, 3 ) ) # 3 x 3 그리드에 1 ~ 9까지 넣는 방법
print( grid )


# - 이 코드가 동작하려면 초기 배열의 규모가 형상이 변경된 배열의 규모와 일치해야 한다.
# - 가능하다면 reshape 메서드가 초기 배열의 사본이 아닌 뷰를 사용하겠지만, 연속되지 않은 메모리 버퍼일 경우에는 그렇지 않을 수도 있다.

# - 또 다른 일반적인 재구조화 패턴은 1차원 배열을 2차원 해이나 열 매트릭스로 전환하는 것이다.
# - 이 작업은 reshape 메서드로 할 수 있으며, 그렇지 않으면 슬라이스 연산 내에 newaxis 키워드를 사용해 더 쉽게 할 수 있다.

# In[72]:


x = np.array( [ 1, 2, 3 ] )
x.reshape( ( 1, 3 ) ) # reshape를 이용한 행 벡터


# In[73]:


x[ np.newaxis, : ] # newaxis를 이용한 행 벡터


# In[74]:


x.reshape( ( 3, 1 ) ) # reshape를 이요한 열 벡터


# In[75]:


x[ :, np.newaxis ] # newaxis를 이용한 열 벡터


# ### 배열 연결 및 분활

# - 여러 배열을 하나로 결합하거나 그 반대로 하나의 배열을 여러 개의 배열로 분활하는 것도 가능하다.

# #### 배열 연결
# 
# - NumPy에서는 주로 np.concatenate, np.vstack, np.hstack 루틴을 이용해 두 배열을 결합하거나 연결한다.

# In[77]:


# np.concatenate는 튜플이나 배열의 리스트를 첫 번째 인수로 취한다.
x = np.array( [ 1, 2, 3 ] )
y = np.array( [ 3, 2, 1 ] )
np.concatenate( [ x, y ] )


# In[78]:


# 한 번에 두 개 이상의 배열을 연결할 수도 있다.
z = [ 99, 99, 99 ]
print( np.concatenate( [ x, y, z ] ) )


# In[79]:


# np.concatenate는 2차원 배열에서도 사용할 수 있다.
grid = np.array( [ [ 1, 2, 3 ],
                   [ 4, 5, 6 ] ] )
np.concatenate( [ grid, grid ] )


# In[80]:


# 두 번째 축을 따라 연결( 0부터 시작하는 인덱스 방식)
np.concatenate( [ grid, grid ], axis = 1 )


# - 혼합된 차원의 배열로 작업할 때는 np.stack( 수직 스택, vertical stack )과 np.hstack( 수평 스택, horizontal stack ) 함수를 사용하는 것이 더 명확하다.

# In[81]:


x = np.array( [ 1, 2, 3 ] )
grid = np.array( [ [ 9, 8, 7 ],
                   [ 6, 5, 4 ] ] )
np.vstack( [ x, grid ] ) # 배열을 수직으로 쌓음


# In[82]:


y = np.array( [ [ 99 ],
                [ 99 ] ] )
np.hstack( [ grid, y ] ) # 배열을 수평으로 쌓음


# #### 배열 분활하기

# - 결합의 반대는 분활로 np.split, np.hsplit, np.vsplit 함수로 구현된다.
# - 각 함수에 분할 지점을 알려주는 인덱스 목록을 전달할 수 있다.

# In[83]:


x = [ 1, 2, 3, 99, 99, 3, 2, 1 ]
x1, x2, x3 = np.split( x, [ 3, 5 ] ) # 3, 5번째 인덱스를 분활 지점으로 한다.
print( x1, x2, x3 )


# - N개의 분할점은 N + 1 개의 하위 배열을 만든다. np.hsplit과 np.vsplit은 서로 비슷하다.

# In[84]:


grid = np.arange( 16 ).reshape( ( 4, 4 ) )
grid


# In[86]:


upper, lower = np.vsplit( grid, [ 2 ] )
print( upper )
print( lower )


# In[87]:


left, right = np.hsplit( grid, [ 2 ] )
print( left )
print( right )


# - np.dsplit은 세 번째 축을 따라 배열을 분할할 것이다. 

# ## NumPy 배열 연산 : 유니버설 함수( universal functions, ufuncs )
# 
# https://numpy.org/doc/stable/reference/ufuncs.html
# 
# 
# - NumPy는 데이터 배열을 사용하여 최적화된 연산을 위한 쉽고 유연한 인터페이스를 제공한다.
# - NumPy 배열의 연산은 아주 빠르거나 아주 느릴 수 있다.
# - 이 연산을 빠르게 만드는 핵심은 벡터화( vectorized ) 연산을 사용하는 것인데
# - 일반적으로 NumPy의 유니버설 함수( universal functions, ufuncs )를 통해 구현된다.
# - 배열 요소에 대한 반복적인 계산을 더 효율적으로 수행하게 해준다.
# 
# 
# - 벡터화 연산은 간단히 배열에 연산을 수행해 각 요소에 적용함으로써 수행할 수 있다.
# - 벡터화 방식은 루프를 NumPy의 기저를 이루는 컴파일된 계층으로 밀어 넣음으로써 훨씬 빠르게 실행되도록 설계되었다.
# 
# 
# - NumPy에서 벡터화 연산은 NumPy 배열의 값에 반복된 연산을 빠르게 수행하는 것을 주목적으로 하는 ufuncs를 통해 구현된다.
# - 유니버설 함수는 매우 유연해서 스칼라와 배열 사이의 연산및 두 배열 간의 연산도 가능하다.
# 
# 
# - ufuncs를 통한 벡터화를 이용한 연산은 파이썬 루프를 통해 구현된 연산보다 대부분 더 효율적이며, 특히 배열의 크기가 커질수록 그 차이가 확연하다.
# - 파이썬 스크립트에서 그러한 루프를 보면 항상 베터화 표현식으로 교체할 수 있을지 고민해야 한다.

# In[89]:


np.random.seed( 0 )

def compute_reciprocals( values ):
    output = np.empty( len( values ) )
    for i in range( len( values ) ):
        output[ i ] = 1.0 / values[ i ]
    return output

values = np.random.randint( 1, 10, size = 5 )
compute_reciprocals( values )


# In[90]:


big_array = np.random.randint( 1, 100, size = 1000000 )
get_ipython().run_line_magic('timeit', 'compute_reciprocals( big_array )')


# In[92]:


print( compute_reciprocals( values ) )
print( 1.0 / values )


# In[93]:


get_ipython().run_line_magic('timeit', '( 1.0 / values )')


# In[94]:


np.arange( 5 ) / np.arange( 1, 6 )


# In[96]:


x = np.arange( 9 ).reshape( ( 3, 3 ) )
2 ** x


# ### NumPy 유니버설 함수( UFuncs )
# 
# - 단일 입력값에 동작하는 단항 ufuncs와 두 개의 입력값에 동작하는 이항 ufuncs로 두 종류가 있다.

# #### 배열 산술 연산
# 
# - NumPy ufuncs는 파이썬의 기본 산술 연산자를 사용하기 때문에 표준 파이썬의 산술 연산자를 모두 사용할 수 있다.

# In[98]:


x = np.arange( 4 )
print( 'x      = ', x )
print( 'x + 5  = ', x + 5 )
print( 'x - 5  = ', x - 5 )
print( 'x * 2  = ', x * 2 )
print( 'x / 2  = ', x / 2 )
print( 'x // 2 = ', x // 2 )
print( '-x     = ', -x )
print( 'x ** 2 = ', x ** 2 )
print( 'x % 2  = ', x / 2 )


# In[99]:


-( 0.5 * x + 1 ) ** 2


# In[100]:


np.add( x, 2 ) # + 연산자는 add 함수의 래퍼( wrapper ) 함수다.


# #### 절대값 함수

# In[101]:


x = np.array( [ -2, -1, 0, 1, 2 ] )
abs( x )


# - 절대값 함수에 대응하는 NumPy ufunc는 np.absolute로, np.abs로 별칭으로도 사용할 수 있다.

# In[102]:


np.absolute( x )


# In[103]:


np.abs( x )


# In[104]:


# ufunc는 복소수 데이터도 처리할 수 있으며, 이 경우 절대값은 크기로 반환한다.
x = np.array( [ 3 -4j, 4 - 3j, 2 + 0j, 0 + 1j ] )
np.abs( x )


# #### 삼각함수

# In[105]:


theta = np.linspace( 0, np.pi, 3 )


# In[106]:


# 기계 정밀도 내에서 계산되면, 그래서 0이어야 하는 값이 언제나 0이 되지는 않는다.
print( 'theta        = ', theta )
print( 'sin( theta ) = ', np.sin( theta ) )
print( 'cos( theta ) = ', np.cos( theta ) )
print( 'tan( theta ) = ', np.tan( theta ) )


# In[107]:


# 역삼각 함수
x = [ -1, 0, 1 ]
print( 'x           = ', x )
print( 'arcsin( x ) = ', np.arcsin( x ) )
print( 'arccos( x ) = ', np.arccos( x ) )
print( 'arctan( x ) = ', np.arctan( x ) )


# #### 지수와 로그

# In[109]:


x = [ 1, 2, 3 ]
print( 'x   = ', x )
print( 'e^x = ', np.exp( x ) )
print( '2^x = ', np.exp2( x ) )
print( '3^x = ', np.power( 3, x ) )


# - 지수의 역인 로그도 사용할 수 있다. 기본 np.log는 자연로그를 제공한다. 2를 밑으로 하는 로그를 계산하거나 10을 밑으로 하는 로그를 계산하는 것 역시 가능하다.

# In[110]:


x = [ 1, 2, 4, 10 ]
print( 'x          = ', x )
print( 'ln( x )    = ', np.log( x ) )
print( 'log2( x )  = ', np.log2( x ) )
print( 'log10( x ) = ', np.log10( x ) )


# In[111]:


# 매우 작은 입력값의 정확도를 유지하고자 할 때 유용한 특화된 버전도 있다.
# 이 함수들은 x가 매우 작을 때 np.log나 np.exp를 사용했을 때보다 더 정확한 값을 내놓는다.
x = [ 0, 0.001, 0.01, 0.1 ]
print( 'exp( x ) - 1 = ', np.expm1( x ) )
print( 'log( 1 + x ) = ', np.log1p( x ) )


# #### 집계

# In[112]:


# 배열을 특정 연산으로 축소하고자 할 때 사용하는 reduce 메서드 사용
# reduce 메서드는 결과가 하나만 남을 때까지 해당 연산을 배열 요소에 반복해서 적용한다.
# add ufunc의 reduce를 호출하면 배열의 모든 요소의 합을 반환한다.
x = np.arange( 1, 6 )
np.add.reduce( x )


# In[113]:


# multiply ufunc에 reduce를 호출하면 모든 배열 요소의 곱을 반환한다.
np.multiply.reduce( x )


# In[114]:


# 계산의 중간 결과를 모두 저장하고 싶다면 대신 accumulate를 사용하면 된다.
np.add.accumulate( x )


# In[115]:


np.multiply.accumulate( x )


# - 배열의 값의 합 구하기

# In[116]:


L = np.random.random( 100 )
sum( L ) # 파이썬 내장 함수


# In[117]:


np.sum( L ) # NumPy 함수


# In[118]:


# sum()과 np.sum()은 같은 결과는 똑같다. 그러나 이 연산이 컴파일된 코드에서 실행되기 때문에 NumPy에서의 연산이 훨씬 더 빠르다.
big_array = np.random.rand( 1000000 )
get_ipython().run_line_magic('timeit', 'sum( big_array )')
get_ipython().run_line_magic('timeit', 'np.sum( big_array )')


# - 최소값과 최대값

# In[119]:


# 파이썬 내장 함수
min( big_array ), max( big_array )


# In[120]:


# NumPy 함수
np.min( big_array ), min( big_array )


# In[121]:


get_ipython().run_line_magic('timeit', 'min( big_array )')
get_ipython().run_line_magic('timeit', 'np.min( big_array )')


# - min, max, sum을 비롯한 다른 여러 NumPy 집계 함수의 경우, 배열 객체 자체의 메서드를 사용하는 더 짧은 구문이 존재한다.

# In[122]:


print( big_array.min(), big_array.max(), big_array.sum() )


# - NumPy 배열을 다룰 때는 가능한 한 NumPy 버전의 집계 함수를 사용

# - 다차원 집계

# - 집계 연산의 보편적인 유형은 행이나 열을 기준으로 집계하는 것이다.

# In[123]:


M = np.random.random( ( 3, 4 ) )
print( M )


# In[124]:


M.sum()


# In[125]:


# 집계 함수는 어느 축( axis )을 따라 집계할 것인지를 지정하는 추가적인 인수를 취한다. 각 열의 최소값을 찾으려면 axis = 0을 지정
M.min( axis = 0 )


# In[126]:


M.min( axis = 1 ) # 행에 대한 최소값


# - axix 키워드는 반환할 차원이 아니라 추소할 배열의 차원을 지정한다.
# - axis = 0으로 지정하는 것은 첫 번째 축을 축소한다는 의미가 된다. 
# - 2차원 배열이라면 각 열의 값들이 집계된다는 뜻이다.

# |함수명|NaN 안전 모드|설명|
# |---|---|---|
# |np.sum|np.nansum|요소의 합 계산|
# |np.prod|np.nanprod|요소의 곱 계산|
# |np.mean|np.nanmean|요소의 평균 계산|
# |np.std|np.nanstd|표준 편차 계산|
# |np.var|np.nanvar|분산 계산|
# |np.min|np.nanmin|최소값 계산|
# |np.max|np.nanmax|최대값 계산|
# |np.argmin|np.nanargmin|최소값의 인덱스 찾기|
# |np.argmax|np.nanargmax|최대값의 인덱스 찾기|
# |np.median|np.nanmedian|요소의 중앙값 찾기|
# |np.percentile|np.nanpercentile|요소의 순위 기반 백분위 수 계산|
# |np.any|N/A|요소 중 참이 있는지 검사|
# |np.all|N/A|모든 요소가 참인지 검사|

# ### 브로드캐스팅

# - 벡터화 연산의 또 다른 방법은 NumPy의 브로드캐스텡 기능을 사용하는 것이다.
# - 브로드캐스팅은 단지 다른 크기의 배열에 이항 유니버설 함수( 덧셈, 뺄셈, 곱셈 등 )을 적용하기 위한 규칙의 집합일 뿐이다.

# - 같은 크기의 배열에서 이항 연산은 배열의 요소 단위로 수행된다는 점을 기억

# In[128]:


a = np.array( [ 0, 1, 2 ] )
b = np.array( [ 5, 5, 5 ] )
a + b


# - 브로드캐스팅을 사용하면 이러한 유형의 이항 연산을 서로 다른 크기의 배열에서 수행할 수 있다.
# - 배열에 스칼라( 0차원 배열이라 생각하면 된다. )를 쉽게 더할 수 있다.

# In[129]:


a + 5


# - 값 5를 배열 [ 5, 5, 5 ]로 확장하거나 복제하고 그 결과를 더하는 연산으로 생각하면 된다.
# - NumPy 브로드캐스팅의 이점은 이 값 복제가 실제로 발생하지 않는다는 것이다.
# - 하지만 브로드캐스킹을 이러한 방식으로 생각하면 이해하기 쉽다.

# In[130]:


M = np.ones( ( 3, 3 ) )
M


# In[131]:


M + a # 1차원 배열 a는 M의 형상에 맞추기 위해 두 번째 차원까지 확장 또는 브로드캐스팅된다.


# In[134]:


a = np.arange( 3 )
b = np.arange( 3 )[ :, np.newaxis ]
print( a )
print( b )


# #### 브로드캐스팅 규칙
# 
# 
# - 규칙 1 : 두 배열의 차원 수가 다르면 더 작은 수의 차원을 가진 배열 형상의 앞쪽( 왼쪽 )을 1로 채운다.
# - 규칙 2 : 두 배열의 형상이 어떤 차원에서도 일치하지 않는다면 해당 차원의 형상이 1인 배열이 다른 형상과 일치하도록 늘어난다.
# - 규칙 3 : 임의의 차원에서 크기가 일치하지 않고 1도 아니라면 오류가 발생한다.

# #### 브로드캐스텡 예제 1

# In[135]:


M = np.ones( ( 2, 3 ) )
a = np.arange( 3 )


# - 두 배열간의 형상
# 
# M.shape = ( 2, 3 )   
# a.shape = ( 3, )
# 
# 
# - 규칙 1에 따라 배열 a가 더 작은 차원을 가지므로 왼쪽을 1로 채운다
# 
# M.shape -> ( 2, 3 )  
# a.shape -> ( 1, 3 )
# 
# 
# - 규칙 2에 따라 첫 번째 차원이 일치하지 않으므로 이 차원이 일치하도록 늘린다.
# 
# M.shape -> ( 2, 3 )  
# a.shape -> ( 2, 3 )
# 
# - 모양이 일치하면 최종 형상이 ( 2, 3 )이 된다.

# In[137]:


M + a


# #### 브로드캐스팅 예제 2

# In[138]:


a = np.arange( 3 ).reshape( ( 3, 1 ) )
b = np.arange( 3 )


# - 두 배열간의 형상
# 
# a.shape = ( 3, 1 )   
# b.shape = ( 3, )
# 
# 
# - 규칙 1에 따라 배열 b의 형상에 1을 덧붙여야 한다.
# 
# a.shape -> ( 3, 1 )  
# b.shape -> ( 1, 3 )
# 
# 
# - 규칙 2에 따라 각 차원을 그에 대응하는 다른 배열의 크기에 일치하도록 늘린다.
# 
# a.shape -> ( 3, 3 )  
# b.shape -> ( 3, 3 )
# 
# - 모양이 일치하면 최종 형상이 ( 3, 3 )이 된다.

# In[139]:


a + b


# #### 브로드케스팅 연산 3

# In[140]:


M = np.ones( ( 3, 2 ) )
a = np.arange( 3 )


# - 두 배열간의 형상
# 
# M.shape = ( 3, 2 )   
# a.shape = ( 3, )
# 
# 
# - 규칙 1에 따라 배열 a의 첫 번째 차원을 M의 첫 번째 차원과 일치하도록 늘린다.
# 
# M.shape -> ( 3, 2 )  
# a.shape -> ( 1, 3 )
# 
# 
# - 규칙 2에 따라 a의 첫 번째 차원을 M의 첫 번째 차원과 일치하도록 늘린다.
# 
# M.shape -> ( 3, 2 )  
# a.shape -> ( 3, 3 )
# 
# - 규칙 3에서 최종 형상이 서로 일치하지 않으므로 이 두 배열은 호환되지 않는다.

# In[141]:


M + a


# In[142]:


a[ :, np.newaxis ].shape


# In[143]:


M + a[ :, np.newaxis ]


# In[ ]:




