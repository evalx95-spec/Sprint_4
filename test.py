from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ''


    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Вечное сияние чистого разума")
        collector.add_new_book("Вечное сияние чистого разума")
        assert len(collector.books_genre) == 1

    def test_add_new_book_empty_name(self, collector):
        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_add_new_book_long_name(self, collector):
        long_name = "a" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_set_book_genre_valid(self, collector):

        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_set_book_genre_invalid_genre(self, collector):

        collector.add_new_book("Полное затмение")
        collector.set_book_genre("Полное затмение", "Поэзия")
        assert collector.get_book_genre("Полное затмение") == ''

    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.books_genre

    def test_get_book_genre_existing(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre("Выдуманная книга") is None

    def test_get_books_with_specific_genre_empty(self, collector):
        result = collector.get_books_with_specific_genre("Ужасы")
        assert result == []

    def test_get_books_with_specific_genre_with_books(self, collector):
        """Список книг определённого жанра"""
        collector.add_new_book("Оно")
        collector.add_new_book("Сияние")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Сияние", "Ужасы")
        result = collector.get_books_with_specific_genre("Ужасы")
        assert "Оно" in result
        assert "Сияние" in result

    def test_get_books_genre(self, collector):
        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", "Мультфильмы")
        books = collector.get_books_genre()
        assert isinstance(books, dict)
        assert "Маленький принц" in books
        assert books["Маленький принц"] == "Мультфильмы"

    def test_get_books_for_children_no_age_rating(self, collector):
        collector.add_new_book("Винни Пух")
        collector.add_new_book("Золушка")
        collector.set_book_genre("Винни Пух", "Мультфильмы")  # нет в genre_age_rating
        collector.set_book_genre("Золушка", "Комедии")  # нет в genre_age_rating
        result = collector.get_books_for_children()
        assert "Винни Пух" in result
        assert "Золушка" in result

    def test_get_books_for_children_with_age_rating(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")  # есть в genre_age_rating
        result = collector.get_books_for_children()
        assert "Оно" not in result

    def test_add_book_in_favorites_valid(self, collector):
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        assert "Властелин колец" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector):
        
        collector.add_new_book("Хоббит")
        collector.add_book_in_favorites("Хоббит")
        collector.add_book_in_favorites("Хоббит")
        assert collector.favorites.count("Хоббит") == 1

    def test_add_book_in_favorites_book_not_exists(self, collector):
        
        collector.add_book_in_favorites("Выдуманная книга")
        assert "Выдуманная книга" not in collector.favorites

    def test_delete_book_from_favorites_existing(self, collector):
        
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.delete_book_from_favorites("Дюна")
        assert "Дюна" not in collector.favorites

    def test_delete_book_from_favorites_not_in_list(self, collector):

        collector.delete_book_from_favorites("Не в избранном")
        
        assert True  


    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("451 градус по Фаренгейту")
        collector.add_book_in_favorites("451 градус по Фаренгейту")
        favorites = collector.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert "451 градус по Фаренгейту" in favorites