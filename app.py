from model.kaiba.kaiba import Kaiba

__author__ = 'Qi.Chen@nyulangone.org'

if __name__ == '__main__':
    k = Kaiba(input_path='/home/shihong/Desktop/Qi_Chen/data/raw_data',
              prefix='HEAD_SAG_3D_MPR',
              output_path='/home/shihong/Desktop/Qi_Chen/data/processed/')
    k.process()

