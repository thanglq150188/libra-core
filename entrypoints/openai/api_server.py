from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
import json
from libra.models.model_factory import ModelFactory
from libra.types.typing import ModelLabel
from typing import Dict, Any

app = FastAPI()

async def stream_response(data: Dict[str, Any]):
    messages = data.get("messages", [])
    # Extract other parameters as needed
    temperature = data.get("temperature", 0.0)
    model_label = data.get("model_label", ModelLabel.AZURE_GPT_4o)
    
    # Create model with dynamic parameters
    model = ModelFactory.create(
        model_label=model_label,
        model_config_dict={
            "temperature": temperature
        },
    )
    
    response = model.stream(messages=messages)
    for chunk in response:
        chunk_delta = json.loads(chunk)['choices'][0]['delta']
        if 'content' in chunk_delta:
            yield f"data: {chunk}\n\n"

@app.post("/chat/completions")
async def stream_model_response(request: Request):
    data = await request.json()
    return StreamingResponse(stream_response(data), media_type="text/event-stream")


if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)