PYTHON=python3
PACKAGE=gerobust

all: compile
	$(PYTHON) -m $(PACKAGE)

t: tests
tests: compile
	pytest $(PACKAGE) -v --ignore=venv/ --doctest-module


compile:  # the C code
	swig -python $(PACKAGE)/geolib.i
	gcc -O3 -frounding-math -fsignaling-nans -I/usr/include/python3.5m $(PACKAGE)/geolib{,_wrap}.c -fPIC --shared -o $(PACKAGE)/_wrapped_geolib.so


register:
	$(PYTHON) setup.py register
upload:
	$(PYTHON) setup.py sdist upload
install:
	$(PYTHON) -m pip install -U $(PACKAGE)

devel:
	pip devel

test_install:
	- rm -r ./venv/lib/python3.5/site-packages/gerobust-*/
	$(PYTHON) setup.py install
	ls -Rc ./venv/lib/python3.5/site-packages/gerobust-*/
	cd && $(PYTHON) -c "import gerobust"
