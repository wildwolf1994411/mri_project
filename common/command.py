import subprocess
import pdb
import shlex

__author__='Qi.Chen@nyulangone.org'

class Command(object):
    KAIBAOPERATION = 'kaiba -i '
    KAIBAVERBOSE = ' -v'
    KAIBAOUTPUTCSV = ' -o '

    @staticmethod
    def kaibai_processing(input_nii, output_csv='foo', verbose=True):
        command = Command.KAIBAOPERATION + input_nii
        if verbose:
            command += Command.KAIBAVERBOSE
        command += Command.KAIBAOUTPUTCSV + output_csv
        print '......command generated now processing.........'
        subprocess.call(shlex.split(command))
        print input_nii + ' processed'
