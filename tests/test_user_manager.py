import pytest

from app.user_manager import UserManager


def test_add_user():
    manager = UserManager()
    manager.add_user("Adam")
    assert manager.count_users() == 1


def test_add_existing_user():
    manager = UserManager()
    manager.add_user("Adam")

    with pytest.raises(ValueError):
        manager.add_user("Adam")


def test_remove_user():
    manager = UserManager()
    manager.add_user("Yanis")
    manager.remove_user("Yanis")
    assert manager.count_users() == 0


def test_remove_unknown_user():
    manager = UserManager()

    with pytest.raises(ValueError):
        manager.remove_user("sarah")
        