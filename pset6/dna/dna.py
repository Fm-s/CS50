import csv
import sys

strDictList = []
strSequences = []

def main():
    with open(sys.argv[1],newline='') as dataFile:
        data = csv.DictReader(dataFile)
        for row in data:
            strDictList.append(row)

    with open(sys.argv[1],newline='') as dataFile:
        dataPlain = csv.reader(dataFile)
        strSequences = next(dataPlain)[1:]

    with open(sys.argv[2]) as sampleFile:
        sampleString = sampleFile.read().strip()

    resultDict = dict()
    for strSeq in strSequences:
        resultDict[strSeq] = checkSequence(sampleString,strSeq)

    for strEntry in strDictList:
        name = strEntry.pop("name")
        if strEntry == resultDict:
            print(name)
            sys.exit(0)
    print("No match")


def checkSequence(sample, strSeq):

    maxSequence = 0
    currentStreak = 0
    sampleArrow = 0
    sequence = False

    while True:
        if len(sample) - sampleArrow < len(strSeq):
            break

        if sample[sampleArrow : len(strSeq) + sampleArrow] == strSeq:
            sampleArrow += len(strSeq)
            if sequence:
                currentStreak += 1;
            else:
                currentStreak = 1
                sequence = not sequence
        else:
            sampleArrow += 1
            if sequence:
                sequence = not sequence
                if currentStreak > maxSequence:
                    maxSequence = currentStreak

    return str(maxSequence)

main()