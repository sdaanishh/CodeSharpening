import unittest
from Comparator import querySuggestor

class TestComparing(unittest.TestCase):
    testComparator = querySuggestor()
#tests assume only two modifications available
    def test_basic(self):#basic test
        self.assertTrue(self.testComparator.possibleMatch('bacon','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('oxymoron','abacus',0,0))
        self.assertFalse(self.testComparator.possibleMatch('abacus','oxymoron',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacons','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','bacons',0,0))

    def test_Single(self):#test single insertion, deletion, change in beginning middle, end
        self.assertTrue(self.testComparator.possibleMatch('abacon','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','zbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('abacon','tbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baacon','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','baacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('batcon','bazcon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','baconz',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baconz','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacona','bacont',0,0))
    def test_Combos(self):#test pairs of modifications.  Apparent that insertions immediately followed by a deletion and vice versa are just single character changes
        #test double insertions, deletions and changes in the beginning middle and end
        self.assertTrue(self.testComparator.possibleMatch('aabacon','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','zzbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('aabacon','zzbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('ban','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','ban',0,0))
        self.assertTrue(self.testComparator.possibleMatch('balln','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baconaa','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','baconzz',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacontt','baconzz',0,0))

        #test pairs of insertion changes in the begining, middle, and end
        self.assertTrue(self.testComparator.possibleMatch('zbacon','atbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('atbacon','zbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baatcon','bazcon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bazcon','baatcon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baconat','baconz',0,0))
        self.assertTrue(self.testComparator.possibleMatch('baconz','baconat',0,0))

        #test pairs of deletion changes in the begining, middle, and end
        self.assertTrue(self.testComparator.possibleMatch('bacln','abacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('tbadon','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','bacloz',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacloz','bacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacon','abacot',0,0))
        self.assertTrue(self.testComparator.possibleMatch('pbacoo','bacon',0,0))

        #test inesrtion deletions where one is the begining and one in the middle
        self.assertTrue(self.testComparator.possibleMatch('baclon','tbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('tbacon','baclon',0,0))

        #test inesrtion deletions where one is the begining and one in the end
        self.assertTrue(self.testComparator.possibleMatch('baconl','tbacon',0,0))
        self.assertTrue(self.testComparator.possibleMatch('tbacon','baconl',0,0))

        #test inesrtion deletions where one is the middle and one in the end
        self.assertTrue(self.testComparator.possibleMatch('baconl','bacton',0,0))
        self.assertTrue(self.testComparator.possibleMatch('bacton','baconl',0,0))
        
    def test_Triples(self):#test three modifications, should all be false
        #consecutive insertions, deletions, and changes, in beginning middle and end
        self.assertFalse(self.testComparator.possibleMatch('baconttt','baconzzz',0,0))
        self.assertFalse(self.testComparator.possibleMatch('aaabacon','cccbacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('aaabacon','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacon','zzzbacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('baconttt','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacon','baconzzz',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacttton','baczzzon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacssson','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacon','baczzzon',0,0))

    def test_TriplesVaried(self):
        #test three modifications in various places, in varied places
        self.assertFalse(self.testComparator.possibleMatch('baconz','ttbacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('ttbacon','baconz',0,0))
        self.assertFalse(self.testComparator.possibleMatch('zbaczonz','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('bacon','zbaczonz',0,0))
        self.assertFalse(self.testComparator.possibleMatch('zbaczonz','tbactont',0,0))
        self.assertFalse(self.testComparator.possibleMatch('baconf','ttbacong',0,0))
        self.assertFalse(self.testComparator.possibleMatch('ffbacon','ttbaconz',0,0))
        self.assertFalse(self.testComparator.possibleMatch('ttbaconz','bacon',0,0))
        self.assertFalse(self.testComparator.possibleMatch('ttbaconz','bacona',0,0))
        self.assertFalse(self.testComparator.possibleMatch('baconz','ttbacona',0,0))
        
        
        
if __name__ == '__main__':
    unittest.main()


comparingTest = TestComparing()
comparingTest.test_basic()
comparingTest.test_Singles()
comparingTest.test_Combos()
comparingTest.test_Triples()
comparintTest.test_TriplesVaried()
