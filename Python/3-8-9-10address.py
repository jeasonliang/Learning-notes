#想出至少 5 个你渴望去旅游的地方。将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
world_address = ['LosAngeles','Beijing','Xiamen','Amsterdam','Caribbean Sea']
print('按照原始排列顺序打印该列表:\n\t',world_address)#按原始排列顺序打印该列表。
print('按照临时排列字母的顺序打印该列表:\n\t',sorted(world_address))#使用 sorted()按字母顺序打印这个列表，同时不要修改它。临时排序
print('按照原始排列顺序打印该列表:\n\t',world_address)#再次打印该列表，核实排列顺序未变。
print('按照临时排列字母相反顺序打印该列表:\n\t',sorted(world_address,reverse=True))#使用 sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print('按照原始排列顺序打印该列表:\n\t',world_address)#再次打印该列表，核实排列顺序未变。
world_address.reverse()#使用.reverse()修改列表元素的排列顺序。
print('修改后的列表:\n\t',world_address)#打印该列表，核实排列顺序确实变了。
world_address.reverse()#使用 reverse()再次修改列表元素的排列顺序。
print('修改回来的列表:\n\t',world_address)#打印该列表，核实排列顺序确实恢复了。
world_address.sort()#使用 reverse()再次修改列表元素的排列顺序。
print('按字母排序打印列表:\n\t',world_address)#打印该列表，核实排列顺序确实变了。
