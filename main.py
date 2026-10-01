from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from gemini_utils import (
    get_home_recommendations,
    get_party_recommendations,
    get_jewelry_recommendations
)

app = FastAPI(
    title="PocketSmart AI",
    description="Smart Budget & Recommendation Assistant"
)

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/generate-home")
async def generate_home(
    request: Request,
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form(...)
):

    result = get_home_recommendations(
        budget,
        room,
        style
    )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "title": "Home Recommendations",
            "result": result
        }
    )


@app.post("/generate-party")
async def generate_party(
    request: Request,
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...)
):

    result = get_party_recommendations(
        budget,
        guests,
        event_type
    )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "title": "Party Recommendations",
            "result": result
        }
    )


@app.post("/generate-jewelry")
async def generate_jewelry(
    request: Request,
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...)
):

    result = get_jewelry_recommendations(
        budget,
        occasion,
        style
    )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "title": "Jewelry Recommendations",
            "result": result
        }
  )
