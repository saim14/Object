class Range:
  def __init__(self, start, stop=None, step=1):
    if step == 0:
      raise ValueError("Step Can't be zero")
    
    if stop is None:
      start, stop = 0, start

    self._length = max(0, (stop - start + step - 1)//step)
    self._start = start 
    self._step = step 

  def __len__(self):
    return self._length

  def __getitem__(self, j):
    if j < 0:
      j+=len(self)

    if not(0 <= j < self._length):
      raise IndexError("Index out of range")

    return self._start + j * self._step
    
