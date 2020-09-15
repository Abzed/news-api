import unittest
from app.models import News_article

class NewsArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_news_article = News_article('abz','abzed','abz-news', 'Abzed gets to Moringa core', 'https://abzed.com', 'https://abzed.abzed/moringachronicals', '2020-09-13 13:23','moringa gets tougher')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article, News_article))
        
if __name__ == '__main__':
    unittest.main()