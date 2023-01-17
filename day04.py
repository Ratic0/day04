# list comprehension

odd_lists = [ i for i in range(1, 11) if i % 2 == 1]
odd_tuple = ( i for i in range(1, 11) if i % 2 == 1)
# for i in range(1, 11):
#     if i% 2 ==1 :
#         odd_lists.append(i)
# print(odd_lists)
print(odd_lists)
print(odd_tuple)
print(type(odd_tuple) # sd==generator 메모리 거의  저장안함)
