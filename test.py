import os;
from os.path import join, isfile, splitext, basename, exists
import sys
from difflib import Differ 
import difflib

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

if len(sys.argv) > 2: 
    tests_dir =  sys.argv[2]
    if(not exists(tests_dir)):
        print("Pasta de teste não existe")
        exit()
else:
    tests_dir = join(lab_dir,"tests")
    if(not exists(tests_dir)):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lab_name = splitext(basename(program_file))[0]
        tests_dir = join(script_dir, "testes", lab_name)
        if(not exists(tests_dir)):
            print("Pasta de teste não encontrada")
            
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

    os.system(f'python {program_file} < {in_file} > {out_actual_file}')
    if exists(out_expected_file):
        with open(out_actual_file, 'r') as actual:
            with open(out_expected_file, 'r') as expected:
                str_actual = actual.read()
                str_expected = expected.read()
                differ = Differ()
                if(str_actual == str_expected):
                    print(f'{COLOR_OKGREEN}Teste {test_name}: Sucesso{COLOR_END}', )
                else:
                    print(f'{COLOR_FAIL}Teste {test_name}: Falha{COLOR_END}', )
                    print(diff_strings(str_expected,str_actual))
                    # O seguinte codigo mostra de forma dividida ao inves de colorida a diferença
                    # sys.stdout.writelines(list(differ.compare(str_expected.splitlines(keepends=True),str_actual.splitlines(keepends=True)))) 




