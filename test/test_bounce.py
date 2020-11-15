import pytest
from exercises.bubble import Bubble


class TestExercise1_3_1:

    def test_bubble_with_color_test(self):

        try:
            a = Bubble(100, 200, (255, 0, 0))
            if a.dx < -1 or a.dx > 1 or a.color != (255, 0, 0):
                pytest.fail("Looks like the constructor is not quite working.")

        except TypeError:
            pytest.fail("The constructor may have not been properly implemented fo this test.")

    def test_bubble_equality_test(self):
        try:
            a = Bubble(100, 200, (255, 0, 0))
            b = Bubble(100, 200, (255, 0, 0))
            c = Bubble(100, 100, (255, 0, 0))

            if a != b or a is b or a == c:
                pytest.fail("Looks like the 'equality' does not quite working.")
        except TypeError:
            pytest.fail("The 'equality' may have not been properly implemented fo this test.")
