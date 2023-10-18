class Personagem:
  def __init__(self, vida, defs, forc, agili):
    self.vida = vida
    self.defs = defs
    self.forc = forc
    self.agili = agili


class Inimigo(Personagem):
  def __init__(self, vida, defs, forc, agili, v_ini,forc_ini,veloc_ini): 
    super().__init__(vida, defs, forc, agili)
    self.v_ini = v_ini
    self.forc_ini = forc_ini
    self.veloc_ini = veloc_ini


class Acoes(Inimigo):
  def __init__(self, vida, defs, forc, agili, v_ini,forc_ini,veloc_ini):
    super().__init__(vida, defs, forc, agili, v_ini,forc_ini,veloc_ini)
    pass

#Atacar e ser atacado
  def atacar(self):
    print(f'Vida total do inimigo: {self.v_ini}')
    while self.v_ini > 0:
      if self.v_ini > 0:
        self.v_ini -= self.forc
        if self.v_ini >= 0:
          print(f'Você atacou o inimigo! Vida atual dele: {self.v_ini}')
        elif self.v_ini < 0:
          print('Você atacou o inimigo! Vida atual dele: 0')
      if self.v_ini <= 0:
        print('Inimigo derrotado! ')

  def ataque_ini(self):
    print(f'Sua vida total: {self.vida}')
    self.resist = self.vida + self.defs
    while self.resist > 0:
      if self.resist > 0:
        self.resist -= self.forc_ini
        if self.vida < 0:
          print(f'Você levou {self.forc_ini} de dano! Vida atual + defesa: 0')
        elif self.vida >= 0:
          print(f'Você levou {self.forc_ini} de dano! Vida atual + defesa: {self.resist}')
      if self.resist <= 0:
        print('Fim de jogo! Tente novamente!')
        

#Coletar armaduras
  def armadura_couro(self):
    self.defs += 1
    print(f'Armadura de couro coletada! Sua defesa agora é: {self.defs}')

  def armadura_prata(self):
    self.defs += 2
    print(f'Armadura de prata coletada! Sua defesa agora é: {self.defs}')
  
  def armadura_ouro(self):
    self.defs += 3
    print(f'Armadura de ouro coletada! Sua defesa agora é: {self.defs}')

  def armadura_platina(self):
    self.defs += 5
    print(f'Armadura de platina coletada! Sua defesa agora é: {self.defs}')

#Coletar armas
  def e_curta(self):
    self.forc += 5
    print(f'Espada curta coletada! Seu dano agora é: {self.forc}')

  def e_longa(self):
    self.forc += 8
    print(f'Espada longa coletada! Seu dano agora é: {self.forc}')

  def arco(self):
    self.forc += 7
    print(f'Arco coletado! Seu dano agora é: {self.forc}')

  def besta(self):
    self.forc += 6
    print(f'Besta coletada! Seu dano agora é: {self.forc}')

  def tridente(self):
    self.forc += 10
    print(f'Tridente coletado! Seu dano agora é: {self.forc}')

#Coletar itens
  def cura_p(self):
    if self.vida < 50:
       self.vida += 10
    else:
      print(f'Poção de cura pequena coletada! Sua vida agora é: {self.vida}')

  def cura_g(self):
    if self.vida < 50:
       self.vida += 20
    else:
      print(f'Poção de cura grande coletada! Sua vida agora é: {self.vida}')

  def pena(self):
    self.agili += 1
    print(f'Pena coletada! Sua agilidade agora é: {self.agili}')
    
  def p_forca(self):
    self.forc += 1
    print(f'Poção de força coletada! Sua força agora é: {self.forc}')
  

#Determinando os atriutos iniciais do personagem e dos inimigos
acao1 = Acoes(50, 0, 1, 1, 60, 15, 1)
acao2 = Acoes(50, 0, 1, 1, 10, 10, 1)


print('Atributos iniciais')
print(f'Vida: {acao1.vida}')
print(f'Defesa: {acao1.defs}')
print(f'Força: {acao1.forc}')
print(f'Agilidade: {acao1.agili}')
print()

#Atacando inimigo com os atributos iniciais 
#(antes de coletar as armas, armaduras e outros itens)
acao2.atacar()
print()
print()

# Coleta de armaduras 
#(a defesa que cada armadura dá acumula na defesa total)
acao1.armadura_couro()
print()
acao1.armadura_prata()
print()
acao1.armadura_ouro()
print()
acao1.armadura_platina()
print()
print()

#Coleta de armas 
#(assim como as armaduras, o dano recebido pelas armas acumula no dano total)
acao1.e_curta()
print()
acao1.e_longa()
print()
acao1.arco()
print()
acao1.besta()
print()
acao1.tridente()
print()
print()

#Coleta de itens (poções, etc)
acao1.cura_p()
acao1.cura_g()
acao1.pena()
acao1.p_forca()
print()
print()

#Atributos após coletar os itens, armas e armaduras
print('Atributos atuais')
print(f'Vida: {acao1.vida}')
print(f'Defesa: {acao1.defs}')
print(f'Força: {acao1.forc}')
print(f'Agilidade: {acao1.agili}')
print()
print()

#Atacando o inimigo e sendo atacado
acao1.atacar()
print()
print()
acao1.ataque_ini()
print()