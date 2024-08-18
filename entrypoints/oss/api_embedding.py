from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
from dotenv import load_dotenv

from libra.embeddings import SentenceTransformerEncoder

load_dotenv()

app = FastAPI()

# Initialize the SentenceTransformerEncoder
encoder = SentenceTransformerEncoder()

class EmbedRequest(BaseModel):
    texts: List[str]

@app.get("/output_dim")
async def get_output_dim():
    return {"output_dim": encoder.get_output_dim()}

@app.post("/embed")
async def embed_texts(request: EmbedRequest):
    if not request.texts:
        raise HTTPException(status_code=400, detail="Input text list is empty")
    
    # Run the embedding in a separate thread to avoid blocking
    loop = asyncio.get_event_loop()
    embeddings = await loop.run_in_executor(None, encoder.embed_list, request.texts)
    
    return {"embeddings": embeddings}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)