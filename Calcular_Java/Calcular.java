
package Calcular_Java;

import java.util.Random;
import java.time.Instant;

/**
 * Calcular
 */
public class Calcular {

    public static float calcularJava(int nsamples) {
        Random random = new Random();
        int acc = 0;
        float x, y;

        for (int i = 0; i < nsamples; i++) {
            x = random.nextFloat();
            y = random.nextFloat();
            if ((x * x + y * y) < 1.0) {
                acc += 1;
            }
        }
        return (float) (4.0 * acc / nsamples);

    }

    public static void main(String[] args) {
        Instant time_inicial = Instant.now();
        float pi_estimacion = calcularJava(999999999);
        Instant time_final = Instant.now();

        double tiempo_ejecucion_Java = (time_final.toEpochMilli() - time_inicial.toEpochMilli()) / 1000.0; // Convertir
                                                                                                           // a segundos
        System.out.println("Resultado Java: " + pi_estimacion + " " + "tardo:"+ " " + tiempo_ejecucion_Java);
    }

}
