import requests
from db import packets

sample_object = packets.SimpleObject(name="jagath")


res = requests.post(
    "http://localhost:5000/create/simple_item", data=sample_object.json()
)

print(res.text)
