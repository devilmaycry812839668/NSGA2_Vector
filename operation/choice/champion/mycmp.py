#!/usr/bin/env python
#encoding:UTF-8

###列表比较 算子 CMP
### 第一位元素升序， 第二位元素降序
def mycmp(a, b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    elif a[1]<b[1]:
        return 1
    elif a[1]>b[1]:
        return -1
    else:
        return 0

