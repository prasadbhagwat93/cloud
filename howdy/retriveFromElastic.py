import urllib2
import json
response = json.load(urllib2.urlopen("https://search-test-domain-mqcxz7p4rs6baqy6hnvqwthssy.us-east-1.es.amazonaws.com/test-domain/_search"))
data = response["hits"]["hits"]
file_name = open("testfile.txt","w")
for i in data:
    file_name.write(str(i["_source"]).encode('ascii', 'ignore'))
    file_name.write("\n")
