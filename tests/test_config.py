import os

from navconfig import BASE_DIR, DEBUG, config

# set configuration for navconfig
os.environ["NAVCONFIG_ENV"] = "drive"
with open("file_env", "r") as f:
    file_id = f.read().replace("\n", "")
os.environ["NAVCONFIG_DRIVE_CLIENT"] = "credentials.txt"
os.environ["NAVCONFIG_DRIVE_ID"] = file_id


print(config)
print("base dir is: ", BASE_DIR)
print("debug is: ", DEBUG)
