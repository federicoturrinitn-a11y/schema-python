# ==========================================
# 🐍 APPUNTI PYTHON - CHEAT SHEET PER ESAME
# ==========================================

# --- 1. VARIABILI E TIPI DI DATO BASE ---
intero = 10
decimale = 3.14
testo = "Ciao mondo"
booleano = True  # In Python True e False vogliono sempre la maiuscola


# --- 2. STRUTTURE DATI (Le collezioni) ---

# LISTE (Modificabili, ordinate, usano parentesi quadre)
lista_spesa = ["mele", "pane", "latte"]
lista_spesa.append("uova")      # Aggiunge un elemento alla fine
primo_elemento = lista_spesa[0] # Gli indici partono SEMPRE da 0

# TUPLE (NON modificabili/immutabili, ordinate, usano parentesi tonde)
coordinate = (45.12, 9.88)
# coordinate[0] = 46.00  <-- Questo darebbe ERRORE, le tuple non si cambiano

# SET / INSIEMI (Non ordinati, elementi unici, usano parentesi graffe)
numeri_unici = {1, 2, 2, 3}     # Python ignora i duplicati, diventa {1, 2, 3}

# DIZIONARI (Coppie chiave-valore, usano parentesi graffe)
studente = {
    "nome": "Giulia",
    "eta": 22,
    "voti": [28, 30, 26]
}
nome_studente = studente["nome"]        # Legge il valore associato alla chiave "nome"
studente["matricola"] = "12345"         # Aggiunge una nuova chiave-valore


# --- 3. CONDIZIONI (IF / ELIF / ELSE) ---
voto_esame = 28

if voto_esame == 30:
    print("Prendi la Lode!")
elif voto_esame >= 18:                  # elif sta per "else if"
    print("Sei Promosso!")
else:
    print("Bocciato, devi ritentare.")


# --- 4. CICLI (LOOPS) ---

# CICLO FOR (Ripete un'azione per ogni elemento di una sequenza)
print("\n--- Stampa lista della spesa ---")
for prodotto in lista_spesa:
    print(prodotto)

# CICLO FOR con range (Genera numeri. range(5) va da 0 a 4)
for numero in range(5):
    pass  # L'istruzione 'pass' non fa assolutamente nulla, serve solo per evitare 
          # errori se lasci un blocco di codice vuoto temporaneamente.

# CICLO WHILE (Continua a girare finché la condizione rimane True)
contatore = 0
while contatore < 3:
    contatore += 1  # Uguale a scrivere: contatore = contatore + 1


# --- 5. FUNZIONI ---
def saluta(nome, esame="Python"):
    """Questa tra tre virgolette è una docstring: serve a spiegare cosa fa la funzione."""
    messaggio = f"Ciao {nome}, in bocca al lupo per l'esame di {esame}!"
    return messaggio # Il return è ciò che la funzione "sputa fuori" alla fine

# Richiamo la funzione e salvo il risultato in una variabile
saluto_personale = saluta("Marco")
print("\n" + saluto_personale)


# --- 6. CLASSI E OGGETTI (Object Oriented Programming - OOP) ---
class Animale:
    # Metodo costruttore (viene chiamato in automatico quando crei l'oggetto)
    def __init__(self, nome, specie):
        self.nome = nome      # 'self' rappresenta l'oggetto stesso che stiamo creando
        self.specie = specie
    
    # Metodo standard della classe
    def presentati(self):
        return f"Sono {self.nome} e sono un {self.specie}."

# Ereditarietà: La classe Cane "eredita" tutte le caratteristiche di Animale
class Cane(Animale):
    def __init__(self, nome, razza):
        # super() serve a chiamare il costruttore della classe "padre" (Animale)
        super().__init__(nome, specie="Cane") 
        self.razza = razza
        
    def fai_verso(self):
        return "Bau!"

# Creazione degli oggetti (Istanze)
mio_cane = Cane("Fido", "Golden Retriever")
print("\n" + mio_cane.presentati())
print(f"Il cane fa: {mio_cane.fai_verso()}")


# --- 7. GESTIONE DEGLI ERRORI (TRY / EXCEPT) ---
print("\n--- Test Gestione Errori ---")
try:
    risultato = 10 / 0                      # Questo genera un errore matematico
except ZeroDivisionError:
    print("Errore: impossibile dividere un numero per zero!")
except Exception as e:                      # Cattura qualsiasi altro errore imprevisto
    print(f"Si è verificato un errore generico: {e}")
finally:
    print("Il blocco 'finally' viene eseguito sempre, sia che ci siano errori o meno.")