# AI E-Commerce Customer Support Agent

# -------------------------------
# PRODUCT DATA
# -------------------------------

products = [
    {
        "id": 1,
        "name": "Black T-Shirt",
        "category": "clothing",
        "price": 499,
        "color": "black"
    },
    {
        "id": 2,
        "name": "Blue Jeans",
        "category": "clothing",
        "price": 999,
        "color": "blue"
    },
    {
        "id": 3,
        "name": "White Sneakers",
        "category": "shoes",
        "price": 1499,
        "color": "white"
    },
    {
        "id": 4,
        "name": "Wireless Headphones",
        "category": "electronics",
        "price": 1999,
        "color": "black"
    },
    {
        "id": 5,
        "name": "Smart Watch",
        "category": "electronics",
        "price": 2499,
        "color": "black"
    }
]


# -------------------------------
# ORDER DATA
# -------------------------------

orders = {
    "1001": {
        "product": "Black T-Shirt",
        "status": "Shipped",
        "delivery": "12 September 2026"
    },

    "1002": {
        "product": "Wireless Headphones",
        "status": "Out for delivery",
        "delivery": "10 September 2026"
    },

    "1003": {
        "product": "Blue Jeans",
        "status": "Processing",
        "delivery": "14 September 2026"
    }
}


# -------------------------------
# MEMORY
# -------------------------------

memory = {
    "name": None,
    "previous_product": None
}


# -------------------------------
# TOOL 1: SEARCH PRODUCTS
# -------------------------------

def search_products(keyword):
    results = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            results.append(product)

    return results


# -------------------------------
# TOOL 2: CHECK ORDER STATUS
# -------------------------------

def check_order(order_id):

    if order_id in orders:
        order = orders[order_id]

        return (
            f"Order #{order_id}\n"
            f"Product: {order['product']}\n"
            f"Status: {order['status']}\n"
            f"Expected delivery: {order['delivery']}"
        )

    return "Sorry, I could not find that order."


# -------------------------------
# TOOL 3: RETURN PRODUCT
# -------------------------------

def return_product(order_id):

    if order_id in orders:

        return (
            f"Return request created successfully for "
            f"Order #{order_id}."
        )

    return "Sorry, order not found."


# -------------------------------
# TOOL 4: RECOMMEND PRODUCTS
# -------------------------------

def recommend_products():

    return [
        products[0],
        products[3],
        products[4]
    ]


# -------------------------------
# DISPLAY PRODUCTS
# -------------------------------

def display_products(results):

    if len(results) == 0:
        print("No products found.")
        return

    print("\nProducts found:")

    for product in results:

        print(
            f"{product['id']}. "
            f"{product['name']} - "
            f"₹{product['price']} - "
            f"{product['color']}"
        )


# -------------------------------
# AI AGENT
# -------------------------------

def ai_agent(user_input):

    text = user_input.lower()

    # ---------------------------
    # Remember user's name
    # ---------------------------

    if text.startswith("my name is"):

        name = user_input[11:].strip()

        memory["name"] = name

        return f"Nice to meet you, {name}!"


    # ---------------------------
    # Greeting
    # ---------------------------

    if text in ["hi", "hello", "hey"]:

        if memory["name"]:
            return f"Hello {memory['name']}! How can I help you?"

        return "Hello! How can I help you?"


    # ---------------------------
    # ORDER STATUS
    # ---------------------------

    if "order" in text and (
        "status" in text or
        "where" in text or
        "track" in text
    ):

        words = text.split()

        for word in words:

            if word.isdigit():

                return check_order(word)

        return "Please provide your order number."


    # ---------------------------
    # RETURN
    # ---------------------------

    if "return" in text:

        words = text.split()

        for word in words:

            if word.isdigit():

                return return_product(word)

        return "Please provide your order number for the return."


    # ---------------------------
    # PRODUCT SEARCH
    # ---------------------------

    if "shirt" in text:

        memory["previous_product"] = "shirt"

        results = search_products("shirt")

        display_products(results)

        return "These are the shirts available."


    if "jeans" in text:

        memory["previous_product"] = "jeans"

        results = search_products("jeans")

        display_products(results)

        return "These are the jeans available."


    if "headphone" in text:

        memory["previous_product"] = "headphones"

        results = search_products("headphone")

        display_products(results)

        return "These are the headphones available."


    if "watch" in text:

        memory["previous_product"] = "watch"

        results = search_products("watch")

        display_products(results)

        return "These are the watches available."


    # ---------------------------
    # RECOMMENDATIONS
    # ---------------------------

    if (
        "recommend" in text or
        "suggest" in text
    ):

        results = recommend_products()

        display_products(results)

        return "Here are some products I recommend."


    # ---------------------------
    # MEMORY TEST
    # ---------------------------

    if "what is my name" in text:

        if memory["name"]:
            return f"Your name is {memory['name']}."

        return "You haven't told me your name yet."


    # ---------------------------
    # HELP
    # ---------------------------

    if "help" in text:

        return """
I can help you with:

1. Product search
2. Order status
3. Returns
4. Product recommendations
5. Remember your name
"""


    # ---------------------------
    # DEFAULT RESPONSE
    # ---------------------------

    return (
        "Sorry, I don't understand that yet. "
        "Type 'help' to see what I can do."
    )


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("=" * 50)
print("       AI E-COMMERCE SUPPORT AGENT")
print("=" * 50)

print("Type 'help' to see available options.")
print("Type 'exit' to stop.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print("Agent: Thank you for shopping with us!")
        break

    response = ai_agent(user_input)

    print("Agent:", response)