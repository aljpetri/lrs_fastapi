# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import json

app = FastAPI(title="National Truck Network in Minnesota")

# Load JSON at startup
with open("Data/mndot_lrs.json") as f:
    segments = json.load(f)
    
# Set up templates folder
templates = Jinja2Templates(directory="templates")

# Route: main page with buttons
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint for route IDs
@app.get("/routes")
def list_routes():
    route_ids = sorted({seg["ROUTE_ID"] for seg in segments})
    return {"routes": route_ids}

@app.get("/segment")
def get_segment(route_id: str, milepoint: float):
    """
    Get the segment that contains a milepoint on a given route.
    """
    for seg in segments:
        if seg["ROUTE_ID"] == route_id and seg["FROM_MEASURE"] <= milepoint <= seg["TO_MEASURE"]:
            return seg
    raise HTTPException(status_code=404, detail="Segment not found")

