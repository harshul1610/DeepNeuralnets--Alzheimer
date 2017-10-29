# DeepNeuralnets for Alzheimer Detection

 ![Dr. Tsuyoshi Hashimoto, author](https://img.shields.io/badge/Author-Dr.%20Tsuyoshi%20Hashimoto%20-green.svg)
 ![Er. Siddhant Kapil, author](https://img.shields.io/badge/Author-Er.%20Siddhant%20Kapil%20-blue.svg)
 ![Er. Harshul Jain, author](https://img.shields.io/badge/Author-Er.%20Harshul%20Jain%20-blue.svg)
 ![Er. Charu Sharma, author](https://img.shields.io/badge/Author-Er.%20Charu%20Sharma%20-blue.svg)

This research project is about the detection of the Alzheimer disease among the patients. Early detection of the Alzheimer disease will help in early treatment, which can prevent the exaggeration of the symptoms. We aim to do so with the help of Deep learning, which is part of machine learning. In this project we use three types of architectures for deep learning.

1. LeNet-5
2. Transfer learning
3. Video Classification

![Normal Brain vs Alzheimer Brain](https://github.com/Tsuyoshi-Hashimoto/DeepNeuralnets--Alzheimer/blob/master/images/alzheimers-brain.jpg)

For the input, we have nii files for Alzheimer, Normal and MCI detection. There are different folders for each of the Alzheimer, MCI and Normal. Each folder includes some .nii files. Each .nii file has the 4-dimensional data in it. Proper preprocessing methods are written in the preprocessing folder to convert this 4-dimensional data into the 2-dimensional and 3-dimensional data. The code for the models is written in seperate folders for each architecture.

### AWS Instructions

We are using Amazon AMI based deep learning machine.

to run the instance follow the procedure as follows:
```
1. go to ec2 instances dashboard
2. go to the instances and note down the instance number of instance. right now it is i-04f3bbcb19741adf5
2. go to the volumes category, and under that, attach the volume vol-075048e19d6d6efcf. To make it active,
   right click the volume and click on attach volume. there will be the pop up. in the pop up put the instance number 
   i-04f3bbcb19741adf5. In the field corresponding to Device: enter /dev/xvda and click on Attach.
4. go to your instances and right click on the instance and click on start.
```

## Run instructions for AWS
```
$ ssh -i <.pem file> ubuntu@<ip>
```

Starting Jupyter notebook
```
$ screen -S jupyter_session
$ jupyter notebook
$ ctrl+a and then press d
```
Password for jupyter notebook is Hashi8424
