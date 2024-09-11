
guestList = ['John Kennedy', 'Arnlod Schwarzenegger', 'Donald Duck']      #3_4
dinInv = 'You are invited to my dinner party my dearest '
invConc = 'Yours truly, Yack.'

print(dinInv + guestList[0] + '!\n' + invConc)
print(dinInv + guestList[1] + '!\n' + invConc)
print(dinInv + guestList[2] + '!\n' + invConc)


newGuest = 'Kamala Harris'     #3_5
print('Unfortunatley, ' + guestList[0] + ' will not be coming to the dinner party.')     

del guestList[0]
guestList.insert(0, newGuest)

print(dinInv + guestList[0] + '!\n' + invConc)
print(dinInv + guestList[1] + '!\n' + invConc)
print(dinInv + guestList[2] + '!\n' + invConc)


print('Notice: A larger venue has been found guest list will be changed and issued promptly.')  #3_6

guestList.insert(0, 'Sydney Sweeny')
guestList.insert(1, 'Keaunu Reeves')
guestList.insert(-1, 'Jack Black')


print(dinInv + guestList[0] + '!\n' + invConc)
print(dinInv + guestList[1] + '!\n' + invConc)
print(dinInv + guestList[2] + '!\n' + invConc)
print(dinInv + guestList[3] + '!\n' + invConc)
print(dinInv + guestList[4] + '!\n' + invConc)
print(dinInv + guestList[5] + '!\n' + invConc)


sorryMsg = 'Due to some need for cuts you are not invited '  #3_7
print('Hello all, two terrorists ran into the new venue and blew it up.\n So, now I\'m broke and the party can only have 2 guests.\n Thanks!')

print(sorryMsg + guestList.pop())
print(sorryMsg + guestList.pop())
print(sorryMsg + guestList.pop())
print(sorryMsg + guestList.pop())

print('You are still invited ' + guestList[0] + '.')
print('You are still invited ' + guestList[1] + '.')

del guestList[0]
del guestList[0]

print(guestList)


print('This is the number of people getting invited:\n ')
print(len(guestList))