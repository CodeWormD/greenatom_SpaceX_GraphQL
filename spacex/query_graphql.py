url = "https://spacex-production.up.railway.app"

query_launches = """
query Query {
  launches {
    mission_name
  }
}
"""

query_rockets = """
query Dragons {
  rockets {
    name
    first_flight
    description
  }
}
"""