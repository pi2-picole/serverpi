#include <stdlib.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <signal.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <termios.h>
#include "Stepper.h"
#include <dirent.h>
#include <fcntl.h>

//Pinos dos perifericos
#define MOTOR1 0
#define MOTOR2 2
#define MOTOR3 3
#define MOTOR4 12
#define MOTOR_SELECAO1 8
#define MOTOR_SELECAO2 9
#define RELE_MOTOR 22

int main(int argc, char **argv)
{
	//Dados do motor
	int motor[4];

	for(int i = 0 ; i < 4 ; i++) {
		motor[i] = atoi(argv[i+1]);
	}

	Stepper myStepper(200, MOTOR1, MOTOR2, MOTOR3, MOTOR4);
	myStepper.setSpeed(60);
	// Pinos 3 e 4 configurados como saida
	pinMode(MOTOR_SELECAO1, OUTPUT);
	pinMode(MOTOR_SELECAO2, OUTPUT);
	pinMode(RELE_MOTOR, OUTPUT);
	
	//Motor
	for(int i = 0 ; i < 4 ; i++)
	{
		while(motor[i]>0)
		{
			digitalWrite(RELE_MOTOR, 1);//Ligar o RELE
			delay(100);//Esperar o RELE ligar
			//Escolher qual motor vai girar
			digitalWrite(MOTOR_SELECAO1, i%2);
			digitalWrite(MOTOR_SELECAO2, i/2);

			printf("Motor %d acionado\n", i+1);//Mostrar no terminal qual motor foi acionado
			myStepper.step(200); // Girar o motor 1 revolucao
			motor[i]--;
			delay(500);
		}
	}
	digitalWrite(RELE_MOTOR, 0);//Desligar RELE

	return 0;
}
