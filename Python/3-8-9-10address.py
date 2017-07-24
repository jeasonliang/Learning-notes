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
#在完成练习 3-4~练习 3-7 时编写的程序之一中，使用 len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
vip_name = ['jeason','angle','lance','chaer']
print('\n\t欢迎VIP:',vip_name[0],vip_name[1],vip_name[2],vip_name[3],'\n\t')
can_not_attend = 'chaer'
vip_name.remove(can_not_attend)
print('因为VIP'+can_not_attend+'无法来!所以我们邀请另外一位嘉宾!')
vip_name.insert(3,'winter')
print('欢迎VIP:','\n\t',vip_name[0],'\n\t',vip_name[1],'\n\t',vip_name[2],'\n\t',vip_name[3])
print('我们刚找到了个更大的桌子,所以更多的VIP将加入')
vip_name.insert(0,'ben')#使用 insert()将一位新嘉宾添加到名单开头。
vip_name.insert(2,'dior')#使用 insert()将另一位新嘉宾添加到名单中间。
vip_name.append('sliaer')#使用 append()将最后一位新嘉宾添加到名单末尾。
#print(vip_name)
#向所邀请的人发出欢迎
print('欢迎VIP:','\n\t',vip_name[0],'\n\t',vip_name[1],'\n\t',vip_name[2],'\n\t',vip_name[3],'\n\t',vip_name[4],'\n\t',vip_name[5],'\n\t',vip_name[6])
print('VIP总人数:',len(vip_name))#使用 len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
