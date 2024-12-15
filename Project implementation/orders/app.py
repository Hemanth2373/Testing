#file order/app.py

from fastapi import FastAPI

#create an instance of fastapi class
#object represents our api application

app= FastAPI(debug=True)

# we import our api module so that the view function can be registered at runtime

from orders.api import api
