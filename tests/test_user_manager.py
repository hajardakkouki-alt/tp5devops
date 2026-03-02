from app.user_manager import add_user

def test_add_user():
    assert add_user("Hajar") == "User Hajar added"