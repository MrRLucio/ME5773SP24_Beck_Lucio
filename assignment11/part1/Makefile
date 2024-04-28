
#FC = ifort


# Define the general flags.
#FCFLAGS = -O0 -L.

#MODSRCS = searchutils.f90
#MAINSRC = main_program.f90

all: f2py #searchutils.mod  f2py

#searchutils.mod: searchutils.f90

#	$(FC) -c searchutils.f90 $(FCFLAGS)
#	ar rc libsearchutils.a searchutils.o
#	ranlib libsearchutils.a


f2py: searchutils.f90

	python3 -m numpy.f2py -c --fcompiler=intelem searchutils.f90 -m searchUtilsTeam01 

.PHONY: clean


clean:
	rm -f *.exe *.o *.mod *.so
