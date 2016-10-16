#!/usr/bin/python
 
import unittest
import pymssql
 
class FooTest(unittest.TestCase):
    """Sample test case""" 
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("FooTest:setUp_:begin")
        self.conn = pymssql.connect(server='eats.database.windows.net',\
            user='th2520@eats',\
            password='123*&$eats',\
            database='AERIS')
        print("FooTest:setUp_:end")
     
    
     
    # test routine A
    def testA(self):
        """Test routine A"""
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Contacts VALUES ('Amy',3333333333 )")
        conn.commit()
        print ("FooTest:testA")

    # test routine B
    def testB(self):
        """Test routine B"""
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute("UPDATE Contacts SET name = 'Nilar' WHERE number = 4545454545")
        conn.commit()        
        print ("FooTest:testB")

    # test routine C
    def testC(self):
        """Test routine C"""
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Contacts WHERE number=4567123456")
        conn.commit()        
        print ("FooTest:testC")

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("FooTest:tearDown_:begin")
        self.conn.close()
        print("FooTest:tearDown_:end")

if __name__ == '__main__':
    unittest.main()