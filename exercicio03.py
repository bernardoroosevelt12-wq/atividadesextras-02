import math

def section(title):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")

# ══════════════════════════════════════════════════════════════
#  EXEMPLOS DO LIVRO (slides páginas 72-76)
# ══════════════════════════════════════════════════════════════

section("EXEMPLO 4.1 — RAM: 2K endereços, 16 bits/célula")
print("  MP com espaço de 2K. Cada célula: 16 bits.")
N, M = 2 * 1024, 16
E = int(math.log2(N))
T = N * M
print(f"  N = 2K = {N} células")
print(f"  E = log₂({N}) = {E} bits  →  tamanho de cada endereço")
print(f"  T = N × M = {N} × {M} = {T} bits = {T//1024} Kbits")

section("EXEMPLO 4.2 — RAM: T=256 Kbits, 8 bits/célula")
print("  MP com máximo de 256K bits. Cada célula: 8 bits.")
T_total, M = 256 * 1024, 8
N = T_total // M
E = int(math.log2(N))
print(f"  N = T/M = {T_total}/{M} = {N} = {N//1024}K células")
print(f"  E = log₂({N}) = {E} bits")

section("EXEMPLO 4.3 — RAM: 2K palavras de 16 bits")
print("  Tamanho REM, RDM, maior endereço e total de bits.")
N, M = 2 * 1024, 16      # palavra = célula = 16 bits
E = int(math.log2(N))
T = N * M
print(f"  REM = E = {E} bits")
print(f"  RDM = M = {M} bits  (tamanho da palavra)")
print(f"  Maior endereço = N-1 = {N-1}₁₀ = {bin(N-1)}₂")
print(f"  T = {N} × {M} = {T} bits = {T//1024} Kbits")

section("EXEMPLO 4.4 — RDM=32b, REM=24b, 2 células/acesso, BD=palavra")
RDM, REM, cel_por_acesso = 32, 24, 2
palavra = RDM                    # BD = palavra = RDM = 32 bits
celula  = palavra // cel_por_acesso   # cada acesso lê 2 células
N_max   = 2 ** REM
T       = N_max * celula
print(f"  Palavra = BD = RDM = {palavra} bits")
print(f"  Célula  = Palavra ÷ 2 = {celula} bits")
print(f"  a) Cap. endereçamento = 2^{REM} = {N_max:,} = {N_max//(2**20)}M células")
print(f"  b) T = {N_max:,} × {celula} = {T:,} bits = {T//(2**20)} Mbits")
print(f"  c) Palavra = {palavra} bits | Célula = {celula} bits")

section("EXEMPLO 4.5 — BE=33b, BD=4 palavras, célula=palavra/8, T_max=64 Gbits")
E_be   = 33
T_max  = 64 * (2**30)             # 64 Gbits em bits
N      = 2 ** E_be                 # células endereçáveis pelo BE
M      = T_max // N                # tamanho da célula em bits
palavra = M * 8                    # célula = palavra / 8  ⟹  palavra = 8 × célula
BD     = 4 * palavra               # BD transfere 4 palavras por acesso
print(f"  T_max = 64G = {T_max:,} bits")
print(f"  N = 2^{E_be} = {N:,} = 8G células")
print(f"  M = T_max/N = {T_max}/{N} = {M} bits/célula")
print(f"  Palavra = 8 × M = 8 × {M} = {palavra} bits")
print(f"  a) Máx. de células = {N:,} = 8G")
print(f"  b) REM = {E_be} bits | BD = 4 × {palavra} = {BD} bits")
print(f"  c) Célula = {M} bits | Palavra = {palavra} bits")


# ══════════════════════════════════════════════════════════════
#  EXERCÍCIOS (slides páginas 78-88)
# ══════════════════════════════════════════════════════════════

section("EXERCÍCIO 1")
print("  MP: palavras de 16 bits em cada célula, barramento de 12 bits.")
print("  Quantos bytes podem ser armazenados?")
E, M = 12, 16
N       = 2 ** E
T_bits  = N * M
T_bytes = T_bits // 8
print(f"  N = 2^{E} = {N} células")
print(f"  T = {N} × {M} = {T_bits} bits")
print(f"  T = {T_bytes} bytes = {T_bytes//1024} KB  ←  RESPOSTA")

