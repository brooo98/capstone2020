import json
import requests
from c20_server.job import Job
from c20_client import reggov_api_doc_error


class DocsJob(Job):

    def __init__(self, page_offset, start_date):
        self.page_offset = page_offset
        self.start_date = start_date

    def get_url(self):
        url = f'https://api.data.gov:443/regulations/v3/document.json?po={self.page_offset}&crd={self.start_date}'
        return url


def docs_job_to_json(docs_job):
    result_dict = {}
    result_dict['job_type'] = 'document'
    result_dict['url'] = docs_job.get_url()

    return json.dumps(result_dict)


def return_list_docs(page_offset, start_date):
    doc_job = DocsJob(page_offset, start_date)

    docs = doc_job.get_url()

    doc_ids = []
    for doc in docs:
        doc_ids.append(doc['document-id'])

    return doc_ids

def get_job(server_url, client_id):

    url = server_url + '/get_job?client_id=' + client_id
    result = requests.get(url)
    return result
