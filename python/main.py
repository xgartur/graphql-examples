# An example to get the remaining rate limit using the Github GraphQL API.

import requests
from dotenv import load_dotenv
import os

load_dotenv()



url=os.getenv("GRAPHQL_URL")
token=os.getenv("TOKEN")

print(url)
print(token)
headers = {"Authorization": f"Bearer {token}"}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(url, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
    {
      usuarios{
        id
        usuariosnuevos
        usuariosactivos
        usuariosregistrados
      }
    }
"""

result = run_query(query) # Execute the query
print(result['data'])