section("EXERCÍCIO 5")
print("  Diferença (endereço, conteúdo, total de bits) entre as organizações:")
configs = [
    ("A: 32K células, 8b",  32*1024, 8),
    ("B: 16K células, 16b", 16*1024, 16),
    ("C: 16K células, 8b",  16*1024, 8),
]
print(f"\n  {'Memória':<22} {'N (células)':>12} {'E (bits end.)':>14} "
      f"{'M (bits)':>10} {'T (bits)':>14}")
print(f"  {'-'*74}")
for nome, N, M in configs:
    E = int(math.log2(N))
    T = N * M
    print(f"  {nome:<22} {N:>12,} {E:>14} {M:>10} {T:>14,}")
print()
print("  Observações:")
print("  • A e B têm a mesma capacidade total (256 Kbits), mas endereços e M diferentes.")
print("  • A tem o dobro das células de C (15 vs 14 bits de endereço) com mesmo M → T dobrado.")
print("  • B tem M dobrado de C com mesmo número de células → T dobrado de C.")

section("EXERCÍCIO 6  (conceitual — sem cálculo)")
print("  REM (Registrador de Endereços da Memória):")
print("    Armazena temporariamente o endereço da célula a ser acessada na")
print("    operação de leitura ou escrita. Seu tamanho = largura do barramento")
print("    de endereços (E bits).")
print()
print("  RDM (Registrador de Dados da Memória):")
print("    Armazena temporariamente o dado transferido entre a MP e o processador.")
print("    Na escrita: recebe o valor a gravar. Na leitura: recebe o valor lido.")
print("    Seu tamanho = unidade de transferência (palavra, M bits).")

section("EXERCÍCIOS 7, 8 e 9  (conceituais — sem cálculo)")
print("  Barramentos processador ↔ MP:")
print("    • BD (Barramento de Dados):     bidirecional — transfere dados (RDM ↔ MP).")
print("    • BE (Barramento de Endereços): unidirecional (CPU→MP) — envia o endereço.")
print("    • BC (Barramento de Controle):  bidirecional — sinais READ, WRITE, WAIT.")
print()
print("  Operação de LEITURA (passos):")
print("    1. (REM) ← endereço   — endereço vai para o BE.")
print("    2. Sinal READ no BC    — controlador decodifica endereço e localiza célula.")
print("    3. (RDM) ← (MP[REM])  — dado colocado no BD pelo controlador.")
print("    4. (reg) ← (RDM)      — dado vai para registrador do processador.")
print()
print("  Operação de ESCRITA (passos):")
print("    1. (REM) ← endereço   — endereço vai para o BE.")
print("    2. (RDM) ← dado       — dado colocado no BD.")
print("    3. Sinal WRITE no BC   — controlador decodifica endereço.")
print("    4. (MP[REM]) ← (RDM)  — dado gravado na célula via BD.")

section("EXERCÍCIO 10")
print("  RDM=16 bits, REM=20 bits, célula=8 bits, N=capacidade máxima.")
RDM, REM, M = 16, 20, 8
N = 2 ** REM
T = N * M
print(f"  a) Barramento de endereços = tamanho do REM = {REM} bits")
print(f"  b) Células por leitura = RDM ÷ M = {RDM} ÷ {M} = {RDM//M} células")
print(f"  c) N = 2^{REM} = {N:,} células")
print(f"     T = {N:,} × {M} = {T:,} bits = {T//(2**20)} Mbits")

section("EXERCÍCIO 11")
print("  Microcomputador: N=32K células, M=8 bits/célula.")
N, M = 32 * 1024, 8
E = int(math.log2(N))
T = N * M
print(f"  a) Maior endereço = N-1 = {N} - 1 = {N-1}")
print(f"  b) Tamanho do barramento de endereços = log₂({N}) = {E} bits")
print(f"  c) RDM = M = {M} bits | REM = E = {E} bits")
print(f"  d) T = {N} × {M} = {T} bits = {T//1024} Kbits")

