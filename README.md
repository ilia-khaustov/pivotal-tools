# pivotal-tools

Set of useful tools for Pivotal API https://www.pivotaltracker.com

## Install

This project requires python3.

You will need to install pip requirements first:

`pip3 install -r requirements.txt`

Second, copy sample config to a new file `config.yaml`:

`cp config.sample.yaml config.yaml`

Third, update your `config.yaml` with `pivotal.project_id` and `pivotal.tracker_token` obtained from Pivotal.

## Use

`python3 generate_weekly_report` to print report for current week

`python3 generate_weekly_report --weeks-ago=1` to print report for previous week