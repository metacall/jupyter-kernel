from ipykernel.kernelapp import IPKernelApp
from . import metacall_jupyter

IPKernelApp.launch_instance(kernel_class=metacall_jupyter)
