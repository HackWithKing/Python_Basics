import json

file = "passwords.json"

def save_password(site, password):
    data = {}
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except:
        pass

    data[site] = password

    with open(file, "w") as f:
        json.dump(data, f)

site = input("Enter site: ")
password = input("Enter password: ")

save_password(site, password)
print("Password saved")
