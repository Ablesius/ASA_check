# ASA_check

A small tool to check which packages in an arch linux system need to be updated
according to ASA e-mails.
The tool is based on pyalpm.

# Installation

1. Clone the project
2. install `pyalpm`

# Usage

	$ ASA_check.py exim firefox webkit2gtk jenkins grafana libnghttp2 gettext
	The following packages are installed with their corresponding version:
	firefox 69.0-1
	webkit2gtk 2.26.0-1
	libnghttp2 1.39.2-1
	gettext 0.20.1-2

This is work in progress, and I'm just getting started. Ideas, feedback etc. are welcome. I'll keep the README updated as good as possible.
