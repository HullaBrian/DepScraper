# DepScraper
DepScraper is a command line utility designed to download a package as well as
its dependencies from the official debian website. If a machine you have cannot
connect to the internet to download and install packages, then DepScraper can be
run on another, internet-facing computer to download the package to install.

## Use
```commandline
>python DepScraper --help
Usage: python -m DepScraper [OPTIONS] PACKAGE

Arguments:
  PACKAGE  [required]

Options:
  --output TEXT        [default: **Current Working Directory**]
  --distribution TEXT  [default: bullseye]
  --help               Show this message and exit.

```
Below is an example run:
```commandline
python DepScraper isc-dhcp-server --output ~/Downloads
```
