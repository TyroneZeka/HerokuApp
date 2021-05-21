from models.user import UserModel

def authenticate(username,password):
    # Gets the jwt-payload by checking if username and password are true
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user
    
def identity(payload):
    # returns the user_id after receiving the payload.
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)