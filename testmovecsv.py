import os
import csv
import shutil

pass_list = ["./test/angry","./test/happy","./test/neutral","./test/sad"]
for path in pass_list:
    os.makedirs(path,exist_ok=True)


with open('./sample_submit.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        old = row[0]
        print(row[0])
        new = row[1]
        print(row[1])
        if os.path.exists("./test/" +old):
            if new == "angry":
                print("〇")
                shutil.move("./test/"+ old,"./test/"+new)
            if new == "sad":
                print("〇")
                shutil.move("./test/"+ old,"./test/"+new)
            if new == "happy":
                print("〇")
                shutil.move("./test/"+ old,"./test/"+new)
            if new == "neutral":
                print("〇")
                shutil.move("./test/"+ old,"./test/"+new)