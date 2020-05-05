#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define NUM_RAND 10000

#define SEED 0
#define DATE 05052020
#define DATE_INV 02025050
#define ABIGPRIME 100019 

/*
So what is a prng? Nothing more than: 

x0 = seed

i > 0
xi = (A * xi-1 + B )% C

By calling it n times we get values x0, x1, x2, ... , xn-1

*/

int my_dummy_prng() {
	
	static int A = DATE, B = DATE_INV, C = ABIGPRIME;
	static long long last = SEED;
	return (int) (last = (((A*last) % INT_MAX) + B) % INT_MAX % C);
	
}
	

int main () {
	
	FILE *c_rand, *dummy_rand;
	
	c_rand = fopen("c_rand.txt", "w");
	dummy_rand = fopen("dummy_rand.txt", "w");
	
	for(int i = 1; i <= NUM_RAND; i++) 
		fprintf(c_rand, "%d%c", rand(), i%10 == 0 ? '\n' : ' ');
	for(int i = 1; i <= NUM_RAND; i++) 
		fprintf(dummy_rand, "%d%c", my_dummy_prng(), i%10 == 0 ? '\n' : ' ');
	
	fclose(c_rand);
	fclose(dummy_rand);
	
	return 0;
}