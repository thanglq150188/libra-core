from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
import json
from libra.models.model_factory import ModelFactory
from libra.types.enums import ModelLabel
from typing import Dict, Any
from libra.config import ChatGPTConfig

app = FastAPI()

async def stream_response(data: Dict[str, Any]):
    messages = data.get("messages", [])
    stream = data.get("stream", True)
    
    # Create model with dynamic parameters
    model = ModelFactory.create(
        model_label=ModelLabel.AZURE_GPT_4o,
        model_config_dict=ChatGPTConfig(stream=stream).__dict__,
    )
    
    response = model.run(messages=messages)
    if model.stream:
        for chunk in response: # type: ignore
            yield f"data: {chunk.json()}\n\n"
    else:
        yield f"data: {response.json()}\n\n" # type: ignore

@app.post("/chat/completions")
async def stream_model_response(request: Request):
    data = await request.json()
    return StreamingResponse(stream_response(data), media_type="text/event-stream")


if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)