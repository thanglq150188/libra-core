import requests
import threading
import time
import random
import json
from typing import Dict, Generator
from queue import Queue

BASE_URL = "http://localhost:8000"  # Replace with your actual API URL

samples = [
    "xin chào",
    # "kiếm cho vài jobs lập trình ok ở HN đi"
]

def chat_completion() -> Generator[Dict, None, None]:
    payload = {
        "messages": [
            {"role": "user", "content": random.choice(samples)}
        ]
    }
    print(payload)
    response = requests.post(f"{BASE_URL}/chat/completions", json=payload, stream=True)
    for line in response.iter_lines():
        if line.startswith(b'data: '):
            data = line[6:]  # Remove 'data: ' prefix
            if data.strip() == b'[DONE]':
                break
            try:
                yield json.loads(data)
            except json.JSONDecodeError:
                print(f"Failed to decode JSON: {data}")

def simulate_user(user_id: int, results: Queue):
    start_time = time.time()
    full_response = ""
    first_response_time = None
    
    for chunk in chat_completion():
        current_time = time.time()
        if first_response_time is None:
            first_response_time = current_time
            time_to_first_response = first_response_time - start_time
            print(f"User {user_id} received first response in {time_to_first_response:.2f}s")
        
        full_response += str(chunk['choices'][0]['delta']['content'])
        print(f'{user_id}: {full_response}')
    
    end_time = time.time()
    
    results.put({
        "user_id": user_id,
        "total_time": end_time - start_time,
        "time_to_first_response": time_to_first_response,
        "response_length": len(full_response)
    })

def main():
    threads = []
    results = Queue()

    num_users = 1
    print(f"Starting load test with {num_users} CCU on streaming chat/completions...")

    for i in range(num_users):
        thread = threading.Thread(target=simulate_user, args=(i, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_time = 0
    total_first_response_time = 0
    total_length = 0

    while not results.empty():
        result = results.get()
        print(f"User {result['user_id']} chat completion: "
              f"Total Time: {result['total_time']:.2f}s, "
              f"Time to First Response: {result['time_to_first_response']:.2f}s, "
              f"Response length: {result['response_length']} chars")
        
        total_time += result['total_time']
        total_first_response_time += result['time_to_first_response'] if result['time_to_first_response'] else 0
        total_length += result['response_length']

    avg_time = total_time / num_users
    avg_first_response_time = total_first_response_time / num_users
    avg_length = total_length / num_users

    print(f"\nAverage total time: {avg_time:.2f}s")
    print(f"Average time to first response: {avg_first_response_time:.2f}s")
    print(f"Average response length: {avg_length:.2f} chars")

if __name__ == "__main__":
    main()