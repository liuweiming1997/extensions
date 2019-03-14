SHELL=/bin/bash

CHROME_CONTAINER = chrome_redis chrome_db
WEB_CRAWLER = web_crawler

define do_command
	cd ./docker/ && $(1)
endef

init:
	@if [[ ! -d ./volumes/log/crawler ]]; then mkdir -p ./volumes/log/crawler; fi
	@if [[ ! -d ./volumes/tmp ]]; then mkdir -p ./volumes/tmp; fi
	@if [[ ! -f ./volumes/log/crawler/crontab.log ]]; then touch ./volumes/log/crawler/crontab.log; fi
	
	# create redis && mysql
	@echo "Running redis"
	$(call do_command, docker-compose up --build -d chrome_redis)

	@echo "Running mysql"
	$(call do_command, docker-compose up --build -d chrome_db)

	# create web crawler crontab
	@echo "Running web_crawler"
	$(call do_command, docker-compose up --build -d web_crawler)

update:
	$(call do_command, docker rm -f $(WEB_CRAWLER) || true)
	@echo "Running web_crawler"
	$(call do_command, docker-compose up --build -d web_crawler)

clean:
	$(call do_command, docker rm -f $(WEB_CRAWLER) $(CHROME_CONTAINER))
