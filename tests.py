import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


@pytest.mark.parametrize('book',['Гарри Поттер','Стихи Пушкина','Властелин колец'])
    def test_add_new_book_true(self,book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert book != 0


    def test_add_new_book_no_gerne(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.books_genre['Гарри Поттер']==''

    def test_set_book_genre_true(self):
        collector = BooksCollector()
        book = collector.add_new_book('Гарри Поттер')
        collector.books_genre[book] = collector.genre_age_rating[0]
        assert collector.books_genre[book]

    @pytest.mark.parametrize('book' ,['Оно','Король лев'])
    def test_get_books_with_specific_genre_true(self,book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book,"Ужасы")
        collector.set_book_genre(book, "Фантастика")
        assert not collector.get_books_with_specific_genre('Ужасы')


    def test_get_book_genre_true(self):
        collector = BooksCollector()
        book = collector.add_new_book('Гордость и предубеждение и зомби')
        collector.books_genre[book] = collector.genre_age_rating[1]
        assert "Детективы" in  collector.books_genre.values()


    def test_get_books_genre_true(self):
        collector = BooksCollector()
        book = collector.get_books_genre()
        assert book != None

    def test_get_boofs_for_children(self):
        collector = BooksCollector()
        book = 'Король Лев'
        genre = 'Мультфильмы'
        collector.add_new_book(book)
        collector.set_book_genre(book,genre)
        assert collector.get_books_for_children()


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) != 0


    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 0


    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        book = collector.get_list_of_favorites_books()
        assert book != None




