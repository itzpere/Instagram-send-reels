# Instagram-send-reels
simple python script that uses instagrapi for taking reels from hash of account storing them and sending them to someone

1. **Clone repo**: Clone the repo localy to your machine.

2. **Update your package list**. Open your terminal and run the following command:

```bash
sudo apt update
```

3. **Install Python**. You can install Python 3 by running:

```bash
sudo apt install python3
```

4. **Verify the installation**. You can check the installed version of Python by running:

```bash
python3 --version
```

5. **Install pip**. Pip is a package manager for Python. You can install it by running:

```bash
sudo apt install python3-pip
```


6. **Install the necessary Python package**: This script uses the `instagrapi` package. You can install it using pip:

```bash
pip3 install instagrapi
```

7. **Create the necessary JSON files**: This script expects two JSON files, `pass.json` and `var.json`, in the same directory. 

- `pass.json` should contain your Instagram username and password in the following format:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

- `var.json` should contain the receiver and users information in the following format:

```json
{
    "receiver": "SendToUser",
    "users": ["TakeReelsFrom", "user1", ...]
}
```

8. **Run the script**: You can now run the script using Python 3:

```bash
python3 insta-user.py
```

Please replace `"your_username"`, `"your_password"`, `"receiver_info"`, and `["user1", "user2", ...]` with your actual Instagram username, password, receiver information, and user list, respectively.


To explain how this script works

1. Login: The script logs into Instagram using the account credentials provided in the pass.json file.

1. Check for saved reels: The script checks the data.json file for any saved reels.

1. Check for saved users: If there are no saved reels, the script checks if there are any saved users in the data.json file.

1. Use provided user list: If there are no saved users, the script uses the list of users provided in the users variable.

1. Random user selection: The script selects one user at random from the available list.

1. Extract reels: The script extracts reels from the selected user's account.

1. Save extracted reels and users: The script saves the extracted reels and the list of users (excluding the user used for extraction) to the data.json file. This ensures that the same user (and hence the same reels) are not used again.

1. Send and remove reel: The script selects one reel from the saved list, sends it, and then removes it from the data.json file to avoid repetition.

In summary, this script automates the process of logging into Instagram, selecting a user, extracting their reels, and sending them, while ensuring that the same user and reels are not used repeatedly.
