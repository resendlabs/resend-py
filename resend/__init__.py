import os

from .api_keys._api_keys import ApiKey, ApiKeys
from .audiences._audience import Audience
from .audiences._audiences import Audiences
from .contacts._contact import Contact
from .contacts._contacts import Contacts
from .domains._domain import Domain
from .domains._domains import Domains
from .emails._attachment import Attachment
from .emails._batch import Batch
from .emails._emails import Email, Emails
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
    "Audience",
    "Contact",
    "Domain",
    "ApiKey",
    "Email",
    "Attachment",
    "Tag",
]
