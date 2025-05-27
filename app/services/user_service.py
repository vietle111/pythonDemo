def create_user(data):
    name = data.get('name')
    age = data.get('age')
    # check
    if not name or not age:
        return {"error": "Missing name or age"}

    return {
        "message": "User created successfully",
        "data": {
            "name": name,
            "age": age
        }
    }

