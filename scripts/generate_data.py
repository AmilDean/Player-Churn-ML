import pandas as pd
import numpy as np


# Set seed
np.random.seed(42)

# 5000 rows
n = 5000  

# Create the synthetic data columns & data
data = {
    "player_id": np.arange(1, n+1),
    "total_playtime_hours": np.random.randint(0, 500, n),
    "sessions_last_30d": np.random.randint(0, 60, n),
    "sessions_last_7d": np.random.randint(0, 20, n),
    "purchases_count": np.random.randint(0, 10, n),
    "max_level": np.random.randint(1, 100, n),
    "friends_count": np.random.randint(0, 50, n),
}

# Convert dictionary into a dataframe
df = pd.DataFrame(data)

# Churn logic (recenly inactive / low playtime)
df["churned"] = (
    ((df["sessions_last_30d"] < 5) &
    (df["total_playtime_hours"] < 50)) | (df["sessions_last_7d"] == 0)
).astype(int)

df.to_csv("player_churn_data.csv", index=False)

print(df.head())
print("Dataset saved as player_churn_data.csv")
