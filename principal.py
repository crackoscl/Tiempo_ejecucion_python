import time
# necesario para usar el .so de c
import ctypes
from calcular_py.calcular import calcular_
from calcular_cython.calcular_cython import calcular_cython

# Cargar el .so de C
lib = ctypes.CDLL('./calcular_c/calcular_c.so')
# Definir los tipos de argumentos y el tipo de retorno de la función
lib.calcularC.argtypes = [ctypes.c_int]
lib.calcularC.restype = ctypes.c_float

# Cargar el .so de Go
libGo = ctypes.CDLL('./calcular_go/calcular_go.so')
# Definir los tipos de argumentos y el tipo de retorno de la función
libGo.CalcularGo.argtypes = [ctypes.c_int]
libGo.CalcularGo.restype = ctypes.c_float

nsamples = 999999999

time_inicial = time.time()
pi_estimacion_py = calcular_(nsamples)
time_final = time.time()
tiempo_ejecucion_py = time_final - time_inicial

print(f"Resultado Python: {pi_estimacion_py} tardo: {tiempo_ejecucion_py:.4f}")

time_inicial_cython = time.time()
pi_estimacion_cython = calcular_cython(nsamples)
time_final_cython = time.time()
tiempo_ejecucion_cython = time_final_cython - time_inicial_cython

print(f"Resultado Cython: {pi_estimacion_cython} tardo: {
      tiempo_ejecucion_cython:.4f}")


time_inicial_c = time.time()
pi_estimacion_c = lib.calcularC(nsamples)
time_final_c = time.time()
tiempo_ejecucion_c = time_final_c - time_inicial_c

print(f"Resultado C: {pi_estimacion_c} tardo: {tiempo_ejecucion_c:.4f}")


time_inicial_go = time.time()
pi_estimacion_go = libGo.CalcularGo(nsamples)
time_final_go = time.time()
tiempo_ejecucion_go = time_final_go - time_inicial_go

print(f"Resultado Go: {pi_estimacion_go} tardo: {tiempo_ejecucion_go:.4f}")
