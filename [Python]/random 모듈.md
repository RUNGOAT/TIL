# random 모듈

<br>

## random()

* 0부터 1 사이의 랜덤 실수를 리턴합니다.

```py
random.random()			# Random float x, 0.0 <= x < 1.0
0.37444887175646646
```

<br>

## uniform()

* 2개의 숫자 사이의 랜덤 실수를 리턴합니다.

```py
random.uniform(1, 10)		# Random float x, 1.0 <= x < 10.0
1.~~~~~~~~
```

<br>

## randint()

* 2개의 숫자 사이의 랜덤 정수를 리턴합니다. (2번째 인자로 넘어온 정수도 범위에 포함시킴)

```py
random.randint(1, 10)		# Integer from 1 to 10, endpoints included
7
```

<br>

## randrange()

* <u>range</u>(start, stop, step) 함수로 만들어지는 정수 중에 하나를 랜덤하게 리턴합니다.

```py
random.randrange(0, 101, 2)		# Even integer from 0 to 100
26
```

<br>

## choice()

* 랜덤하게 하나의 원소를 선택합니다.

```py
random.choice('abcdefghij')		# Choose a random element
'c'
```

<br>

## sample()

* 랜덤하게 여러 개의 원소를 선택합니다.

```py
random.sample([1, 2, 3, 4, 5], 3)		# Choose 3 element
[4, 1, 5]
```

<br>

## shuffle()

* 원소의 순서를 랜덤하게 바꿉니다.

```py
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
items
[7, 3, 2, 5, 6, 4, 1]
```

