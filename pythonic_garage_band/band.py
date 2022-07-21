class Band(): 
  def __init__(self, name, arr):
    self.name = name
    self.members = arr

class Musician():
  def __init__(self, instrument, name):
    self.instrument = instrument
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"


class Guitarist(Musician):
  def __init__(self, name):
    super().__init__("guitar", name)

  def __repr__(self):
    return f"Guitarist instance. Name = {self.name}"

  def get_instrument(self):
    return "guitar"


class Bassist(Musician):
  def __init__(self, name):
    super().__init__("bass", name)

  def __repr__(self):
    return f"Bassist instance. Name = {self.name}"

  def get_instrument(self):
    return "bass"


class Drummer(Musician):
  def __init__(self, name):
    super().__init__("drums", name)

  def __repr__(self):
    return f"Drummer instance. Name = {self.name}"

  def get_instrument(self):
    return "drums"

