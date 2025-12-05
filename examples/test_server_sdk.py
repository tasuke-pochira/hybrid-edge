from hybrid_edge import HybridServer

# 1. Define Secrets (or load them from .env automatically)
# You can pass them explicitly if you want to override .env
server = HybridServer(
    secret_key="my-super-secret-password",
    port=5000
)

# 2. Go Global
print("Starting my custom AI Node...")
server.start()