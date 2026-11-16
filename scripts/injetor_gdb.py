# Injetor que unifica a injeção de falhas

import os
import gdb

gdb.execute("set pagination off")
gdb.execute("set confirm off")

# Lendo parâmetros do orquestrador
registrador_alvo = os.environ.get("FI_REG", "r3")
bit_alvo = int(os.environ.get("FI_BIT", "0"))
passos = int(os.environ.get("FI_STEPS", "0"))

try:
    # Conectar ao QEMU
    gdb.execute("target remote :1234")

    # Adicionar pontos de parada
    gdb.execute("break rotina_alvo")
    gdb.execute("break Fim_execucao")
    gdb.execute("break HardFault_handler")
    gdb.execute("break MemManage_handler")
    gdb.execute("break BusFault_handler")
    gdb.execute("break UsageFault_handler")

    # Avança até o início da rotina alvo
    gdb.execute("continue")

    # Avança n passos
    for _ in range(passos):
        gdb.execute("stepi")
    
    # Lê o valor original do registrador alvo e injeta um bit flip
    valor_registrador = int(gdb.parse_and_eval(f"(unsigned int)${registrador_alvo}")) & 0xFFFFFFFF
    valor_alterado = valor_registrador ^ (1 << bit_alvo)

    gdb.execute(f"set ${registrador_alvo} = {valor_alterado}")
    print(f"[GDB_INJ] REG={registrador_alvo} BIT={bit_alvo} STEPS={passos} ORIG=0x{valor_registrador:08x} CORR=0x{valor_alterado:08x}")

    # Continua a execução do programa
    gdb.execute("continue")

    # Verifica em qual função o programa parou
    frame = gdb.selected_frame()
    func_parada = frame.name() if frame and frame.name() else "Desconhecida"
    print(f"[GDB_STATUS] PAROU_EM={func_parada}")

except gdb.error as e:
    print(f"[GDB_ERROR] {str(e)}")

finally:
    # Desconecta do GDB e encerra o script
    try:
        gdb.execute("kill")
    except Exception:
        pass
    gdb.execute("quit")