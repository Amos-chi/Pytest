# Time : 2023/1/13 15:20
import pytest

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
class TestPractices:

    def test_practice1(self):
        print('practice1')
        #raise Exception('Error!')

    def test_practice3(self):
        print('practice3')
        #raise Exception('Error!')

    def test_practice2(self):
        print('practice2')

if __name__ == '__main__':
    pytest.main()