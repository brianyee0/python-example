import re
import sys

# Run like this:
#
# $ python process-file.py test-file
#
# Use `sys.argv` to read in the first argument after
# the script itself.
with open(sys.argv[1],"r") as input_file:
  file_contents = input_file.read()

p = re.compile('(ipsum|Lorem)')
output = p.sub(r'--\1--', file_contents)

with open("output-file","w") as output_file:
  output_file.write(output)
