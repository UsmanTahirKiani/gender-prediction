import csv
import time
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch import ElasticsearchException
import configurations as conf
import data_helpers as pyfun


es=Elasticsearch([conf.host_addr+':'+conf.host_port])

print(es.indices.delete(index=conf.index_name, ignore=[400, 404]))

response = es.indices.create(
    index=conf.index_name,
    body=conf.mapping,
    ignore=400 # ignore 400 already exists code
)


with open('tracks_rizwan_alvi.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count>0:
            if int(row[0]) > 1:
                address = pyfun.getReverseGeocodedAddress(str(row[9]) + ' ' + str(row[10]), 'Nominatim')
                # address = str(address.address).split(',')[0]
                # print(row[9])
                if row[7] != '':
                    doc = {
                        'id': int(row[0]),
                        'speed': round(float(row[12])*3.6),
                        'bearing': float(row[13]),

                            'dbm': int(row[7]),
                        'address': address.address,
                        'location':
                            {
                                "lat": row[9],
                                "lon": row[10]
                            }
                    }
                    # print(doc)
                    res = es.index(index=conf.index_name, id=row[0], body=doc)
                    # res = es.index(index=conf.index_name, id=1, body=doc)

                    #time.sleep(1)
                    print(doc)

        line_count += 1