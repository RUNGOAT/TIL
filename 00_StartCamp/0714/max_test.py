def max(a):
    max1 = 0
    for i in range(len(a)):
        if max1 < a[i]:
            max1 = a[i]  
    print(max1)

arr = [1, 5, 2, 7, 9]
max(arr)

# 나 -------------------------------------------
# max = 0

# for i in range(len(arr)):
#     if max > arr[i]:
#         max = max
#     else:
#         max = arr[i]

# print(max)

# 교수님-----------------------------------------
# max = 0

# for i in range(len(arr)):
#     if max < arr[i]:
#         max = arr[i]
# print(max)



# # 최대값의 index 구하기
# max_idx = 0

# for i in range(len(arr)):
#     if arr[max_idx] < arr[i]:
#         max_idx = i
# print(max_idx)
# print(arr[max_idx])