"""simple cli api using click module"""


import click
import commands.scrambler as scrambler



@click.group(help="simple cli tool example")
def start():
  """used as an entry point for the cli program
  """
  pass
  
start.add_command(scrambler.scrambler)