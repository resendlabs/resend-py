import os

from .api_keys._api_keys import ApiKeys
from .api_keys._api_keys import ApiKey
from .audiences._audiences import Audiences
from .contacts._contacts import Contacts
from .domains._domains import Domains
from .emails._attachment import Attachment
from .emails._batch import Batch
from .emails._emails import Emails
from .emails._emails import Email
from .emails._tag import Tag
from .request import Request
from .version import get_version

# Config vars
api_key = os.environ.get("RESEND_API_KEY")
api_url = os.environ.get("RESEND_API_URL", "https://api.resend.com")

# API resources
from .emails._emails import Emails  # noqa

__all__ = [
    "get_version",
    "Request",
    "Emails",
    "ApiKeys",
    "Domains",
    "Batch",
    "Audiences",
    "Contacts",
    # Types
    "ApiKey",
    "Email",
    "Attachment",
    "Tag",
]
