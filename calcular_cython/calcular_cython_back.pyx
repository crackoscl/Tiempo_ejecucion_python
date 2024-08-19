from libc.stdlib cimport rand, srand, RAND_MAX
from libc.time cimport time
"""
calcular el valor de π utilizando el método de Monte Carlo
"""

cpdef calcular_cython(int nsamples):
    cdef int i, acc=0
    cdef float x, y , ret_pi

    # Inicializa la semilla para el generador de números aleatorios
    srand(time(NULL))


    for i in range(nsamples):
        x = rand() / float(RAND_MAX)
        y = rand() / float(RAND_MAX)
        if (x * x + y * y) < 1.0:
            acc += 1
    ret_pi = 4.0 * acc / nsamples
    return ret_pi
