from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(
    title="My API",
    description="API",
    version="v1",
    servers=[{"url": "http://127.0.0.1:8080"}],
)


# -------------------------------------------------------------------
# Response model
# -------------------------------------------------------------------

class PointResponse(BaseModel):
    type: str = Field(..., description="The type")
    id: str = Field(..., description="The id")
    name: str = Field(..., description="The name")

    lat: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude",
    )

    lon: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude",
    )

    asl: Optional[float] = Field(
        ...,
        description="Meters above Sea-Level",
    )

    distanceKm: float = Field(
        ...,
        description="Kilometer distance from the point",
    )


# -------------------------------------------------------------------
# Mock response
# -------------------------------------------------------------------

MOCK_RESPONSE = [
    {
        "id": "id1",
        "lat": 47.558399,
        "name": "name1",
        "type": "type1",
        "asl": 279,
        "distanceKm": 0,
        "lon": 7.57327,
    },
    {
        "id": "id2",
        "lat": 0,
        "name": "name2",
        "type": "type2",
        "asl": None,
        "distanceKm": 5320.3,
        "lon": 0,
    },
]


# -------------------------------------------------------------------
# Endpoint
# -------------------------------------------------------------------

@app.get(
    "/point",
    response_model=List[PointResponse],
    summary="Nearest Points",
    description="Get nearest points",
    responses={
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "string",
                    }
                }
            },
        }
    },
)
def get_points(
    lat: float = Query(
        ...,
        ge=-90,
        le=90,
        description="WGS 84 Standard Latitude",
        examples=[0],
    ),
    lon: float = Query(
        ...,
        ge=-180,
        le=180,
        description="WGS 84 Standard Longitude",
        examples=[0],
    ),
    asl: float = Query(
        0.0,
        ge=-500,
        le=9000,
        description="Height above sea level",
        examples=[0.0],
    ),
    maxHeightDiff: Optional[float] = Query(
        None,
        ge=1,
        le=1000,
        description="Maximum height difference",
    ),
    maxDistance: float = Query(
        100.0,
        ge=1,
        le=10000,
        description="Maximum distance",
        examples=[100.0],
    ),
    nNeighbors: int = Query(
        5,
        ge=1,
        le=100,
        description="Maximum number of neighbors",
        examples=[5],
    ),
):
    return MOCK_RESPONSE


# -------------------------------------------------------------------
# Run locally
# -------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8080,
    )
