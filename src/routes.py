import os

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src import models, schemas

router = APIRouter()
project_path = f'{os.path.dirname(os.path.realpath(__file__))}'
templates = Jinja2Templates(directory=f'{project_path}/templates')

# Frontend endpoints


@router.get('/')
def homepage() -> FileResponse:
    return FileResponse(f'{project_path}/static/index.html')


@router.get('/admin')
def admin_homepage() -> FileResponse:
    return FileResponse(f'{project_path}/static/admin.html')


# Backend endpoints


@router.post('/url/')
def shorten_url(request: schemas.URLBase) -> schemas.URLInfo:
    url = models.URL(target_url=request.target_url)
    url.generate_keys()
    url.generate_urls()
    return url


@router.get('/url/{key}')
def forward_to_shortned_url(key: str) -> RedirectResponse:
    url = models.URL.fetch(key=key)
    url.register_visitor()
    return RedirectResponse(url.target_url)


@router.get('/admin/{secret_key}')
def get_url_admin_info(request: Request, secret_key: str) -> HTMLResponse:
    url = models.URL.fetch(secret_key=secret_key)
    url.generate_urls()
    data = {
        'request': request,
        'target_url': url.target_url,
        'admin_url': url.admin_url,
        'url': url.url,
        'clicks': url.clicks,
        'is_active': url.is_active,
    }
    return templates.TemplateResponse('admin.html', data)


@router.delete('/admin/{secret_key}')
def delete_url(secret_key: str):
    url = models.URL.fetch(secret_key=secret_key)
    url.deactivate()
    return {'detail': 'Sucessfully deactivated URL'}
