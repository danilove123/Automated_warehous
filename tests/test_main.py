from typing import Union
from unittest.mock import patch
import pytest
from contextlib import nullcontext as does_not_raise
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from sqlalchemy import Table, Column, String, Integer, create_engine
from main import app
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = TestClient(app)


def culc_sum(a: int, b: int):
    return a + b
def culc_devision(a: Union[int, float], b: Union[int, float]):
    return a / b


class Tests_group_1:
    @pytest.mark.parametrize(
        "username, age, email,password, phone, expectation", [
            ("strissdsssngS", 30, "user@example.com","stssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strisssssngAAA", 30, "user@example.com","stsssringst11","Unknown", does_not_raise()),
            ("strissaqngAAA", 10, "user@example.com","stsssringst11","Unknown", pytest.raises(Exception)),
        ]
    )
    def test_create_del_users(self,username, age, email,password,phone,expectation):
        with expectation:
            result_create = client.post(
                url="/create_user",
                json={"username": username,"age":age,"email":email,"password":password,"phone":phone}
            )
            result_delete = client.delete(
                url=f"/delete_user/?username={username}&password={password}",
            )
            assert result_create.status_code == 201
            assert result_delete.status_code == 204


