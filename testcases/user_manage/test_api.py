# Time : 2023/2/2 10:14


# Time : 2023/1/13 15:20
import pytest

from common.common_util import Common


# class TestPractices(Common):
#
#     def test_practice1(self,db):
#         print(f'practice1: {db}')
#
#     def test_practice2(self):
#         print('practice2')
#
#     def test_practice3(self):
#         print('practice3')

# @pytest.mark.usefixtures('sql_func')
# class TestPractices2:
#
#     def test_practice4(self):
#         print('practice4')

class TestPrametrize():

    @pytest.mark.parametrize('caseinfo',['cassie','qiangzhang','jojo'])
    def test_01(self,caseinfo):
        print('测试parametrize用法1')

    @pytest.mark.parametrize('arg1,arg2', [['name','cassie'],['age','18']])
    def test_02(self, arg1,arg2):
        print(f'测试parametrize用法2 {arg1} {arg2}')