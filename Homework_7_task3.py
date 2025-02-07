import pytest

class UserManager:
    """Класс для управления пользователями."""

    def __init__(self):
        self.users = {}

    def add_user(self, name: str, age: int):
        """Добавляет пользователя."""
        self.users[name] = age

    def remove_user(self, name: str):
        """Удаляет пользователя."""
        self.users.pop(name, None)

    def get_all_users(self):
        """Возвращает список всех пользователей."""
        return list(self.users.keys())

@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um

def test_add_user(user_manager):
    user_manager.add_user("Charlie", 40)
    assert "Charlie" in user_manager.get_all_users()

def test_remove_user(user_manager):
    user_manager.remove_user("Alice")
    assert "Alice" not in user_manager.get_all_users()

@pytest.mark.skipif(len(user_manager().get_all_users()) < 3, reason="Недостаточно пользователей")
def test_skip_if_less_than_three(user_manager):
    assert len(user_manager.get_all_users()) >= 3
