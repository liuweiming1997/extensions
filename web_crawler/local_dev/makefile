SHELL=/bin/bash

CHROME_CONTAINER = chrome_redis chrome_db
WEB_CRAWLER = web_crawler

define do_command
	cd ./docker/ && $(1)
endef

init:
	mkdir -p ./volumes/log ./volumes/tmp
	
	# create redis && mysql
	@echo "Running redis"
	$(call do_command, docker-compose up --build -d chrome_redis)

	@echo "Running mysql"
	$(call do_command, docker-compose up --build -d chrome_db)

	# create web crawler crontab
	@echo "Running web_crawler"
	$(call do_command, docker-compose up --build -d web_crawler)

update:
	$(call do_command, docker rm -f $(WEB_CRAWLER))
	@echo "Running web_crawler"
	$(call do_command, docker-compose up --build -d web_crawler)

clean:
	$(call do_command, docker rm -f $(WEB_CRAWLER) $(CHROME_CONTAINER))
