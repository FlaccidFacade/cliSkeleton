import click.testing as ct
import src.main as cli

def test_no_arg_fail():
  """test how the program reacts when there is no arguments"""
  runner = ct.CliRunner()
  result = runner.invoke(cli.start, [])
  assert result.exit_code == 2
  assert result.output == "Usage: start [OPTIONS] FILES... REPORT\nTry 'start --help' for help.\n\nError: Missing argument 'FILES...'.\n"

def test_main_success_1():
  """test how the program reacts when there is proper arguments
  use example1 inputs
  """
  runner = ct.CliRunner()
  result = runner.invoke(cli.start,["Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json"])
  assert result.exit_code == 0
  assert result.exception == None

def test_main_success_2():
  """test how the program reacts when there is proper arguments
  use example2 inputs
  """
  runner = ct.CliRunner()
  result = runner.invoke(cli.start,["Example1/courses.csv", "Example1/students.csv", "Example1/tests.csv", "Example1/marks.csv", "Example1/output.json"])
 
  assert result.exit_code == 0
  assert result.exception == None


def test_main_help():
  """test how the program reacts when --help is used
  """
  runner = ct.CliRunner()
  result = runner.invoke(cli.start,["--help"])
  assert result.exit_code == 0
  assert result.output == 'Usage: start [OPTIONS] FILES... REPORT\n\n  Entry point for click program handles arguemnts\n\n  Args:     files (Path): the path for the csv files to use     report (Path):\n  the path for the JSON report to be created\n\nOptions:\n  --help  Show this message and exit.\n'
