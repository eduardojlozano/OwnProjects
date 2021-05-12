import requests

originalUrl = 'https://tcms.aiojiraapps.com/aio-tcms/api/v1/project/CDC/testcycle/CDC-CY-1/testcase'
url = 'http://tcms.aiojiraapps.com/aio-tcms/api/v1/project/CDC/testcycle/CDC-CY-1/testcase'
response = requests.get(url)

print(f'Response: {response}')

headers = {'Authorizacion': 'Aioauth NDVkZmZjNGEtOWZiMy00YzQ5LWIyYzEtZmZhZDRlYzAzNjRm'}
response2 = requests.get(url, headers)  # despues le agregue eso y nada

print(f'Response: {response2}')


payload = dict(key1='NDVkZmZjNGEtOWZiMy00YzQ5LWIyYzEtZmZhZDRlYzAzNjRm')
responsePost = requests.post(url, payload)
print(responsePost)