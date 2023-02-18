from code.stage_3_code.Result_Saver import Result_Saver
from code.stage_3_code.Setting_Up import Setting_Up
from code.stage_3_code.Evaluator import Evaluate
from code.stage_3_code.Method_CNN_MNIST import Method_CNN_MNIST
from code.stage_3_code.Dataset_Loader_MNIST import Dataset_Loader
import torch
import numpy as np

if 1:
    # ####
    np.random.seed(2)
    torch.manual_seed(2)

    data_obj = Dataset_Loader('mnist', '')
    data_obj.dataset_source_folder_path = '../../data/stage_3_data/'
    data_obj.dataset_source_file_name = 'MNIST'

    method_obj = Method_CNN_MNIST('MNIST', '')

    result_obj = Result_Saver('save', '')
    result_obj.result_destination_folder_path = '../../result/stage_3_result/MNIST'
    result_obj.result_destination_file_name = 'result'

    setting_obj = Setting_Up('MNIST_Setting', '')

    evaluate_obj = Evaluate('eva', '')

    print('************ Start ************')
    setting_obj.prepare(data_obj, method_obj, result_obj, evaluate_obj)
    setting_obj.print_setup_summary()
    setting_obj.load_run_save_evaluate()
    print('************ Finish ************')
    # ------------------------------------------------------
