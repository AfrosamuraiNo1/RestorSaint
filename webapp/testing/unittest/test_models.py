from webapp.user.models import User


def test_new_user():
    user = User(username='patkennedy',  password_plaintext='FlaskIsAwesome',
                role='user', email='patkennedy79@gmail.com')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.set_password != 'FlaskIsAwesome'
    assert user.role == 'user'


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly

    УЧИТЫВАЯ пользовательскую модель
    КОГДА создается новый пользователь
    ЗАТЕМ проверьте, правильно ли определены поля email, password_hashed, authenticated и active
    """
    user = User(username='patkennedy', password_plaintext='FlaskIsAwesome',
                role='user', email='patkennedy79@gmail.com')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.password_hashed != 'FlaskIsAwesome'
    assert user.__repr__() == '<User patkennedy>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly

    УЧИТЫВАЯ пользовательскую модель
    КОГДА создается новый пользователь
    ЗАТЕМ проверьте, правильно ли определены поля email и password_hashed
    """
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password_hashed != 'FlaskIsAwesome'


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext

    УЧИТЫВАЯ существующего пользователя
    КОГДА пароль для пользователя установлен
    ЗАТЕМ проверьте, что пароль сохранен правильно, а не в виде обычного текста
    """
    new_user.set_password('MyNewPassword')
    assert new_user.password_hashed != 'MyNewPassword'
    assert new_user.is_password_correct('MyNewPassword')
    assert not new_user.is_password_correct('MyNewPassword2')
    assert not new_user.is_password_correct('FlaskIsAwesome')


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    УЧИТЫВАЯ существующего пользователя
    КОГДА идентификатор пользователя определен в значение
    ЗАТЕМ проверьте, что идентификатор пользователя возвращает строку (а не целое число), как это необходимо Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'
