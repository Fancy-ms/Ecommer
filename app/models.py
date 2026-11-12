from sqlalchemy import Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float)
    image: Mapped[str] = mapped_column(String(500))
    category: Mapped[str] = mapped_column(String(80))


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(180))
    phone: Mapped[str] = mapped_column(String(30))
    delivery_address: Mapped[str] = mapped_column(Text)
    product_name: Mapped[str] = mapped_column(String(120))
    amount: Mapped[float] = mapped_column(Float)
