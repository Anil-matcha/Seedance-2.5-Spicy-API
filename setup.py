from setuptools import setup

setup(
    name="seedance-2-5-spicy-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for ByteDance's Seedance 2.5 Spicy API — the relaxed-moderation variant of the Seedance 2.5 flagship model, delivered via MuAPI. Native 4K, 30s clips, native audio, Omni Reference, Video Edit/Extend, and Motion Control.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["seedance_2_5_spicy_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
