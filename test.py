
import os
import re 
import subprocess

output = os.popen("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'").read()
branch = (os.environ['branch'])
output = output.split("\n")
output.remove('')

for dir in output:
  dir = dir.replace('/', '')
  function_name = dir + '_' + branch
  zip_dir = 'zip -r -j temp.zip %s/*' % (dir)
  os.system(zip_dir)
  lambda_cmd = 'aws lambda update-function-code --function-name %s --zip-file "fileb://temp.zip"' % (function_name)
  print (lambda_cmd)
  os.system(lambda_cmd) 
  os.system('rm -rf temp.zip')
