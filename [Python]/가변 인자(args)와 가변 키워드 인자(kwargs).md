# 가변 인자(*args)와 가변 키워드 인자(**kwargs)

> 가변 인자 설명에 앞서 패킹, 언패킹을 살펴봄

* 패킹
  * 여러 개의 데이터를 묶어서 변수에 할당한느 것

```py
numbers = (1, 2, 3, 4, 5)	# 패킹
print(numbers)	# (1, 2, 3, 4, 5)
```

* 언패킹
  * 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것

```py
numbers = (1, 2, 3, 4, 5)
a, b, c, d, e = numbers		# 언패킹
print(a, b, c, d, e)	# 1 2 3 4 5
```
<br>
> 패킹, 언패킹

* 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야 함

```py
numbers = (1, 2, 3, 4, 5)	# 패킹
a, b, c, d, e, f = numbers	# 언패킹
# ValueError: not enough values to unpack (expected 6, got 5)
```

* 언패킹시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

```py
numbers = (1, 2, 3, 4, 5)	# 패킹

a, b, *rest = numbers		# 1, 2를 제외한 나머지를 rest에 대입
print(a, b, rest)	# 1 2 [3, 4, 5]

a, *rest, e = numbers		# 1, 5를 제외한 나머지를 rest에 대입
print(rest)		# [2, 3, 4]
```

<br>

> Asterisk (*)와 가변 인자

* *는 시퀀스 언패킹 연산자라고도 불리며, 시퀀스를 풀어 헤치는 연산자
  * 주로 <u>**튜플**</u>이나 <u>**리스트**</u>를 언패킹하는데 사용
  * *를 활용하여 가변 인자를 만들 수 있음

```py
def func(*args):
	print(args)
	print(type(args))
	
func(1, 2, 3, 'a', 'b')
'''
(1, 2, 3, 'a', 'b')
<class 'tuple'>
'''
```

* packing을 통해 받은 모든 숫자들의 합을 구하는 함수 만들기

```py
def sum_all(*numbers)
	result = 0
	for number in numbers:
		result += number
	return result
	
print(sum_all(1, 2, 3))		# 6
print(sum_all(1, 2, 3, 4, 5, 6)) # 21
```

<br>

> 가변 키워드 인자(**kwargs)

* 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용

* **kwargs는

  <u>**Dictionary**</u>로 묶여 처리되며, parameter에 **를 붙여 표현

```py
def family(**kwargs):
	for key, value in kwargs.items():
		print(key, ':', value)

family(father= '아부지', mother= '어무니', baby= '아기')
'''
father : 아부지
mother : 어무니
baby : 아기
```

<br>

> 가변인자(*args)와 가변 키워드 인자(**kwargs) 동시 사용 가능

```py
def print_family_name(*parents, **pets):
	print('아버지 :', parents[0])
	print('어머니 :', parents[1])
	if pets:
		print('반려동물들..')
		for title, name in pets.items():
			print(f'{title} : {name}'')
			
print_family_name('아부지', '어무이', dog='멍멍이', cat='냥냥이')
```

