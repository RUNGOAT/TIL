# Dictionary 추가

## 1. +=

```py
detail = {'age': []}
detail['age'] += [20]
detail['age'] += ['twenty']
print(detail)

# {'age': [20, 'twenty']}
```

<br>

## 2. append()

```py
if 'age' in detail:
	detail['age'].append('30')
	print(detail)
	
# {'age': [20, 'twenty', '30']}
```

<br>

## 3. update()

```py
detail = {}
detail['age'] = []
detail.update({'age': [1, 2, 3]})
print(detail)

# {'age': [1, 2, 3]}
```

<br>

## 4. dict()

```py
lst = [4, 5, 6]
detail = dict({'age': lst})
print(detail)

# {'age': [4, 5, 6]}
```



