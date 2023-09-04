import pytest
from account.models import Account


@pytest.fixture
def user_creation():
    return Account.objects.create_user(
        username = 'sqwedqwd',
        email = 'qwqwdq@gmail.com',
        password = '12345',
    )

@pytest.mark.django_db
def test_user_creation(user_creation):
    user_creation.save()
    assert user_creation.username == 'sqwedqwd'

@pytest.mark.django_db
def test_superuser_creation():
    user = Account.objects.create_superuser(
        username = 'sqwedqwd',
        email = 'qwqwdq@gmail.com',
        password = '12345',
    )
    assert user.is_superuser

@pytest.mark.django_db
def test_staff_superuser_creation():
    user = Account.objects.create_superuser(
        username = 'sqwedqwd',
        email = 'qwqwdq@gmail.com',
        password = '12345',
    ) 
    assert user.is_staff

@pytest.mark.django_db
def test_user_creation_fail():
    with pytest.raises(Exception):
        Account.objects.create_user(
            password='12345',
            is_staff=False
        )




