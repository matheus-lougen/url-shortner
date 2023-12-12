from __future__ import annotations

import secrets
import string

from fastapi import HTTPException
from sqlalchemy import Boolean, Column, Integer, String

from src.config import get_settings
from src.database import Base, session

settings = get_settings()


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)

    @classmethod
    def fetch(cls, **kwargs) -> URL:
        url = session.query(URL).filter_by(**kwargs).first()
        if not url:
            raise HTTPException(status_code=404, detail='The requested URL was not found on the database')
        if not url.is_active:
            raise HTTPException(status_code=404, detail='The requested URL was deactivated')
        return url

    def generate_keys(self: URL) -> None:
        chars = string.ascii_letters + string.digits
        self.key = "".join(secrets.choice(chars) for _ in range(10))
        self.secret_key = "".join(secrets.choice(chars) for _ in range(20))
        self.upload()

    def generate_urls(self: URL) -> None:
        self.url = f'{settings.base_url}/url/{self.key}'
        self.admin_url = f'{settings.base_url}/admin/{self.secret_key}'

    def register_visitor(self: URL) -> None:
        self.clicks += 1
        self.upload()

    def deactivate(self: URL) -> None:
        self.is_active = False
        self.upload()

    def upload(self: URL) -> None:
        session.add(self)
        session.commit()
