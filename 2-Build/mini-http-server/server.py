import socket

# Configure server connection settings
HOST = '127.0.0.1' 
PORT = 8080

def start_server():
    # Create a raw network socket (IPv4, TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"🚀 Server running locally at http://{HOST}:{PORT} ... Ctrl+C to stop.")
        
        while True:
            # Wait for an incoming browser connection
            conn, addr = s.accept()
            with conn:
                request = conn.recv(1024).decode('utf-8')
                if not request:
                    continue
                
                # Format a raw cryptographic-safe HTTP/1.1 response
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                    "<h1>🎯 Success! Your Custom Socket Server Works!</h1>"
                    "<p>This raw HTML text was served directly out of your socket.</p>"
                )
                
                # Send back response and close connection
                conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
