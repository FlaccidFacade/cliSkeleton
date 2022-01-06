import click
from modules.conversion.csv_to_JSON import Report


@click.command()
@click.argument('files', nargs=4, type=click.Path(exists=True, readable=True))
@click.argument('report', nargs=1, type=click.Path(exists=True, writable=True))
def start(files,report):
  """Entry point for click program handles arguemnts

  Args:
      files (Path): the path for the csv files to use
      report (Path): the path for the JSON report to be created
  """
  #create report object given the file paths specified
  report = Report(files[0],files[1],files[2],files[3],report)#TODO Write test to cover this
  #generate a report for all students in files
  report.generate_all()#TODO Write test to cover this
  #write the report to JSON file
  report.write_JSON()#TODO Write test to cover this


if __name__ == '__main__':
  start()#TODO Write test to cover this