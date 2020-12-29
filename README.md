# photo_upload_api
Steps to run the api:
- clone the repo to your local machine
- `cd photo_upload_api`
- create a virtual environment and activate the virtual environment
- `pip install requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate` 
- `python manage.py createsuperuser --email admin@example.com --username admin`
- create a password with the next prompt
- `python manage.py runserver`

interacting with the API:
- with the server running, open localhost:8000 on your browser to see the interactable API
- click on the `http://127.0.0.1:8000/image/` link on the page to interact with the image endpoints
- click on the `http://127.0.0.1:8000/album/` link on the page to interact with the album endpoints

to add images to a new album:
send a PATCH request in the following format: 

```
curl --location --request PATCH 'http://localhost:8000/album/<int:primary_key_of_album>/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--data-raw '{
    "image": [integer ids of images, ]
}'
```

