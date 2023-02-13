import requests
from query_graphql import query_launches, query_rockets, url


def launches_data():
    response = requests.post(url, json={'query': query_launches})
    return response


def rockets_data():
    response = requests.post(url, json={'query': query_rockets})
    return response