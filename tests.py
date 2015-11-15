import unittest
from mikolaj import Mikolaj
from mikolajki_generator import MikolajkiGenerator


class MikolajkiGeneratorTest(unittest.TestCase):
    def setUp(self):
        test_mikolajs_data = self.test_mikolajs_data()
        self.mikolajki = MikolajkiGenerator(test_mikolajs_data)

    def test_mikolajs_data(self):
        mikolajs = []
        mikolajs.append(Mikolaj("Rafal Lizon", 'lizonr@gmail.com'))
        mikolajs.append(Mikolaj("Antek Grzanka", 'antoni.grzanka@gmail.com'))
        # mikolajs.append(Mikolaj("Kinga Hepner", 'kinga.hepner@gmail.com'))
        # mikolajs.append(Mikolaj("Paulina Karp", 'paulina.karp@gmail.com'))
        # mikolajs.append(Mikolaj("Slawomir Holda", 'slawomir.holda@gmail.com'))
        # mikolajs.append(Mikolaj("Andrzej Romanski", 'andrzej.romanski@gmail.com'))
        # mikolajs.append(Mikolaj("Bartek Lizon", 'bartek.lizon@gmail.com'))
        return mikolajs


    def test(self):
        self.mikolajki.make_lottery()

    def test_mikolaj_can_not_make_present_for_himself(self):
        results = self.mikolajki.chose_chosen_one()
        for result in results:
            self.assertIsNot(result[0], result[1])

    def test_every_mikolaj_have_his_chosen_one(self):
        results = self.mikolajki.chose_chosen_one()
        for result in results:
            self.assertIsNotNone(result[0])
            self.assertIsNotNone(result[1])

    def test_send_email(self):
        results = self.mikolajki.chose_chosen_one()
        print results
        custom_results = []
        for result in results:
            if result[0].username=="Rafal Lizon":
                custom_results.append(result)
            if result[0].username=="Antek Grzanka":
                custom_results.append(result)
        self.mikolajki.send_emails_to_users(custom_results)
