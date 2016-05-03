# vswds
very simple watchdog script

This script is intended to run on cron and keep the customer's scripts running if they failed.
It is not suitable to high frequency neither real time checks.

#How it Works

- It assumed that several scripts are running on memory. Each script is related to a customer and collects specific information from it. These scripts have the "coleta-<customer-name>.py" format.
- Run every x minutes on the cron and check if all the customers listed on "custumers' file have their scripts running.
- If the watchdog can't find a customer's script it instantiates it
