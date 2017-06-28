all:
	g++ -c Stepper.cpp -lwiringPi
	g++ -o rodar_motor rodar_motor.cpp Stepper.o -lwiringPi
