PYTHON=python3
PACKAGE=gerobust

all: compile
	$(PYTHON) -m $(PACKAGE)

t: test
test:
	pytest $(PACKAGE) -v --ignore=venv/ --doctest-module


compile:  # the C code
	gcc -O3 -frounding-math -fsignaling-nans $(PACKAGE)/predicates.c -fPIC --shared -o $(PACKAGE)/lib_predicates.so


test_register:
	$(PYTHON) setup.py register -r https://testpypi.python.org/pypi
test_install:
	$(PYTHON) setup.py sdist upload -r https://testpypi.python.org/pypi
	$(PYTHON) -m pip install -U -i https://testpypi.python.org/pypi $(PACKAGE)

register:
	$(PYTHON) setup.py register
upload:
	$(PYTHON) setup.py sdist upload
install:
	$(PYTHON) -m pip install -U $(PACKAGE)

devel:
	pip devel
