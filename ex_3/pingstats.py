import re
import statistics
import matplotlib.pyplot as plt
import json

# Read the destinations file
with open('./destinations.json', 'r') as f:
    destinations = json.load(f)


# Dictionary to store results
ping_results = {}

# Read the output files
for destination in destinations.keys():
    format = destination.replace(".", "")
    with open(f"{format}.txt", 'r') as f:
        output = f.read()
        rtt_times = re.findall(r'time=([\d.]+) ms', output)
        rtt_times = list(map(float, rtt_times))
        ping_results[destination] = rtt_times

# Get the distance data
dist_data = [d for d in destinations.values()]

# Calculate the mean RTT and jitter for each destination
rtt_data = []
jitter_data = []
for destination in destinations:
    
    # Calculate the mean RTT
    rtt = ping_results[destination]
    rtt_mean = statistics.mean(rtt)

    # Calculate the jitter
    jitter = [abs(rtt[i] - rtt[i-1]) for i in range(1, len(rtt))]
    jitter_mean = statistics.mean(jitter)
    
    # Add the results to the lists
    rtt_data.append(rtt_mean)
    jitter_data.append(jitter_mean)

# Plot the results
fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=(10, 8))
# Plot the mean RTT data
ax1.plot(dist_data, rtt_data, marker='o', color='b')
ax1.set_ylabel('Mean RTT (ms)')
# Plot the jitter data
ax2.plot(dist_data, jitter_data, marker='o', color='r')
ax2.set_xlabel('Distance (km)')
ax2.set_ylabel('Jitter (ms)')
plt.show()
