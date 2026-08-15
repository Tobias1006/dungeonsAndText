import unittest

if __name__ == '__main__':
    # Durchsucht den Ordner 'tests' automatisch nach allen Dateien, die auf '_test.py' enden
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests', pattern='*_test.py')

    # Tests ausführen
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)