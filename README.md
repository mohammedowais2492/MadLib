This project supports only one endpoint as of now - /madlib. 
When the user sends a GET request to this URL, a madlib sentence with the format It was a {adjective} day. I went downstairs to see if I could {verb} dinner. I asked, "Does the stew need fresh {noun}?"
is returned. 

To run this project on Docker container, run the following commands:

1. docker build . -t django_app
2. docker run -p 8080:8080 -i -t django_app

This will run the Django management server on port 8080.
