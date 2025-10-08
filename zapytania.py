import requests as req

ENDPOINT = "https://todo.pixegami.io/"

request_body = """

{
  "content": "umyj naczynia",
  "user_id": "string",
  "task_id": "string",
  "is_done": false
} """

response = req.put(f"{ENDPOINT}/create-task", request_body)
print(response.status_code)
print(response.json())





