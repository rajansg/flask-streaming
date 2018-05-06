from pythonosc import osc_message_builder
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 8000)

while(True):
	client.send_message("filter", "hello")
	print("sent hello")
