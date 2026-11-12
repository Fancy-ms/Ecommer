# Northstar Store

A small server-rendered storefront built with FastAPI, Jinja2, HTML, CSS, SQLAlchemy, and SQLite.

## Pages
- `/` — product collection
- `/products/{product_id}` — product details
- `/checkout/{product_id}` — customer and delivery form
- `/order-confirmation` — order confirmation
- `/about` — about page
- `/contact` — contact details

There is no login, authentication, admin page, cart, payment integration, or quantity selection.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Change store details, products, and image paths

Edit `app/config.py`.

- `STORE_NAME` and `STORE_TAGLINE` change the store branding.
- `CONTACT_EMAIL`, `CONTACT_PHONE`, and `STORE_ADDRESS` change contact information.
- `ABOUT_IMAGE` changes the About page image.
- `PRODUCTS` contains product names, descriptions, prices, categories, and image paths.

Place your local image files in `static/images/` and update the corresponding paths in `app/config.py`.

Expected image filenames:
- `static/images/hero.jpg`
- `static/images/about.jpg`
- `static/images/product-1.jpg`
- `static/images/product-2.jpg`
- `static/images/product-3.jpg`

You can replace these files with your own images or use full image URLs in `app/config.py`.

## Database

SQLite database `store.db` is created automatically. The product catalog is inserted only when the products table is empty. If you change product data in `app/config.py` after the database has already been created, the existing database products will not be overwritten. To reload the initial catalog during development, stop the server and delete `store.db`, then start the server again.

## Note

This is a learning project. It stores basic order details but does not include payment processing, authentication, email notifications, inventory handling, or production-grade security. Do not collect real customer data until appropriate security and privacy protections are added.
