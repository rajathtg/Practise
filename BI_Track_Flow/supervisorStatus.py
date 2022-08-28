'''-- =============================================================================================================================
-- Job Name     : supervisorStatus.py 
-- Description  : Python script to get status of a supervisor from Druid.
-- Author       : Rajath
-- Create Date  : 17-Feb-2022
-- ------------------------------------------------------------------------
--  Change History
-- ------------------------------------------------------------------------
--  Date         Author                 Description 
--  ------------ ----------------- ---- ------------------------------------
--  17-Feb-2022   Rajath          		Initial version
-- ============================================================================================================================='''

import requests
import json
from datetime import datetime
import argparse
import configparser
from logger.logger import get_logger
import time

"""
Main method for generating datasets.
Args: 
-d (dataset) : dataset key for which supervisor status is required.
"""	

def main(args):

	# Variables related to Job status for logging
	#FLOW_TYPE = args.flow_type
	#superlogger = get_logger(args.flow_type)
	#JOB_ID = args.jobid
	#STEP_NAME = args.step
	#JOB_NAME = args.jobname
	#JOB_UID = args.jobuid
	#
	#JOB_START = {"flow_type":FLOW_TYPE, "job_id":JOB_ID, "job_uid":JOB_UID, "job_name":JOB_NAME, "step":STEP_NAME, "status":"Started"}
	#JOB_INPROGRESS = {"flow_type":FLOW_TYPE, "job_id":JOB_ID, "job_uid":JOB_UID, "job_name":JOB_NAME, "step":STEP_NAME,  "status":"InProgress"}
	#JOB_COMPLETED = {"flow_type":FLOW_TYPE, "job_id":JOB_ID, "job_uid":JOB_UID, "job_name":JOB_NAME, "step":STEP_NAME, "status":"Completed"}
	#JOB_FAILED = {"flow_type":FLOW_TYPE, "job_id":JOB_ID, "job_uid":JOB_UID, "job_name":JOB_NAME, "step":STEP_NAME, "status":"Failed"}
	

	try:
		#Reading the configs
		type = args.action
		key = args.dataset
		config = configparser.ConfigParser()
		config.read(args.configuration)
		#superlogger.info("Creating connection with Druid.", extra=JOB_INPROGRESS)		
		## Druid connection details
		_host = config.get('druid', 'host')
		_port = config.get('druid', 'port')
		ip_address = _host+':'+_port
		supervisor_status = 'http://%s/druid/indexer/v1/supervisor/%s/%s'
		#Importing the status of the supervisor
		import_status = requests.get(supervisor_status %(ip_address,key,'status'))
		#Converting the imported data from string to a dict
		status = import_status.json()
		#To extract the ststus of the supervisor
		current_status = status['payload']['state']
		
		if type == 'status':
			print(current_status)
		elif type == 'suspend':
			if current_status == 'SUSPENDED':
				print("Supervisor is already in 'Suspended' state")
			else:
				post_status = requests.post(supervisor_status %(ip_address,key,type))
				#time.sleep(3)
				print("Request initiated to suspend the supervisor")
		elif type == 'resume':
			if current_status == 'RUNNING':
				print("Supervisor is already in 'Running' state")
			else:
				post_status = requests.post(supervisor_status %(ip_address,key,type))
				#time.sleep(3)
				print("Request initiated to resume the supervisor")		
		else:
			print("Provide valid action 'suspend','resume' or 'status'")

				
	except Exception as e:
		#superlogger.error("Process failed with following message: ", extra=JOB_FAILED, exc_info=True)	
		print("process failed")
		raise
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Job Delete Current")
	parser.add_argument('-d', dest="dataset", required=True, help="Please provide dataset key as per the config file")
	parser.add_argument('-a', dest="action", required=True, help="Please provide action 'suspend','resume' or 'status'")
	parser.add_argument('-c', dest="configuration", required=True, help="Please provide path of configuration file")
	#parser.add_argument('-f', dest="flow_type", required=True, help="Please provide flow_type (dimension, facerd)")
	#parser.add_argument('-ji', dest="jobid", required=True, help="Please provide jobid")
	#parser.add_argument('-jn', dest="jobname", required=True, help="Please provide jobname")
	#parser.add_argument('-ju', dest="jobuid", required=True, help="Please provide jobuid(Unique Id)")
	#parser.add_argument('-js', dest="step", required=True, help="Please provide Step Name")
	#parser.add_argument('-dc', dest="druid_cluster", required=True, help="Please provide druid cluster (druid_granular, druid_aggregate)")

	main(parser.parse_args())