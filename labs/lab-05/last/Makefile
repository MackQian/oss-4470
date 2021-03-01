all: static_block dynamic_block
clean:
	rm static_block dynamic_block stlib.a shlib.so block.o program.o
block.o: source/block.c
	cc -c source/block.c -o block.o
program.o: program.c
	cc -c program.c -o program.o
stlib.a: block.o
	ar qc stlib.a block.o
shlib.so: block.o
	cc -shared -o shlib.so block.o
dynamic_block: shlib.so program.o
	cc program.o shlib.so -o dynamic_block -Wl,-rpath='$$ORIGIN'
static_block: stlib.a program.o
	cc program.o stlib.a -o static_block