import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.Us = Runner("Усэйн", 10)
        self.Andr = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)


    def test_run_an(self):
        andr_nik = Tournament(90, self.Andr, self.Nik)
        results = andr_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["1"] = zabeg

        self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 1")


    def test_run_un(self):
       us_nik = Tournament(90, self.Us, self.Nik)
       results = us_nik.start()

       zabeg = ""
       for key, value in results.items():
           zabeg += str(key) + ": " + str(value) + " "
       all_results["2"] = zabeg

       self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 2")


    def test_run_uan(self):
        us_andr_nik = Tournament(90, self.Us, self.Andr, self.Nik)
        results = us_andr_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["3"] = zabeg

        self.assertTrue(results[3] == "Ник", "Неверное имя последнего бегуна в забеге 3")


if __name__ == "__main__":
    unittest.main()