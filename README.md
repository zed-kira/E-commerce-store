# E-commerce-store
A demo E-commerce store with 10 pages as well as a fully functional cart

# Installation :

follow these steps to clone and get this app running :

NOTE : you need to change the settings for the secret-key and database in config/settings.py for the app to run succesfully as well as making DEBUG=True .
 
 - First clone this repo and install pipenv :

            $ git clone https://github.com/ouhadjilyes/E-commerce-store.git
            $ cd E-commerce-store
            $ pip install pipenv

 - then you need to create a virtual environment and install the required dependencies :
            
            $ pipenv install -r requirements.txt
            $ pipenv shell 
            $ python3 manage.py runserver 
           
 - then visit -> http://127.0.0.1:8000/


 - Screenshot : 
 ![Screenshot](https://user-images.githubusercontent.com/87667883/147891694-a2a9f7c3-f929-49d8-8eb9-3ed5905fa884.png)
