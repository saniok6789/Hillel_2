import unittest
from unittest.mock import patch
import requests

class WebService:
    """Сервис для работы с веб-данными."""
    
    def get_data(self, url: str) -> dict:
        """Получает данные с веб-сайта."""
        response = requests.get(url)
        return response.json()

class TestWebService(unittest.TestCase):
    """Тестирование WebService с моками."""
    
    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        """Тест успешного получения данных."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test"}

        service = WebService()
        data = service.get_data("https://example.com")

        self.assertEqual(data, {"data": "test"})
    
    @patch("requests.get")
    def test_get_data_404(self, mock_get):
        """Тест ошибки 404."""
        mock_get.return_value.status_code = 404

        service = WebService()
        data = service.get_data("https://example.com")

        self.assertNotEqual(data, {"data": "test"})

if __name__ == "__main__":
    unittest.main()
