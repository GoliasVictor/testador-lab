import os;
from os.path import join, isfile, splitext, basename, exists
import sys
from difflib import Differ 

if(len(sys.argv) < 2):
	program_file = input("Nome do arquivo do programa: ")
else:
	program_file = sys.argv[1]
while not exists(program_file):
	program_file = input("Arquivo invalido, insira um arquivo valido: ")
if(not os.path.isabs(program_file)):
	program_file = os.path.abspath(program_file)

lab_dir = os.path.dirname(program_file)
tests_dir = join(lab_dir,"tests") if len(sys.argv) < 3 else sys.argv[2]

print("Arquivo do programa:", sys.argv[1])
print("Pasta de teste:",tests_dir )

actual_out_dir = join(tests_dir, "actual")
if(not exists(actual_out_dir)):
	os.mkdir(actual_out_dir)

files = [ join(tests_dir,f) for f in os.listdir(tests_dir) if isfile(join(tests_dir, f))]
files.sort()
in_files = [ f for f in files if f.endswith("in") ]
for in_file in in_files:
	test_name = splitext(basename(in_file))[0]
	out_actual_file = join(actual_out_dir, test_name+".out")
	out_expected_file = join(tests_dir, test_name+".out")

	os.system(f'python3 {program_file} < {in_file} > {out_actual_file}')
	with open(out_actual_file, 'r') as actual:
		with open(out_expected_file, 'r') as expected:
			str_actual = actual.readlines()
			str_expected = expected.readlines()
			differ = Differ()
			if(str_actual == str_expected):
				print(f'Teste {test_name}: Sucesso', )
			else:
				print(f'Teste {test_name}: Falha', )
				sys.stdout.writelines(list(differ.compare(str_expected,str_actual)))

