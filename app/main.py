from fastapi import FastAPI

app = FastAPI(
    title="Secure Notes Security Lab",
    description="A security-focused notes API",
    version ="0.1.0",
)

@app.get("/")

async def root():
    return {"message": "Secure Notes API is runnuing"}

@app.get("/health")
async def health():
    return {"status": "ok"}