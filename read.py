data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1
        if count % 1000 == 0:
            print(len(data))
        
print('總共讀取', len(data), '筆資料')

print(data[0])


sum_len = 0
for d in data:
  sum_len = sum_len + len(d)
print('留言平均長度為', sum_len / len(data))


new = [] 
for d in data:
  if len(d) < 100:
      new.append(d)
print('總共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for m in data:
  if 'good' in m:
      good.append(m)
print('總共有', len(good), '筆留言提到good')


hi = []
for h in data:
  if 'hi' in h:
      hi.append(h)
print('總共有', len(hi), '筆留言提到hi')


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('>>請問想查什麼字?')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('字典裡沒有這個字哦~!')
print('感謝使用本查詢功能')
