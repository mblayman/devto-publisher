"""Publish scheduled articles to DEV."""
import datetime
import logging

from dateutil.parser import parse
from flask import Flask

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    """Zappa expects to have an app. Give it a basic one."""
    return "ok"


def publish_scheduled_articles():
    scheduled_articles = get_scheduled_articles()
    for scheduled_article in scheduled_articles:
        if should_publish(scheduled_article):
            publish(scheduled_article)


def get_scheduled_articles():
    """Get the schedule from GitHub."""
    logger.info("Fetch schedule.")
    import json

    with open("articles.json", "r") as f:
        return json.load(f)


def should_publish(article):
    """Check if the article should be published.

    This depends on if the date is in the past
    and if the article is already published.
    """
    publish_date = parse(article["publish_date"])
    now = datetime.datetime.now(datetime.timezone.utc)
    # TODO: check against existing published articles.
    return publish_date < now


def publish(article):
    """Publish the article."""
    print("publishing", article)
    # TODO: fill this in.
    # response = requests.put(f'https://dev.to/api/articles/{article_id}', json=data, headers={'api-key': os.environ['DEV_API_KEY']})


if __name__ == "__main__":
    publish_scheduled_articles()
