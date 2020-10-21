# Creating Progression class
class Progression:
    """Iteration producing a generic progression
    Default iterator produces whole number W = {0, 1, 2, 3, ...}
    """

    def __init__(self, start=0):
        """Initializing the current the first value of the progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        This should be overridden by a subclass to customize progression.

        If the current is set to None, that is the end of a finite progression
        :return:
        """
        self._current += 1

    def __next__(self):
        """ Returns the next element or StopIteration error in case of NoneType"""
        if self._current is None:
            raise StopIteration("None doesn't have a next value ")
        else:
            answer = self._current  # Records current value to return
            self._advance()  # Advance to prepare for next time
            return answer  # return the answer

    def __iter__(self):
        """An iterator return itself as an iterator"""

    def print_progression(self, n):
        """ Printes the next n values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))


# Creating ArithmeticProgression
class ArithmeticProgression(Progression):  # inherit from progression
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        :param increment: the fixed constant to add to each term (default 1)
        :param start: the first term of the progression (default 0)
        """
        super().__init__()
        self._increment = increment

    def _advance(self):  # Override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


# Creating GeometricProgression
class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression

        :param base: the fixed constant multiplied to each term (default 2)
        :param start: the first term of the progression (default 1)
        """
        super(GeometricProgression, self).__init__(start)
        self._base = base

    def _advance(self):
        """Updating current value by multiplying it by the base value"""
        self._current *= self._base


# Creating FibonacciProgression
class FibonacciProgression(Progression):
    """Iterates procusing a generalized Fibonacci progression"""

    def __init__(self, first=0, second=1):
        """Creates a new geometric progression

        :param first: the first term of the progression (default 0)
        :param second: the second term of progression (default 1)
        """
        super(FibonacciProgression, self).__init__(first)
        # super(self).__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taling sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current

FibonacciProgression(first=0, second=1).print_progression(n=1000)