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
print('抱歉!因为座位已给别人抢先预订,所以只能邀请两位嘉宾!')
#使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
del_vip = vip_name.pop()
print('对不起!'+del_vip+'!下次再邀请你!')
del_vip = vip_name.pop()
print('对不起!'+del_vip+'!下次再邀请你!')
del_vip = vip_name.pop()
print('对不起!'+del_vip+'!下次再邀请你!')
del_vip = vip_name.pop()
print('对不起!'+del_vip+'!下次再邀请你!')
del_vip = vip_name.pop()
print('对不起!'+del_vip+'!下次再邀请你!')
print(vip_name[0],vip_name[1]+'!'+'欢迎你们的到来!')#对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
#使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
del vip_name[0]
del vip_name[-1]
print(vip_name)
