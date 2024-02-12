from fastapi import FastAPI, File, Form, UploadFile
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


# Define a list of allowed origins for CORS
# You can use ["*"] to allow all origins, but it's recommended to list specific origins for production
origins = [
    "http://localhost:3000",  # Assuming your React app runs on localhost:3000
]


# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that are allowed to make requests
    allow_credentials=True,  # Whether to support cookies in the requests
    # Which methods to allow, ["GET", "POST"] or ["*"] for all
    allow_methods=["*"],
    # Which headers to allow, can be specific or ["*"] for all
    allow_headers=["*"],
)


@app.post("/submit-spec")
async def submit_spec(text: str = Form(...), file: Optional[UploadFile] = File(None)):
    # Process the text
    print(f"Received text: {text}")

    # Process the file if it is not None
    if file:
        file_contents = await file.read()
        # Depending on what you want to do with the file, you might save it or process it
        # For example, to save the file, you would open a new file and write the contents
        # This is just an example to print the file size
        print(f"Received file with size: {len(file_contents)} bytes")

    # You can return a response to acknowledge the receipt
    return {"message": "Received the spec successfully", "text": text, "file": file.filename if file else "No file uploaded"}


@app.get("/test")
def test():
    return "hello"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
