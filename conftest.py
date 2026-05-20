from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()