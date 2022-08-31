import os


# def segregation():
  # path = '/home/runner/os-foldery/templates'
def segregation():
  important_files = ['.cache','venv','.config','.upm','poetry.lock','pyproject.toml','replit.nix','.replit','.breakpoints','main.py']
  for file in os.listdir():
    if file not in important_files and file != 'templates' and not file.endswith('_files'):
      end_file = file.split('.')
      start_file = end_file[0]
      end_file = end_file[1]
      directory = '{}_{}'.format( start_file, end_file)
      if directory in os.listdir():
        os.system('mv ' + start_file+'.'+end_file +' ' +end_file+'_files')
      else:
        os.system('mkdir ' + end_file +'_files')
        os.system('mv ' + start_file+'.'+end_file +' ' +end_file+'_files') 
      

segregation()   