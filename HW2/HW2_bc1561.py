from pyspark import SparkContext
import csv
import sys

def cuisine_camis(pid, record):
    import csv
    if pid==0:
        next(record)
    reader = csv.reader(record)
    for row in reader:
        camis = row[0]
        cuisine = row[7]
        yield (camis, cuisine)

if __name__=='__main__':
    sc = SparkContext()

    NYC_RESTAURANT = sys.argv[1]

    nyc_rest = sc.textFile(NYC_RESTAURANT, use_unicode=False).cache()

    nyc_rest_records = sat.mapPartitionsWithIndex(nyc_rest)

    nyc_rest_records.mapPartitionsWithIndex(cuisine_camis) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(lambda x,y: 1) \
            .map(lambda x: (x[0][1], 1)) \
            .reduceByKey(lambda x,y: x+y) \
            .top(25, key=lambda x: x[1]).saveAsTextFile(sys.argv[-1])
