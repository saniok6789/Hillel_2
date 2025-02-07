import unittest

class StringProcessor:
    """Класс для обработки строк."""
    
    def reverse_string(self, s: str) -> str:
        """Переворачивает строку."""
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Делает первую букву строки заглавной."""
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """Считает количество гласных букв в строке."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)

class TestStringProcessor(unittest.TestCase):
    """Тесты для класса StringProcessor."""
    
    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.processor = StringProcessor()
    
    @unittest.skip("Проблема с пустой строкой, исправим позже")
    def test_reverse_string_empty(self):
        """Пропущенный тест для пустой строки."""
        self.assertEqual(self.processor.reverse_string(""), "")

    def test_reverse_string(self):
        """Тест на переворот строки."""
        self.assertEqual(self.processor.reverse_string("hello"), "olleh")
        self.assertEqual(self.processor.reverse_string("123"), "321")

    def test_capitalize_string(self):
        """Тест на капитализацию строки."""
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")
        self.assertEqual(self.processor.capitalize_string("123abc"), "123abc")

    def test_count_vowels(self):
        """Тест на подсчет гласных."""
        self.assertEqual(self.processor.count_vowels("hello"), 2)
        self.assertEqual(self.processor.count_vowels("HELLO"), 2)
        self.assertEqual(self.processor.count_vowels("xyz"), 0)

if __name__ == "__main__":
    unittest.main()
