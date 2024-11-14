import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_below_zero_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), None)

    def test_zero_to_twelve_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_thirteen_ticket_price(self):   
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_twenty_ticket_price(self): 
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_twentyone_to_sixty_ticket_price(self):      
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_sixty_ticket_price(self):          
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_above_sixty_ticket_price(self):      
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

if __name__ == '__main__':
    unittest.main()