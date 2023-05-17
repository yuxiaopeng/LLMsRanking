import requests

def get_access_token():
    with open('../access_token.txt', 'r') as f:
        access_token = f.read().strip()
    return access_token

url = 'https://api.github.com/graphql'
json = { 'query' : '{search(query: "LLM sort:stars-desc", type: REPOSITORY, first: 10) {edges {node {... on Repository { name description url stargazers {stars: totalCount} forkCount}}}}}' }
api_token = get_access_token()
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)