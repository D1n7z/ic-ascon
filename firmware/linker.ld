/* Código adaptado do repositorio: https://github.com/cortexm/baremetal */

ENTRY(RESET_handler)

MEMORY
{
    /* Aponta o inicio da memória FLASH */
    FLASH (rx) : ORIGIN = 0x00000000, LENGTH = 16M
    /* Aponta o inicio da memória RAM  */
    RAM (rwx)  : ORIGIN = 0x20000000, LENGTH = 4M
}

/* Aponta o endereço do topo da stack da RAM */
_estack = ORIGIN(RAM) + LENGTH(RAM);

SECTIONS
{
    .text :
    {
        /* Coloca o vetor de interrupções no início da memória FLASH */
        KEEP(*(.isr_vector))
        
        *(.text*)
        *(.rodata*)
        . = ALIGN(4);
    } > FLASH

    __data_load = LOADADDR(.data);

    .data :
    {
        . = ALIGN(4);
        __data_start = .;
        *(.data*)
        . = ALIGN(4);
        __data_end = .;
    } > RAM AT > FLASH

    .bss :
    {
        . = ALIGN(4);
        __bss_start = .;
        __bss_start__ = .;
        *(.bss*)
        *(COMMON)
        . = ALIGN(4);
        __bss_end = .;
        __bss_end__ = .;
    } > RAM

    . = ALIGN(4);
    end = .;
    __end__ = .;
}