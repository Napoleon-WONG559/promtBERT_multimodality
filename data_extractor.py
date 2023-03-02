import csv

class DataExtractor(object):
    def __init__(self,
                 filename):
        record=[]
        with open(filename,newline='') as csvfile:
            read=csv.reader(csvfile)
            count=0
            for item in read:
                record.append(item)
                count+=1
                if(count==6836):
                    break
        self.data=record

    