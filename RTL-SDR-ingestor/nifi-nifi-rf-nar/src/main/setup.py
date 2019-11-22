from setuptools import setup, find_packages

import pythonsdr

shortdesc = "NiFiWrappers for cusignal, a GPU Accelerated Signal Stream Processing Library"
longdesc = """
These Niwwfi wrappers can be run on a E.g an Nvidia Jetson GPU as a gateway node or for downstream sensors  using MiNiFi with multiple `RTL-SDR` USB Software Defined Radio (SDR) connections collecting data gives us the ability collect data in parallel working woth multiple devices working on different frequency ranges from 30Mhz to 2.6Ghz..  CUDA allows for Stream processing capable of processing AI algorithms on upto 8 high definition video streams, theese cusignal Wrappers wil bring data from these sensors, Cameras and SDRs back to a central Nifi Server where they cna be feed into any `.nar algorithm`.  Current plan to create Apache Mahaout, with as little GPU <--> Mahout Distributed matrices, giving the ability to scale naiveily and still hve a wide array of mathmematical functions for analysis.  cuSignal builds on the RAPIDS, Chainer, Numba, and PyTorch ecosystem to yield easy to use, GPU accelerated signal processing functionals. Ported directly from scipy.signal, cuSignal tries to remain API compliant -- often via a direct copy.
""""

setup(
    name='cusignal',
    version='0.1',
    description=shortdesc,
    long_description=longdesc,
    url='https://github.com/andrewpalumbo/RTL-SDR-Ingestor',
    packages=find_packages(),
    author='Andrew Palumbo',
    include_package_data=Trie
)
