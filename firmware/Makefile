# Nomes das ferramentas
CC = arm-none-eabi-gcc
MACH = cortex-m3

# FLAGS DE COMPILAÇÃO 
# -mcpu=$(MACH): Diz que o alvo é o Cortex-M3
# -mthumb: Aponta o formato de instruções do ARM que o Cortex-M3 usa (Thumb)
# -O0: Desliga as otimizações do compilador 
# -g: Guarda informações de debug para o GDB conseguir ler as linhas de código depois
# --specs=rdimon.specs: Substitui a biblioteca padrão do C pela versão de Semihosting
CFLAGS = -mcpu=$(MACH) -mthumb -O0 -g --specs=rdimon.specs

# FLAG DE LINKAGEM
# -T linker.ld: Diz onde está o mapa de memória da nossa placa
LDFLAGS = -T linker.ld

# ARQUIVOS DO PROJETO
SRCS = startup.c main.c

# Nome do arquivo final gerado Executable and Linkable Format
TARGET = firmware.elf


# Regra para compilar o código
build:
	$(CC) $(CFLAGS) $(LDFLAGS) $(SRCS) -o $(TARGET)

# Regra para rodar o QEMU
# -M mps2-an385: O nome exato da nossa placa virtual
# -m 16M: 16 Megabytes de memória
# -nographic: Roda direto no terminal, sem tentar abrir uma janela nova
# -kernel: O arquivo que ele vai tentar executar
# -semihosting: O comando que avisa o QEMU para interceptar os printfs
run: build
	qemu-system-arm -M mps2-an385 -cpu $(MACH) -m 16M -nographic -kernel $(TARGET) -semihosting

# Regra para limpar a sujeira (apaga o arquivo compilado antigo)
clean:
	rm -f $(TARGET)