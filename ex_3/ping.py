import subprocess
import json

# Read the destinations file
with open('./destinations.json', 'r') as f:
    destinations = json.load(f)

# Number of packets to send
packets = 20

for destination in destinations.keys():
    format = destination.replace(".", "")
    output_file = f"{format}.txt"

    # Create the ping command
    ping_cmd = ["ping", "-c", str(packets), destination]

    # Open the output file 
    with open(output_file, "w") as f:
        # Run the ping command and write the output to the file
        subprocess.run(ping_cmd, stdout=f)
