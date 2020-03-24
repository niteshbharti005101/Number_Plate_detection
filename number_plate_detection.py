import requests
import base64
import json

def number_plate(image_path):
    secret_key = 'Your Secret Key'
    with open(image_path, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=ind&secret_key=%s' % (secret_key)
    r = requests.post(url, data = img_base64)
    try:
        print("Car number = ", r.json()['results'][0]['plate'])
        print("Model Colour = ", r.json()['results'][0]['vehicle']['color'][0]['name'])
        print("Car body_type = ", r.json()['results'][0]['vehicle']['body_type'][0]['name'])
        print("Car Maker = ", r.json()['results'][0]['vehicle']['make'][0]['name'])
        print("Car Model = ", r.json()['results'][0]['vehicle']['make_model'][0]['name'])
        
    except:
        print("No number plate found")
