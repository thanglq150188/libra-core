import asyncio
import time
from dotenv import load_dotenv
from libra.embeddings import OpenAIEmbedding  # Assuming the class is in a file named openai_embedding.py

async def async_embed_task(embedding, text):
    return await embedding.async_embed([text])

async def run_async_test(embedding, texts, num_users):
    start_time = time.time()
    tasks = [async_embed_task(embedding, text) for text in texts[:num_users]]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time

def run_sync_test(embedding, texts, num_users):
    start_time = time.time()
    for text in texts[:num_users]:
        embedding.embed_list([text])
    end_time = time.time()
    return end_time - start_time

async def main():
    load_dotenv()
    
    embedding = OpenAIEmbedding()
    num_users = 100
    
    # Generate 100 similar but slightly different texts
    base_text = "Cuộc sống có nhiều điều thú vị và ý nghĩa."
    texts = [f"{base_text} Đây là câu số {i+1}." for i in range(num_users)]
    
    print(f"Running tests with {num_users} concurrent users...")
    
    # Run synchronous test
    sync_time = run_sync_test(embedding, texts, num_users)
    print(f"Synchronous execution time: {sync_time:.2f} seconds")
    
    # Run asynchronous test
    async_time = await run_async_test(embedding, texts, num_users)
    print(f"Asynchronous execution time: {async_time:.2f} seconds")
    
    # Calculate and print the speedup
    speedup = sync_time / async_time
    print(f"Speedup: {speedup:.2f}x")

if __name__ == "__main__":
    asyncio.run(main())