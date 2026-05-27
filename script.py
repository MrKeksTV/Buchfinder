import os
import google.generativeai as genai

# 1. API-Schlüssel konfigurieren (Muss als Umgebungsvariable gesetzt sein)
# Anleitung: https://google.com
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Bitte setzte die Umgebungsvariable 'GEMINI_API_KEY'.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_book_info(pages_input):
    """Generiert Informationen über das Buch 'Zebraland' basierend auf Seitenzahlen."""
    
    # Prompt für die KI erstellen
    prompt = f"""
    Du bist ein Experte für das Jugendbuch 'Zebraland' von Michael Stavarič.
    Der Nutzer bereitet eine Präsentation für den Deutschunterricht vor.
    
    Bitte liefere eine detaillierte Zusammenfassung und Analyse für folgende Seiten: {pages_input}
    
    Beziehe dich exakt auf den Inhalt dieser Seiten im Buch 'Zebraland'.
    Strukturierte deine Antwort mit folgenden Punkten:
    1. Wichtige Handlungsereignisse auf diesen Seiten.
    2. Auftretende Charaktere und deren Entwicklung/Verhalten.
    3. Zentrale Motive, Symbole oder Themen, die hier wichtig sind.
    4. Relevante Zitate oder Kernmomente (falls zutreffend).
    """
    
    print(f"Lade Informationen für Seiten: {pages_input}... Bitte warten.")
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Fehler bei der Anfrage: {e}"

def main():
    print("--- Zebraland Deutschunterricht Helfer ---")
    print("Formateingaben Beispiele: '22-33', '6' oder 'alle Seiten'")
    
    while True:
        user_input = input("\nWelche Seiten möchtest du analysieren? (oder 'exit' zum Beenden): ").strip()
        
        if user_input.lower() == 'exit':
            print("Programm beendet.")
            break
            
        if not user_input:
            print("Bitte gib eine Seitenzahl ein.")
            continue
            
        result = get_book_info(user_input)
        print("\n=== ERGEBNIS ===")
        print(result)
        print("================\n")

if __name__ == "__main__":
    main()
