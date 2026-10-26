import gdb

gdb.execute("set pagination off")

print("Injetor de falhas iniciado.")

# Conectar ao QEMU
gdb.execute("target remote :1234")

# Adicionar ponto de interrupção no início da função main
gdb.execute("break main")
gdb.execute("continue")

# Pula para o início do laço for
for _ in range(3):
    gdb.execute("next")

# Entrar no laço for
for _ in range(8):
    gdb.execute("stepi")

# Lê o valor do registrador r3
valor_r3 = gdb.parse_and_eval("$r3")
print(f"Valor original do registrador r3: {valor_r3}")

# Altera o valor do registrador r3 para 100
print("Alterando o valor do registrador pc para 0.")
gdb.execute("set $pc = 0")

# Continua a execução do programa
print("Continuando a execução do programa")
gdb.execute("continue")

# Desconecta do GDB e encerra o script
gdb.execute("quit")
