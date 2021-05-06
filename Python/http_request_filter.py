#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the Elasticsearch low-level client library
from datetime import timedelta, time
from elasticsearch import Elasticsearch
import requests
import json
import schedule
from time import sleep

es = Elasticsearch()
elastic_client = Elasticsearch(["elasticsearch:9200"])

def job():
    api_Rennes = requests.get('https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-du-trafic-en-temps-reel&q=traveltimereliability%20%3E=%2050&rows=1000')

    es.index(index='transport-rennes-data', body=json.loads(api_Rennes.content)) 


#mise en place d'un schedule pour lancer le programme
schedule.every(5).minutes.until(timedelta(hours=1)).do(job)

while True :
    schedule.run_pending()
    sleep(1)