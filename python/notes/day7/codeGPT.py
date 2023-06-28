import json
import requests
import matplotlib.pyplot as plt

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

for i in todos:
  if i["completed"]:
    try:
      todos_by_user[i["userId"]]["completed"] += 1
    except KeyError:
      todos_by_user[i["userId"]] = {"completed": 1, "non_completed": 0}
  else:
    try:
      todos_by_user[i["userId"]]["non_completed"] += 1
    except KeyError:
      todos_by_user[i["userId"]] = {"completed": 0, "non_completed": 1}

# Extract user IDs and their corresponding completed and non-completed task counts
user_ids = []
completed_counts = []
non_completed_counts = []

for user_id, counts in todos_by_user.items():
  user_ids.append(user_id)
  completed_counts.append(counts["completed"])
  non_completed_counts.append(counts["non_completed"])

# Plotting the bar graph
x = range(len(user_ids))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, completed_counts, width, label='Completed')
rects2 = ax.bar(x,
                non_completed_counts,
                width,
                label='Non-Completed',
                bottom=completed_counts)

ax.set_xlabel('User ID')
ax.set_ylabel('Task Count')
ax.set_title('Completed and Non-Completed Tasks by User')
ax.set_xticks(x)
ax.set_xticklabels(user_ids)
ax.legend()


# Add labels to the bars
def autolabel(rects):
  for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center',
                va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()
