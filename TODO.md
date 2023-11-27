import database.py
In initializing function
create 5 tables
- Person (data from csv file)
	Attributes (or keys):
	- ID
	- First
	- Last
	- Type
- Login(data from csv file)
	Attributes (or keys):
	- ID
	- Username
	- Password
	- Role
- Project
	Attributes (or keys):
	- ProjectID
	- Title
	- Lead
	- Member1
	- Member2
	- Advisor
	- Status
- Advisor_pending_table
	Attributes (or keys):
	- ProjectID
	- to_be_advisor
	- Response
	- Response_date
- Member_pending_request
	Attributes (or keys):
	- ProjectID
	- to_be_member
	- Response
	- Response_date

In Login function
write a code that ask a user for a username and password then return a list of [ID and role] if the input is correct if not return None

In exit function
return csv file from the tables

write a unique code for each role
- Admin
	- can update all the tables by editing in database
- Student
	- can call pending requests
	- accept or deny the requests
		if accept
			- project table update, ID of the student will be in the project's dict
			- login update, role change to member
			- member_pending_request update, response 'yes'
		if deny
			- member_pending_requests update, response 'no'
	- create a project, check if deny all member requests
		- project table update, add project
		- login table update, role change to lead
		- send out requests to those whose role is student
			- member_pending_request update
- Lead
	- can call project status (pending member, pending advisor, ready to solicit an advisor)
	- can modify project information
		- project table update
	- can see who has responsed to the requests sent out
	- can send out requests to potential members
		- member_pending_request table update
	- after all potential members have accepted or denied the requests, can send out the request to a potential advisor (once at a time)
		- advisor_pending_request table update
- Member
	- can call project status
	- can modify project information
		- project table update
	- can see who has responded to the requests sent out


