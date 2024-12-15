from orders.app import app
from datetime import datetime
from starlette import status
from uuid import UUID
from starlette.responses import Response
from starlette import status
from http import HHTPStatus


order = {
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': 'delivered',
    'created': datetime.now(),
    'order':[
        {
            'product':'cappacino',
            'size':'medium',
            'quantity': 1
        }
    ]
}

@app.get('/orders')
def get_orders():
    return {'orders':[order]}

@app.post('/orders', status_code=status.HTTP_201_CREATED)
def create_order():
    return order

@app.get('/orders/{order_id}')
def update_order(order_id: UUID):
    return order

@app.put('/orders/{order_id}')
def update_order(order_id:UUID):
    return order