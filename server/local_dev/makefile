SHELL=/bin/bash

CHROME_SERVER = chrome_server

define do_command
	cd ./docker/ && $(1)
endef

init:
	@if [[ ! -d ./volumes/log ]]; then mkdir -p ./volumes/log; fi
	@if [[ ! -d ./volumes/tmp ]]; then mkdir -p ./volumes/tmp; fi
	
	# create chrome_server
	@echo "Running chrome_server"
	$(call do_command, docker-compose up --build -d chrome_server)

update:
	$(call do_command, docker rm -f $(CHROME_SERVER) || true)
	@echo "Running updating chrome_server"
	$(call do_command, docker-compose up --build -d chrome_server)

clean:
	$(call do_command, docker rm -f $(CHROME_SERVER))
