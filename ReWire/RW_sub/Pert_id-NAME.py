'''
Perubation ID is pulled from R code- DeSEq2 and limma 
'''

# import json, requests
# from pprint import pprint

# L1000FWD_URL = 'https://maayanlab.cloud/l1000fwd/'

# query_string = 'BRD-A93236127'
# response = requests.get(L1000FWD_URL + 'synonyms/' + query_string)
# if response.status_code == 200:
# 	pprint(response.json())
# 	json.dump(response.json(), open('api1_result.json', 'w'), indent=4)


# import json, requests
# from pprint import pprint

# L1000FWD_URL = 'https://maayanlab.cloud/l1000fwd/'s

# query_string = 'dex'
# response = requests.get(L1000FWD_URL + 'synonyms/' + query_string)
# if response.status_code == 200:
# 	pprint(response.json())
# 	json.dump(response.json(), open('api1_result.json', 'wb'), indent=4)
import requests
import json

url = "https://maayanlab.cloud/L1000FWD/query"
input_ids = ['s-001']

payload = {
    "input": input_ids,
    "searchMethod": "PERT_ID",
    "share": True,
    "pert_id": True,
    "limit": 50
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()

    # Check if the API returned a valid response with data
    if 'data' in data:
        json_data = data['data']

        # Output the JSON data to the console
        print(json_data)

        # Write the JSON data to a file named 'api_result.json'
        with open('api_result.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    else:
        print("No data found in the response.")
else:
    print("Error:", response.status_code, response.text)
