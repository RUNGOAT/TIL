# format()

> 포매팅 이란

문자열을 이쁘게 만드는 방법

* '{index 0}, {index 1}.format(값0, 값1)'

  ```py
  # 값0, 값1
  ```

  

> 문자열 정렬하기

```py
# 왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')print(s9)

# 오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')print(s10)

# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')print(s11)
```

* 결과값

```py
this is left      | done a    |
this is      right| done    b |
this is   center  | done   c  |
```

<br>

> 문자열에 공백이 아닌 값 채우기

```py
# 왼쪽 정렬
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a')print(s12) 

# 오른쪽 정렬
s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b')print(s13) 

# 가운데 정렬
s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')print(s14)
```

* 결과값

```py
this is left------| done aoooo|
this is +++++right| done 0000b|
this is ..center..| done @@c@@|
```

<br>

> 자리수와 소수점 표현하기

```py
# 정수 N자리
s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(s15)

# 소수점 N자리
s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
print(s16)
```

* 결과값

```py
정수 3자리 : 12345, 012
아래 2자리 : 123.12, 아래 5자리 : 3.14000
```

s15 : 정수의 자리수를 표현할 때는 '0**N**d'로 표현합니다. **N**은 원하는 자릿수를 입력하면 됩니다.

자릿수가 부족한 경우는 자동으로 0으로 채워집니다.

s16 : 소수점 자리수를 표현할 때는 '0.Nf'로 표현합니다. N은 소수점 아래 표시할 자릿수를 입력하면 됩니다.

이것도 마찬가지로 남는 부분은 0으로 표시됩니다.