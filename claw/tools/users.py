from database import get_connection


def get_user(external_id: str):

    connection = get_connection()

    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE external_id = ?
        """,
        (external_id,)
    ).fetchone()

    connection.close()


    if not user:
        return {
            "error": "Usuario no encontrado"
        }


    return dict(user)