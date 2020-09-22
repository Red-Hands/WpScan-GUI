PROGRAM_NAME=wpscan-gui
VERSION=1.23.2

DATA_DIR=/usr/share
DOCS_DIR=$(DATA_DIR)/doc
PROGRAM_DIR=/usr/local/bin


install:

	
	install -Dm755 wpscan-gui.sh $(PROGRAM_DIR)/$(PROGRAM_NAME)
	install -Dm755 wpscan.py $(PROGRAM_DIR)/wpscan.py
uninstall:

	rm -Rf $(PROGRAM_DIR)/$(PROGRAM_NAME)
	rm -Rf $(DATA_DIR)/$(PROGRAM_NAME)
	rm -Rf $(DOCS_DIR)/$(PROGRAM_NAME)
