import unittest
from mergesort import mergeSorter


class TestMergeSort(unittest.TestCase):
    testMergeSort = mergeSorter()
    #test various edge cases, and scenarios
    def test_Various(self):
        self.assertTrue(self.testMergeSort.mergeSort([1,2,3,4,5]) == [1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([1,2,3,4,2]) != [1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([5,4,3,2,1]) == [1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([-1,1,2,3,4,5]) == [-1,1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([0,1,2,3,4,5]) == [0,1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([-1,0,1,2,3,4,5]) == [-1,0,1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([1,2,5,3,4]) == [1,2,3,4,5])
        self.assertTrue(self.testMergeSort.mergeSort([1]) == [1])
        self.assertTrue(self.testMergeSort.mergeSort([]) == [])
        self.assertTrue(self.testMergeSort.mergeSort([1]) != [1,2])
        self.assertTrue(self.testMergeSort.mergeSort([]) != [1])
        self.assertTrue(self.testMergeSort.mergeSort([1]) != [])
        self.assertTrue(self.testMergeSort.mergeSort([1,2]) != [1])

if __name__ == '__main__':
    unittest.main()

testMergeSorting = TestMergeSort()
testMergeSorting.test_Various()
