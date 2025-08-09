import subprocess

def test_help_menu():
    result = subprocess.run(["python3", "-m", "qmatsim", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "QMatSim CLI" in result.stdout
