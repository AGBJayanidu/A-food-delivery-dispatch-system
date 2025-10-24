import random
import matplotlib.pyplot as plt
import os

# Create a folder to save charts
output_folder = "simulation_charts"
os.makedirs(output_folder, exist_ok=True)

# Simulation Settings
SIMULATION_TIME = 60       # total simulation time in minutes
ORDER_ARRIVAL_RATE = 5     # new order every 5 minutes (on average)
DELIVERY_TIME_MIN = 8      # delivery duration min
DELIVERY_TIME_MAX = 12     # delivery duration max

def run_simulation(num_riders):
    time_now = 0
    order_queue = []
    riders = [0] * num_riders
    completed_orders = 0
    total_waiting_time = 0
    max_queue_length = 0
    calls_that_waited = 0
    max_wait_time = 0

    while time_now < SIMULATION_TIME:
        # New order arrival
        if random.randint(1, ORDER_ARRIVAL_RATE) == 1:
            order_queue.append(time_now)

        max_queue_length = max(max_queue_length, len(order_queue))

        # Assign orders to free riders
        for i in range(num_riders):
            if riders[i] <= time_now and len(order_queue) > 0:
                order_time = order_queue.pop(0)
                waiting_time = time_now - order_time
                total_waiting_time += waiting_time
                if waiting_time > 0:
                    calls_that_waited += 1
                max_wait_time = max(max_wait_time, waiting_time)
                delivery_duration = random.randint(DELIVERY_TIME_MIN, DELIVERY_TIME_MAX)
                riders[i] = time_now + delivery_duration
                completed_orders += 1

        time_now += 1

    avg_wait = total_waiting_time / completed_orders if completed_orders > 0 else 0
    return {
        "num_riders": num_riders,
        "completed_orders": completed_orders,
        "avg_wait": avg_wait,
        "max_wait": max_wait_time,
        "calls_waited": calls_that_waited,
        "max_queue": max_queue_length
    }

# ----------------------------
# Run Experiments with Different Numbers of Riders
# ----------------------------
rider_counts = [3, 5, 8]
results = []

for riders in rider_counts:
    summary = run_simulation(riders)
    results.append(summary)
    print("\n--- Simulation Summary ---")
    print(f"Number of riders: {summary['num_riders']}")
    print(f"Total deliveries completed: {summary['completed_orders']}")
    print(f"Average waiting time: {summary['avg_wait']:.2f} minutes")
    print(f"Maximum waiting time: {summary['max_wait']} minutes")
    print(f"Orders that had to wait: {summary['calls_waited']}")
    print(f"Maximum queue length: {summary['max_queue']}")

# ----------------------------
# Prepare Data for Charts
# ----------------------------
labels = [f"{r} Riders" for r in rider_counts]
avg_waits = [r["avg_wait"] for r in results]
completed_orders = [r["completed_orders"] for r in results]
max_queues = [r["max_queue"] for r in results]

# ----------------------------
# Save Average Waiting Time Chart
plt.figure(figsize=(6,5))
plt.bar(labels, avg_waits, color='#6A0DAD')
plt.title("Average Waiting Time")
plt.ylabel("Minutes")
plt.savefig(os.path.join(output_folder, "average_waiting_time.png"))
plt.close()

# ----------------------------
# Save Completed Orders Chart
plt.figure(figsize=(6,5))
plt.bar(labels, completed_orders, color='#FF8C00')
plt.title("Completed Orders")
plt.ylabel("Orders")
plt.savefig(os.path.join(output_folder, "completed_orders.png"))
plt.close()

# ----------------------------
# Save Maximum Queue Length Chart
plt.figure(figsize=(6,5))
plt.bar(labels, max_queues, color='#B22222')
plt.title("Maximum Queue Length")
plt.ylabel("Orders Waiting")
plt.savefig(os.path.join(output_folder, "max_queue_length.png"))
plt.close()

print(f"\nAll charts saved in folder: {output_folder}")
