import time
import sys

from prometheus_client import Gauge
from prometheus_client import start_http_server

from config import AppConfig
from jira_test import test_jira_load_ticket_seconds

if __name__ == '__main__':

    config_file = 'atlassian-exporter.ini'

    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    app_config = AppConfig(filename=config_file)

    # Start up the server to expose the metrics.
    print('Starting http server on port: ' + str(app_config.HTTP_PORT))
    start_http_server(app_config.HTTP_PORT)

    # Generate some requests.
    g1 = Gauge(app_config.EXPORTER_METRIC_NAME_LOGIN, 'Num of seconds to login to JIRA with Selenium webdriver')
    g2 = Gauge(app_config.EXPORTER_METRIC_NAME_LOAD, 'Num of seconds to load JIRA issue page with Selenium webdriver')
    while True:
        login_time_sec = None
        load_issue_sec = None
        try:
            login_time_sec, load_issue_sec = test_jira_load_ticket_seconds(app_config)
        except Exception as e:
            print(e)
        if login_time_sec and load_issue_sec:
            g1.set(login_time_sec)
            g2.set(load_issue_sec)

        time.sleep(app_config.EXPORTER_SCRAPE_PERIOD_SEC)
