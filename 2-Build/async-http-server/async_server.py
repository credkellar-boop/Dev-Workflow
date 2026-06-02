import asyncio

HOST = '127.0.0.1'
PORT = 8085

async def handle_client(reader, writer):
    """Handles an incoming browser connection within the single-threaded event loop."""
    try:
        # Read the incoming HTTP request bytes asynchronously
        request_data = await reader.read(4096)
        request_text = request_data.decode('utf-8')
        
        if not request_text:
            return

        # Parse the first line of the HTTP request headers
        first_line = request_text.split('\n')[0]
        print(f"📥 Received Request: {first_line}")

        # Simulate a non-blocking network or database delay (e.g., fetching user data)
        # This tells the event loop: "Go handle other requests while I wait!"
        await asyncio.sleep(0.5)

        # Construct a valid standard HTTP/1.1 response payload
        html_content = "<html><body><h1>⚡ Single-Threaded Async Server</h1></body></html>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(html_content)}\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{html_content}"
        )

        # Write response and flush the buffer asynchronously
        writer.write(response.encode('utf-8'))
        await writer.drain()
        
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    finally:
        # Cleanly close the client network socket stream channel
        writer.close()
        await writer.wait_closed()

async def main():
    # Spin up the high-performance async socket server wrapper
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f"⚡ Async HTTP Server spinning on http://{HOST}:{PORT}")

    # Keep the event loop open and executing indefinitely
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    # Initialize and boot the application root Event Loop
    asyncio.run(main())
