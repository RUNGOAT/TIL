# strip(), rstrip(), lstrip() - 문자 제거

* strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거한다.

* lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거
* rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거

* 인자를 전달하지 않으면 String에서 공백을 제거

<br>

## 공백(white space) 제거

다음 코드는 `strip()`에 인자를 전달하지 않습니다. 인자를 전달하지 않으면 문자열에서 공백을 제거합니다.

```python
text = ' Water boils at 100 degrees '
print('[' + text.rstrip() + ']')
print('[' + text.lstrip() + ']')
print('[' + text.strip() + ']')
```

결과

```log
[ Water boils at 100 degrees]
[Water boils at 100 degrees ]
[Water boils at 100 degrees]
```

<br>

## 동일한 문자 제거

인자로 문자 1개를 전달하면 그 문자와 동일한 것을 모두 제거합니다. 동일하지 않은 문자가 나올 때까지 제거합니다.

```python
text = '0000000Water boils at 100 degrees 000'
print(text.lstrip('0'))
print(text.rstrip('0'))
print(text.strip('0'))
```

결과

```log
Water boils at 100 degrees 000
0000000Water boils at 100 degrees
Water boils at 100 degrees
```

<br>

## 여러 문자 제거

인자로 여러 문자를 전달하면 그 문자들과 동일한 것들을 모두 제거합니다. 동일하지 않은 문자가 나올 때까지 제거합니다.

```python
text = ",,,,,123.....water....pp"
print(text.lstrip(',123.p'))
print(text.rstrip(',123.p'))
print(text.strip(',123.p'))
```

결과

```log
water....pp
,,,,,123.....water
water
```

다음 예제도 위와 동일하게 여러 문자를 인자로 전달하였습니다.

```python
text = ' Water boils at 100 degrees '
print(text.lstrip(' Water'))
print(text.rstrip(' degrees '))
print(text.strip(' degrees '))
```
결과
```py
boils at 100 degrees
 Water boils at 100
Water boils at 100
```