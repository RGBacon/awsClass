import json
import requests

###########################################
#Example
###########################################
response =requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# map of userUD to number of complete TODOs per user
todos_by_user = {}

for i in todos:
  if i["completed"]:
    try:
      todos_by_user[i["userId"]] +=1
    except KeyError:
      todos_by_user[i["userId"]] = 1

top_users = sorted(todos_by_user.items(),key=lambda x: x[1], reverse=True)

max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
  if num_complete < max_complete:
    break
  users.append(str(user))
  
max_users = " and ".join(users)

def keep(todo):
  is_complete = todo["completed"]
  has_max_count = str(todo["userId"]) in users
  return is_complete and has_max_count

with open("filtered_data.json", "w") as data_file:
  filtered_todos = list(filter(keep, todos))
  json.dump(filtered_todos, data_file, indent=2)