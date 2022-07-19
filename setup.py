from setuptools import setup, find_namespace_packages

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=["ldm." + p for p in setuptools.find_namespace_packages(where="ldm")] + ["ldm"],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
