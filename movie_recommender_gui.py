import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import joblib
from fuzzywuzzy import process

# Załaduj model i dane
df, cosine_sim = joblib.load('movie_recommender_model.pkl')

# Debugowanie: wypisz kolumny DataFrame
print(df.columns)

def get_recommendations(title, cosine_sim=cosine_sim):
    # Znajdź najbliższe dopasowanie tytułu filmu
    closest_match = process.extractOne(title, df['Movie'])[0]
    
    # Znajdź indeks filmu na podstawie tytułu
    try:
        idx = df[df['Movie'].str.lower() == closest_match.lower()].index[0]
    except IndexError:
        raise ValueError("Movie not found")

    # Oblicz podobieństwo filmów
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Pobierz 5 najbardziej podobnych filmów

    # Pobierz tytuły filmów
    movie_indices = [i[0] for i in sim_scores]
    return df['Movie'].iloc[movie_indices].tolist()

def suggest_titles(event=None):
    typed = entry.get()
    if typed:
        suggestions = process.extract(typed, df['Movie'], limit=5)
        suggestion_box['values'] = [suggestion[0] for suggestion in suggestions]
        suggestion_box.current(0)
    else:
        suggestion_box['values'] = []

def on_recommend(event=None):
    title = suggestion_box.get()
    if title:
        try:
            recommendations = get_recommendations(title)
            result_listbox.delete(0, tk.END)
            for rec in recommendations:
                result_listbox.insert(tk.END, rec)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Required", "Please enter a movie title")

# Stwórz GUI
root = ThemedTk(theme="breeze")
root.title("Movie Recommender")
root.geometry("500x400")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label = ttk.Label(frame, text="Enter a movie title:")
label.grid(row=0, column=0, pady=5, padx=5)

entry = ttk.Entry(frame, width=50)
entry.grid(row=1, column=0, pady=5, padx=5, sticky=(tk.W, tk.E))
entry.bind('<KeyRelease>', suggest_titles)

suggestion_label = ttk.Label(frame, text="Did you mean:")
suggestion_label.grid(row=2, column=0, pady=5, padx=5)

suggestion_box = ttk.Combobox(frame, width=47, state="readonly")
suggestion_box.grid(row=3, column=0, pady=5, padx=5, sticky=(tk.W, tk.E))

button = ttk.Button(frame, text="Recommend", command=on_recommend)
button.grid(row=4, column=0, pady=10)

result_listbox = tk.Listbox(frame, height=10, width=50)
result_listbox.grid(row=5, column=0, pady=10, padx=5, sticky=(tk.W, tk.E))

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=result_listbox.yview)
scrollbar.grid(row=5, column=1, pady=10, sticky=(tk.N, tk.S))
result_listbox['yscrollcommand'] = scrollbar.set

# Powiąż klawisz Enter z przyciskiem Recommend
entry.bind('<Return>', on_recommend)
suggestion_box.bind('<Return>', on_recommend)

root.mainloop()
