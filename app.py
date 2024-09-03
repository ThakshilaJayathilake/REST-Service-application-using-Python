from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tasks = []

class Task(Resource):
# Get a Task
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        return task

# Create a Task
    def post(self):
        data = request.get_json()
        task_id = len(tasks) + 1
        task = {'id': task_id, 'title': data['title'], 'description': data['description']}
        tasks.append(task)
        return task, 201

# Update a Task
    def put(self, task_id):
        data = request.get_json()
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        task.update(data)
        return task

# Delete a Task
    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return {'message': 'Task deleted'}

api.add_resource(Task, '/task', '/task/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
