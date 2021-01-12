class Hamming_Distance:
    @staticmethod
    def hamming_string(word_a, word_b):
        dist = 0
        w1 = list(word_a.lower())
        w2 = list(word_b.lower())
        wl = len(w1)
        if len(w1) == len(w2):
            for i in range(wl):
                if w1[i] != w2[i]:
                    dist += 1
                else:
                    pass
            return dist
        else:
            raise IndexError('For Calculation of Hamming Distance The String Should be of equal length')

    @staticmethod
    def hamming_int(int_a, int_b):
        if not isinstance(int_a, int):
            raise ValueError('int_a should be an integers but %s was provided', type(int_a))
        if not isinstance(int_b, int):
            raise ValueError('int_b should be an integers but %s was provided', type(int_b))

        by_1 = list(bin(int_a))
        by_2 = list(bin(int_b))
        if len(by_1)<len(by_2):
            diff = len(by_2) - len(by_1)
            for _ in range(diff):
                by_1.append(0)
        elif len(by_2)<len(by_1):
            diff = len(by_1) - len(by_2)
            for _ in range(diff):
                by_2.append(0)
        else:
            pass

        dist = 0
        int_len = len(by_1)
        if len(by_1) == len(by_2):
            for i in range(int_len):
                if by_1[i] != by_2[i]:
                    dist += 1
                else:
                    pass
        else:
            raise ValueError('Check the implementation')

        return dist


if __name__ == '__main__':
    print(Hamming_Distance.hamming_string(word_a='rover is', word_b='river'))
    print(Hamming_Distance.hamming_int(int_a=14, int_b=9))
