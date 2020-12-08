# elasticsearch configurations
host_addr = '3.139.84.150'
#host_addr = '192.168.18.70'
# host_addr = 'localhost'
# host_port = '9200'
host_port = '8057'
elastic_username = 'elastic'
elastic_password = 'elastic123'
index_name = 'rizwan_tracks'
batch_size = 200000

file_path = 'D:\\AirUniversity\\FBR_Processing\\taxpayer_5000.csv'
# sr_no,taxpayer_name,registration_no,tax_paid
mapping = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "location" : {
              "type" : "geo_point"
            },
            'id': {"type": "integer"},
            'speed': {"type": "float"},
            'bearing': {"type": "float"},
            'address': {"type": "keyword"},
            'dbm': {"type": "integer"}

            # ,
            # 'month': {"type": "date", "format": "dd-MMM-yy"},
            # 'taxpayer_name': {"type": "keyword"},
            # 'registration_no': {"type": "text"},
            # 'tax_paid': {"type": "long"}
        }
    }
}

query_body = {
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "District": "BAHAWALNAGAR"
          }
        }
      ]
    }
  }
}