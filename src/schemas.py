from __future__ import annotations

from typing import Optional

import validators
from fastapi import HTTPException
from pydantic import BaseModel, validator


class URLBase(BaseModel):
    target_url: str

    @validator('target_url')
    def validade_url(cls: URLBase, target_url: str) -> Optional[str]:
        if not validators.url(target_url):
            raise HTTPException(status_code=400, detail='Your provided URL is not valid')
        return target_url


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        from_attributes = True


class URLInfo(URL):
    url: str
    admin_url: str
