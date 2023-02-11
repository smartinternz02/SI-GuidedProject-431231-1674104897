import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "vfWNCWk2Ox12sD7ZvlRkoIg4tN14kgBs_sOVB8qGjm7v"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight"], "values": [[5,4,3,8,2,4,3,8]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/88107f78-bcd4-4712-9aa7-b0e7a7d6fee4/predictions?version=2023-02-10', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())