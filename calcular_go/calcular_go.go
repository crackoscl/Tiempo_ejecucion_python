package main

/*
#include <stdint.h>
*/

import "C"
import (
	"math/rand"
	"time"
)

//export CalcularGo
func CalcularGo(nsamples int32) float32 {
	var acc int64 = 0
	var x, y float64

	if nsamples <= 0 {
		return 0.0
	}

	rand := rand.New(rand.NewSource(time.Now().UnixNano()))

	for i := int32(0); i < nsamples; i++ {
		x = rand.Float64()
		y = rand.Float64()
		if (x*x + y*y) < 1.0 {
			acc++
		}
	}
	ret_pi := 4.0 * float32(acc) / float32(nsamples)
	return ret_pi

}

func main() {}
