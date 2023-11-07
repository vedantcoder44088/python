import matplotlib.pyplot as plt

# Sample data
teams = ['A', 'B', 'C', 'D']
scores = [3, 5, 2, 7]

# Creating a bar plot for the scoreboard
plt.figure(figsize=(8, 6))
plt.bar(teams, scores, color=['skyblue', 'salmon', 'lightgreen', 'lightcoral'])
plt.title('Sports Scoreboard', fontsize=16)
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Scores', fontsize=12)
plt.show()

