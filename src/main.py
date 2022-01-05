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
@click.argument('files', nargs=4, type=click.Path(exists=True, readable=True))
@click.argument('report', nargs=1, type=click.Path(exists=True, writable=True))
def start(files,report):
  for filename in files:
    click.echo(filename)
  click.echo(report)

if __name__ == '__main__':
  start()

#TODO remove this and that
  #python3 src/main.py e2/courses.csv e2/students.csv e2/tests.csv e2/marks.csv e2/output.json