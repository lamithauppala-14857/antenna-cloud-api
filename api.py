from fastapi import FastAPI
import os

app = FastAPI(title="Antenna Cloud API")

# Root route to prevent 404
@app.get("/")
def root():
    return {"status": "API is live!"}

# Example endpoint
@app.get("/hello")
def hello():
    return {"message": "Hello World"}

# Add more endpoints below as needed
# @app.get("/another-endpoint")
# def another():
#     return {"data": "This is another endpoint"}

# Run with uvicorn when executed directly
if __name__ == "__main__":
    import uvicorn
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=True)

