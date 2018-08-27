import requests
import shutil
from PIL import Image
import json
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import StringIO   
import io     




#getting random user data from a api
api = "https://randomuser.me/api/?results=5000"
r = requests.get(url = api)
data = r.json()

#storing the data on a file
with open('data4.txt','w') as outfile:
    json.dump(data,outfile)
outfile.close()

#loading the data on to a json object
with open('data4.txt') as json_file:
    data = json.load(json_file)


#printing the data on a pdf using canvas
canvas = canvas.Canvas("pdfsample15.pdf", pagesize=letter)

for i in range(1,6):
    name = data['results'][i+11]['name']['first']
    dob = data['results'][i+11]['dob']['date']
    phone = data['results'][i+11]['location']['street']
    
    #using an api to get a random doodle based on the text
    api = "https://robohash.org/api/"+name
    r = requests.get(url = api )

    filename = "img52"+str(i)+".png"
    with open(filename,'wb') as out_file:
        out_file.write(r.content)
    out_file.close()
    
    
    
    canvas.drawImage(filename,10,800-(i*100)+2,100,100)
    canvas.drawString(150,800-(i*100),phone)
    canvas.drawString(150,800-(i*100)+20,dob)
    canvas.drawString(150,800-(i*100)+40,name)

canvas.save()