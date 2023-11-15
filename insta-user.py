from instagrapi import Client
import json
import os
import random
import time

#get username and password
try:
    with open('pass.json', 'r') as file:
        passdata = json.load(file)
    if "username" in passdata and "password" in passdata:
        username = passdata['username']
        password = passdata['password']
    else:
        print("The 'username' and/or 'password' keys do not exist in the 'pass.json' file.")
        exit(1)
except Exception as e:
    print("The file 'pass.json' does not exist. create it and add the username and password")
    exit(1)

try:
    with open('var.json', 'r') as file:
        vardata = json.load(file)
    if "receiver" in vardata and "users" in vardata:
        users = vardata['users']
        receiver = vardata['receiver']
    else:
        print("The 'receiver' and/or 'users' keys do not exist in the 'var.json' file.")
        exit(1)
except Exception as e:
    print("The file 'pass.json' does not exist. create it and add the username and password")
    exit(1)

#data file path
file_path = "./data-users.json"

#get random hash from data
def getuser():
    with open(file_path, 'r') as json_file:
        tempdata = json.load(json_file)
    user = tempdata["users"][random.randint(0, len(tempdata["users"])-1)]
    return user
#get posts from user
def getUserMedia(tmpuser):
    userid = cl.user_id_from_username(tmpuser)
    userClips = cl.user_clips(userid, 2)
    return [element.id for element in userClips]
    

cl = Client()
cl.login(username, password)
time.sleep(random.randint(10,20))
try: #check if data is valid file if not make a new one
    if not os.path.exists(file_path):
        print("no file exists")
        with open(file_path, 'w') as json_file:
            json.dump({"ids": [], "users": []}, json_file)
    elif os.stat(file_path).st_size == 0:
        print("file is empty")
        with open(file_path, 'w') as json_file:
            json.dump({"ids": [], "users": []}, json_file)

    with open(file_path, 'r') as json_file: #load data from file
        data = json.load(json_file)

    if "users" not in data or "ids" not in data:
        with open(file_path, 'w') as json_file:
            json.dump({"ids": [], "users": []}, json_file)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    #check if there are videos saved and if not get them from user and if there is no hash get hash
    if len(data["users"]) == 0:
        print('users empty')
        with open(file_path, 'w') as json_file:
            json.dump({"ids": data["ids"], "users": users}, json_file)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    if len(data["ids"]) == 0:
        print('ids empty')
        tempuser = getuser()
        data["users"].remove(tempuser)
        with open(file_path, 'w') as json_file:
            json.dump({"ids": getUserMedia(tempuser), "users": data["users"]}, json_file)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    #get random media and send it
    rand = random.randint(0, len(data["ids"])-1)
    media = data["ids"][rand]
    sendto = cl.user_id_from_username(receiver)
    cl.direct_media_share(media, [sendto])
    print("sent")
    #delete media sent
    data["ids"].remove(media)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

except Exception as e:
    print(f"An error occurred: {e}")
#out
cl.logout()