# Instagram-send-reels
simple python script that uses instagrapi for taking reels from hash of account storing them and sending them to someone
things you need to do to get this script to work:
- install python
- run ```pip install instagrapi```
- create new file in main folder called "pass.json", paste this into it and change username and password:
  ```
  {
    username : "your-username",
    password : "your-password"
  }
  ```
- edit the script and in the var receiver you set the username of the person you want to sent to and in users you set the accounts you want to take reels from
you can also change in getUserMedia() how many videos to take and store before taking the new ones
