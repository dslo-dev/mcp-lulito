from tools.users import get_user
from tools.tasks import create_task, list_tasks


print("Usuario:")
print(
    get_user("8669568433")
)


print("\nCreando tarea:")

print(
    create_task(
        1,
        "Probar MCP Lulito",
        "Primera tarea creada desde Python"
    )
)


print("\nTareas:")

print(
    list_tasks(1)
)