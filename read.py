data = []
count = 0
with open('reviews.txt', 'r') as f:
 	for line in f:
 		data.append(line)
 		count += 1 #count = count + 1
 		if count % 1000 == 0:
 			print(len(data))
 		
print('總共讀取', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len / len(data))

new = [] 
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(d), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in data:
		good.append(d)
print('總共有', len(good), '筆留言提到good')

hi = []
for d in data:
	if 'hi' in data:
		hi.append(d)
print('總共有', len(good), '筆留言提到hi')