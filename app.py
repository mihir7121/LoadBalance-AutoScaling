from flask import Flask, request
import time

app = Flask(__name__)

request_counter = 0

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@app.route('/fibonacci', methods=['GET'])
def fib_endpoint():
    global request_counter 
    request_counter += 1  

    n = request.args.get('n')
    
    if n is None:
        print(f'Total requests served: {request_counter}') 
        return 'N is not provided', 204

    try:
        n = int(n)
    except ValueError:
        print(f'Total requests served: {request_counter}') 
        return 'Invalid input', 400 

    start_time = time.time()
    result = fibonacci(n)
    elapsed_time = time.time() - start_time
    print(f'Total requests served: {request_counter}') 
    return f'Fibonacci({n}) = {result}, computed in {elapsed_time:.4f} seconds from server-n\n'

@app.route('/health', methods=['GET'])
def health_check():
    return '', 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)