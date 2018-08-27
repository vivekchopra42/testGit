import json
import os
from string import ascii_uppercase
import requests
import pdfkit
import time
import hashlib

drive = ""
URL_USER = "https://randomuser.me/api/?nat=us,dk,fr,gb"  # user profile fetch api url


# Generating unique images for each user

def unique_img(md5):
    img_URL = "https://robohash.org/" + md5 + "/"
    PARAMS = {"set": "set4"}
    get_res = requests.get(url=img_URL, params=PARAMS)

    if (get_res.status_code == requests.codes.ok):
        return get_res.url


# generating md5 for each user for unique user image

def md5_gen(name):
    st = name + str(time.time())
    print(hashlib.md5(st.encode()).hexdigest())
    return hashlib.md5(st.encode()).hexdigest()


# user data object
def userData_dict(u_data):
    desig = u_data["name"]["title"].capitalize()
    Fname = u_data["name"]["first"].capitalize()
    Lname = u_data["name"]["last"].capitalize()
    # name = u_data["name"]["title"] + "." + u_data["name"]["first"] + " " + u_data["name"]["last"]
    name = desig + "." + Fname + "." + Lname
    gender = u_data["gender"]
    email = u_data["email"]
    age = str(u_data["dob"]["age"])
    address = u_data["location"]["street"] + ", " + u_data["location"]["city"].capitalize() + ", " + u_data["location"][
        "state"].capitalize()

    user = {"desig": desig,
            "firstname": Fname,
            "lastname": Lname,
            "Fullname": name,
            "gender": gender,
            "email": email,
            "address": address,
            "age": age,
            "unique_image": unique_img(md5_gen(name))  # generating unique profile picture for every user
            }
    return user


def userTXTprofile(user):
    filename = user["firstname"]
    f = open(drive + "/txt/" + filename + ".txt", "a")
    json.dump(user, f, indent=4, sort_keys=True)
    f.close()


def userHTMLprofile(user):
    filename = user["firstname"]
    hf = open(drive + "/html/" + filename + ".html", "w", encoding='utf-8')
    hf.write("<html><meta charset=""UTF-8""><body><table>")
    hf.write("<tr><td>Name : " + user["Fullname"] + "<br>Email : " + user["email"] + "<br>Gender : " + user[
        "gender"] + "<br>Age :  " + user["age"] + "<br>Address : " + user["address"] + "  </td>   <td> <img  src=" +
             user["unique_image"] + " > </td>      </tr>")
    hf.write("</table></body></html>")
    hf.close()


def userPdfprofile(user):
    filename = user["firstname"]
    pdfkit.from_file(drive + "/html/" + filename + '.html', drive+"/pdf/" + filename + '.pdf')

# checking which drives are present in system other than 'C:'
def checkDir():
    for drive in ascii_uppercase:
        if os.path.exists(drive + ":") and drive != 'C':
            print("creating folders in drive : " + drive)

            return drive + ":"
        else:
            print("no")
    return ""

# making directories if they do not already exist in given drive

def mkDir(drive):
    try:
        os.mkdir(drive + "/html/")
        os.mkdir(drive + "/pdf/")
        os.mkdir(drive + "/txt/")
        print("Directory Created ")
    except FileExistsError:
        print("Directory  already exists")


if os.name == 'nt':                     #checking if the operating system is windows
    drive = checkDir()
    if (drive != ""):

        mkDir(drive)
    else:                               # creating folders in C drive if no other drive exists
        drive="C:"
        mkDir(drive)

# TODO code for when operating system is not windows

for i in range(0, 1):
    r = requests.get(url=URL_USER)

    if (r.status_code == requests.codes.ok):
        u_data = r.json()
        u_data = u_data["results"][0]
        user = userData_dict(u_data)
        userTXTprofile(user)
        userHTMLprofile(user)
        userPdfprofile(user)
    print(user)
else:
    print(r.status_code)
