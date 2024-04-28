from .DictionaryManager import DictionaryManager
class UserInterface:
    def __init__(self):
        self.manager = DictionaryManager()


    def display_menu(self):
        """Metoda pro zobrazení hlavního menu."""
        print("---- Slovníková aplikace ----")
        print("1. Přidat nové slovo")
        print("2. Aktualizovat překlad slova")
        print("3. Smazat slovo ze slovníku")
        print("4. Zobrazit statistiky")
        print("0. Konec")

    def run(self):
        """Metoda pro spuštění uživatelského rozhraní."""
        while True:
            self.display_menu()
            choice = input("Vyberte možnost: ")
            if choice == "1":
                self.add_word_prompt()
            elif choice == "2":
                self.update_translation_prompt()
            elif choice == "3":
                self.delete_word_prompt()
            elif choice == "4":
                self.display_statistics()
            elif choice == "0":
                print("Děkujeme za použití slovníkové aplikace.")
                break
            else:
                print("Neplatná volba, zkuste to znovu.")

    def add_word_prompt(self):
        """Metoda pro vyzvání uživatele k zadání nového slova a jeho překladu."""
        word = input("Zadejte anglické slovo: ")
        translation = input("Zadejte český překlad: ")
        self.manager.add(word, translation)

    def update_translation_prompt(self):
        """Metoda pro vyzvání uživatele k aktualizaci překladu existujícího slova."""
        word = input("Zadejte slovo pro aktualizaci překladu: ")
        new_translation = input("Zadejte nový překlad: ")
        self.manager.update_translation(word, new_translation)

    def delete_word_prompt(self):
        """Metoda pro vyzvání uživatele k odstranění slova ze slovníku."""
        word = input("Zadejte slovo pro smazání: ")
        self.manager.delete_word(word)

    def display_statistics(self):
        """Metoda pro zobrazení statistik o slovníku."""
        print("--- Statistiky ---")
        n = int(input("Zadej počet slov, k zobrazení: "))
        print("Nejpopulárnější slova: ")
        self.manager.display_statistics(n)
        print("\nNejméně populární slova: ")
        self.manager.display_least_popular_words(n)

# Spuštění uživatelského rozhraní
if __name__ == "__main__":
    ui = UserInterface()
    ui.run()