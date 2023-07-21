from server.celery import app
import time
import requests


@app.task
def request_githubinfo(username: str) -> None:

    try:
        request_url = 'https://api.github.com/users/{0}/repos'.format(username)
        response = requests.get(request_url)
        if response.status_code == 404:
            return "User '{0}' not found".format(username)
        elif response.status_code != 200:
            raise Exception('Error request github.com')
        result = []
        data = response.json()
        for row in data:
            result.append({'owner': row['owner']['login'], 'name': row['name'], "stars": row['stargazers_count'], 'url': row['html_url']})
        return result
    except Exception as ex:
        return "Error: {0}".format(ex)
