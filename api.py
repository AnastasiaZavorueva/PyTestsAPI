import json
import os
import uuid
import requests
from settings import VALID_EMAIL, VALID_PASSWORD


class Pets:
    """ API library for website http://34.141.58.52:8080/#/ """

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered_and_deleted(self) -> json:
        """ Request to site swagger to register and delete a user """
        e = uuid.uuid4().hex
        data = {
            "email": f'{e}@gmail.com',
            "password": '1234',
            "confirm_password": '1234'
        }
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status

    def get_token(self) -> json:
        """ Request to site swagger to get a users token using the specified email and password """
        data = {
            "email": VALID_EMAIL,
            "password": VALID_PASSWORD
        }
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """ Request to site swagger to get a list of users(my_id) """
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.json
        return status, my_id

    def add_pet(self) -> json:
        """ Request to site swagger to add a new pet """
        my_token = self.get_token()[0]
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "id": my_id,
            "name": "Tom",
            "type": "cat",
            "age": 2,
            "gender": "Male",
            "owner_id": my_id,
            "likes_count": None,
            "liked_by_user": False
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def add_pet_photo(self, pet_id) -> json:
        """ Request to site swagger to add the photo to a pet """
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pic_path = os.path.join(os.path.dirname(__file__), 'tests/Photo/cat.jpg')
        files = {'pic': ('cat.jpg', open(pic_path, 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def add_pet_like(self, pet_id) -> json:
        """ Request to site swagger to add a like to a pet """
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_pet(self,pet_id) -> json:
        """ Request to site swagger to pet data by its id """
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_name = res.json()['pet']['name']
        pet_type = res.json()['pet']['type']
        pet_age = res.json()['pet']['age']
        owner_id = res.json()['pet']['owner_id']
        pet_gender = res.json()['pet']['gender']
        id_pet = res.json()['pet']['id']
        return status, pet_name, pet_type, pet_age, pet_gender, owner_id, id_pet, pet_id

    def update_pet(self,pet_id) -> json:
        """ Request to site swagger to update pet data """
        my_token = self.get_token()[0]
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "id": pet_id,
            "name": 'Tom1',
            "type": 'dog',
            "age": 22,
            "owner_id": my_id
        }
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def add_pet_comment(self,pet_id) -> json:
        """ Request to site swagger to add the comment to a pet """
        my_token = self.get_token()[0]
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "user_id": my_id,
            "pet_id": pet_id,
            "date": "2022-12-04T17:26:47.800Z",
            "message": "the best pet",
            "user_name": "svetatest1@gmail.com"
        }
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        comment_id = res.json()['id']
        return status, comment_id

    def get_pet_by_user_id(self) -> json:
        """ Request to site swagger to get a list of the user's pets """
        my_token = self.get_token()[0]
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "skip": 0,
            "num": 10,
            "type": "cat",
            "petName": None,
            "user_id": my_id
        }
        res = requests.post(self.base_url + f'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        pets = res.json()
        return status, pets

    def delete_pet(self, pet_id) -> json:
        """ Request to site swagger to delete a pet"""
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status