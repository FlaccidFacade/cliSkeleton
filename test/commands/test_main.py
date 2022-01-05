from click.testing import CliRunner
import src.main as cli

def test_no_command():
  runner = CliRunner()
  result = runner.invoke(cli.start, [])
  assert result.exit_code == 0

def test_scrambler_as_comm():
  runner = CliRunner()
  result = runner.invoke(cli.start, ["scrambler", "Peter"])
  assert result.exit_code == 0
  assert result.output == "ePter\n"

def test_scrambler_as_comm_no_arg():
  runner = CliRunner()
  result = runner.invoke(cli.start, ["scrambler"])
  assert result.exit_code == 2
  assert result.output is not None

def test_fakeCommand_as_comm():
  runner = CliRunner()
  result = runner.invoke(cli.start, ["fakeCommand", "Peter"])
  assert result.exit_code == 2
  assert result.output is not None

def test_fakeCommand_as_comm_no_arg():
  runner = CliRunner()
  result = runner.invoke(cli.start, ["fakeCommand"])
  assert result.exit_code == 2
  assert result.output is not None


