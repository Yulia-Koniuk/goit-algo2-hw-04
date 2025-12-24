class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key: str, value):
        # Методи повинні опрацьовувати помилки введення некоректних даних.
        # Вхідні параметри обох методів мають бути рядками.
        if not isinstance(key, str):
            # Критерії прийняття 4. Обробляються некоректні вхідні дані (10 б).   
            raise TypeError(f"Key must be a string, got {type(key).__name__}")
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value

# Клас Homework має успадковувати базовий клас Trie.
class Homework(Trie):
    # Критерії прийняття 1. Метод count_words_with_suffix повертає кількість слів, що закінчуються на заданий pattern. За відсутності слів повертає 0. Враховує регістр символів (10 б).
    def count_words_with_suffix(self, pattern) -> int:
        # Методи повинні опрацьовувати помилки введення некоректних даних.
        # Вхідні параметри обох методів мають бути рядками.
        if not isinstance(pattern, str):
            # Критерії прийняття 4. Обробляються некоректні вхідні дані (10 б).            
            raise TypeError("pattern must be a string")
        if pattern == "":
            return 0

        count = 0
        nodes_to_check = [(self.root, "")]
        while nodes_to_check:
            node, prefix = nodes_to_check.pop()
            if node.value is not None and prefix.endswith(pattern):
                count += 1
            for char, child in node.children.items():
                nodes_to_check.append((child, prefix + char))
        # Метод count_words_with_suffix має повертати ціле число.
        return count

    # Критерії прийняття 2. Метод has_prefix повертає True, якщо існує хоча б одне слово із заданим префіксом. Повертає False, якщо таких слів немає. Враховує регістр символів (10 б).
    def has_prefix(self, prefix) -> bool:
        # Методи повинні опрацьовувати помилки введення некоректних даних.
        # Вхідні параметри обох методів мають бути рядками.
        if not isinstance(prefix, str):
            # Критерії прийняття 4. Обробляються некоректні вхідні дані (10 б).
            raise TypeError("prefix must be a string")
        if prefix == "":
            # Метод has_prefix має повертати булеве значення.
            return False
        node = self.root
        for char in prefix:
            if char not in node.children:
                # Метод has_prefix має повертати булеве значення.
                return False
            node = node.children[char]
        # Метод has_prefix має повертати булеве значення.
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]

    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") is True  # apple, application
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True  # banana
    assert trie.has_prefix("ca") is True  # cat

    # Критерії прийняття 3. Код проходить усі тести (10 б).
    print("Перевірка з шаблону програми:")
    print(trie.count_words_with_suffix("e"))
    print(trie.count_words_with_suffix("ion"))
    print(trie.count_words_with_suffix("a"))
    print(trie.count_words_with_suffix("at"))

    print(trie.has_prefix("app"))
    print(trie.has_prefix("bat"))
    print(trie.has_prefix("ban"))
    print(trie.has_prefix("ca"))

    # Критерії прийняття 5. Методи працюють ефективно на великих наборах даних (10 б).
    for i in range(10000):
        words.append(f"word{i}")
    
    for i, word in enumerate(words):
        trie.put(word, i)

    print("Перевірка ефективності на великих наборах даних:")
    print(trie.count_words_with_suffix("e"))      
    print(trie.count_words_with_suffix("ion"))   
    print(trie.count_words_with_suffix("a"))     

    print(trie.has_prefix("app"))                 
    print(trie.has_prefix("word9999"))          
    print(trie.has_prefix("nonexistent"))















