//Código adaptado do repositorio: https://github.com/cortexm/baremetal

#include <stdint.h>

// Aponta que a função main() está em outro arquivo 
extern int main(void);

// Aponta os endereços das seções do programa
extern uint32_t __data_start, __data_end, __data_load;
extern uint32_t __bss_start, __bss_end;

// Puxa o endereço do topo da RAM 
extern uint32_t _estack; 

void copy_data(void) {
    uint32_t *src = &__data_load;
    uint32_t *dst = &__data_start;
    while (dst < &__data_end) *dst++ = *src++;
}

void zero_bss(void) {
    uint32_t *dst = &__bss_start;
    while (dst < &__bss_end) *dst++ = 0;
}

void RESET_handler(void) {
    copy_data();
    zero_bss();
    main();
    while (1);
}

// Define a tabela de vetores de interrupção
__attribute__((section(".isr_vector")))
uint32_t *vector_table[] = {
    (uint32_t *)&_estack,       // Posição 0: Onde fica o Stack (Pilha)
    (uint32_t *)RESET_handler,  // Posição 1: Onde começa o código
};