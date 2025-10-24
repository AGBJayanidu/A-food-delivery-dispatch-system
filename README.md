# Food Delivery Dispatch System Simulation

## Overview

This project simulates a **food delivery dispatch system** where customer orders are assigned to a limited number of delivery riders. The simulation tracks key performance metrics, such as average waiting time, total completed deliveries, orders that had to wait, and maximum queue length. It allows experimentation with different numbers of riders to analyze system performance under varying resource configurations.

## Features

- Configurable number of delivery riders.
- Random order arrivals and variable delivery times.
- FIFO order queue management when all riders are busy.
- Records key metrics: average waiting time, total deliveries, maximum waiting time, orders that waited, and maximum queue length.
- Generates bar charts to visualize performance metrics for each scenario.

## Requirements

- Python 3.7 or higher
- Packages:
  - `matplotlib` (for generating charts)
  - `os` (standard Python library for file operations)

Install `matplotlib` via pip:

```bash
pip install matplotlib
```

## File Structure

```
simulation_charts/                 # Folder where generated charts will be saved
food_delivery_simulation.py        # Python script containing the simulation code
README.md                          # This file
```

## Usage Instructions

1. **Run the Simulation**  
   Execute the Python script:

   ```bash
   python food_delivery_simulation.py
   ```

2. **Adjust Simulation Parameters (Optional)**  
   Inside `food_delivery_simulation.py`, you can modify parameters such as:

   ```python
   SIMULATION_TIME = 60       # Total simulation duration in minutes
   ORDER_ARRIVAL_RATE = 5     # Average time (minutes) between order arrivals
   DELIVERY_TIME_MIN = 8      # Minimum delivery duration in minutes
   DELIVERY_TIME_MAX = 12     # Maximum delivery duration in minutes
   rider_counts = [3, 5, 8]   # Number of riders to simulate
   ```

3. **View Simulation Results**  
   After execution, the console will display a summary for each rider configuration:

   ```
   --- Simulation Summary ---
   Number of riders: X
   Total deliveries completed: Y
   Average waiting time: Z minutes
   Maximum waiting time: W minutes
   Orders that had to wait: V
   Maximum queue length: U
   ```

4. **View Charts**  
   The simulation automatically generates three bar charts in the `simulation_charts` folder:
   - `average_waiting_time.png`
   - `completed_orders.png`
   - `max_queue_length.png`

## Example Output

**Console Output (Sample):**

```
--- Simulation Summary ---
Number of riders: 3
Total deliveries completed: 14
Average waiting time: 0.79 minutes
Maximum waiting time: 5 minutes
Orders that had to wait: 4
Maximum queue length: 2
```

**Generated Charts:**  
Bar charts showing average waiting time, completed orders, and maximum queue length for different rider configurations.

## Notes

- The simulation uses **randomized order arrivals and delivery times**, so results may vary slightly on each run.
- To get more consistent results, you can run multiple iterations and average the metrics.
- The system is **time-based and event-driven**, modeling realistic rider availability and queue behavior.
