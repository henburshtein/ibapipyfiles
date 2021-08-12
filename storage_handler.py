import csv

def csvhandler(self, f, tup1):
        writer = csv.writer(f)
        writer.writerow(tup1)
        f.close()