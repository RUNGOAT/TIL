get() 활용

0725 workshop

```python
def count_blood(blood_type_list):
    blood_type_dict = {}

    for type in blood_type_list:
        # blood_type_dict.update({type: blood_type_list.count(type)})
        
        # if blood_type_dict.get(blood):
        #     blood_type_dict[type] += 1
        # else:
        #     blood_type_dict[type] = 1
        
        blood_type_dict[type] = blood_type_dict.get(type, 0) + 1

    return blood_type_dict
    

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]))
```

