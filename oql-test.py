from os import environ
from omnivoreql import OmnivoreQL

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

api_key = environ.get('OMNIVORE_API_KEY', "FFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF")

omnivoreql_client = OmnivoreQL(api_key)

profile = omnivoreql_client.get_profile()

# result = omnivoreql_client.save_url("https://pypi.org/project/omnivoreql/")

# articles = omnivoreql_client.get_articles()

# username = profile['me']['profile']['username']
# slug = articles['search']['edges'][0]['node']['slug']
# articles = omnivoreql_client.get_article(username, slug)

# labels = omnivoreql_client.get_labels()
# subscriptions = omnivoreql_client.get_subscriptions()