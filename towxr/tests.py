from unittest import TestCase, main

from towxr import nice

class Nicer(TestCase):
    def test_replace(self):
        self.assertEqual(
            'ed-stelmach-alberta-premier',
            nice('Ed Stelmach (Alberta Premier)')
        )


if __name__ == '__main__':
    main()
