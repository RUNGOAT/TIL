# stack 활용

0726 workshop

3. 솔로 천국 만들기

```python
def lonely(lst):
    
    stack = [lst[0]]
    for i in range(1, len(lst)):
        if stack[-1] != lst[i]:
            stack.append(lst[i])
    return stack

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))

    # lone = set()
    # lst2 = []
    # for i in range(len(lst)-1):
    #     if lst[i] != lst[i+1]:
    #         if lst[0] != lst[1]:
    #             lone.add(lst[0])            # 첫 번째 값이 연속되지 않으면 바로 lone에 추가
    #         lst2.append(list(lone)[0])      # set타입의 lone에 저장된 값 하나를 lst2에 대입
    #         lone = set()                    # 대입하고 초기화
    #         lone.add(lst[i+1])              # 초기화 후 다음 숫자 대입
    #         if i+1 == len(lst)-1:           # 연속되지 않은 다음 숫자가 마지막이라면
    #             lst2.append(lst[i+1])       # 바로 lst2에 대입
    #     else:
    #         lone.add(lst[i])
    #         if i == len(lst) - 2:           # 연속되는 숫자가 마지막이라면
    #             lst2.append(list(lone)[0])  # 바로 lst2에 대입
    # return lst2

```



