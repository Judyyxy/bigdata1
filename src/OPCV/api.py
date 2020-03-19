import os
from sodapy import Socrata
from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get


token = os.getenv('APP_KEY')
client = Socrata('data.cityofnewyork.us', token)
dataid = "nc67-uf89"

def get_data(page_size, idx=None) -> dict:
	try:
		if idx is None:
			res = client.get(dataid, limit=page_size)
		else:
			res = client.get(dataid, limit=page_size, offset=idx*page_size)
		return res
	except Exception as e:
		print(f"Exception occured {e}")
		raise

		
def create_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    return es
	
