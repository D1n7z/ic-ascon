#include <stdio.h>

extern void initialise_monitor_handles(void);

int main(void) {
    initialise_monitor_handles();

    printf("\nHello, World!\n");
    return 0;
}