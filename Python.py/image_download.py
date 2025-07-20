import requests
url = 'https://youtube.com/shorts/9NwPkHnx_BA?si=lUwHhITPagcMhv8o'

with open('flag1.mp3','wb') as f:
    f.write((requests.get(url)).content)

