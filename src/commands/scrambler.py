import click
import modules.silly.magic as magic

@click.command()
@click.option("--word", prompt="Word", help="The word to use.")
def scrambler(word):
  """Used to scramble the first two characters of the given word.

  Args:
      word ([type]): [description]
  """
  click.echo(magic.swap_O_Matic(word))