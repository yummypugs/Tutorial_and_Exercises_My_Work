# Introduction to Data Analytics in Business

This repo provides exercises, solutions and tutorial materials for the
course *Introduction to Data Analytics in Business* at Frankfurt School
of Finance and Management.

## Tutorials

[Tutorial 1: Setup and Introduction to Python and Pandas](https://iewaij.quarto.pub/tutorial-1-setup-and-introduction-to-python-and-pandas/)  
[Tutorial 2: Dimensionality Reduction](https://iewaij.quarto.pub/tutorial-2-dimensionality-reduction/)  
[Tutorial 3: Loss and Optimization](https://iewaij.quarto.pub/tutorial-3-loss-and-optimization/)  
[Tutorial 4: Data Science as Craftsmanship](https://iewaij.quarto.pub/tutorial-4-data-science-as-craftsmanship/)  
[Tutorial 5: Network Analysis](https://quartopub.com/sites/iewaij/tutorial-5-network-analysis)

## Solutions

[Solution 1: Pandas](https://quartopub.com/sites/iewaij/solution-1-pandas)  
[Solution 2: Dimensionality Reduction](https://quartopub.com/sites/iewaij/solution-2-dimensionality-reduction)  
[Solution 3: Linear Regression](https://quartopub.com/sites/iewaij/solution-3-linear-regression)  
Solution 4: Network Analysis

## Setup

### Package Managers

A package manager is a software tool that automates the process of
installing, upgrading, and removing computer programs (incl. software,
applications, packages) for a computer consistently. You can think of it
as an “App Store” for your computers without accounts, passwords and
clicking with a mouse. I recommend using
[Winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/)
for Windows, [Homebrew](https://brew.sh/) for macOS. For Linux and
Windows Subsystem for Linux, the choice of package managers usually
depends on which distribution you are using.

### Windows

[Winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/)
should be pre-installed on your Windows PC. If not, refer to
[documentation](https://docs.microsoft.com/en-us/windows/package-manager/winget/).
You can search, install, uninstall applications in Power Shell or
Command Prompt.

    winget search <APPLICATION-NAME>
    winget install <APPLICATION-NAME>
    winget upgrade <APPLICATION-NAME>
    winget uninstall <APPLICATION-NAME>

For this course, I recommend installing the following software:

    winget install Git.Git
    winget install CondaForge.Mambaforge
    winget install Microsoft.WindowsTerminal
    winget install Microsoft.VisualStudioCode

Add the following directories to your Environment Variable `Path`:

    C:\Users\<USER-NAME>\mambaforge\condabin
    C:\Program Files\Git\cmd

Verify that you have successfully installed git and mambaforge with the
following command:

    git --help
    mamba --help

### macOS

[Homebrew](https://brew.sh/) needs to be installed by the user of macOS.
Open your terminal, type the following command:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Similar to Winget, you can search, install, uninstall applications in
Terminal.

    brew search <APPLICATION-NAME>
    brew install <APPLICATION-NAME>
    brew upgrade <APPLICATION-NAME>
    brew uninstall <APPLICATION-NAME>

For this course, I recommend installing the following software:

    brew install git mambaforge iterm2 visual-studio-code


Please run the following commands to setup your shell for mambaforge:

    conda init "$(basename "${SHELL}")"
    mamba init

Verify that you have successfully installed git and mambaforge with the
following command:

    git --help
    mamba --help

## Git

Git is a version control software. Forget about
`presentation_version_final.pptx`
`presentation_version_final_final.pptx` on your shared folders that
nobody can figure out which file to use. Git gives you the superpower to
track code changes and sync your work with your teammates. We start from
the very basics, which is the file system navigation and the `clone`
command.

In your terminal (it can be any terminal, e.g. Windows Terminal, iTerm2,
VS Code), you usually start at the user’s folder, denoted as `~`. You
can list your current files with `ls` command:

    ls

Then you can move to different folder using `cd`:

    cd Documents

It is always recommended to have a unique folder for your code and
projects. Let’s create a folder called `Code` using `mkdir`:

    mkdir Code

And we can `cd` into it:

    cd Code

Now, we are ready to clone this course’s Git repository using `git`:

    git clone https://gitlab.com/ComputationalScience/intro-data-analytics.git

Again, we `cd` into it:

    cd intro-data-analytics

This folder has already been initialized, and it is your “local” folder,
which is different to the “remote” folder that everyone sees. You can do
all the git operations locally without pushing to the remote folder. For
this `intro-data-analytics` folder, you cannot push any changes because
you do not have the permission, which might be a good thing since you
know you will not accidentally delete the whole repository for the whole
class.

Unlike OneDrive or iCloud Dive, the separation of local and remote
folders means changes are not synced automatically. You can sync your
local folder from the remote folder using `git pull` if you do not have
any local changes:

    git pull

## Virtual Environments

By default, any Python interpreter installed runs in its own global
environment. They aren’t specific to a particular project. For example,
if you just run `python`, `python3`, or `py` at a new terminal, you’re
running in that interpreter’s global environment. Any packages that you
install or uninstall affect the global environment and all programs that
you run within it. This means that if Project A requires pandas at
version 0.9 while Project B requires pandas at version 1.1, it is
impossible to work on both project simultaneously.

To prevent such clutter, developers often create a virtual environment
for a project. When you install a package into a virtual environment,
any packages you install are installed only in that environment. When
you then run a Python program within that environment, you know that
it’s running against only those specific packages.

### Mambaforge

If you have followed the instructions and have successfully installed
the recommended packages, that means you have the best Python package
and environment manager on your computer, which is great! Mambaforge is
basically [miniconda](https://docs.conda.io/en/latest/miniconda.html)
with the following features pre-configured:

-   [`conda-forge`](https://conda-forge.org/) set as the default (and
    only) channel to provide more updated and comprehensive coverage of
    packages.
-   [`mamba`](https://github.com/mamba-org/mamba) in place of `conda` to
    provide better dependency solving and faster package installation.
    Even though I use `mamba` instead of `conda` throughout this
    tutorial, the command with `mamba` is the same as `conda`. You can
    refer to conda’s [cheat
    sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
    and just replace `conda` with `mamba`.

It is totally fine if you have no idea what this means. I have used
Python for almost 5 years, Mambaforge is hands down my favourite
configuration for package and environment management for data science in
Python. You may also have heard about pip and virtualenv, which are the
mainstream package and environment management tools for Pythonista. The
main advantage of conda over pip is that, you can install and update
python itself within a conda environment. With pip, you have to install
an entirely new virtual environment every time you want to switch to a
different python version.

### Create Virtual Environments

Let’s create a virtual environment called `machine-learning`:

    mamba create -n machine-learning

You can then activate this environment:

    mamba activate machine-learning

Now you can install packages and run code in this specific environment,
without worrying about conflicts with your other projects.

You can also leave the environment by deactivating:

    mamba deactivate

For this course, I have prepared a `environment.yml` file that contains all
packages required, you can create an environment defiend by `environment.yml`
called `intro-data-analytics` and install all required packages using one command:

    mamba env create -f environment.yml
    mamba activate intro-data-analytics

You may also update your existing environment from `environment.yml`:

    mamba env update -f environment.yml

### Install Python and Packages

Most packages you need for this course should already been included in
`environment.yml`. Here I talk about installing packages without using
`environment.yml` file. Since you are using conda or mamba, it is always
preferred to install packages with conda or mamba if they are available.
Make sure you are in the right environment, and use the following
command:

    mamba install python=3.10 pandas jupyterlab

There are always cases when you have to use `pip` to install packages because they are not available on `conda-forge`:

    pip install watermark

Now, with everything installed, you are good to go. To verify the
installation is working, let’s first launch `jupyter lab`:

    jupyter lab