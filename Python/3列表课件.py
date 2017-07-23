#访问列表元素 索引从 0 而不是 1 开始 最后一个可以用-1表示 同理倒数第二个可以用-2表示
Colour = ['red','Orange','yellow','green','blue','purple','White','black']
print(Colour)
print(Colour[0].title(),Colour[-1].title())
print("My favorite color is",'"'+Colour[4].title()+'!"')#注意引号不能和列表元素一起

moto = ['honda','yamaha','suzuki','bmw']
print(moto)
print(moto[-1].title())
#修改列表元素 例如把列表moto最后的的bmw改为ducati
moto[-1] = 'ducati'
print(moto)
print(moto[-1].title())
#在列表中添加元素 用函数.append() 将元素添加到了列表末尾
moto.append('bmw')
print(moto)
print(moto[-1].title())
#在列表中插入元素:使用方法insert()可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
moto.insert(2,'Kawasaki')
moto.insert(-1,'bmw')
print(moto)
#从列表中删除元素:
#1.使用del语句删除元素
print(moto)
del moto[-1]
print(moto)
#2. 使用方法pop()删除元素
print('使用pop()删除元素')
del_moto = moto.pop()
print(moto)
print(del_moto)
#3.删除指定位置的元素
#输出是一个简单的句子，指出了最先购买的是哪款摩托车：
first_owned = moto.pop(0)
print('The first moto iowned was a',first_owned+'.')
#4.根据值删除元素:有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
moto.remove('ducati')
print(moto)
moto.insert(2,'ducati')
too_expensive = 'ducati'
moto.remove(too_expensive)
print(moto)
print("\n\tA",too_expensive.title(),"is too expensive for me.\n")
#组织列表
#永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()#利用.sort()函数对列表按字母顺序abcd排列
print(cars)
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)#利用.sort()函数加参数reverse=True对列表按字母顺序abcd排列相反的排列.
print(cars)
number = ['3','2','1','4','5','0','-1']
number.sort()
print(number)
number.sort(reverse=True)
print(number)
a = [3,2,5,4,1,0,-1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
#临时排序
#要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。
print('临时排序')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars,reverse=True))#调用函数sorted()后，列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True。
print('原来的排序:')
print(cars)
#倒着打印列表
#要反转列表元素的排列顺序，可使用方法reverse()。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽车：
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#注意，reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
#方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。
#确定列表长度:使用函数len()可快速获悉列表的长度。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

