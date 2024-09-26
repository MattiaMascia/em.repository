import os
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score

# Imposta il livello di log di TensorFlow per sopprimere i messaggi INFO e WARNING
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = Tutti i log, 1 = INFO, 2 = WARNING, 3 = ERROR
warnings.filterwarnings('ignore', category=UserWarning, module='keras.layers.core.dense')

# Caricamento dei dataset
movies_df = pd.read_csv('CSV_PULITI/FINALE/movies_metadata_finale_small.csv')
ratings_df = pd.read_csv('CSV_PULITI/FINALE/ratings_small_finale.csv')

# Preprocessing dei dati
merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# One-Hot Encoding per le colonne categoriali
encoder = OneHotEncoder(sparse_output=False)
encoded_genres = encoder.fit_transform(merged_df['genres_list'].values.reshape(-1, 1))

# Creazione di un dataframe di input per il modello
X = pd.concat([pd.DataFrame(encoded_genres, columns=encoder.get_feature_names_out()),
               merged_df[['budget', 'runtime', 'popularity', 'vote_average', 'userId']]], axis=1)

# Target: valutazione del film
y = merged_df['rating'].values

# Suddivisione dei dati in set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Normalizzazione delle caratteristiche
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Costruzione del modello
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compilazione del modello
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Addestramento del modello
model.fit(X_train_scaled, y_train, epochs=1, batch_size=32, validation_data=(X_test_scaled, y_test))

# Funzione di raccomandazione
def recommend_movies(user_id, ratings_df, model, movies_df, num_recommendations=20):
    user_movies = ratings_df[ratings_df['userId'] == user_id]
    seen_movie_ids = user_movies['movieId'].unique()
    
    if not user_movies.empty:
        print(f"Film visti dall'utente {user_id}:")
        for index, row in user_movies.iterrows():
            title = movies_df[movies_df['movieId'] == row['movieId']]['title'].values[0]
            print(f" - {title} (Rating: {row['rating']})")
    else:
        print(f"L'utente {user_id} non ha visto alcun film.")

    unseen_movies = movies_df[~movies_df['movieId'].isin(seen_movie_ids)]
    unseen_genres_encoded = encoder.transform(unseen_movies['genres_list'].values.reshape(-1, 1))
    
    unseen_X = pd.DataFrame(unseen_genres_encoded, columns=encoder.get_feature_names_out())
    unseen_X = pd.concat([unseen_X, unseen_movies[['budget', 'runtime', 'popularity', 'vote_average']].reset_index(drop=True)], axis=1)
    unseen_X = unseen_X.reindex(columns=X_train.columns, fill_value=0)
    unseen_X_scaled = scaler.transform(unseen_X)

    predicted_ratings = model.predict(unseen_X_scaled)
    unseen_movies['predicted_rating'] = predicted_ratings.flatten()
    
    recommended_movies = unseen_movies.sort_values(by='predicted_rating', ascending=False).head(num_recommendations)
    return recommended_movies[['title', 'predicted_rating']]

# Funzione per arrotondare le predizioni al numero intero più vicino
def round_to_nearest_int(predictions):
    return np.rint(predictions).astype(int)

