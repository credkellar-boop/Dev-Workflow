import socket
import threading

# Configuration
LB_HOST = '127.0.0.1'
LB_PORT = 8000
BACKEND_SERVERS = [('127.0.0.1', 8081), ('127.0.0.1', 8082)]

current_server_index = 0
index_lock = threading.Lock()

def get_next_backend():
    """Selects the next backend server using Round Robin."""
    global current_server_index
    with index_lock:
        backend = BACKEND_SERVERS[current_server_index]
        current_server_index = (current_server_index + 1) % len(BACKEND_SERVERS)
        return backend

def handle_client(client_socket):
    """Forwards data between the client browser and the selected backend server."""
    backend_host, backend_port = get_next_backend()
    print(f"🔄 Routing request to backend server -> {backend_host}:{backend_port}")
    
    try:
        # Connect to the chosen backend server
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((backend_host, backend_port))
        
        # Receive request from browser and forward to backend
        client_data = client_socket.recv(4096)
        if client_data:
            backend_socket.sendall(client_data)
            
            # Receive response from backend and forward back to browser
            backend_response = backend_socket.recv(4096)
            if backend_response:
                client_socket.sendall(backend_response)
    except Exception as e:
        print(f"❌ Error communicating with backend: {e}")
    finally:
        client_socket.close()
        backend_socket.close()

def start_load_balancer():
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    lb_socket.bind((LB_HOST, LB_PORT))
    lb_socket.listen()
    print(f"⚖️ Load Balancer live at http://{LB_HOST}:{LB_PORT}")
    
    while True:
        client_socket, addr = lb_socket.accept()
        # Handle each request in a separate thread to support concurrent traffic
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_load_balancer()
