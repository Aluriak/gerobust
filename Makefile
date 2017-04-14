PYTHON=python3
PACKAGE=gerobust
TEST_DIR=test/

all:
	$(PYTHON) -m $(PACKAGE)

t: tests
tests:
	- $(PYTHON) setup.py build_ext -i
	pytest $(TEST_DIR) -v


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
	$(MAKE) tests
