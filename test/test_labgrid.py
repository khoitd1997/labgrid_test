import labgrid.target
from labgrid.driver import (
    ShellDriver,
    SSHDriver,
    ManualPowerDriver,
    ExternalPowerDriver,
)

import time
import pytest


def test_external_power(target: labgrid.target.Target):
    driver: ExternalPowerDriver = target.get_driver("ExternalPowerDriver")
    driver.on()
    time.sleep(5)
    driver.off()


@pytest.mark.skip(reason="Require manual so only test when needed")
def test_manual_power(target: labgrid.target.Target):
    driver: ManualPowerDriver = target.get_driver("ManualPowerDriver")
    driver.on()
    time.sleep(5)
    driver.off()


def test_serial_echo(target: labgrid.target.Target):
    driver: ShellDriver = target.get_driver("ShellDriver")
    result = driver.run_check("echo OK")
    assert "OK" in result


def test_ssh_echo(target: labgrid.target.Target):
    driver: SSHDriver = target.get_driver("SSHDriver")
    result = driver.run_check("echo OK")
    assert "OK" in result
