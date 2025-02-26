from fastapi import FastAPI, UploadFile, File
from chain import summarize

app = FastAPI()

@app.get("/")
async def root():
    print("Hello World")
    
@app.post("/summarize")
async def summarize_text(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        return {"error": "Invalid file type"}
    content = await file.read()
    
    text = content.decode("utf-8")
    summary = summarize(text)
    return {"Summary": summary}