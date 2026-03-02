from app.user_manager import add_user

def test_add_user():
    result = add_user("Hajar")
    assert result == "User Hajar added"