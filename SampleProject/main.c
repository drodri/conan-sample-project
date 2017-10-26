#include <project.h>

uint16_t counter = 0;
void inc(void) 
{
    static uint8_t state = 0;
    if(++counter == 500) 
    {
        state ^= 1;
        LED_1_Write(state);       
        counter = 0;
    }
}

int main()
{
    CySysTickInit();
    CySysTickSetCallback(0, inc);
    CySysTickEnable();
    CyGlobalIntEnable; 
    for(;;)
    {
   
    }
}
