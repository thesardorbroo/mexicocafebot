
class UserOB:
    def __init__(self,id,user_id,username,phone_number,seria,step,language,last_food, description, status, location):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.phone_number = phone_number
        self.seria = seria
        self.step = int(step)
        self.language = language
        self.last_food = last_food
        self.description = description
        self.status = status
        self.location = "longitude:latitude".split(":") if location is None else location.split(":")

