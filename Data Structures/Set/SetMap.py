class Set:
  def __init__(self, element=None):
    self.data = {}
    self.size = 0

    if element is not None:
      for value in element:
        self.add(value)

  def add(self, element):
    if element not in self.data:
      self.data[element] = 1
      self.size += 1

  def has(self, element):
    return element in self.data

  def delete(self, element):
    if element in self.data:
      del self.data[element]
      self.size -= 1
      return True

    return False

  def clone(self):
    return Set(list(self.data.keys()))

  def union(self, other):
    union = self.clone()
    for element in other:
      union.add(element)

    return union;

  def intersection(self, other):
    intersection = Set()
    for element in self.data:
      if other.has(element):
        intersection.add(element)

    return intersection

  def difference(self, other):
    difference = Set()
    for element in self.data:
      if other.has(element) is False:
        difference.add(element)

    return difference

  def subset(self, other):
    for element in self.data:
      if other.has(element) is False:
        return False

    return True

  def __str__(self):
    return str(self.data.keys())

  def __iter__(self):
    return iter(self.data.keys())
