from abc import ABCMeta, abstractmethod

class Estacionamentos(metaclass = ABCMeta):

  @staticmethod
  @abstractmethod
  def gerarEG(self):
    pass
  
  @staticmethod
  @abstractmethod
  def gerarExt(self):
    pass

  @staticmethod
  @abstractmethod
  def retorno(self):
    pass

class Builder(Estacionamentos):

  def __init__(self):
    self.estacionamento = Estacionamento()

  def gerarEG(self):
    self.estacionamento.tipos.append('Edificio Garagem')
    return self

  def gerarExt(self):
    self.estacionamento.tipos.append('Estacionamento Externo')
    return self

  def retorno(self):
    self.gerarEG()
    self.gerarExt()
    return self.estacionamento.tipos
    

class Estacionamento():

  def __init__(self):
    self.tipos = []

class Director():

  @staticmethod
  def construct():
    return Builder().retorno()
    