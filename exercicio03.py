rom = {
    0b00: 0b0101,
    0b01: 0b1011,
    0b10: 0b1110,
    0b11: 0b0000,
}

def ler_rom(endereco):
    if endereco not in rom:
        raise ValueError(f"Endereço inválido: {endereco}")
    return rom[endereco]

for endereco in range(4):
    conteudo = ler_rom(endereco)
    print(f"End. {endereco:02b} → {conteudo:04b}")