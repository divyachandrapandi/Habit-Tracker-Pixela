import requests
from datetime import datetime

###----------------DEFINITION---------------###
"""GET - user get data from external system"""
"""POST - user post data in external system"""
"""PUT - user updates the their post in external system"""
"""DELETE - user delete post in external system"""

USERNAME = "divya55"
AUTH_TOKEN = "passhatj"
# TODO  pixela user account creation
user_account_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": AUTH_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=user_account_endpoint, json=user_parameters)
# print(response.text)
# TODO creating a graph
graph_endpoint = f"{user_account_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": AUTH_TOKEN,
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Book Reading - Accomplishment",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# TODO to view graph
# https://pixe.la/v1/users/divya55/graphs/graph1.html

# TODO post a pixel
"""https://www.w3schools.com/python/python_datetime.asp"""
today = datetime.now()
DATE = today.strftime("%Y%m%d")
pixel_endpoints = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": DATE,
    "quantity": "60",
}
# response = requests.post(url=pixel_endpoints, json=pixel_config, headers=headers)
# print(response)
# TODO update a pixel
update_pixel = f"{graph_endpoint}/{GRAPH_ID}/{DATE}"

update_config = {
    "quantity": "90",
}
# response = requests.put(url=update_pixel, json=update_config, headers=headers)
# print(response.text)
# TODO Delete a  pixel
delete_pixel = update_pixel
# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)
