# Movie Recommender

## Opis

Movie Recommender to program umożliwiający otrzymywanie rekomendacji filmów na podstawie podobieństwa treści. Program korzysta z danych o filmach hollywodzkich, aby wytrenować model rekomendacyjny i udostępnia interfejs graficzny (GUI) do wprowadzania tytułu filmu i otrzymywania rekomendacji.

## Uruchamianie programu

Aby uruchomić program, wykonaj następujące kroki:

1. **Pobranie plików projektu**: Pobierz wszystkie pliki projektu do jednego folderu. Pliki te to:
    - `train_movie_recommender.py`
    - `movie_recommender_gui.py`
    - `movies.csv`
    - `requirements.txt`

3. **Instalacja wymaganych bibliotek**: Użyj `pip` do zainstalowania wszystkich wymaganych bibliotek. Możesz to zrobić za pomocą pliku `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

    lub zainstalować biblioteki ręcznie:

    ```sh
    pip install pandas scikit-learn joblib ttkthemes fuzzywuzzy python-Levenshtein
    ```

4. **Trenowanie modelu**: Uruchom skrypt `train_movie_recommender.py`, aby wytrenować model:

    ```sh
    python train_movie_recommender.py
    ```

    Skrypt ten wczyta dane z pliku `movies.csv`, stworzy model rekomendacji i zapisze go do pliku `movie_recommender_model.pkl`.

5. **Uruchomienie GUI**: Po wytrenowaniu modelu, uruchom skrypt `movie_recommender_gui.py`:

    ```sh
    python movie_recommender_gui.py
    ```

    Ten skrypt uruchomi interfejs GUI, który pozwoli na wpisanie tytułu filmu i otrzymanie rekomendacji.

## Autor

Wojciech Murszewski s222738 



