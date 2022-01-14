import pytest
import random


def test_check_return_value_for_name_property(john_american):
    assert john_american.name == "John"


def test_check_return_value_for_age_property(john_british):
    assert john_british.age == 23


def test_check_return_value_for_gender_property(john_american):
    assert john_american.gender == "male"


def test_check_return_value_for_nationality(mia_japan):
    assert mia_japan.nationality.name == 'Japan'


def test_check_return_value_for_nationality_negative(john_american):
    assert john_american.nationality.name != 'Japan'


def test_check_raise_exception_for_validate_method(john_american):
    method = getattr(
        john_american, 
        f"_{john_american.__class__.__name__}__validate_gender"
    )
    with pytest.raises(Exception):
        method("test")


def test_check_method_validate_male(john_american):
    method = getattr(
        john_american,
        f"_{john_american.__class__.__name__}__validate_gender"
    )
    assert method('male') == 'male'


def test_check_method_validate_female(mia_japan):
    method = getattr(
        mia_japan,
        f"_{mia_japan.__class__.__name__}__validate_gender"
    )
    assert method('female') == 'female'


def test_check_raise_exception_for_change_gender(mia_japan):
    with pytest.raises(Exception):
        mia_japan.change_gender('other')


def test_check_change_gender_to_female(john_american):
    john_american.change_gender('female')
    assert john_american.gender == 'female'


def test_check_change_gender_to_male(mia_japan):
    mia_japan.change_gender('male')
    assert mia_japan.gender == 'male'


def test_check_grow(john_british):
    random_number = int(random.random() * 10)
    for time in range(random_number):
        john_british.grow()
    assert john_british.age == 23 + random_number


def test_check_change_name_positive(john_british):
    john_british.change_name('Pedro')
    assert john_british.name == 'Pedro'


def test_check_change_name_negative(john_british):
    john_british.change_name('Pedro')
    assert john_british.name != 'John'


def test_check_raise_exception_for_change_name(john_american):
    with pytest.raises(Exception):
        john_american.change_name('John')


def test_check_change_name_return_correct_name_type(john_british):
    john_british.change_name('Bob')
    assert type(john_british.name) is str


def test_check_grow_return_correct_grow_type(john_american):
    john_american.grow()
    assert type(john_american.age) is int


def test_check_change_gender_return_correct_gender_type(john_american):
    john_american.change_gender('female')
    assert type(john_american.gender) is str


def test_check_method_validate_return_correct_type(mia_japan):
    method = getattr(
        mia_japan,
        f"_{mia_japan.__class__.__name__}__validate_gender"
    )
    assert type(method('female')) is str


def test_check_nationality_name_return_value_correct_type(mia_japan):
    assert type(mia_japan.nationality.name) is str
