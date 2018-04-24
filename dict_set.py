#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#dict 相当于map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['BOb'] #取值

'bob' in d ##判断dict 是否包含key

d.keys()

##set 和java中set一样
#要创建一个set，需要提供一个list作为输入集合：

_set = set(range(5))

_set.add(22)
print(_set)
_set.remove(2)