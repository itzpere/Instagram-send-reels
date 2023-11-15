# Instagram-send-reels
simple python script that uses instagrapi for taking reels from hash of account storing them and sending them to someone
things you need to do to get this script to work:
- install python
- run ```pip install instagrapi```
- create new file in main folder called "pass.json", paste this into it and change username and password:
  ```json
  {
    username : "your-username",
    password : "your-password"
  }
  ```
- create new file in main folder called "var.json", paste this into it and change users and receiver:
```json
{
    "receiver" : "User-who-will-receive-the-message",
    "users" : ["users","to","take", "reels", "from"]
}
```

edit the script and in the var receiver you set the username of the person you want to sent to and in users you set the accounts you want to take reels from
you can also change in getUserMedia() how many videos to take and store before taking the new ones

to explain this code process in more details, it will log in to acc you provided in pass.json then it will check data.json for some saved reels if it doesnt have any then it will check if there are users saved in that file if there are none then it will take the list of users you provided in users var then it will pick one at random and extract reels from it. after that it will save the extracted reels and users to the data.json but it will not save user used for extracting reels (so it doesnt repeat the same user again hanse the same reels) and then it will take one reel from file send it and remove it from data (so it doesnt repeat)
