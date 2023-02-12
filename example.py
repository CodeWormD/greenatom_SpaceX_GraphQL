import requests
import pprint

query_company_ceo_coo_name = """
query Query {
  launches {
    mission_name
    rocket {
      rocket_name
    }
  }
}
"""


response = requests.post("https://spacex-production.up.railway.app", json={'query': query_company_ceo_coo_name})
x = response.json()
ls = x['data']['launches']
print(ls)
# for i in range(5):
#     print(ls[i])

