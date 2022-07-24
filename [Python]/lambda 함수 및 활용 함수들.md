# lambda 함수

<u>**lambda parameter : 표현식**</u>

ex)

```py
# 삼각형의 넓이를 구하는 공식 - def
def triangle_area(b, h):
	return 0.5 * b * h
print(triangle_area(5, 6))	# 15.0

# 삼각형의 넓이를 구하는 공식 - lambda
triangle_area = lambda b, h : 0.5 * b * h
print(triangle_area(5, 6))	# 15.0

```

<br>

<br>

## 1. 활용 map()

<u>**map(function, iterable)**</u>

* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고,

  그 결과를 map object로 반환

* iterable로부터 원소를 하나씩 꺼내서 function를 적용시킨 다음, 그 결과를 map object로 반환

```py
print(map(lambda x: x ** 2, range(5)))
# <map object at 0x000001E9B70F3100>

print(list(map(lambda x: x ** 2, range(5))))
# [0, 1, 4, 9, 16]
```

<br>

## 2. 활용 filter()

<u>**filter(function, iterable)**</u>

* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고,

  그 결과가 True인 것들을 filter object로 반환

```py
print(list(filter(lambda x: x < 5, range(10))))
# [0, 1, 2, 3, 4]
```

<br>

## 3.  활용 zip()

<u>**zip(*iterables)**</u>

* 복수의 iterable을 모아 **튜플**을 원소로하는 zip object를 반환

```py
girls = ['1', '2']
boys = ['11', '22']
pair = zip(girls, boys)

print(list(pair))
# [('1', '11'), ('2', '22')]
```

<br>

## 4. 활용 reduce()

<u>**reduce(함수, 시퀀스)**</u>

* 시퀀스(문자열, 리스트, 튜플, 레인지)의 원소들을 누적적으로 함수에 적용시킨다.

```py
from functools import reduce
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
# 10
# 위 예제는 0과 1을 더하고, 거기에 2를 더하고, 거기에 3을 더하고.....한 마디로 전부 다 더한다

reduce(lambda x, y: y + x, 'abcde')
# 'edcba'
```

