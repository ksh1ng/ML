'''
<hw0-1>
words.txt (input):
ntu ml mlds ml ntu ntuee

Q1.txt (output):
ntu 0 2
ml 1 2
mlds 2 1
ntuee 3 1
'''
f_name = input("f_name:")

infile = open(f_name,'r')
outfile = open('Q1.txt', 'w')

record = {}
index = 0
line = infile.readline()
while line:
    list_line = line.split()
    for item in list_line:
        if item not in record:
            record[item] = [index,0]
            index += 1

        record[item][1] += 1
    line = infile.readline()


#print(record)
result = sorted(record.items(), key=lambda x: x[1][0])


for x in result:
    str1 = ' '.join(str(e) for e in x[1])  #ex:x = ('meant', [2, 1]) -->str1 = '2, 1'


    outfile.write(x[0] +' ' + str1 + '\n')          #ex: x = ('meant', [2, 1])  --> print: 'meant, 2, 1'

infile.close()
outfile.close()

'''
hw0-2
1. 讀取 westbrook.jpg
2. 將每個pixel的RGB數值都減半(ex: (122, 244, 245)-> (61, 122, 122))，再將圖片輸出為 Q2.jpg
3. RGB數值記得要去掉小數點!(無條件捨去)
'''

from  PIL import Image
p = Image.open('westbrook.jpg')
width, height = p.size
#print(width, height)

for w in range(width):
    for h in range(height):
        r, g, b = p.getpixel((w,h))

        p.putpixel((w,h), (r//2, g//2, b//2))
p.save('Q2.jpg')
