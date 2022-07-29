# enumerate() 활용

0726 workshop

2. 소대소대

```python
def low_and_up(s):
    alpha_list = []

    for idx, word in enumerate(s):
        if idx % 2:
            alpha_list.append(word.upper())
        else:
            alpha_list.append(word.lower())

    # for i in range(len(s)):
    #     if i % 2:
    #         alpha_list.append(s[i].upper())
    #     else:
    #         alpha_list.append(s[i].lower())

    return ''.join(alpha_list)


print(low_and_up('apple'))
print(low_and_up('banana'))
```

