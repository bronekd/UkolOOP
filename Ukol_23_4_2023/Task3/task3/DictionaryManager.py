from .Word import Word
class DictionaryManager:
    def __init__(self):
        self.dictionary = {}

    def add(self, word, translation):
        "Metoda přidání nového slova"
        if word not in self.dictionary:
            self.dictionary[word] = translation
            print(f"Slovo: {word}, bylo úspěšně přidáno do slovníku ")
        else:
            print(f"Slovo: {word}, již existuje ve slovníku")

    def update_translation(self, word, new_translation):
        "metoda pro aktualizaci překladu"
        if word in self.dictionary:
            self.dictionary[word] = new_translation
            print(f"Překlad slova '{word}' byl aktualizován.")
        else:
            print(f"Slovo '{word}' není ve slovníku, nelze aktualizovat překlad.")

    def delete_word(self, word):
        "metoda pro odstranění slova"
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"Slovo '{word}' bylo ostraněno ze slovníku")
        else:
            print(f"Slovo '{word}' není ve slovníku, nelze aktualizovat")

    def display_top_words(self, n):
        """Metoda pro zobrazení nejpopulárnějších slov na základě počtu dotazů."""
        sorted_words = sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)
        print(f"Nejpopulárnější slova:")
        for word, translation in sorted_words[:n]:
            print(f"{word}: {translation}")

    def display_least_popular_words(self, n):
        """Metoda pro zobrazení nejméně populárnějších slov na základě počtu dotazů."""
        sorted_words = sorted(self.dictionary.items(), key=lambda x: x[1])
        print(f"Nejméně populárnější slova:")
        for word, translation in sorted_words[:n]:
            print(f"{word}: {translation}")


# Testování přidání slov
manager = DictionaryManager()
manager.add("hello", "ahoj")
manager.add("apple", "jablko")
manager.add("hello", "ahoj")  # Zopakování slova, již existuje