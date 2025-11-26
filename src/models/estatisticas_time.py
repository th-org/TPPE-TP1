class EstatisticasTime:
    
    
    def __init__(self):
       
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
    
    def registrar_gols_marcados(self, n: int) -> None:
        
        self._validar_gols(n)
        self.gols_marcados += n
    
    def registrar_gols_sofridos(self, n: int) -> None:
        
        self._validar_gols(n)
        self.gols_sofridos += n
    
    def _validar_gols(self, n: int) -> None:
        
        if n < 0:
            raise ValueError("Gols não podem ser negativos")
    
    def adicionar_vitoria(self) -> None:
        
        self.vitorias += 1
        self.pontos += 3
    
    def adicionar_empate(self) -> None:
        
        self.empates += 1
        self.pontos += 1
    
    def adicionar_derrota(self) -> None:
        
        self.derrotas += 1
    
    def calcular_saldo_gols(self) -> int:
        
        return self.gols_marcados - self.gols_sofridos
    
    def total_jogos(self) -> int:
        
        return self.vitorias + self.empates + self.derrotas
    
    def aproveitamento(self) -> float:
        
        jogos = self.total_jogos()
        if jogos == 0:
            return 0.0
        
        pontos_possiveis = jogos * 3
        return (self.pontos / pontos_possiveis) * 100
