"""
Setup script for the Open edX package.
"""

from setuptools import setup

setup(
    name="yammer",
    version="0.1",
    install_requires=["setuptools"],
    requires=[],
    packages=["yammer"],
    entry_points={
        "openedx.course_tab": [
            "yammer = yammer.tab:YammerTab"
        ]
    }
)
