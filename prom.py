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

    app_config = AppConfig(config_file)

    # Start up the server to expose the metrics.
    print('Starting http server on port: ' + str(app_config.HTTP_PORT))
    start_http_server(app_config.HTTP_PORT)

    # Generate some requests.
    g = Gauge(app_config.EXPORTER_METRIC_NAME, 'Num of seconds to login and load JIRA page with Selenium webdriver')
    while True:
        val = None
        try:
            val = test_jira_load_ticket_seconds(app_config)
            print(val)
        except Exception as e:
            print(e)
        if val:
            g.set(val)
        time.sleep(app_config.EXPORTER_SCRAPE_PERIOD_SEC)
