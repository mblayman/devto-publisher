import logging

from flask import Flask

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    """Zappa expects to have an app. Give it a basic one."""
    return "ok"


def publish_scheduled_posts():
    logger.info("Testing publishing")
