/************************************************************/
/* Author: Caden Coffin */
/* Major: Computer Science */
/* Creation Date: September 13, 2023 */
/* Due Date: September 19, 2023 */
/* Course: CSC328 010 */
/* Professor Name: Dr. Scwesinger */
/* Assignment: #2 */
/* Filename: project2.c */
/* Purpose: This program uses the fork() system call 
to create children and parent processes given
by entries in the command line. */
/************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int x; 

/*************************************************************************/
/* */
/* Function name: childCreation */
/* Description: Actions for child proccesses. Takes the children and user inputs . */
/*              to complete tasks written in code block */
/* Parameters: childNum (current child) */
/*             num (pointer to integer for action) */
/*             nump (pointer to integer for action) */
/* Return Value: none */
/* */
/*************************************************************************/
void childCreation(int childNum, int *num, int *nump);



/*************************************************************************/
/* */
/* Function name: createProcCon */
/* Description: Creates number of processes  concurrently based off of user input. Cannot exceed */
/* 10 entries or fall below 1. */
/* Parameters: numproc (the number of processes entered) */
/*             intnum (initial value of integer variable to be used by children) */
/*             intnump (initial value of integer pointer to be used by children) */
/* Return Value: none */
/* */
/*************************************************************************/
void createProcCon(int numproc, int *intnum, int *intnump);

/*************************************************************************/
/* */
/* Function name: createProcSeq */
/* Description: Creates number of processes  Sequentially based off of user input. Cannot exceed */
/* 10 entries or fall below 1. */
/* Parameters: numproc (the number of processes entered) */
/*             intnum (initial value of integer variable to be used by children) */
/*             intnump (initial value of integer pointer to be used by children) */
/* Return Value: none */
/* */
/*************************************************************************/
void createProcSeq(int numproc, int *intnum, int *intnump);

/*************************************************************************/
/* */
/* Function name: waitProc */
/* Description: Waits for certain number of process to be completed. */
/* Parameters: numproc (the number of processes entered) */
/* Return Value: none - waits for child processes to exit */
/* */
/*************************************************************************/
void waitProc(int numproc);

int main(int argc, char *argv[]) { 

if (argc <5) {
		printf("Arguments:<Number of Procs. > <Init. value of X> <Init. value of Num> <Init. value of Nump> [output file]\n");
		return 1;
	}
	
if (argc >6) {
		printf("Arguments:<Number of Procs. > <Init. value of X> <Init. value of Num> <Init. value of Nump> [output file]\n");
		return 1;
}

	int num;
	int nump;
	
	int numproc = atoi(argv[1]);
	x = atoi(argv[2]);
	int intnum = atoi(argv[3]);
	int* intnump = (int *)malloc(sizeof(int));
	*intnump = atoi(argv[4]);
	
	/* FILE* usage from https://users.cs.utah.edu/~germain/PPS/Topics/C_Language/file_IO.html */
	FILE *outputFile = fopen(argv[5], "w");
	
	createProcSeq(numproc,&intnum, intnump);
	printf("Sequential Creation Compelte\n");
	createProcCon(numproc, &intnum, intnump);
	
	waitProc(numproc);
	

	printf("Program complete\n");
	
	if (outputFile != stdout) {
		fclose(outputFile);
	}
	return 0;

}

void childCreation(int childNum, int *num, int *nump){
		pid_t pid = getpid(); 
		
		printf("BEFORE INCREMENT: Child %d (PID %d):  x = %d, num = %d, nump = %d\n", childNum, pid, x, *num, *nump);
		
		x += 50; 
		(*num)++;
		(*nump)++;
		
		printf("AFTER INCREMENT: Child %d (PID %d): x = %d, num = %d, nump = %d\n", childNum, pid, x, *num, *nump);
		
		exit(0);
}

void createProcCon(int numproc, int *intnum, int *intnump){
	if (numproc > 10) { 
		printf("Fork Failed, No more then 10 child processes\n");
		exit(1);
	}
	
	if (numproc <= 0) {
		printf("Fork Failed, more then 0 child processes required\n");
		exit(1);
	}
	
	for (int i = 1; i <= numproc; i++) {
	pid_t child = fork();
	
	if (child == -1){
		perror("Fork Failed");
		exit(1);
	}
		if (child == 0) {
		childCreation(i, intnum, intnump);
		exit(0);
		}
	}
}

void createProcSeq(int numproc, int *intnum, int *intnump){
	if (numproc > 10) { 
		printf("Fork Failed, No more then 10 child processes\n");
		exit(1);
	}
	
	if (numproc <= 0) {
		printf("Fork Failed, more then 0 child processes required\n");
		exit(1);
	}
	
	for (int i = 1; i <= numproc; i++) {
	pid_t child = fork();

	if (child == -1) {
            perror("Fork Failed");
            exit(1);
        }
		if (child == 0) {
		childCreation(i, intnum, intnump);
		exit(0);
		}
		else{
			wait(NULL);
		}
	}
}
void waitProc  (int numproc) {
	for (int i = 0; i < numproc; i++) {
		wait(NULL);
	}
}
