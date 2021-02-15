/**include library contents into code such that the functionality contained therein can be used**/
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <random>

/**declare that we use the standard namespace - saves me typing std::cout etc.**/
using namespace std;

/**Forward declare our PRNG wrappers**/
double random(double lower, double upper);
double random_mt(double lower, double upper);

/**Used by the random number generator to create a sequence of seemingly unrelated numerals**/
unsigned int globalSeed;

/**The values that we will set from the command line arguments char ** argv **/
unsigned int numberOfTrials;
double circleRadius;
double squareLength;

/**Number of decimal places to print the final pi value **/
unsigned int answerPrecision = 15;

/**Mersenne Twister PRNG**/
mt19937 mt_rand;

int main(int argc, char ** argv) {
	
	/**prevents bad input**/
	if (argc != 4) {
		cout << "Use: ./main NumberOfTrials CircleRadius SquareSide" << endl;
		return -1;
	}
	/**Set the seed as the time since the Epoch. Will result in a unique pseudo-random
	in a time period >= 1s**/
	globalSeed = time(nullptr);
	srand(globalSeed);
	mt_rand.seed(globalSeed);

	/**Parse our command-line arguments**/
	numberOfTrials = atoi(argv[1]);
	circleRadius = atof(argv[2]);
	squareLength = atof(argv[3]);

	/**prevent bad input**/
	if (circleRadius > (squareLength/2)) {
	cout << "Circle radius must be <= squareLength/2" << endl;
	return -1;
	}
	
	unsigned int successfulHits = 0;

	/**Print out session data for reference**/
	cout << "RAND_MAX: "<< RAND_MAX << endl;
	cout << "Using seconds since the Epoch: " << globalSeed << " as rand() seed" << endl;
	cout << "Number of trials: " << numberOfTrials << endl;
	cout << "Circle radius: " << circleRadius << endl;
	cout << "Square length: " << squareLength << endl;


	for (int i = 0; i < numberOfTrials; i++) {



		// **********************YOUR CODE HERE**********************
	
	
	}

	cout << "Successful hits: " << successfulHits << endl;
	
	double piEstimation = 0.0; //************************************* REPLACE WITH YOUR ESTIMATOR ****
	
	cout.precision(answerPrecision);
	cout << "Pi estimate: " << fixed << piEstimation << endl;
	return 0;
}

/**The definition for our pseudo-random number generator. Wrapped to provide more utility.
Since we are placing this below our main function, we have to forward declare this at the begining.**/
double random(double lower, double upper) {
	double r = (double) rand() / RAND_MAX;
	return (lower + (upper * r));
}

/**Mersenne-twister PRNG. This one is a little more complicated (and potentially more confusing) to use. random(double, double) provides a fine estimation also**/
double random_mt(double lower, double upper) {
	uniform_real_distribution<double> dist(lower, upper);
	return dist(mt_rand);
}



