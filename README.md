# wxflightpath

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Overview

wxflightpath retrieves a text-based observation and forecast for flight planning.
Given specific origin and destination OACI codes, this project determines all stations
within and around the flight path, retrieves all observations (METARs), and forecasts (TAFs)
renders them in text mode and audio.
There is an option to upload the result on an S3 bucket and return the result in a 200 OK response
if you properly configure it.
There is also an option to run it as a webserver.
Enjoy!
## Limitation
This is currently limited to French airfields. 
Future developments may include other airfields.
## Installation
The steps below assume you're running on a Linux/MacOS system.
To install wxflightpath, use the following steps:
### Step1 Optional but recommended : create a venv
creating a python virtual environment avoids any problems with\
existing python interpreter configurations on your system.
```bash
$ python3 -m venv wxflightpath-venv
$ source wxflightpath-venv/bin/activate
```
### Step2 : install the requirements.

```bash
$ pip install -r requirements.txt
```
### Step3 : configure wxflightpath.
in the project root directory there is aconfiguration file: default.cfg.
#### Step3.1 : get a security token for the avwx.rest api.
sign up and obtain a token from https://info.avwx.rest/
#### Step3.2 : Optional - configure your AWS infrastructure.
sign up to or use an AWS account on https://aws.amazon.com/ \
if you want to run this locally or remotely with AWS.
details on how to do it are out of scope of this project.
just know that you need an S3 bucket and You need to put your avwx\
secret token in Secrets manager.
#### Step3.3 : configure default.cfg.
Configure default.cfg properly by either:
- adding a token in the SECURITY section
- adding the secrets and S3 bucket name in the AWS section
to run the AWS Lambda demo (requires AWS prior configuration).
if you wish to run this as an HTTPS endpoint configure properly the HTTPS section:
- add the server certificate and key paths
- add the https port your server will be listening to

There is an option to use an AWS generated certificate using ACM for free and use it on an EC2 instance.
#### Step3.4 : run the smoke test.
run the tests using the shell script in the scripts directory.
```bash
$ cd scripts/
$ sh run_tests.sh
```
Fix any issues if you can. Otherwize [report an issue](https://github.com/amenai1979/wxflightpath/issues)

#### Step3.5
Enjoy!

## Usage

from the project root using a terminal (Linux)
```bash
$ cd scripts/
$ sh run_wxcrawler_demo.sh 
```
if you want to run the AWS lambda demo:

```bash
$ cd scripts/
$ sh run_wxcrawler_aws_demo.sh 
```
for demo purposes the run_wxcrawler_aws_demo.sh scripts also generates an audio briefing file, you can find it in the audio/ folder.

if you want to run it as a webserver (using Flask)

```bash
$ cd scripts/
$ sh run_wxcrawler_https_server.sh
````

Then in another terminal:

```bash
$ curl https://yourhostname.com:8443/brief?origin=LFPT&destination=LFRU
````
if you have AWS configured properly you may choose to use the S3 object generated:

```bash
$ curl -L https://yourhostname.com:8443/brief-redirect?origin=LFPT&destination=LFRU
````
This will automatically follow the redirect and display the briefing text.

## Project Details

Author: [Alexandre Menai](https://www.linkedin.com/in/menai/)\
Email: amenai@amenai.net\
Version: 1.0\
Development Status: 3 - Alpha\
Python Version: 3.11

## Links

Source Code: https://github.com/amenai1979/wxflightpath/ \
Bug Reports: https://github.com/amenai1979/wxflightpath/issues

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

## Contributing

If you'd like to contribute to wxflightpath, please check the CONTRIBUTING.md file for guidelines.

## Acknowledgments

Kudos to [Sam Drew](https://github.com/sam-drew) the author of [picket](https://github.com/sam-drew/picket) that is used in this project.
Kudos to [Christian Quest](https://www.sia.aviation-civile.gouv.fr/produits-numeriques-en-libre-disposition/les-bases-de-donnees-sia/donnees-aeronautiques-xml-airac-13-23.html) who ceated the data used in this project 
