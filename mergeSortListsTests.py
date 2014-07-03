import unittest
from mergesortlists import mergeSorterLists


class TestMergeSortList(unittest.TestCase):
    testMergeSort = mergeSorterLists()
    #test various edge cases, and scenarios, algorithm is same as merge sort, but want to make sure behavior isn't changed by modifications
    def test_Various(self):
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1],['b',2],['c',3],['f',4],['d',5]]) == [['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1],['b',2],['c',3],['f',4],['d',2]]) != [['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['d',5],['f',4],['c',3],['b',2],['a',1]]) == [['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['negative',-1],['a',1],['b',2],['c',3],['f',4],['d',5]]) == [['negative',-1],['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['zero',0],['a',1],['b',2],['c',3],['f',4],['d',5]]) == [['zero',0],['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['negative',-1],['zero',0],['a',1],['b',2],['c',3],['f',4],['d',5]]) == [['negative',-1],['zero',0],['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1],['b',2],['c',3],['d',5],['f',4]]) == [['a',1],['b',2],['c',3],['f',4],['d',5]])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1]]) == [['a',1]])
        self.assertRaises(self.testMergeSort.mergeSortList([1]) == [1])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1]]) != [['a',1],['b',2]])
        self.assertTrue(self.testMergeSort.mergeSortList([]) != [['a',1]])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1]]) != [])
        self.assertTrue(self.testMergeSort.mergeSortList([['a',1],['b',2]]) != [['a',1]])

if __name__ == '__main__':
    unittest.main()

testMergeSortinglist = TestMergeSortList()
testMergeSortinglist.test_Various()
