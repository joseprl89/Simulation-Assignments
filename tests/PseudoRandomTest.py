import unittest
import tempfile
import os

import src.pac1.PseudoRandom as PseudoRandom

class PseudoRandomTest (unittest.TestCase):
    
    def testPseudoRandomGeneratorLargeM(self):
        # Create the tempfile and pseudorandom number
        random = PseudoRandom.Random(10, 2**32)
        _, fileName = tempfile.mkstemp()
        file = open(fileName, 'w')
        
        # Generate 10000 random numbers
        for value in range(10000):
            result = str(random.nextInt()) 
            file.write(result + "\n");
        
        # Test with dieharder
        print("Diehard test for Large m")
        os.system("dieharder -a -f " + fileName)
        
        # Close the file
        file.close();


    def testPseudoRandomGeneratorSmallM(self):
        # Create the pseudorandom generator and the tempfile
        random = PseudoRandom.Random(10,32)
        _, fileName = tempfile.mkstemp()
        file = open(fileName, 'w')
        
        # Create 10000 random numbers
        for value in range(10000):
            result = str(random.nextInt()) 
            file.write(result + "\n");      
        
        # Test with dieharder
        print("Diehard test for Small m")
        os.system("dieharder -a -f " + fileName)
        
        # Close the file
        file.close();


if __name__ == '__main__':
    unittest.main()