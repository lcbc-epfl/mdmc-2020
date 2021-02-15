#include <iostream>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <string>

using namespace std;

double calculateStateOccupancy(double reducedTemperature, int stateEnergy);
double calculateStateOccupancy_s1(double reducedTemperature, int stateEnergy);
double calculateStateOccupancy_s2(double reducedTemperature, int stateEnergy);
double calculateStateOccupancy_rotor(double reducedTemperature, int stateEnergy);

void outputToFile(double *distribution, string outputFile);

int numberOfEnergyLevels = 0;
double reducedTemperature = 0.0;
double partitionFunction = 0.0;

double *distribution;

int main(int argc, char * argv []) {
	
	numberOfEnergyLevels = atoi(argv[1]);
	reducedTemperature = atof(argv[2]);

	distribution = new double [numberOfEnergyLevels];
	for(int i = 0; i < numberOfEnergyLevels; i++)
	{
		// To modify. Compute distribution and partition function//
		distribution[i]=1.0;
  		partitionFunction=1.0;
	}
	outputToFile(distribution, "results.dat");
	delete [] distribution;

	
	return 0;
}

void outputToFile(double *distribution, string outputFile) {
	ofstream output;
	output.open(outputFile);

  	for (int i = 0; i < numberOfEnergyLevels; i++) {
    		output << i << " " << distribution[i]/partitionFunction << "\n";
  	}
  	output.close();
}

double calculateStateOccupancy(double reducedTemperature, int i) {
  	//Calculate the occupancy for state i without degenerescence
	double stateOccupancy = 1.0;
	return stateOccupancy;
}

double calculateStateOccupancy_s1(double reducedTemperature, int i) {
  	//Calculate the occupancy for state i with s+1 degenerescence
	double stateOccupancy = 1.0;
	return stateOccupancy;
}

double calculateStateOccupancy_s2(double reducedTemperature, int i) {
  	//Calculate the occupancy for state i with s+2 degenerescence
	double stateOccupancy = 1.0;
	return stateOccupancy;
}

double calculateStateOccupancy_rotor(double reducedTemperature, int i) {
  	//Calculate the occupancy for state i of a linear rotor 
	double stateOccupancy = 1.0;
	return stateOccupancy;
}

