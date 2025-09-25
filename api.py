from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Antenna Cloud JSON API")

# Define input data model
class AntennaData(BaseModel):
    frequency: List[float]
    amplitude: List[float]

# Create route to process JSON input
@app.post("/process_json")
async def process_json(data: AntennaData):
    if len(data.frequency) != len(data.amplitude):
        return {"error": "Frequency and amplitude lists must have the same length."}
    
    # Example calculations
    avg_amplitude = sum(data.amplitude) / len(data.amplitude)
    max_amplitude = max(data.amplitude)
    min_amplitude = min(data.amplitude)

    return {
        "message": "Data processed successfully",
        "average_amplitude": avg_amplitude,
        "max_amplitude": max_amplitude,
        "min_amplitude": min_amplitude,
        "frequency": data.frequency,
        "amplitude": data.amplitude
    }

