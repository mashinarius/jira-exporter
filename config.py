import configparser


class AppConfig(object):
    def __init__(self, filename):

        config = configparser.ConfigParser()
        print('reading configuration from file: ' + str(filename))
        config.read(filename)

        jira_config = config['JIRA']
        wiki_config = config['WIKI']
        selenoid_config = config['SELENOID']
        exporter_config = config['EXPORTER']

        self.HTTP_PORT = 8000

        self.JIRA_USERNAME = jira_config['username']
        self.JIRA_PASSWORD = jira_config['password']

        if jira_config.get('check-url'):
            self.JIRA_CHECK_URL = jira_config['check-url']
        else:
            self.JIRA_CHECK_URL = "https://my.jira.com"

        self.WIKI_USERNAME = wiki_config['username']
        self.WIKI_PASSWORD = wiki_config['password']

        if wiki_config.get('check-url'):
            self.WIKI_CHECK_URL = wiki_config['check-url']
        else:
            self.WIKI_CHECK_URL = "https://my.wiki.com"

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


        # JIRA metrics
        if exporter_config.get('metric-name-jira-open-login-page'):
            self.EXPORTER_METRIC_JIRA_PAGE1 = exporter_config['metric-name-jira-open-login-page']
        else:
            self.EXPORTER_METRIC_JIRA_PAGE1 = 'jira_open_login_page_seconds'

        if exporter_config.get('metric-name-jira-load-issue-page'):
            self.EXPORTER_METRIC_JIRA_PAGE2 = exporter_config['metric-name-jira-load-issue-page']
        else:
            self.EXPORTER_METRIC_JIRA_PAGE2 = 'jira_load_ticket_page_seconds'

        if exporter_config.get('metric-name-jira-total'):
            self.EXPORTER_METRIC_JIRA_TOTAL = exporter_config['metric-name-jira-total']
        else:
            self.EXPORTER_METRIC_JIRA_TOTAL = 'jira_load_total_seconds'


        # WIKI metrics
        if exporter_config.get('metric-name-wiki-login-page'):
            self.EXPORTER_METRIC_WIKI_PAGE1 = exporter_config['metric-name-wiki-login-page']
        else:
            self.EXPORTER_METRIC_WIKI_PAGE1 = 'wiki_open_login_page_seconds'

        if exporter_config.get('metric-name-wiki-load-page'):
            self.EXPORTER_METRIC_WIKI_PAGE2 = exporter_config['metric-name-wiki-load-page']
        else:
            self.EXPORTER_METRIC_WIKI_PAGE2 = 'wiki_load_default_page_seconds'

        if exporter_config.get('metric-name-wiki-total'):
            self.EXPORTER_METRIC_WIKI_TOTAL = exporter_config['metric-name-wiki-total']
        else:
            self.EXPORTER_METRIC_WIKI_TOTAL = 'wiki_load_total_seconds'


