from database import get_connection


def create_task(
    user_id: int,
    title: str,
    description: str | None = None
):

    connection = get_connection()


    user = connection.execute(
        """
        SELECT id
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()


    if not user:
        connection.close()

        return {
            "error": "Usuario inválido"
        }


    connection.execute(
        """
        INSERT INTO tasks(
            user_id,
            title,
            description
        )
        VALUES(?,?,?)
        """,
        (
            user_id,
            title,
            description
        )
    )


    connection.commit()
    connection.close()


    return {
        "success": True,
        "message": "Tarea creada"
    }



def list_tasks(user_id: int):

    connection = get_connection()

    tasks = connection.execute(
        """
        SELECT *
        FROM tasks
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchall()


    connection.close()


    return [
        dict(task)
        for task in tasks
    ]