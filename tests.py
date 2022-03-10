import unittest
import gestform


class MyTestCase(unittest.TestCase):
    #Test plusieurs variantes de numérateur et dénominateurs
    def test_divisible(self):
        self.assertTrue(gestform.est_divisible(6, 3))
        self.assertTrue(gestform.est_divisible(10, 5))
        self.assertTrue(gestform.est_divisible(-10, 5))
        self.assertTrue(gestform.est_divisible(30, 3, 5))
        self.assertTrue(gestform.est_divisible(-30, 3, 5))
        self.assertTrue(gestform.est_divisible(0, 3, 5))
        self.assertFalse(gestform.est_divisible(8, 3, 5))
        self.assertFalse(gestform.est_divisible(10, 3, 5))
        self.assertFalse(gestform.est_divisible(8, 3))
        self.assertFalse(gestform.est_divisible(-10, 3, 5))
        self.assertFalse(gestform.est_divisible(-8, 3))
        self.assertFalse(gestform.est_divisible(8, 5))

    #Test si la longeur et les intervalles des la liste sont respectés
    def test_liste_aleatoire(self):
        self.assertEqual(len(gestform.liste_aleatoire(10)), 10)
        self.assertEqual(gestform.liste_aleatoire(4,1,1),[1,1,1,1])

    #Test toutes les différentes sorties possible de la fonction gestform
    def test_gestform(self):
        self.assertEqual(gestform.gestform(30),"Gestform")
        self.assertEqual(gestform.gestform(10),"Forme")
        self.assertEqual(gestform.gestform(9),"Geste")
        self.assertEqual(gestform.gestform(8),8)


if __name__ == '__main__':
    unittest.main()
