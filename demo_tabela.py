"""
Script de demonstração da tabela de classificação final.
Execute: python demo_tabela.py
"""
import random
from src.models.campeonato import Campeonato
from src.models.time import Time


def main():
    print("=" * 95)
    print("DEMONSTRAÇÃO - SIMULAÇÃO COMPLETA DO BRASILEIRÃO 2025")
    print("=" * 95)
    print()
    
    # Cria campeonato com 20 times
    campeonato = Campeonato("Brasileirão Série A 2025")
    
    times = [
        "Atlético-MG",
        "Bahia",
        "Botafogo",
        "Bragantino",
        "Ceará",
        "Corinthians",
        "Cruzeiro",
        "Flamengo",
        "Fluminense",
        "Fortaleza",
        "Grêmio",
        "Internacional",
        "Juventude",
        "Mirassol",
        "Palmeiras",
        "Santos",
        "São Paulo",
        "Sport",
        "Vasco",
        "Vitória"
    ]
    
    print("📋 Adicionando times...")
    for nome in times:
        campeonato.adicionar_time(Time(nome))
    print(f"✅ {len(campeonato.times)} times adicionados")
    print()
    
    print("🎲 Gerando rodadas (38 rodadas - turno e returno)...")
    campeonato.criar_rodada()
    print(f"✅ {len(campeonato.rodadas)} rodadas geradas")
    print()
    
    print("⚽ Simulando resultados de todas as partidas...")
    
    # Seed aleatória - cada execução gera resultados diferentes
    # Para debug/testes: descomente a linha abaixo para resultados reproduzíveis
    # random.seed(42)  # Fixando seed: sempre mesmos resultados
    
    placares_possiveis = [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3),
        (0, 4), (1, 4), (2, 4)
    ]
    
    total_partidas = 0
    for rodada in campeonato.rodadas:
        for partida in rodada.partidas:
            placar = random.choice(placares_possiveis)
            partida.registrar_placar(placar[0], placar[1])
            total_partidas += 1
    
    print(f"✅ {total_partidas} partidas simuladas")
    print()
    
    # Gera e exibe a tabela final
    print("📊 Gerando tabela de classificação final...")
    print()
    tabela = campeonato.gerar_tabela_final()
    print(tabela)
    
    # Estatísticas adicionais
    classificacao = campeonato.classificacao()
    campeao = classificacao[0]
    vice = classificacao[1]
    rebaixado = classificacao[-1]
    
    print("\n" + "=" * 95)
    print("📈 ESTATÍSTICAS DESTACADAS")
    print("=" * 95)
    print(f"\n🏆 CAMPEÃO: {campeao.nome}")
    print(f"   Pontos: {campeao.pontos} | Vitórias: {campeao.vitorias} | "
          f"Saldo: {campeao.saldo_gols():+d} | Gols: {campeao.gols_marcados}")
    
    print(f"\n🥈 VICE: {vice.nome}")
    print(f"   Pontos: {vice.pontos} | Vitórias: {vice.vitorias} | "
          f"Saldo: {vice.saldo_gols():+d} | Gols: {vice.gols_marcados}")
    
    print(f"\n⬇️  LANTERNA: {rebaixado.nome}")
    print(f"   Pontos: {rebaixado.pontos} | Vitórias: {rebaixado.vitorias} | "
          f"Saldo: {rebaixado.saldo_gols():+d} | Gols: {rebaixado.gols_marcados}")
    
    # Times em zonas especiais
    libertadores = [t.nome for t in classificacao[1:6]]
    sulamericana = [t.nome for t in classificacao[6:12]]
    rebaixados = [t.nome for t in classificacao[-4:]]
    
    print(f"\n🌎 LIBERTADORES (2º ao 6º):")
    print(f"   {', '.join(libertadores)}")
    
    print(f"\n🏆 SUL-AMERICANA (7º ao 12º):")
    print(f"   {', '.join(sulamericana)}")
    
    print(f"\n⬇️  REBAIXADOS (17º ao 20º):")
    print(f"   {', '.join(rebaixados)}")
    
    print("\n" + "=" * 95)
    print("✅ Simulação concluída com sucesso!")
    print("=" * 95)


if __name__ == "__main__":
    main()
