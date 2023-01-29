#!/root/miniconda3/bin/python
import os
import sys
import time
from mmdet.apis import inference_detector, init_detector

def detection(num, score_thr):

    config = 'mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'
    checkpoint = 'mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
    model = init_detector(config, checkpoint, device='cpu')

    path = 'upload/'
    extension = '.png'
    image_path = f'{path}{num}{extension}'
    image_path_out = f'{path}{num}.out{extension}'

    ts = time.time()
    result = inference_detector(model, image_path)

    image_path = model.show_result(image_path, result, score_thr=score_thr, thickness=1, show=False, out_file=image_path_out, text_color='red', bbox_color='green')

    common_time = time.time() - ts  
    print( 'processing time:' ,int(common_time) )



if len(sys.argv) < 2:
    print('fail parameters')
    exit(0)


filename = 'upload/{}.png'.format(sys.argv[1])
if not os.path.isfile(filename):
    print( 'filename {} do not exist'.format(filename) )
    exit(0)

if len(sys.argv) == 3:
    print( 'start id=' , sys.argv[1])
    detection(sys.argv[1], float(sys.argv[2]))
else:
    print( 'start id=' , sys.argv[1], 'prd=', sys.argv[2])
    detection(sys.argv[1], 0.5)
