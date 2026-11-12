"""
Edit this file to customize the store name, contact details, page images,
and product images. Keep image files in static/images/ or use full image URLs.
"""

STORE_NAME = "Northstar Store"
STORE_TAGLINE = "Thoughtful essentials for everyday living."

CONTACT_EMAIL = "hello@yourstore.com"
CONTACT_PHONE = "+91 00000 00000"
STORE_ADDRESS = "Your city, India"

ABOUT_IMAGE = "/static/images/about.jpg"

# Change these image paths whenever you add your own product images.
# Local images should be placed inside static/images/.
PRODUCTS = [
    {
        "name": "Everyday T-Shirt",
        "description": "A comfortable everyday essential with a clean, versatile fit.",
        "price": 599.00,
        "image": "/static/images/product-1.jpg",
        "category": "Clothing",
    },
    {
        "name": "Everyday Sneakers",
        "description": "Lightweight sneakers designed for daily plans and easy styling.",
        "price": 1899.00,
        "image": "/static/images/product-2.jpg",
        "category": "Footwear",
    },
    {
        "name": "Classic Backpack",
        "description": "A practical everyday bag with room for the things you carry most.",
        "price": 1299.00,
        "image": "/static/images/product-3.jpg",
        "category": "Accessories",
    },
]
