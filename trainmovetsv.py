import os
import csv
import shutil

pass_list = ["./train/angry","./train/happy","./train/neutral","./train/sad"]
for path in pass_list:
    os.makedirs(path,exist_ok=True)


with open('./train_master.tsv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in csvreader:
        old = row[0]
        print(row[0])
        new = row[3]
        print(row[3])
        if os.path.exists("./train/" + old):
            if new == "angry":
                print("〇")
                shutil.move("./train/"+ old,"./train/"+new)
            if new == "sad":
                print("〇")
                shutil.move("./train/"+ old,"./train/"+new)
            if new == "happy":
                print("〇")
                shutil.move("./train/"+ old,"./train/"+new)
            if new == "neutral":
                print("〇")
                shutil.move("./train/"+ old,"./train/"+new)