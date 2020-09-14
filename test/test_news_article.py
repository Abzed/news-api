import unittest
from app.models import News_article

class NewsArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_news_article = News_article('abz','abz-news', 'Abzed gets to Moringa core', 'As he is ready to complete his studies he faces Python as a tough opponent', 'https:abzed.abzed/moringachronicals', 'https://abzed.image', '2020-09-13 13:23','moringa gets tougher')
        
    def test_instance(self):
        self.assertEqual(isinstance(self.new_news_article))
        
if __name__ == '__main__':
    unittest.main()