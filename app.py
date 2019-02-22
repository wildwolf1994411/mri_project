from model.kaiba.kaiba import Kaiba
import config

__author__ = 'Qi.Chen@nyulangone.org'

if __name__ == '__main__':
    k = Kaiba(input_path=config.INPUT_PATH,
              prefix=config.PREFIX,
              output_path=config.OUTPUT_PATH,
              nii_only=config.NII_ONLY)
    k.process()

