- Faculty
	- can see pending requests to become an advisor
	- accept or deny the requests
		if accept
			- change role to advisor
			- update project table
			- advisor_pending_request update, response 'yes'
		if deny
			- advisor_pending_request update, response 'no'
	- can see project table
	- evaluate step
		if the project is approved
			- change project status to approved
		else
			- change project status to denied
- Advisor
	- can see pending requests to become an advisor
	- accept or deny the requests
		if accept
			- update project table
			- advisor_pending_request update, response 'yes'
		if deny
			- advisor_pending_request update, response 'no'
	- evaluate step
		if the project is approved
			- change project status to approved
		else
			- change project status to denied
	
