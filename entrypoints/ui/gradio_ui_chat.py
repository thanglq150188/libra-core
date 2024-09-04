import gradio as gr
from libra.agents.async_libra_agent import AsyncLibraAgent
from libra.response import streams as st
import asyncio

chat_agent = AsyncLibraAgent()

async def chatbot(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response_generator = chat_agent.astep(messages=history_openai_format)
    
    full_response = ""
    async for chunk in response_generator:
        if st.is_valid(chunk):
            chunk_text = st.content_of(chunk)
            full_response += chunk_text
            yield full_response

iface = gr.ChatInterface(
    chatbot,
    chatbot=gr.Chatbot(height="70vh"),
    textbox=gr.Textbox(placeholder="Ask something about MB Bank...", container=False, scale=7),
    title="MB Bank ChatBot",
    description="Ask questions about MB Bank and get answers!",
    theme="soft",
    examples=[
        "MB có công ty con không?",
        "Các dịch vụ ngân hàng MB cung cấp là gì?",
        "MB Bank được thành lập năm nào?",
    ],
    cache_examples=False,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
    concurrency_limit=10
)

if __name__ == "__main__":
    iface.launch(share=True)