import requests
import json

# CREATE A NEW USER
API_URL = 'https://hng-stagetwo-1f2d786746f2.herokuapp.com/api'
data = {
    'name': 'New User',
    'age': 27,
    'email': 'user@example.com'
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
    'name': 'Oluwatuyi Ojo',
    'age': 20,
    'email': 'tuyi@example.com'
}

json_data_updated = json.dumps(data_to_update)

updated_user = requests.put(f'{API_URL}/10', data=json_data_updated, headers=headers)
if updated_user.status_code == 201:
    print('User deleted successfully')
else:
    print('Error:', updated_user.status_code, updated_user.text)


# LOAD ALL CURRENT USERS
get_response = requests.get(API_URL)

print(get_response.text)
