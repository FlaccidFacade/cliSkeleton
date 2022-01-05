from click.testing import CliRunner
import src.commands.scrambler as scrambler

def test_scrambler_length_5():
  runner = CliRunner()
  result = runner.invoke(scrambler.scrambler, ["Peter"])
  assert result.exit_code == 0
  assert result.output == 'ePter\n'


def test_scrambler_length_2():
  runner = CliRunner()
  result = runner.invoke(scrambler.scrambler, ["Pe"])
  assert result.exit_code == 0
  assert result.output == 'eP\n'

def test_scrambler_length_1():
  runner = CliRunner()
  result = runner.invoke(scrambler.scrambler, ["P"])
  assert result.exit_code == 0
  assert result.output == 'P\n'

def test_scrambler_no_arg():
  runner = CliRunner()
  result = runner.invoke(scrambler.scrambler, [])
  assert result.exit_code == 2
  assert result.output is not None