import requests
import json

API_URL = 'https://hng-stagetwo-agp4b7p37-halfboyfriend.vercel.app/api'
# CREATE A NEW USER
data = {
    'name': 'Ayomide'
}
headers = {'Content-Type': 'application/json'}

json_data = json.dumps(data)

response = requests.post(API_URL, data=json_data, headers=headers)
if response.status_code == 201:
    print('Person created successfully, please reload data base')
else:
    print('Error:', response.status_code, response.text)


# DELETE A USER BY ID

deleted_user = requests.delete(f'{API_URL}/6')
if deleted_user.status_code == 201:
    print('User deleted successfully')
else:
    print('Error:', deleted_user.status_code, deleted_user.text)

# UPDATE CURRENT USER BY ID
data_to_update = {
    'name': 'Idris',
}

json_data_updated = json.dumps(data_to_update)

updated_user = requests.put(f'{API_URL}/11', data=json_data_updated, headers=headers)
if updated_user.status_code == 201:
    print('User updated successfully')
else:
    print('Error:', updated_user.status_code, updated_user.text)


get_response = requests.get(f'{API_URL}/11')

print(get_response.text)
