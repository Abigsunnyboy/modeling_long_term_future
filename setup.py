# Copyright (c) Facebook, Inc. and its affiliates.
from setuptools import setup

setup(
    name='babyai',
    version='0.0.2',
    license='BSD 3-clause',
    keywords='memory, environment, agent, rl, openaigym, openai-gym, gym',
    packages=['babyai', 'babyai.levels', 'babyai.agents', 'babyai.utils'],
    install_requires=[
        'gym>=0.9.6',
        'numpy>=1.10.0'
    ],
    dependency_links=[
    ]
)
