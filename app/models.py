from pydantic import BaseModel

class RadarRequest(BaseModel):
    criteria: list[str]
    entities: dict[str, list[float]]
