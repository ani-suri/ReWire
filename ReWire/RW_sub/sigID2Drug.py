import json
import requests


signature_id = 'CPC006_MCF7_6H:BRD-A13122391-001-01-9:0.08'

# Extracting the pert_id from the signature_id
pert_id = signature_id.split(':')[1]
pert_id = pert_id.split('-')
pert_id = pert_id[1] + '-' + pert_id[2]
print(pert_id)

# # Retrieving the data from the API
# response = requests.get(L1000FWD_URL + pert_id)

# # Check if the response is successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON data
#     data = response.json()
    
#     # Find the drug information corresponding to the pert_id
#     drug_info = next((item for item in data if item["pert_id"] == pert_id), None)
    
#     if drug_info:
#         # Print the drug name
#         print("Drug Name:", drug_info["Name"])
#     else:
#         print("Drug information not found.")
# else:
#     print("Failed to retrieve data from the API.")
