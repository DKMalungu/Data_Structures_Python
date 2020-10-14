class RangeLocal:
    """ Aclass that mimic'c the bilt -in range class"""

    def __init__(self, start, stop=None, step=1):
        """ Initialize a Range instance"""

        if step==0:
            raise ValueError("step can't be 0")

        if stop is None:
            start, stop=0, start

        # Claculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entires in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k <0:
            k+=len(self)

        if not 0<=k<self._length:
            raise IndexError('Index out of range')

        return self._start+k*self._step

if __name__ == '__main__':
    range_obj = RangeLocal(start=0, stop=100, step=2)
    for i in range_obj:
        print(i)