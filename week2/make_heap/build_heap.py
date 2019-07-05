# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]

    # n = int(raw_input())
    # self._data = [int(s) for s in raw_input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # print(self._data)
    def shift_down(i):
      while 2 * i + 1 < len(self._data):
        j = 2 * i + 2 if 2 * i + 2 < len(self._data) and self._data[2 * i + 1] > self._data[2 * i + 2] else 2 * i + 1
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
        i = j

    for i in range(len(self._data) // 2 + 1, -1, -1):
      shift_down(i)
      # print(self._data)

    # print(self._data)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
