import configparser


class AppConfig(object):
    def __init__(self, filename):

        config = configparser.ConfigParser()
        config.read(filename)

        jira_config = config['JIRA']
        selenoid_config = config['SELENOID']
        exporter_config = config['EXPORTER']

        self.HTTP_PORT = 8000

        self.JIRA_USERNAME = jira_config['username']
        self.JIRA_PASSWORD = jira_config['password']

        if jira_config.get('check-url'):
            self.JIRA_CHECK_URL = jira_config['check-url']
        else:
            self.JIRA_CHECK_URL = "https://my.jira.com"

        if selenoid_config.get('hub-url'):
            self.SELENOID_HUB_URL = selenoid_config['hub-url']
        else:
            self.SELENOID_HUB_URL = "http://127.0.0.1:4444/wd/hub"

        if selenoid_config.get('browser'):
            self.SELENOID_BROWSER = selenoid_config['browser']
        else:
            self.SELENOID_BROWSER = "chrome"

        if selenoid_config.get('browser-version'):
            self.SELENOID_BROWSER_VERSION = selenoid_config['browser-version']  # None #"66.0"
        else:
            self.SELENOID_BROWSER_VERSION = None

        if exporter_config.get('scrape-period-seconds'):
            self.EXPORTER_SCRAPE_PERIOD_SEC = int(exporter_config['scrape-period-seconds'])
        else:
            self.EXPORTER_SCRAPE_PERIOD_SEC = 300

        if exporter_config.get('scrape-timeout-seconds'):
            self.EXPORTER_SCRAPE_TIMEOUT_SEC = int(exporter_config['scrape-timeout-seconds'])
        else:
            self.EXPORTER_SCRAPE_TIMEOUT_SEC = 300

        if exporter_config.get('metric-name'):
            self.EXPORTER_METRIC_NAME = exporter_config['metric-name']
        else:
            self.EXPORTER_METRIC_NAME = 'jira_load_ticket_seconds'
