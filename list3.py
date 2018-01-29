players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
# 开始索引位置:结束索引位置
print(players[0:3])
print(players[-3:])

# clone 一个
players2 = players[:]
players.append('player1')
players2.append('player2')
print(players)
print(players2)