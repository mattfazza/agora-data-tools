import pytest
from agoradatatools.etl import utils
from synapseclient import Synapse

file_object = {
    "id": "syn25838546",
    "format": "table",
    "final_filename": "teams",
    "provenance": [],
    "destination": "syn25871921"
}


def test_login():
    assert type(utils._login_to_synapse()) is Synapse


def test_yaml():
    # tests if a valid file renders a list
    assert type(utils._get_config()) is list

    # tests if a bad file will
    with pytest.raises(SystemExit) as err:
        utils._get_config(config_path="./tests/test_assets/bad_config.yaml")
    assert err.type == SystemExit
    assert err.value.code == 9

    with pytest.raises(SystemExit) as err:
        utils._get_config(config_path="./tests/test_assets/bad_config.yam")
    assert err.type == SystemExit
    assert err.value.code == 2


if __name__ == "__main__":
    pytest.main()
