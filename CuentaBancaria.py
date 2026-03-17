class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular      # público
        self._tipo   = "ahorros"   # protegido
        self.__saldo = saldo        # privado

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, v):
        if v >= 0: self.__saldo = v
        else: raise ValueError("Negativo")

c = CuentaBancaria("Ana", 1000)
print(c.saldo)   # 1000 via @property
c.saldo = 1500   # usa @setter