from api import Pets

pet = Pets()

def test_get_registered_and_deleted():
    status = pet.get_registered_and_deleted()
    assert status == 200

def test_get_token():
    status = pet.get_token()[1]
    token = pet.get_token()[0]
    assert status == 200
    assert token

def test_get_list_users():
    status = pet.get_list_users()[0]
    my_id = pet.get_list_users()[1]
    assert status == 200
    assert my_id

def test_add_pet():
    data = pet.add_pet()
    status = data[1]
    pet_id = data[0]
    pet.delete_pet(pet_id)
    assert status == 200
    assert pet_id
    return pet_id

def test_add_pet_photo():
    pet_id = pet.add_pet()[0]
    status = pet.add_pet_photo(pet_id)[0]
    pet.delete_pet(pet_id)
    assert status == 200

def test_get_pet():
    pet_id = pet.add_pet()[0]
    data = pet.get_pet(pet_id)
    status = data[0]
    pet_name = data[1]
    pet_type = data[2]
    pet_age = data[3]
    pet_gender = data[4]
    owner_id = data[5]
    id_pet = data[6]
    pet.delete_pet(pet_id)
    assert status == 200
    assert pet_name == 'Tom'
    assert pet_type == 'cat'
    assert pet_age == 2
    assert pet_gender == 'Male'
    assert owner_id == pet.get_token()[2]
    assert id_pet == pet_id

def test_delete_pet():
    pet_id = pet.add_pet()[0]
    status = pet.delete_pet(pet_id)
    assert status == 200

def test_update_pet():
    pet_id = pet.add_pet()[0]
    status = pet.update_pet(pet_id)[1]
    pet.delete_pet(pet_id)
    assert status == 200

def test_add_pet_comment():
    pet_id = pet.add_pet()[0]
    data = pet.add_pet_comment(pet_id)
    status = data[0]
    comment_id = data[1]
    pet.delete_pet(pet_id)
    assert status == 200
    assert comment_id

def test_get_pet_by_user_id():
    pet_id = pet.add_pet()[0]
    status = pet.get_pet_by_user_id()[0]
    pets = pet.get_pet_by_user_id()[1]
    pet.delete_pet(pet_id)
    assert status == 200
    assert pets

def test_add_pet_like():
    pet_id = pet.add_pet()[0]
    status = pet.add_pet_like(pet_id)
    pet.delete_pet(pet_id)
    assert status == 200

""" If the pet has a like, then it cannot be liked again """
def test_add_two_pet_likes():
    pet_id = pet.add_pet()[0]
    pet.add_pet_like(pet_id)
    status = pet.add_pet_like(pet_id)
    pet.delete_pet(pet_id)
    assert status == 403

