import os
import sys
import shutil
import datetime
import subprocess
import academic.academic


def run(prg, dir=None):
    process = subprocess.Popen(
        prg.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir)
    out, err = process.communicate()
    if err:
        print(err.decode('utf-8', 'ignore'))
    else:
        print(out.decode('utf-8', 'ignore'))
    return out, err


def replace_line(file_name, a, b):
    with open(file_name, "r") as fid:
        lines = fid.readlines()
    for i, l in enumerate(lines):
        if a in l:
            lines[i] = b
    with open(file_name, "w") as fid:
        fid.writelines(lines)


def build_cv():
    build_dir = os.path.join('cv', 'build')
    if not os.path.isdir(build_dir):
        os.mkdir('cv/build')
    run('cmake ..', build_dir)
    run('make', build_dir)
    shutil.copy(os.path.join(build_dir, 'cv.pdf'),
                os.path.join('static', 'files', 'cv.pdf'))
    # shutil.rmtree(build_dir)


### --- Add bibliography. --- ###
academic.academic.import_bibtex('cv/src/biblio.bib', overwrite=True)

### --- Update date. --- ###
replace_line('config/_default/config.toml', 'copyright = ',
             'copyright = "Copyright &copy; 2019 Julien Vanharen - Last update ' + datetime.datetime.now().strftime('%b %Y') + '"\n')

# ### --- Compile with Hugo. --- ###
run('hugo')

# ### --- Build CV. --- ###
build_cv()

# ### --- Deploy. --- ###
run('rsync -avz --delete public/ jvanhare@nfs.saclay.inria.fr:~/public_html/')
