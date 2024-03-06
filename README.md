# Simple Chat Application

This is a simple chat application implemented in Python using sockets. It allows multiple clients to connect to a server and chat with each other.

## Functionality

- The server listens for incoming connections from clients on a specified IPv4 address and port.
- Each client can send messages to the server, which are then broadcasted to all connected clients.
- Clients can also disconnect from the server by sending the message 'q'.

## How to Use

1. Run the server script (`Server.py`) on a machine with a publicly accessible IPv4 address.
2. Run the client script (`Client.py`) on multiple machines within the same local area network (LAN).
3. When prompted, enter your name in the client script to identify yourself.
4. Start typing messages in the client script and press Enter to send them to the server. Your messages will be broadcasted to all other connected clients.
5. To exit the client script, type 'q' and press Enter.

## Changing the IPv4 Address

If you need to change the IPv4 address of the server, follow these steps:

1. Open the `Server.py` file in your text editor.
2. Locate the `SERVER_HOST` variable at the top of the file.
3. Change the value of `SERVER_HOST` to the desired IPv4 address.
4. Save the file.

## Note

- All machines running the client script must be connected to the same local area network (LAN) as the server in order to communicate with each other.
- Make sure that the port specified in the `SERVER_PORT` variable in both the server and client scripts is not blocked by any firewall or network restrictions.
