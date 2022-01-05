"""simple cli api using click module"""


import click

# import commands.scrambler as scrambler

#TODO REMOVE THIS STUFF BEFORE SUBMITION FOR CLEAN UP

# @click.group(help="simple cli tool example")
# def start():
#   """used as an entry point for the cli program
#   """
#   pass
  
# start.add_command(scrambler.scrambler)


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def start(files):
  for filename in files:
    click.echo(filename)

if __name__ == '__main__':
  start()