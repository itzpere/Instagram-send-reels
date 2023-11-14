from instagrapi import Client
import json
import os
import random
import time

#get username and password
with open('pass.json', 'r') as file:
    passdata = json.load(file)
username = passdata['username']
password = passdata['password']

#changable vars
file_path = "./data.json"
receiver = "itz.pere"
hashs = ['programing', 'programming', 'programmer', 'coding', 'codinglife', 'web', 'webdevelopment', 'webdeveloper', 'developer', 'dev']

#get random hash from data
def uphash():
    with open(file_path, 'r') as json_file:
        tempdata = json.load(json_file)
    hash = tempdata["hashs"][random.randint(0, len(tempdata["hashs"])-1)]
    return hash
#get top posts in hash
def gethash(hashT):
    hashtop = cl.hashtag_medias_top(hashT, 24)
    return [element.id for element in hashtop]
    

cl = Client()
cl.login(username, password)
time.sleep(random.randint(10,20))
try: #check if data is valid file
    if not os.path.exists(file_path):
        print("no file exists")
        with open(file_path, 'w') as json_file:
            json.dump({"ids": gethash(hashs[random.randint(0, len(hashs)-1)]), "hashs": hashs}, json_file)
    elif os.stat(file_path).st_size == 0:
        print("file is empty")
        with open(file_path, 'w') as json_file:
            json.dump({"ids": gethash(hashs[random.randint(0, len(hashs)-1)]), "hashs": hashs}, json_file)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    if "hashs" not in data or "ids" not in data:
        with open(file_path, 'w') as json_file:
            json.dump({"ids": gethash(hashs[random.randint(0, len(hashs)-1)]), "hashs": hashs}, json_file)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    #check if there are videos saved and if not get them from hash and if there is no hash get hash
    if len(data["hashs"]) == 0:
        with open(file_path, 'w') as json_file:
            json.dump({"ids": data["ids"], "hashs": hashs}, json_file)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    if len(data["ids"]) == 0:
        temphash = uphash()
        data["hashs"].remove(temphash)
        with open(file_path, 'w') as json_file:
            json.dump({"ids": gethash(temphash), "hashs": data["hashs"]}, json_file)
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
