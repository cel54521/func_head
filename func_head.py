import glob
import re
import os
import csv
import re


#cファイル検索
l = glob.glob('test/**/*.c', recursive=True)

for file in l:
    print(file)
    with open(file,mode="r") as f:
        data = f.read()
        #csv読み込み
        with open('list.txt') as f:
            reader = csv.reader(f)
            print(reader)

            for func in reader:
                print(func)
                funcName = func[0]
                funcComment = func[1]
                data = re.sub(r'\/\*.*\*\/(\n\/\*.*\*\/\n.*(void|int|char|long|float)\s+' + re.escape(funcName) + r'\s*\(.*\)\s*{)', '/* 関数名:' + func[1] + ' */\\1', data)
    
    with open(file,mode="w") as f:
        f.write(data)
    
