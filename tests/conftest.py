import pytest
from kink import di

from src.container.container import init_container


@pytest.fixture(autouse=True, scope="function")
def init_testing_container():
    init_container()
    yield
    di.clear_cache()
