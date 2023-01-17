# list
# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])

big_bang = ['GD', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']
big_bang.insert(1, '김박사')
exo.append(big_bang)
print(exo)
print(exo[2][2]) #태양
exo[-2] = '시우민'
print(exo[2].pop()) # 승리 pop
print(exo)
print(exo[2].pop(-2)) # 탑 pop
print(exo)
del exo[2][-1]
 # 대성 del
exo[2].remove('김박사')
print(exo)