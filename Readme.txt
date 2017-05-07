To start the server for the CLI version of the game. Note: socketServer.py listens on port 5555
python socketServer.py

To start the client for the CLI version of the game. Note: serverIP should be the IP address socketServer.py is running on. If server and client are on the same machine, use "localhost"
python telnetClient.py serverIP 5555

To start the server for the GUI version of the game 
python gameServer.py

To start the client for the GUI version of the game 
python gameClient.py serverIP 5555

GameBoard Legends:

Characters:
M - Colonel Mustard
s - Miss Scarle
P - Professor Plum
G - Mr. Green
W - Mrs. White
B - Mrs. Peacock

Weapons:
R - Rope
L - Lead Pipe
K - Knife
H - Wrench
C - Candlestick
V - Revolver
