import labgrid.target
from labgrid.driver import ShellDriver, SSHDriver

# ExternalPowerDriver


def test_serial_echo(target: labgrid.target.Target):
    driver: ShellDriver = target.get_driver("ShellDriver")
    result = driver.run_check("echo OK")
    assert "OK" in result


def test_ssh_echo(target: labgrid.target.Target):
    driver: SSHDriver = target.get_driver("SSHDriver")
    result = driver.run_check("echo OK")
    assert "OK" in result
