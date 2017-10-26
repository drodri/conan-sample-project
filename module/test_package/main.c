#include <stdint.h>
#include <stdio.h>
#include "module.h"

int main(void) {
	uint8_t a = 1;
	uint8_t b = 255;
	uint16_t c = add(a, b);
	printf("result %d", c);
}