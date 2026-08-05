from dataclasses import dataclass


@dataclass
class User:
    id: int
    external_id: str
    name: str
    nickname: str | None
    city: str | None
    occupation: str | None


@dataclass
class Task:
    id: int
    user_id: int
    title: str
    description: str | None
    status: str
    priority: str