# Funzione per la visualizzazione della matrice di confusione
def visualizza_matrice_di_confusione(test, etichetta, modello):
    # Previsione delle valutazioni
    predicted_ratings = modello.predict(test)
    
    # Arrotonda al numero intero più vicino
    predicted_ratings = round_to_nearest_int(predicted_ratings)
    
    # Assicura che le previsioni siano tra 0 e 10
    predicted_ratings = np.clip(predicted_ratings, 0, 10)
    
    # Calcolo della matrice di confusione
    cm = confusion_matrix(etichetta, predicted_ratings)
    
    # Calcolo dell'accuratezza
    accuracy = accuracy_score(etichetta, predicted_ratings)
    print(f'Accuratezza: {accuracy * 100:.2f}%')

    # Creazione di una maschera per evidenziare la diagonale
    mask = np.eye(cm.shape[0], dtype=bool)
    
    # Visualizzazione della matrice di confusione con evidenziazione della diagonale
    plt.figure(figsize=(10, 7))
    
    # Heatmap con colori diversi per la diagonale
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, linewidths=0.5, linecolor='black', square=True)
    
    # Applicazione di un colore diverso per la diagonale
    sns.heatmap(cm, mask=~mask, annot=False, cmap="Reds", cbar=False, linewidths=0.5, linecolor='black', square=True)

    # Aggiungere etichette
    plt.xlabel('Voti previsti')
    plt.ylabel('Voti reali')
    plt.title(f'Matrice di Confusione\nAccuratezza: {accuracy * 100:.2f}%')
    
    plt.show()

# Funzione per aggiungere un nuovo utente
def aggiungi_utente(merged_df):
    # Trova il massimo userId attuale e incrementa di 1
    max_user_id = merged_df['userId'].max()
    new_user_id = max_user_id + 1
    
    # Aggiungi il nuovo utente al DataFrame
    merged_df = merged_df.append({'userId': new_user_id}, ignore_index=True)
    
    print(f"Nuovo utente aggiunto con ID: {new_user_id}")
    return new_user_id, merged_df

# Funzione per aggiungere valutazioni di film
def valuta_film(user_id, movies_df, num_ratings=5):
    top_movies = movies_df.nlargest(num_ratings, 'vote_count')[['movieId', 'title', 'vote_count']]
    
    for index, movie in top_movies.iterrows():
        print(f"\nFilm: {movie['title']} (Vote Count: {movie['vote_count']})")
        visto = input("Hai visto questo film? (s/n): ").strip().lower()
        
        if visto == 's':
            while True:
                try:
                    valutazione = int(input("Inserisci la tua valutazione da 1 a 10: "))
                    if 1 <= valutazione <= 10:
                        break
                    else:
                        print("Valutazione non valida. Deve essere un numero da 1 a 10.")
                except ValueError:
                    print("Valutazione non valida. Devi inserire un numero.")
            
            # Aggiungi la valutazione nel DataFrame
            return {'userId': user_id, 'movieId': movie['movieId'], 'rating': valutazione}

    print("Hai completato la valutazione dei film.")
    return None

# Modifica del menu per includere le nuove funzionalità
def menu(merged_df):
    while True:
        print("\nMenu:")
        print("1. Visualizza raccomandazioni per un utente")
        print("2. Visualizza matrice di confusione")
        print("3. Aggiungi un nuovo utente e le valutazioni dei film")
        print("4. Esci")
        
        scelta = input("Seleziona un'opzione (1-4): ")
        
        if scelta == "1":
            user_id = int(input("Inserisci l'ID utente: "))
            recommended = recommend_movies(user_id=user_id, ratings_df=ratings_df, model=model, movies_df=movies_df)
            print("\nRaccomandazioni per l'utente", user_id)
            print(recommended)
        
        elif scelta == "2":
            print("\nVisualizzazione della matrice di confusione...")
            visualizza_matrice_di_confusione(X_test_scaled, y_test, model)
        
        elif scelta == "3":
            print("\nAggiunta di un nuovo utente...")
            new_user_id, merged_df = aggiungi_utente(merged_df)
            print("\nInizio della valutazione dei film...")
            while True:
                rating_info = valuta_film(new_user_id, movies_df)
                if rating_info is not None:
                    ratings_df = ratings_df.append(rating_info, ignore_index=True)
                    print(f"Valutazione aggiunta: {rating_info['rating']} per il film ID {rating_info['movieId']}")
                else:
                    break
        
        elif scelta == "4":
            print("Uscita...")
            break
        
        else:
            print("Scelta non valida. Riprova.")

# Esegui il menu
menu(merged_df)

