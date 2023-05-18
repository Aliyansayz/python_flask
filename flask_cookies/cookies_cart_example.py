Certainly! Let's take the example of a shopping website built with Flask. 
Here's how cookies can be used to enhance the user experience:

```python
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Check if the user has a cart cookie
    cart = request.cookies.get('cart')
    if cart:
        # If the cart cookie exists, retrieve its value
        items = cart.split(',')
    else:
        items = []

    # Render the homepage template and pass the items in the cart
    return render_template('index.html', cart_items=items)

@app.route('/add_to_cart/<item>')
def add_to_cart(item):
    # Retrieve the existing cart or create a new one
    cart = request.cookies.get('cart')
    if cart:
        items = cart.split(',')
    else:
        items = []

    # Add the item to the cart
    items.append(item)

    # Create a response and set the cart cookie
    response = make_response('Item added to cart!')
    response.set_cookie('cart', ','.join(items))

    return response

if __name__ == '__main__':
    app.run()
```

In this example, the `/` route is the homepage of the shopping website. 
When a user visits this route, it checks if the user has a cart cookie. 
If the cookie exists, it retrieves the items in the cart. Otherwise, it initializes an empty list.

The `/add_to_cart/<item>` route is triggered when a user adds an item to the cart. 
It first retrieves the existing cart or creates a new one if it doesn't exist. 
It then appends the new item to the cart list. Finally, it creates a response and sets the cart cookie with the updated cart items.

The use of cookies in this example allows the website to remember the user's cart between requests. 
When the user adds items to the cart, the cart cookie is updated, ensuring that the user's selections persist across different pages or visits to the website.

Note that this is a simplified example for illustration purposes. 
In a real-world scenario, you would need to consider security measures, such as encrypting sensitive data in cookies, as well as handling scenarios like removing items from the cart or handling multiple users' carts simultaneously.
