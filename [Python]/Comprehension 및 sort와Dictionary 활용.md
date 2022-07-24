## List Comprehension

* [expression **for** 변수 **in** iterable]

* list(expression **for** 변수 **in** iterable)

<br>

## Dictionary comprehension

* {키 : 값 **for** 요소 **in** iterable}
* dict({키 : 값 **for** 요소 **in** iterable})



### sort 와 dictionary 활용

```py
# 반장 투표에서 {후보자 : 투표 수} 형태의 dictionary 생성
student_dict.update({student : vote})

print(sorted(student_dict.items()))
# [('강디티', 2), ('김철수', 3), ('김해킹', 2), ('박해피', 5), ('이영희', 4), ('조민지', 3), ('한케이', 2)]

print(sorted(student_dict.items(), key= lambda x : x[1], reverse = True))
# [('박해피', 5), ('이영희', 4), ('조민지', 3), ('김철수', 3), ('한케이', 2), ('강디티', 2), ('김해킹', 2)]

# value 값 기준으로 sorted한 후에 다시 dictionary 전환
student_sort = {k : v for k, v in sorted(student_dict.items(), key= lambda x : x[1], reverse=True)}
# {'박해피': 5, '이영희': 4, '조민지': 3, '김철수': 3, '한케이': 2, '강디티': 2, '김해킹': 2}
```



