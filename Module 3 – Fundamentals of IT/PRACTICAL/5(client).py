import requests

response = requests.get("http://localhost:8080")
print("Status Code:", response.status_code)
print("Response Content:", response.text[:200])  # show first 200 characters


# How it works:

# Run server.py → starts a simple HTTP server at localhost:8080.
# Run client.py → sends a request to the server.
# Server responds with the content of the directory (default webpage).
# Client prints status + some content.

# This shows how HTTP communication works between a client (browser/script) and a server.