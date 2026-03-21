from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from FastAPI2"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dvirus")
def health():
    return {"status": "ok here is the dvirus endpoint"}



@app.get("/welcome")
def health():
    return {"status": "welocme webhook2"}




@app.get("/waf")
def health():
    return {"status": "welocme waf"}