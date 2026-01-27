import subprocess
import sys
import pytest

def run(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return res.stdout.strip()

def test_sum_csv(request):
    data_file = request.config.getoption("--data-file")
    expected = request.config.getoption("--expected")
    atol = float(request.config.getoption("--atol"))

    assert data_file is not None
    assert expected is not None

    expected = float(expected)
    out = float(run([sys.executable, "sum_csv.py", data_file]))
    assert out == pytest.approx(expected, abs=atol)
