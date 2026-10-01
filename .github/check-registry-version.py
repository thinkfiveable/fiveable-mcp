"""Skip identical published metadata and reject edits to immutable versions."""
import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen

metadata = json.loads(Path(os.environ["SERVER_METADATA"]).read_text())
url = (
    "https://registry.modelcontextprotocol.io/v0.1/servers/"
    + quote(metadata["name"], safe="")
    + "/versions/"
    + quote(metadata["version"], safe="")
)
try:
    with urlopen(url, timeout=20) as response:
        published = json.load(response)["server"]
except HTTPError as error:
    if error.code != 404:
        raise
    already_published = False
else:
    if published != metadata:
        raise SystemExit("This version already exists with different metadata; increment its version.")
    already_published = True

with Path(os.environ["GITHUB_OUTPUT"]).open("a") as output:
    output.write(f"already_published={str(already_published).lower()}\n")
print("Identical version already published." if already_published else "New version ready to publish.")
