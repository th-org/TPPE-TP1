from .estatisticas_time import EstatisticasTime

class Time:
    
    
    def __init__(self, nome: str):
       
        self.nome = nome
        self.estatisticas = EstatisticasTime()
    
    
    
    @property
    def pontos(self) -> int:
       
        return self.estatisticas.pontos
    
    @property
    def vitorias(self) -> int:
        
        return self.estatisticas.vitorias
    
    @property
    def empates(self) -> int:
        
        return self.estatisticas.empates
    
    @property
    def derrotas(self) -> int:
        
        return self.estatisticas.derrotas
    
    @property
    def gols_marcados(self) -> int:
        
        return self.estatisticas.gols_marcados
    
    @property
    def gols_sofridos(self) -> int:
        
        return self.estatisticas.gols_sofridos
    
    

    def registrar_gols_marcados(self, n: int) -> None:
     
        self.estatisticas.registrar_gols_marcados(n)

    def registrar_gols_sofridos(self, n: int) -> None:
        
        self.estatisticas.registrar_gols_sofridos(n)

    def adicionar_vitoria(self) -> None:
        
        self.estatisticas.adicionar_vitoria()

    def adicionar_empate(self) -> None:
        
        self.estatisticas.adicionar_empate()

    def adicionar_derrota(self) -> None:
        
        self.estatisticas.adicionar_derrota()

    def saldo_gols(self) -> int:
        
        return self.estatisticas.calcular_saldo_gols()