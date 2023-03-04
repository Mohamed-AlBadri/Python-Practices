import subprocess

# prompt the user to input the server address to ping
server_address = input("Enter the IP address to ping: ")

# ping the server using the subprocess module
response = subprocess.run(['ping', '-c', '1', server_address], stdout=subprocess.PIPE)

# check the response status code to see if the server is online
if response.returncode == 0:
    print(f"{server_address} is online")
else:
    print(f"{server_address} is offline")

