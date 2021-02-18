# Toy-MD
This is a tiny repository with Python code to play with molecular
dynamics (MD) simulations. It can be extended for testing and
trying new algorithms or potentials. 

Disclaimer: the stuff in here is not suitable for production simulations.

Example for running:
	
	./toy_md.py -h

This will give you the command line help for the script.

To run the CO2 simulation example 

	cd carbon-dioxide

	../toy_md.py -c co2.pdb -p params.txt -f force_field.txt -o traj.pdb -w co2-output.pdb


## License

This code is licensed under the MIT-License.
