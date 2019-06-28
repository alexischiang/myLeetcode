strs = ['flow','flower','flight']
for index in range(len(strs)):
    if strs[index][0] == strs[index + 1][0]:
        flag = 1
    else:
        flag = 0
