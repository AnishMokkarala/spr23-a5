CC = gcc
CFLAGS = -Wall -Wextra
OBJECTS = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o calculator

main.o: main.c operations.h
	$(CC) $(CFLAGS) -c main.c

addition.o: addition.c operations.h
	$(CC) $(CFLAGS) -c addition.c

subtraction.o: subtraction.c operations.h
	$(CC) $(CFLAGS) -c subtraction.c

multiplication.o: multiplication.c operations.h
	$(CC) $(CFLAGS) -c multiplication.c

division.o: division.c operations.h
	$(CC) $(CFLAGS) -c division.c

clean:
	rm -f $(OBJECTS) calculator
