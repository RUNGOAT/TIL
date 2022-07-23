# [python] 정렬 함수 sort, sorted_key= lambda, function/ reverse



### **3. Parameter**

sort, sorted 모두 key, reverse 매개변수를 갖고 있다.

 

**3-1. reverse**

bool값을 넣는다. 기본값은 reverse=False(오름차순)이다.

reverse=True를 매개변수로 입력하면 내림차순으로 정렬할 수 있다.

```
>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort(reverse=True)
>>> print(num_list)
[79, 22, 15, 10, 8]

>>> print(sorted(['좋은하루','good_morning','굿모닝','niceday'], reverse=True))
['좋은하루', '굿모닝', 'niceday', 'good_morning']
```

 

**3-2. key**

정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.

key 값을 기준으로 정렬되고 기본값은 오름차순이다. 

```
>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
```

 

여러 개의 요소를 가진 경우, 튜플로 사용할 수 있다.

```
>>> tuple_list = [('좋은하루', 0),
    	          ('niceday', 1), 
    	          ('좋은하루', 5), 
    	          ('good_morning', 3), 
    	          ('niceday',5)]
                  
>>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
>>> print(tuple_list)
[('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]
```

 <br>

[출처](https://ooyoung.tistory.com/59)

