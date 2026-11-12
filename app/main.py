from pathlib import Path

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .config import (
    ABOUT_IMAGE,
    CONTACT_EMAIL,
    CONTACT_PHONE,
    STORE_ADDRESS,
    STORE_NAME,
    STORE_TAGLINE,
    PRODUCTS,
)
from .database import Base, engine, get_db
from .models import Order, Product

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title=STORE_NAME)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

Base.metadata.create_all(bind=engine)


def seed_products():
    db = next(get_db())
    try:
        if db.query(Product).count() == 0:
            db.add_all([Product(**product) for product in PRODUCTS])
            db.commit()
    finally:
        db.close()


@app.on_event("startup")
def startup():
    seed_products()


def page_context(**values):
    return {
        "store_name": STORE_NAME,
        "store_tagline": STORE_TAGLINE,
        "contact_email": CONTACT_EMAIL,
        "contact_phone": CONTACT_PHONE,
        "store_address": STORE_ADDRESS,
        **values,
    }


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.id).all()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=page_context(products=products),
    )


@app.get("/products/{product_id}")
def product_detail(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context=page_context(product=product),
    )


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context=page_context(about_image=ABOUT_IMAGE),
    )


@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context=page_context(),
    )


@app.get("/checkout/{product_id}")
def checkout(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse(
        request=request,
        name="checkout.html",
        context=page_context(product=product),
    )


@app.post("/orders/{product_id}")
def place_order(
    product_id: int,
    customer_name: str = Form(..., min_length=2, max_length=120),
    email: str = Form(...),
    phone: str = Form(..., min_length=7, max_length=30),
    delivery_address: str = Form(..., min_length=5),
    db: Session = Depends(get_db),
):
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    order = Order(
        customer_name=customer_name.strip(),
        email=email.strip(),
        phone=phone.strip(),
        delivery_address=delivery_address.strip(),
        product_name=product.name,
        amount=product.price,
    )
    db.add(order)
    db.commit()
    return RedirectResponse(url="/order-confirmation", status_code=303)


@app.get("/order-confirmation")
def order_confirmation(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="confirmation.html",
        context=page_context(),
    )
