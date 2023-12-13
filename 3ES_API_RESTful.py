# Prueba a hacer una aplicación web Flask que implemente una API básica para administrar tareas. 
# La API debe permitir realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una lista de tareas.

from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task" : "Buy Milk"},
    {"id": 2, "task" : "Workout"},
]

# Ruta para obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Ruta para agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify({'message': 'Task added successfully'})

# Ruta para actualizar una tarea por ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message' : 'Unable to find task'}, 404)

# Ruta para eliminar una tarea por ID
@app.route('/tasks/<int:tarea_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message' : 'Task deleted successfully'})
    return jsonify({'message' : 'Unable to find task'}, 404)

if __name__ == '__main__':
    app.run(debug=True)