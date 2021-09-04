from starlette.templating import Jinja2Templates
from starlette.requests import Request
import fastapi

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")

##@router.get('/', include_in_schema=False)
@router.get("/", include_in_schema=False)
async def index(request: Request):
    data = {"request": request}
    return templates.TemplateResponse("home/index.html", data)


@router.get("/about", include_in_schema=False)
async def about(request: Request):
    data = {"request": request}
    return templates.TemplateResponse("home/about.html", data)


@router.get("/contact", include_in_schema=False)
async def contact(request: Request):
    data = {"request": request}
    return templates.TemplateResponse("home/contact.html", data)


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
