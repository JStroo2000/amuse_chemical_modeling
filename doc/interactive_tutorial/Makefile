# convert all ipynb to rst files for inclusion into the 
# amuse documentation
#
# makefile depends on nbconvert script 
#
# nbconvert from github:
# https://github.com/ipython/nbconvert
# nbconvert depends on 
# ipython, markdown and pygments python modules
# plus pandoc app (pandoc needs haskell platform installed)
#
# 
#

AMUSE_DIR?=../..
-include ${AMUSE_DIR}/config.mk

NBCONVERT=jupyter nbconvert

PYTHONPATH=$(AMUSE_DIR)/src

PAGES=\
	01-Loading_AMUSE.ipynb\
	02-Quantities_with_units.ipynb\
	03-Generic_units.ipynb\
	04-Collections_of_Particles.ipynb\
	05-Attributes_and_functions_on_particle_collections.ipynb\
	06-Using_a_community_code.ipynb\
	07-Channels.ipynb\
	08-Grids.ipynb\

RSTPAGES=$(PAGES:.ipynb=.rst)
RSTFILES=$(PAGES:.ipynb=_files)

all: $(RSTPAGES)

clean:
	rm -f $(RSTPAGES)
	rm -Rf $(RSTFILES)
	
%.rst:%.ipynb
	$(NBCONVERT) --to rst "$<"
	
%.txt:%.rst
	python create_title.py "$<" > "$@"
	cat "$<" >> "$@"

notebook:
	jupyter notebook --pylab inline
