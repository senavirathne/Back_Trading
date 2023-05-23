import parameters
from websocketclient import WebSocketClient

client = WebSocketClient(parameters.url, parameters.headers, parameters.output_file)
try:
    client.run()
except Exception as e:
    client.write_to_file()
    print("WebSocket connection closed: " + str(e))
