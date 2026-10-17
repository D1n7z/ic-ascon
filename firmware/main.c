#include <stdio.h>

extern void initialise_monitor_handles(void);

int main(void) {
    initialise_monitor_handles();

    volatile int soma = 0;

    printf("Início da execução do programa\n");
    for (int i = 0; i < 5; i++) {
        soma += i;
    }
    printf("Soma: %d\n", soma);

    return 0;
}