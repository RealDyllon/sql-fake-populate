from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from pathlib import Path


def get_credentials():
    full_file_path = Path(__file__).parent.joinpath('credentials.yaml')
    with open(full_file_path) as settings:
        settings_data = load(settings, Loader=Loader)
    return settings_data
