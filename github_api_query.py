import requests

url = 'https://api.github.com/graphql'
json = { 'query' : '{search(query: "LLM", type: REPOSITORY, first: 10) {edges {node {... on Repository { name description url stargazerCount forkCount}}}}}' }
api_token = "your api token"
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)