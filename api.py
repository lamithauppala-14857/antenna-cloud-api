from fastapi import FastAPI, Query
import pandas as pd
import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse

app = FastAPI(title="Antenna Cloud API")

# Load CSV once when the app starts
df = pd.read_csv("data.csv")  # make sure your CSV is in the project folder

@app.get("/")
def root():
    return {"status": "API is live!"}

@app.get("/plot")
def plot_graph(frequency: float = Query(..., description="Frequency to plot")):
    # Filter CSV data based on frequency column
    filtered = df[df["Frequency"] == frequency]  # adjust column name

    # Generate graph
    plt.figure()
    plt.plot(filtered["X"], filtered["Y"])  # replace X, Y with your actual columns
    plt.title(f"Graph for frequency {frequency}")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Save graph to bytes
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    # Return image as response
    return StreamingResponse(buf, media_type="image/png")