section("EXERCÍCIO 12")
print("  Endereço: 2C81₁₆  |  Conteúdo: F5A₁₆  |  célula = palavra, 1 acesso = 1 célula.")
end_h, cont_h = "2C81", "F5A"
end_dec  = int(end_h,  16)
cont_dec = int(cont_h, 16)
# Número de hex digits × 4 bits cada
REM_b = len(end_h)  * 4   # 4 dígitos hex → 16 bits
RDM_b = len(cont_h) * 4   # 3 dígitos hex → 12 bits
N_max = 2 ** REM_b
T_max = N_max * RDM_b
print(f"  {end_h}₁₆ = {end_dec}₁₀  →  {len(end_h)} dígitos hex × 4 = {REM_b} bits")
print(f"  {cont_h}₁₆ = {cont_dec}₁₀  →  {len(cont_h)} dígitos hex × 4 = {RDM_b} bits")
print(f"  a) REM = {REM_b} bits  |  RDM = {RDM_b} bits")
print(f"  b) N_máx = 2^{REM_b} = {N_max:,} células")
print(f"     T_máx = {N_max:,} × {RDM_b} = {T_max:,} bits = {T_max//1024} Kbits")

section("EXERCÍCIO 13")
print("  Memória 64KB; grupos de 128 chars escritos a partir de 27FA₁₆ (A, B, C...)")
print("  Qual o endereço do 1º J?")
ini  = int("27FA", 16)
tam_grupo = 128
grupos_antes_J = ord('J') - ord('A')   # A=0, B=1, ..., I=8, J=9 → 9 grupos antes
end_J = ini + grupos_antes_J * tam_grupo
print(f"  Início = 27FA₁₆ = {ini}₁₀")
print(f"  Grupos antes do J: {grupos_antes_J}  (A, B, C, D, E, F, G, H, I)")
print(f"  Offset = {grupos_antes_J} × {tam_grupo} = {grupos_antes_J * tam_grupo} bytes")
print(f"  1º J em: {ini} + {grupos_antes_J * tam_grupo} = {end_J}₁₀")
print(f"         = {hex(end_J).upper().replace('0X','0x')}₁₆  ←  RESPOSTA")

section("EXERCÍCIO 14")
print("  Interface: DRAM=R$5,00 | SRAM=R$1,00")
print("  Custo/bit: DRAM=R$0,00001 | SRAM=R$0,00002")
print("  A partir de quantos bits a DRAM é mais barata?")
ci_S, ci_D = 1.0,     5.0
cb_S, cb_D = 0.00002, 0.00001
# ci_D + n*cb_D < ci_S + n*cb_S
# n*(cb_S - cb_D) > ci_D - ci_S
n_critico = round((ci_D - ci_S) / (cb_S - cb_D))   # 400 000 exato
n_test    = n_critico + 1
print(f"\n  Custo SRAM = {ci_S} + n × {cb_S}")
print(f"  Custo DRAM = {ci_D} + n × {cb_D}")
print(f"\n  Igualdade de custos:")
print(f"    {ci_D} + n × {cb_D} = {ci_S} + n × {cb_S}")
print(f"    n × ({cb_S} - {cb_D}) = {ci_D} - {ci_S}")
print(f"    n = {n_critico:,} bits  ←  ponto de equilíbrio (custos iguais)")
print(f"\n  DRAM mais barata quando n > {n_critico:,} bits")
print(f"\n  Verificação com n = {n_test:,} bits (acima do break-even):")
print(f"    Custo SRAM = R$ {ci_S + n_test * cb_S:.2f}")
print(f"    Custo DRAM = R$ {ci_D + n_test * cb_D:.2f}  ✓ DRAM efetivamente mais barata")

section("EXERCÍCIO 21")
print("  Sistema: processador → cache → memória principal")
print("  tc=8 ns | tm=70 ns | eficiência cache=96% | 100 acessos consecutivos")
tc, tm, h = 8, 70, 0.96
n_total = 100
hits   = int(h * n_total)
misses = n_total - hits

