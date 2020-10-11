---
layout: post
title: "CTC in Tensorflow"
date: 2018-11-19
---

Connectionist Temporal Classification (CTC) was proposed by Alex Graves in 

One common error of ctc using tensorflow or other framework.

W tensorflow/core/util/ctc/ctc_loss_calculator.cc:144] No valid path found.

Some reasons lead to this error:
1. The sequence of data is shorter than the sequence of label. --> There is no valid path to map.
2. The sequence of data is too long [https://github.com/tensorflow/tensorflow/issues/4193]
   --> The product of probabilities along the temporal dimension is over the maximum value of datatype (usually float).
   Note that: the probabilities here are usually represented by -log(P)
   ln(a + b) = ln(a) + ln(1 + exp(ln(b) - ln(a))) --> it could be exploded with long sequence.
   
Safety length of sequence for training with CTC in tensorflow using "float" type is less than 10000 timesteps.

With extended to "double" type, the length could be extended to 20000 timesteps.

Official site: [https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss]

Issues: [https://github.com/MaybeShewill-CV/CRNN_Tensorflow/issues/122]

Solution
- Clip values before CTC layer or clip gradients do not work.

- Modify source code and recompile

Python wrapper ctc_ops [https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/ctc_ops.py]
C source of ctc_loss 
[https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/util/ctc/ctc_loss_calculator.cc]
[https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/util/ctc/ctc_loss_calculator.h]

Modify source code to float64/double [https://github.com/tensorflow/tensorflow/pull/21822/files]
Exp function in C++ [https://en.cppreference.com/w/c/numeric/math/exp]
Numerical limits [https://en.cppreference.com/w/cpp/types/numeric_limits/infinity]

Compile from source on Windows [https://www.tensorflow.org/install/source_windows]
[https://medium.com/@amsokol.com/update-1-how-to-build-and-install-tensorflow-gpu-cpu-for-windows-from-source-code-using-bazel-and-c2e86fec9ef2]

Install via pipenv
[https://docs.python-guide.org/dev/virtualenvs/]

ERRORS during build from source:

Bazel's requirements for working on Windows [https://docs.bazel.build/versions/master/windows.html#requirements]
No toolchain found for cpu 'x64_windows' [https://github.com/bazelbuild/bazel/issues/2594]
