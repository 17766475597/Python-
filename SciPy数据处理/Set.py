#集合不允许有重复元素
aSet = set('sunrise')
bSet = set('sunset')
print(aSet&bSet)
print(aSet|bSet)
print(aSet^bSet)
aSet-=set('sun')
print(aSet)

aSet.add('!')
print(aSet)
aSet.remove('!')
print(aSet)
aSet.update('Yeah')
print(aSet)
aSet.clear()
print(aSet)