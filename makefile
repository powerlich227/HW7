CFLAGS = -shared
LIBS = -lm
CC = gcc

all: libhmwk7

simulation.o:	simulation.c simulation.h
	$(CC) $(CFLAGS)	-fpic -c simulation.c

libhmwk7:	simulation.o
	$(CC) $(CFLAGS) $(LIBS) -o libhmwk7.so simulation.o

clean:
	rm -f *.o libhmwk7
