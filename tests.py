import main
import unittest

class Tests(unittest.TestCase):
  def testPropertyAtrAsserton(self):
    worker = main.Boss("Ihor", 4)
    self.assertTrue(worker.name == "Ihor")

  def testPropertySumMethod(self):
    wrokerHandler = main.WorkerHandler()
    worker1 = main.Boss("Ihor", 5)
    worker2 = main.Advanced("Artem", 4)
    worker3 = main.Noob("Dima", 5)

    wrokerHandler.addWorker(worker1)
    wrokerHandler.addWorker(worker2)
    wrokerHandler.addWorker(worker3)
    wrokerHandler.logWorkers()

    self.assertEqual(wrokerHandler.countSalaries(), 28800)

if __name__ == '__main__':
  unittest.main()