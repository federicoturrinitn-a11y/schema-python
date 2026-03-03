# schema-python
=========================================================
🗄️ APPUNTI DATABASE - CHEAT SHEET SCHEMA ER PER ESAME
=========================================================

Lo Schema ER serve a progettare il database PRIMA di scrivere il codice SQL.
Si basa su 3 elementi principali: Entità, Attributi e Relazioni.

--- 1. I BLOCCHI FONDAMENTALI ---

🟩 ENTITÀ (I "Soggetti")
- Cosa sono: Oggetti, persone o concetti del mondo reale.
- Come si disegnano: Rettangoli.
- Come si scelgono: Sono i "nomi" (es. STUDENTE, LIBRO, AUTORE, PROFESSORE).
- Regola: Il nome dell'entità va sempre al SINGOLARE.

🔵 ATTRIBUTI (Le "Caratteristiche")
- Cosa sono: I dati che descrivono un'entità.
- Come si disegnano: Ellissi o pallini collegati all'entità.
- Esempio: Per l'entità STUDENTE, gli attributi sono Nome, Cognome, Data_Nascita.
- 🔑 CHIAVE PRIMARIA (Primary Key - PK): È l'attributo UNICO che identifica 
  quell'entità (es. Matricola, Codice Fiscale, ID_Libro). Si disegna 
  sottolineando il nome dell'attributo, oppure pallino nero pieno.

🔶 RELAZIONI (I "Collegamenti")
- Cosa sono: Il legame logico tra due entità.
- Come si disegnano: Rombi.
- Come si scelgono: Sono i "verbi" (es. SCRIVE, PRESTA, ISCRITTO).
- Esempio: L'entità AUTORE [Scrive] l'entità LIBRO.


--- 2. LE CARDINALITÀ (La parte più importante all'esame!) ---

Le cardinalità indicano "quanti" elementi di un'entità partecipano alla relazione.
Si scrivono con due numeri (Minimo, Massimo) vicino all'entità.

Tipi di associazione massima (quella che definisce il database):
* 1:1 (Uno a Uno):
  Esempio: MARITO e MOGLIE. 
  Un marito ha 1 sola moglie, una moglie ha 1 solo marito.

* 1:N (Uno a Molti):  <-- La più usata!
  Esempio: MADRE e FIGLIO.
  Una madre può avere N figli. Un figlio ha 1 sola madre biologica.
  (Nei database, la chiave primaria dell' "1" finisce come chiave esterna nell' "N").

* N:M (Molti a Molti):
  Esempio: STUDENTE e CORSO.
  Uno studente frequenta N corsi. Un corso è frequentato da M studenti.
  (⚠️ REGOLA ESAME: Nei database SQL le relazioni N:M non si possono fare! 
  Dovrai "spezzarle" creando una terza tabella in mezzo, es. "Iscrizione").


--- 3. ESEMPIO PRATICO (Il tuo database "Libri") ---

[ AUTORE ] (Entità)
  |-- ID_Autore (Attributo - Chiave Primaria)
  |-- Nome (Attributo)
  |-- Nazionalità (Attributo)
  |
 < SCRIVE > (Relazione)  --> Cardinalità: Un autore scrive (1, N) libri.
  |                      --> Un libro è scritto da (1, N) autori. (Molti a Molti!)
  |
[ LIBRO ] (Entità)
  |-- ID_Libro (Attributo - Chiave Primaria)
  |-- Titolo (Attributo)
  |-- N_Copie (Attributo)


--- 4. TRUCCHI SALVA-ESAME ---
1. Trova prima tutti i "Sostantivi" nel testo del problema: diventeranno le Entità.
2. Trova i "Verbi" che collegano i sostantivi: diventeranno le Relazioni.
3. Chiediti sempre: "Un [Entità A] quanti [Entità B] può avere al massimo?". 
   Questo ti salva sulle cardinalità.
4. Non scordare MAI di sottolineare la Chiave Primaria (ID)!
=========================================================