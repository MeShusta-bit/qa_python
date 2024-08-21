import pytest
from main import BooksCollector



class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert len(collector.get_books_genre()) == 1



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
        collector.add_new_book('Гарри Поттер')
        books = collector.get_books_genre()
        assert len(books) == 1

    def test_get_books_for_children(self):
        collector = BooksCollector()
        book = 'Король Лев'
        genre = 'Мультфильмы'
        collector.add_new_book(book)
        book = collector.set_book_genre(book,genre)
        assert collector.get_books_for_children()==['Король Лев']


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1


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
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')
        book = collector.get_list_of_favorites_books()
        assert book == ['Гарри Поттер']




