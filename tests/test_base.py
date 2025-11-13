import pytest
from pydantic import BaseModel

from factoria.exceptions import IncompleteFactoryError
from factoria.base import BaseFactory


class DummyModel(BaseModel):
    name: str
    age: int


class DummyFactory(BaseFactory):
    def definition(self):
        return DummyModel(name="Alice", age=30)


def test_make_returns_single_model():
    factory = DummyFactory()
    model = factory.make()

    assert isinstance(model, DummyModel)
    assert model.name == "Alice"
    assert model.age == 30


def test_count_returns_multiple_models():
    factory = DummyFactory().count(3)
    models = factory.make()

    assert isinstance(models, list)
    assert len(models) == 3
    assert all(isinstance(m, DummyModel) for m in models)


def test_chained_usage_returns_correct_number_of_models():
    models = DummyFactory().count(5).make()
    assert len(models) == 5


def test_definition_must_be_implemented():
    class IncompleteFactory(BaseFactory):

        def definition(self) -> BaseModel: ...

    with pytest.raises(IncompleteFactoryError):
        IncompleteFactory()
