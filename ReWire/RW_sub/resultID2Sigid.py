import json, requests
from pprint import pprint

L1000FWD_URL = 'https://maayanlab.cloud/l1000fwd/'

result_id = '6519d01fc99977002d2bcb09'
response = requests.get(L1000FWD_URL + 'result/topn/' + result_id)
if response.status_code == 200:
	pprint(response.json())
	json.dump(response.json(), open('api4_result.json', 'w'), indent=4)