T_medio = tc + (1 - h) * tm
print(f"\n  Fórmula: T_médio = tc + (1-h) × tm")
print(f"    = {tc} + {1-h:.2f} × {tm}")
print(f"    = {tc} + {(1-h)*tm:.2f}")
print(f"    = {T_medio:.2f} ns  ←  RESPOSTA")

t_total = hits * tc + misses * (tc + tm)
print(f"\n  Verificação com {n_total} acessos:")
print(f"    {hits} acertos × {tc} ns            = {hits*tc} ns")
print(f"    {misses}  falhas  × ({tc}+{tm}) ns  = {misses*(tc+tm)} ns")
print(f"    Total = {t_total} ns  →  Média = {t_total/n_total:.2f} ns  ✓")

section("EXERCÍCIOS 27 e 28")
print("  Quantos bits são necessários para endereçar células?")
for label, N in [("128G células", 128 * 2**30),
                 ("32K  células", 32  * 2**10)]:
    E = int(math.log2(N))
    print(f"  {label}: N = 2^{E}  →  E = {E} bits")

section("EXERCÍCIO 26  (conceitual — sem cálculo)")
print("  Projetar ROM com 8 células de 4 bits cada (similar à Fig. 4.18).")
print()
print("  • N = 8 células → precisa de 3 bits de endereço (2³=8).")
print("    Usar um decodificador 3-para-8 com entradas A₂, A₁, A₀.")
print("  • M = 4 bits por célula → 4 linhas de saída (S₃, S₂, S₁, S₀).")
print("  • Para cada uma das 8 linhas de seleção, conectar (fusível aberto/fechado)")
print("    nas colunas S correspondentes ao valor desejado.")
print("  • Exemplo de conteúdo (valores livres para escolher):")
end_vals = [("000",0b1010), ("001",0b0101), ("010",0b1111), ("011",0b0000),
            ("100",0b1100), ("101",0b0011), ("110",0b1001), ("111",0b0110)]
print(f"    {'End.':>5}  {'Conteúdo':>8}  (binário)")
for addr, val in end_vals:
    print(f"    {addr:>5}    {val:04b}  ({val})")

section("EXERCÍCIO 31")
print("  Imagem: 640×420 pixels | 4 bytes/pixel")
W, H, bpp = 640, 420, 4
px = W * H
bytes_img = px * bpp
bytes_10  = bytes_img * 10
ram_128   = 128 * 1024**2
qtd       = ram_128 // bytes_img

print(f"\n  a) Memória para 1 imagem:")
print(f"       {W} × {H} × {bpp} = {bytes_img:,} bytes ≈ {bytes_img/1024:.1f} KB")

print(f"\n  b) Memória para 10 imagens:")
print(f"       {bytes_10:,} bytes = {bytes_10/(1024**2):.4f} MB ≈ {bytes_10/(1024**2):.2f} MB")

print(f"\n  c) Imagens em 128 MB de RAM:")
print(f"       {ram_128:,} ÷ {bytes_img:,} = {qtd} imagens completas")

section("EXERCÍCIO 32")
print("  ROM: 16 linhas de endereço, 4 linhas de saída de dados.")
le, ld = 16, 4
N      = 2 ** le
T_bits = N * ld
T_kb   = (T_bits // 8) // 1024
print(f"  N = 2^{le} = {N:,} células de {ld} bits cada")
print(f"  T = {N:,} × {ld} = {T_bits:,} bits")
print(f"  T = {T_bits//8:,} bytes = {T_kb} KB  ←  RESPOSTA")

section("EXERCÍCIOS 33 e 34  (conceituais — sem cálculo)")
print("  33) 'Um computador com mais poder de processamento pode armazenar mais programas'?")
print("      FALSO. Capacidade de memória e poder de processamento são grandezas")
print("      independentes. Um processador rápido com pouca RAM armazena poucos")
print("      programas ao mesmo tempo.")
print()
print("  34) 'Vale aumentar a capacidade de MP para que o acesso aos discos seja mais rápido'?")
print("      VERDADEIRO. Mais RAM reduz a necessidade de acesso ao disco (memória")
print("      secundária), que é ordens de grandeza mais lento. O SO usa a RAM extra")
print("      como cache de disco (page cache) e reduz o swap, acelerando o sistema.")