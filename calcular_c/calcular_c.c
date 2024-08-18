
#include <stdio.h>
#include <stdlib.h> // Para rand() y RAND_MAX

float calcularC(int nsamples) {
    int i ,acc = 0;
    float x , y , ret_pi;
    int samples;

    for (i = 0; i < nsamples; i++){
        x = (float)rand() / RAND_MAX;
        y = (float)rand() / RAND_MAX;
        if ((x * x + y * y) < 1.0){
            acc += 1;
        }
    }
    ret_pi = 4.0 * acc / nsamples;
    return ret_pi;
    
}
