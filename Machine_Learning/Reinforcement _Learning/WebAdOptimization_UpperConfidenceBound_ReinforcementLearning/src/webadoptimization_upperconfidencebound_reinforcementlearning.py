# **Web Ad Optimization using Upper Confidence Bound (UCB) Algorithm in Reinforcement Learning**

### Importing the basic libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import io

# Uploading the dataset (dataset.csv should be in your local machine)
# Note: In a local environment, you can directly read the CSV file using pd.read_csv('dataset.csv')
# In Google Colab, you need to upload the file first using the following code:

# from google.colab import files
# uploaded = files.upload()

"""### Importing the dataset"""

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

"""# *BASIC INFO*"""

observations = dataset.shape[0]   # number of users
no_of_ads = dataset.shape[1]      # number of ads

"""# *RANDOM STRATEGY (BASELINE)*"""

random_total_reward = 0

for n in range(observations):
    ad = random.randrange(no_of_ads)
    reward = dataset.values[n, ad]
    random_total_reward += reward

print("\nTotal Reward (Random Strategy):", random_total_reward)

"""# *Upper Confidence Bound algorithm*"""

ads_selected = []
ad_counts = [0] * no_of_ads
ad_rewards = [0] * no_of_ads
total_reward = 0

for n in range(observations):
    ad = 0
    max_upper_bound = 0

    for i in range(no_of_ads):
        if ad_counts[i] > 0:
            average_reward = ad_rewards[i] / ad_counts[i]
            delta_i = math.sqrt((3/2) * math.log(n + 1) / ad_counts[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = float('inf')  # ensures each ad is selected at least once

        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i

    # Store selected ad
    ads_selected.append(ad)

    # Update counts and rewards
    ad_counts[ad] += 1
    reward = dataset.values[n, ad]
    ad_rewards[ad] += reward
    total_reward += reward

"""# *RESULTS*"""

ctr = total_reward / observations
best_ad = ad_rewards.index(max(ad_rewards))

print("\n===== FINAL RESULTS =====")
print("Total Reward (UCB):", total_reward)
print("Total Reward (Random):", random_total_reward)
print("Improvement over Random: {:.2f}%".format(
    (total_reward - random_total_reward) / random_total_reward * 100
))
print("Click Through Rate (CTR):", ctr)
print("Best Performing Ad Index:", best_ad)
print("Rewards per Ad:", ad_rewards)

"""### Visualizing Result"""

plt.bar(range(no_of_ads), ad_counts)
plt.title('Ad Selection Distribution (UCB)')
plt.xlabel('Ad Index')
plt.ylabel('Number of Times Selected')
plt.show()