# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from absl import logging,flags,app
from feature_scaling import inverse_scale,scale
from s3_smart_open.filehandler import get_filenames, read_pckl, to_pckl, to_pd_fth, read_pd_fth
import os

FLAGS = flags.FLAGS

flags.DEFINE_string('input_path',default=None,help='Path where feature files in feahter format were found')
flags.DEFINE_string('output_path',default=None,help='Path where scaled features in feather format were stored')
flags.DEFINE_enum('stage','fit',['fit','transform', 'inverse'],'Wether to fit_transform, transform a dataframe or inverse scale.')
flags.DEFINE_list('filename_list',default=[],help='List of filenames for feature scaling')
flags.DEFINE_enum('method',None,['Normalizer','MinMaxScaler','MaxAbsScaler','StandardScaler','RobustScaler','QuantileTransformer','PowerTransformer'],help='Method for feature scaling')
flags.DEFINE_string('scaler_obj',None,'Filename of the scaler that should be used.')
flags.DEFINE_string('config',default='{}',help='Parameters for method .fit_transform')

flags.mark_flag_as_required('input_path')
flags.mark_flag_as_required('output_path')


def main(argv):
    """Scales or inverse scales pandas dataframes with the help of scikitlearn
    """    
    del argv

    # Read Filenames
    filenames = get_filenames(input_path=FLAGS.input_path, filenames_list=FLAGS.filename_list, file_types=".fth")
    assert len(filenames) > 0 , 'Length of List = 0. At least one element is required'


    for filename in filenames:
        dataframe = read_pd_fth(FLAGS.input_path, filename)

        if FLAGS.stage == 'fit':
            scaler, df = scale(dataframe=dataframe, method=FLAGS.method, scaler=None, config=eval(FLAGS.config))

        elif FLAGS.stage == 'transform':
            scaler = read_pckl(FLAGS.input_path, FLAGS.scaler_obj)
            scaler, df = scale(dataframe=dataframe, method=FLAGS.method, scaler=scaler, config=None)

        elif FLAGS.stage == 'inverse':
            scaler = read_pckl(FLAGS.input_path, FLAGS.scaler_obj)
            df = inverse_scale(dataframe=dataframe, scaler=scaler)

            
        to_pd_fth(FLAGS.output_path,filename,df)
        to_pckl(FLAGS.output_path,os.path.splitext(filename)[0]+'_scaler.pckl',scaler)

if __name__ == '__main__':
    app.run(main)
