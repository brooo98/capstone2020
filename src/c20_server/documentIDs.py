import requests
import sys



def documentIDs(docket_id):
    api_key = 'XrgkjYhyspWt9bx3NQmygeTcKusMJ5BnFwvwVk06'

    url = ('https://api.data.gov/regulations/v3/documents.json?api_key={}&docketId={}')

    url = url.format(api_key,docket_id)

    response = requests.get(url)
    if response.status_code == 200:
        documents = response.json().get('documents', {})
        documentsIds = [document['documentId'] for document in documents]
        print('documents ids for docket id: ' + docket_id + '\n')
        print(documentsIds)
