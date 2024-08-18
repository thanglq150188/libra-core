from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import json
from libra.models.model_factory import ModelFactory
from libra.types.enums import ModelLabel
from typing import Dict, Any
from libra.config import ChatGPTConfig
from libra.functions.retrieval_functions import job_retriever


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

async def stream_response(data: Dict[str, Any]):
    messages = data.get("messages", [])
    stream = data.get("stream", True)
    
    # Create model with dynamic parameters
    model = ModelFactory.create(
        model_label=ModelLabel.GPT_4o,
        model_config_dict=ChatGPTConfig(stream=stream, temperature=0.0).__dict__,
    )
    
    response = model.run(messages=messages)
    if model.stream:
        for chunk in response: # type: ignore                        
            yield f"data: {chunk.json()}\n\n"
    else:
        yield f"data: {response.json()}\n\n" # type: ignore
    
    yield "data: [DONE]\n\n"
        
        
@app.post("/chat/completions")
async def stream_model_response(request: Request):
    data = await request.json()
    return StreamingResponse(stream_response(data), media_type="text/event-stream")


@app.post("/search_jobs")
async def search_jobs(request: Request):
    data = await request.json()
    query = data['query']
    top_k = int(data['top_k'])
    results = job_retriever.query(
        query=query,
        top_k=top_k
    )
    return JSONResponse(content=results)


if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    import uvicorn
    import os
    
    uvicorn.run(app, host=os.environ['HOST'], port=int(os.environ['PORT']))