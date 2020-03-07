install:
	python -m pip install --user requests name_prettier tabulate
	mkdir -p ~/.local/bin
	cp plany.py ~/.local/bin/plany
