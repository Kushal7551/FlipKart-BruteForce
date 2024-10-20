<br/>


## Installation

Install Pytorch with :
````
pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
````
Install the requirements with:
```shell
pip install -r requirements.txt
```

Download weights:
````
mkdir weights
cd weights
````
Download weights from 
ECT_SAL.pth https://drive.google.com/file/d/1Tx0pxy3MZAPfmCw-NPAV40dGS1CrIKrT/view?usp=drive_link
Logo_Detection_Yolov8.pth  https://drive.google.com/file/d/1jv1Emtla54SURmhp3TL1qM3E2rS-eNVr/view?usp=sharing
````
cd ..
cd saliency_prediction
mkdir pretrained_models
cd pretrained_models
````
Download weights from
resnet50-0676ba61.pth https://drive.google.com/file/d/1l6B2VrQfx44y2ZwT3Bt5TTXDq-XEMzoZ/view?usp=sharing
````
cd ..
cd ..
````

## Brand-Logo Detection

### Inference

You can use the following command to run the brand logo detection code:

```shell
python main_detection_yolov8.py --model="weights/Logo_Detection_Yolov8.pt" --image="test_images/test.jpg" --save-result
```

The results will be present in the results directiory.