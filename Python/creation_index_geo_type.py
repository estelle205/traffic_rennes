#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the Elasticsearch low-level client library
from elasticsearch import Elasticsearch
import requests
import json
import schedule
from time import sleep
from datetime import timedelta, time

data_array = dict()
es = Elasticsearch()
elastic_client = Elasticsearch(["elasticsearch:9200"])

Settings = {
  "mappings": {
    "properties": {
        "geo_point_2d" : {
            "type" : "geo_point"
            }
        }
    }
}

es.indices.create(index="transport-rennes-geopoints", body=Settings)

def job() :
    api_Rennes = requests.get('https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-du-trafic-en-temps-reel&q=traveltimereliability%20%3E=%2050&rows=1000')
    data_rennes = json.loads(api_Rennes.content)

    for records in data_rennes['records'] :
        del records['datasetid']
        del records['recordid']

        for i in records['fields'].items() :
            
            if i[0] == 'geo_point_2d' :

                data_array = {"geo_point_2d" : i[1]}
                es.index(index="transport-rennes-geopoints", body=data_array)

            else :
                print('rien dutout')

#mise en place d'un schedule pour lancer le programme
schedule.every(5).minutes.until(timedelta(hours=1)).do(job)

while True :
    schedule.run_pending()
    sleep(1)