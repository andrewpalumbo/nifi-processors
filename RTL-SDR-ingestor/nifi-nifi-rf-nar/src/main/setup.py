from setuptools import setup, find_packages

import pythonsdr

shortdesc = "NiFiWrappers for cusignal, a GPU Accelerated Signal Stream Processing Library"
longdesc = """
These Nifi wrappers can be run on a E.g an Nvidia Jetson GPU as a gateway node or for downstream sensors
 The wrapers are meant for both MiFi and MiNifi; using MiNiFi with multiple `RTL-SDR` USB Software Defined Radio (SDR) 
 connections collecting data gives us the ability collect data in parallel working woth multiple devices working on 
 different frequency ranges from 30Mhz to 2.6Ghz..  CUDA allows for Stream processing capable of processing AI algorithms 
 on upto 8 high definition video streams, theese cusignal Wrappers wil bring data from these sensors, Cameras and SDRs 
 back to a central Nifi Server where they cna be feed into any `.nar algorithm`.  Current plan to create Apache Mahaout conpatible DistributedRowMatrices[complex6d4]
 which will require some maintenance on the mahout side, however mahout already has GPU capabilities, so will stream samp-les into the DRM for amnalysis. , 
 with as little GPU <--> Mahout Distributed matrices, giving the ability to scale naiveily and still hve a wide array of
 mathmematical functions for analysis in mahouton spark with little effort effort.  NiFif is a great place to start with this.. eeventually 
 would like to use KNox to secure whichever connection we do with (pre)processed data from gateway to the main NiFiServer backed by an ASG of GPUmachines, with 
  cuSignal which builds on the RAPIDS, Chainer, Numba, and PyTorch ecosystem to yield 
 easy to use, GPU accelerated signal processing functionals. Ported directly from scipy.signal, cuSignal tries to remain API compliant -- often via a direct copy.
"""

setup(
    name='nifi-cusignal-iot',
    version='0.1',
    description=shortdesc,
    long_description=longdesc,
    url='https://github.com/andrewpalumbo/nifi-processors',
    packages=find_packages(),
    author='Andrew Palumbo',
    include_package_data=True
)
