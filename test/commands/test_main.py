from click.testing import CliRunner
import src.main as cli

def test_no_arg():
  """test how the program reacts when there is no arguments"""
  runner = CliRunner()
  result = runner.invoke(cli.start, [])
  assert result.exit_code == 2

def test_main_success_1():
  """test how the program reacts when there is proper arguments
  use example1 inputs
  """
  runner = CliRunner()
  #TODO run main with arguements
  # result = runner.invoke(cli.start,)
  # assert result.exit_code == 2
  # assert result.output is not None
  pass

def test_main_success_2():
  """test how the program reacts when there is proper arguments
  use example2 inputs
  """
  runner = CliRunner()
  #TODO run main with arguements
  # result = runner.invoke(cli.start,)
  # assert result.exit_code == 2
  # assert result.output is not None
  pass

