guestList = ['John Kennedy', 'Arnlod Schwarzenegger', 'Donald Duck']

#No. 1 Modifying
guestList[-1] = 'Daphne Duck'
print(guestList[-1])

#No. 2 Append
guestList.append('Donald Duck')
print(guestList[-1])

#No. 3 Insert
guestList.insert(0, 'Bobbert Rice')
print(guestList[0])

#No. 4 Del
del guestList[-2]
print(guestList)

#No. 5 Pop
print(guestList.pop())

#No. 6 Remove
guestList.remove('Bobbert Rice')
print(guestList)

#No. 7 Sort
guestList.sort()
print(guestList)
guestList.sort(reverse=True)
print(guestList)

#No. 8 Sorted
print(sorted(guestList))
print(sorted(guestList, reverse=True))

#No. 9 Reverse
guestList.reverse()
print(guestList)

#No. 10 Len
print(len(guestList))
