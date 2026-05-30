from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from .radar_engine import generate_radar
from .insights import generate_insights
from .disclaimer import get_disclaimer

app = FastAPI(title="RFB Radar App")

class RadarRequest(BaseModel):
    criteria: list[str]
    entities: dict[str, list[float]]

@app.post("/radar")
def create_radar(req: RadarRequest):
    image_path = generate_radar(req.criteria, req.entities)
    insights = generate_insights(req.criteria, req.entities)
    disclaimer = get_disclaimer()

    return {
        "image": image_path,
        "insights": insights,
        "disclaimer": disclaimer
    }

@app.get("/radar-image")
def get_radar_image():
    return FileResponse("radar_output.png")
