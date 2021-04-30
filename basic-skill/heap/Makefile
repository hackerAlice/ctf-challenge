cc=gcc
target=mthread

all : $(target)
.PHONY : all

mthread : mthread.c
	$(cc) -pthread -m32 $< -o $@


clean:
	rm $(target)
