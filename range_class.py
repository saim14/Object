class Range:
  def __init__(self, start, stop=None, step=1):
    #If there is one operator I use no space, e.g: 'step==0'
    if step==0:
      raise ValueError("Step Can't be '0'")
    if stop is None:
      start, stop = 0, start
    self._length=max(0,(stop-start+step-1)//step)
    self._start=start
    self._step=step
  def __len__(self):
    return self._length
  def __getitem__(self, position):
    if position<0:
      position+=len(self)
    if not (0 <= position < self._length):
      raise IndexError("Index out of range")
    #If there is multiple operator I use space, e.g: 'self._start + position * self._step'
    return self._start + position * self._step
    
