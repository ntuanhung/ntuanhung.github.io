---
layout: post
title: "Build TF from source on Windows"
date: 2018-12-18
---
0. Environment
  * I verified the following steps on Windows Server 2012 R2 (Standard) 64bit

1. Prerequisite (Note that, doing the following process step-by-step)
  * Windows 64bit might be 7 or newer.
  
  * Install Python 3
Install a Python 3.5.x or Python 3.6.x **64-bit** release for Windows at [here](https://www.python.org/downloads/windows/). 
Select pip as an optional feature and add it to your %PATH% environmental variable.
  
  * Install python dependencies via pip
Install the TensorFlow pip package dependencies:

```
pip3 install six numpy wheel
pip3 install keras_applications==1.0.6 --no-deps
pip3 install keras_preprocessing==1.0.5 --no-deps
```

The dependencies are listed in the [setup.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py) file under REQUIRED_PACKAGES.
  
  * Install Microsoft Visual C++ build tools 
  - [Microsoft Visual C++ 2015 Redistributable Update 3](http://download.microsoft.com/download/6/A/A/6AA4EDFF-645B-48C5-81CC-ED5963AEAD48/vc_redist.x64.exe)
  - [Microsoft Build Tools 2015 Update 3](http://download.microsoft.com/download/5/F/7/5F7ACAEB-8363-451F-9425-68A90F98B238/visualcppbuildtools_full.exe)
  
  Or even install Visual Studio (optional)
VS2015 Update 3 or newer is required. For students, VS Community 2015 is appropriate version, which can be downloaded at [here](https://my.visualstudio.com/Downloads?q=visual%20studio%202015&wt.mc_id=o~msft~vscom~older-downloads).
You should restart your computer to complete this step.

Note that, verify the existence of folder ```C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC```

  * Install MSYS2
Install MSYS2 for the bin tools needed to build TensorFlow. 
If MSYS2 is installed to ``C:\tools\msys64``, add ```C:\tools\msys64\usr\bin``` to your %PATH% environment variable. 

Then, using cmd.exe, run:
```
pacman -S git patch unzip
```
 
  * Download and install Bazel
I verified 0.20.0 version of Bazel. Download [here](https://github.com/bazelbuild/bazel/releases/download/0.20.0/bazel-0.20.0-windows-x86_64.exe)

Copy the file "bazel-0.20.0-windows-x86_64.exe" to folder ```C:\tools\bazel```
Rename the file from "bazel-0.20.0-windows-x86_64.exe" to "bazel.exe"

Add ```C:\tools\bazel``` to your ```%PATH%``` environment variable.
  
Add new environment variables:
- BAZEL_SH with value of ```C:\tools\msys64\usr\bin\bash.exe```
- BAZEL_VC with value of ```C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC```

  * Install GPU support (Optional)
Download and Install NVIDIA CUDA SDK and cuDNN

See the [Windows GPU support guide](https://www.tensorflow.org/install/gpu) to install the drivers and additional software required to run TensorFlow on a GPU.

2. Build pip-package of TensorFlow from source
  * Download source code of TensorFlow
Using cmd.exe, run the following commands and do NOT close cmd:
```
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
git checkout branch_name  # r1.9, r1.10, r1.11, r1.12, etc.
```

I built successfully with r1.12.

  * Configure building process
Run the following command:
```
python ./configure.py
```

The following is an example 
```
python ./configure.py
Starting local Bazel server and connecting to it...
................
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is C:\python36\python.exe]: 

Found possible Python library paths:
  C:\python36\lib\site-packages
Please input the desired Python library path to use.  Default is [C:\python36\lib\site-packages]

Do you wish to build TensorFlow with CUDA support? [y/N]: Y
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]:

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: 7.0

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]: C:\tools\cuda

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,7.0]: 3.7

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is /arch:AVX]: 

Would you like to override eigen strong inline for some C++ compilation to reduce the compilation time? [Y/n]:
Eigen strong inline overridden.

Configuration finished
```

  * Build pip-package
If your computer has a limit memory, please insert the following argument to the compile command
```
--local_resources 2048,.5,1.0
```
  
Compile command for CPU
```
bazel build --define=no_tensorflow_py_deps=true --incompatible_remove_native_http_archive=false --cpu=x64_windows --compiler=msvc-cl --copt=-nvcc_options=disable-warnings --config=opt --define=no_tensorflow_py_deps=true //tensorflow/tools/pip_package:build_pip_package
```

Compile command for GPU
```
bazel build --define=no_tensorflow_py_deps=true --incompatible_remove_native_http_archive=false --cpu=x64_windows --compiler=msvc-cl --copt=-nvcc_options=disable-warnings --config=opt --config=cuda --define=no_tensorflow_py_deps=true //tensorflow/tools/pip_package:build_pip_package
```

Build pip-package from compiled components
```
bazel-bin\tensorflow\tools\pip_package\build_pip_package C:/tmp/tensorflow_pkg
```

3. Install from pip-package
  * Directly install to python on system
Using pip or pip3 to install the compiled whl file.
pip install C:/tmp/tensorflow_pkg/tensorflow-version-cp36-cp36m-win_amd64.whl
  
  * Install to a virtual environment of python
In case you do NOT want to install and overwrite a new compiled TF to your python on system.
Or you want to verify that new compiled TF.

- Install via pipenv via pip[https://docs.python-guide.org/dev/virtualenvs/] using cmd.exe
```
pip install pipenv
```

- Create virtual environment
```
mkdir my_project_folder
virtualenv --system-site-packages <full path to my_project_folder>
```

- Active virtual environment
```
<full path to my_project_folder>\Scripts\activate.bat
```

- Install dependencies
```
pip install six numpy wheel
pip install keras_applications==1.0.5 --no-deps
pip install keras_preprocessing==1.0.3 --no-deps
```

- Install via pip as previous

4. Verify installed TF

Make a script file with content as follows

```
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
session = tf.Session()
print(session.run(hello))
```

Then, run the script file by python. If you installed TF in virtual environment, please active virtual environment and run script file from that.

5. Errors during build from source:
- Bazel's requirements for working on Windows [https://docs.bazel.build/versions/master/windows.html#requirements] No toolchain found for cpu 'x64_windows' [https://github.com/bazelbuild/bazel/issues/2594]

- Fix for "not found cuda"
Added the content of file "./tensorflow/tools/bazel.rc" on top of (hidden) file "./tensorflow/.tf_configure.bazelrc" & build happens.

- If you found any errors, please click [here](https://github.com/ntuanhung/ntuanhung.github.io/issues/new) to report the issue to discuss with me.
Please inform your problem as the following form
```
**System information**
    OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Arch Linux 4.15 x86_64
    Mobile device (e.g. iPhone 8, Pixel 2, Samsung Galaxy) if the issue happens on mobile device:
    TensorFlow installed from (source or binary): source, building ci_build.sh from TF distro
    TensorFlow version: latest from master
    Python version: tried both 2.7 and 3
    Installed using virtualenv? pip? conda?:
    Bazel version (if compiling from source): tried both 0.20.0 and 0.19.2
    GCC/Compiler version (if compiling from source):
    CUDA/cuDNN version:
    GPU model and memory:

**Describe the problem**

**Provide the exact sequence of commands / steps that you executed before running into the problem**

**Any other info / logs**
```
