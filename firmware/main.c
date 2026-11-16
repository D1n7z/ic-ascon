#include <stdio.h>

extern void initialise_monitor_handles(void);

__attribute__((noinline)) 
int rotina_alvo(void) {
    volatile int soma = 0;
    for (int i = 0; i < 5; i++) {
        soma += i;
    }
    return soma;
}

int main(void) {
    initialise_monitor_handles();

    int resultado = rotina_alvo();
    printf("RESULTADO: %d\n", resultado);

    return 0;
}