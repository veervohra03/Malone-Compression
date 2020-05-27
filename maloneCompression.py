# Veer Vohra
# Malone Compression
# May 2020

import sys
from pathlib import Path

def main():
    cin = input("Welcome\n1 - Input a message\n2 - Compress a file\n>>> ")
    if cin == "1":
        text()
    elif cin == "2":
        textfile()

def text():
    cin1 = input("Message:\n>>> ")
    comped = maloneCompression(cin1)
    print("\nCompressed string :", comped)
    print("Ratio =", len(comped)/len(cin1), "\n")

def textfile():
    if len(sys.argv) >= 2  and sys.argv[1][-4:] == ".txt":
        with open(sys.argv[1], 'r') as f:
            data = f.read().replace('\n', '')
            f.close()
            size = Path(sys.argv[1]).stat().st_size
        comped = maloneCompression(data)
        with open('compressed.txt', 'a') as f:
            f.write(comped)
            f.close()
            compedSize = Path('compressed.txt').stat().st_size
        print("Ratio =", compedSize/size, "\n")

    else:
        print("Please re-run with a text file provided as an arguements")


def maloneCompression(string):
    query = string
    with open('adj.txt', 'r') as f:
        data = f.read().replace('\n', ' ').split(' ')
        f.close()
    stopwords = ['the', 'it', 'do'] + data
    querywords = query.split()
    arr  = [word for word in querywords if word.lower() not in stopwords]
    i = 0
    while i < len(arr):
        if arr[i][-3:].lower() == "ing":
            arr[i] = arr[i][:-3]
            if arr[i][len(arr[i]) - 1] == arr[i][len(arr[i]) - 2]:
                arr[i] = arr[i][:-1]
        elif arr[i][-2:].lower() == "ed":
            arr[i] = arr[i][:-2]
        elif "'" in arr[i]:
            arr[i] = "".join(arr[i].split("'")[0])
        if arr[i][:-2].lower() == "no":
            arr[i] = "no"
        i += 1
    return " ".join(arr).replace("I", "me").replace("a lot", "big").replace("my", "me").replace("thanks", "thank").replace("thank you", "thank")

main()
