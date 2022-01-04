"""simple cli api using click module"""


import click
import commands.scrambler as scrambler



@click.group(help="simple cli tool example")
def start():
  """[summary]
  """
  pass
  
start.add_command(scrambler.scrambler)