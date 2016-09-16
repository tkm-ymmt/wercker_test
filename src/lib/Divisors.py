# ３つの整数 aa、bb、cc を読み込み、aa から bb までの整数の中に、cc の約数がいくつあるかを求めるプログラムを作成してください。

class Divisors(object):
    def __init__(self, a, b, c):
        self.length = self._get_divisor(a, b, c)

    def _get_divisor(self, a, b, c):
        _temp = [n for n in range(a, b) if n%c==0 ]
        return len(_temp)

