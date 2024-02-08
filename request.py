import requests

url_choose_image = 'http://127.0.0.1:5000/choose_image'
url_run_inference = 'http://127.0.0.1:5000/run_inference'
url_display_animation = 'http://127.0.0.1:5000/display_animation'

payload = {'selected_image': 'interview'}  

response = requests.post(url_choose_image, data=payload)
print(response.json()) 

response = requests.post(url_run_inference, json=payload)
print(response.json())  

response = requests.get(url_display_animation)
print(response.text) 
