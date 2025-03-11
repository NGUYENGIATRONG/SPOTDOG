import numpy as np
import matplotlib.pyplot as plt

# Load data from .npy files
FLH = np.load('joint_angle_1.npy')  # Front Left Hip
FLK = np.load('joint_angle_2.npy')  # Front Left Knee
FRH = np.load('joint_angle_3.npy')  # Front Right Hip
FRK = np.load('joint_angle_4.npy')  # Front Right Knee
BLH = np.load('joint_angle_5.npy')  # Back Left Hip
BLK = np.load('joint_angle_6.npy')  # Back Left Knee
BRH = np.load('joint_angle_7.npy')  # Back Right Hip
BRK = np.load('joint_angle_8.npy')  # Back Right Knee

# Create a sequence for time steps
steps = range(len(FLH))

# Create a figure with 8 subplots
fig, axs = plt.subplots(8, 1, figsize=(10, 12), sharex=True)

# Plot each joint angle in its own subplot
axs[0].plot(steps, FLH, label='FLH (Front Left Hip)', color='blue')
axs[0].set_ylabel('Angle (°)')
axs[0].legend(loc='upper right')
axs[0].grid(True)

axs[1].plot(steps, FLK, label='FLK (Front Left Knee)', color='cyan')
axs[1].set_ylabel('Angle (°)')
axs[1].legend(loc='upper right')
axs[1].grid(True)

axs[2].plot(steps, FRH, label='FRH (Front Right Hip)', color='orange')
axs[2].set_ylabel('Angle (°)')
axs[2].legend(loc='upper right')
axs[2].grid(True)

axs[3].plot(steps, FRK, label='FRK (Front Right Knee)', color='red')
axs[3].set_ylabel('Angle (°)')
axs[3].legend(loc='upper right')
axs[3].grid(True)

axs[4].plot(steps, BLH, label='BLH (Back Left Hip)', color='green')
axs[4].set_ylabel('Angle (°)')
axs[4].legend(loc='upper right')
axs[4].grid(True)

axs[5].plot(steps, BLK, label='BLK (Back Left Knee)', color='lime')
axs[5].set_ylabel('Angle (°)')
axs[5].legend(loc='upper right')
axs[5].grid(True)

axs[6].plot(steps, BRH, label='BRH (Back Right Hip)', color='purple')
axs[6].set_ylabel('Angle (°)')
axs[6].legend(loc='upper right')
axs[6].grid(True)

axs[7].plot(steps, BRK, label='BRK (Back Right Knee)', color='magenta')
axs[7].set_ylabel('Angle (°)')
axs[7].set_xlabel('Time Steps')
axs[7].legend(loc='upper right')
axs[7].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
