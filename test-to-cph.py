import os;
from os.path import join, isfile, splitext, basename, exists
import sys
from difflib import Differ 
import difflib
import hashlib
import json

COLOR_FAIL = '\033[91m'
COLOR_OKGREEN = '\033[92m'
COLOR_END = '\033[0m'



#Fonte: https://gist.github.com/ines/04b47597eb9d011ade5e77a068389521?permalink_comment_id=4075340#gistcomment-4075340
def diff_strings(a: str, b: str) -> str:
    output = []
    matcher = difflib.SequenceMatcher(None, a, b)
    green = '\x1b[38;5;16;48;5;2m'
    red = '\x1b[38;5;16;48;5;1m'
    end = '\x1b[0m'
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == 'equal':
            output.append(a[a0:a1])
        elif opcode == 'insert':
            output.append(f'{green}{b[b0:b1]}{end}')
        elif opcode == 'delete':
            output.append(f'{red}{a[a0:a1]}{end}')
        elif opcode == 'replace':
            output.append(f'{green}{b[b0:b1]}{end}')
            output.append(f'{red}{a[a0:a1]}{end}')
    return ''.join(output)

if(len(sys.argv) < 2):
    program_file = input("Nome do arquivo do programa: ")
else:
    program_file = sys.argv[1]
while not exists(program_file):
    program_file = input("Arquivo invalido, insira um arquivo valido: ")
if(not os.path.isabs(program_file)):
    program_file = os.path.abspath(program_file)

lab_dir = os.path.dirname(program_file)
lab_name = splitext(basename(program_file))[0]

if len(sys.argv) > 2: 
    tests_dir =  sys.argv[2]
    if(not exists(tests_dir)):
        print("Pasta de teste não existe")
        exit()
else:
    tests_dir = join(lab_dir,"tests")
    if(not exists(tests_dir)):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tests_dir = join(script_dir, "testes", lab_name)
        if(not exists(tests_dir)):
            print("Pasta de teste não encontrada")
hash = hashlib.md5(program_file.encode()).hexdigest();
cph_filename = f'.{os.path.basename(program_file)}_{hash}.prob'
cph_dir = join(lab_dir,".cph")
cph_path = join(cph_dir,cph_filename)
print("Arquivo do programa:", program_file)
print("Pasta de teste:",tests_dir )
print("Caminho CPH",  cph_path)

if not exists(cph_dir):
   os.mkdir(cph_dir)



print("hash", )



def get_cph_tests():
	tests = []
	files = [ join(tests_dir,f) for f in os.listdir(tests_dir) if isfile(join(tests_dir, f))]
	files.sort()
	in_files = [ f for f in files if f.endswith("in") ]
	for i, in_file in enumerate(in_files):
		test_name = splitext(basename(in_file))[0]
		out_file = join(tests_dir, test_name+".out")
		with open(in_file, 'r') as inp:
			with open(out_file, 'r') as out:
				str_input = inp.read()
				str_output = out.read()
				tests.append({
					"id": i,
					"input": str_input,
					"output": str_output
				})
	return tests

str_cph_content = json.dumps({
	"name": "Local: "+lab_name,
	"url": program_file,
	"tests": get_cph_tests(),
	"interactive": False,
	"memoryLimit": 1024,
	"timeLimit": 3000,
	"srcPath": program_file,
	"group": "local",
	"local": True
})





with open(cph_path, 'w') as f:
   f.write(str_cph_content)
