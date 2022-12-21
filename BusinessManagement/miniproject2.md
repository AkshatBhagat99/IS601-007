<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Akshat Mahesh Bhagat (ab2634)</td></tr>
<tr><td> <em>Generated: </em> 12/3/2022 8:53:39 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ab2634" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467664-4d5b94ec-3a18-47f2-99ac-b19801fe4050.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the homepage of the website with updated ucid<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467662-b49a0808-7628-4854-9948-43c1e78a06b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot has the company table from vscode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467663-82258368-8fae-4857-9efc-72c3a3201bb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot has the employee table from vscode<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467782-b71d42f3-8afa-40e0-991d-0233d3d911f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot has the code which checks if the file is csv else<br>will reject. And also the csv file should be read as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467783-1626193c-dfd1-41d3-8d1e-d1109cb61198.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows the code where employee and the company data should append<br>as a dict in their respective list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467784-8c77f9f2-bf2c-4a57-b41f-8c376f5ac8f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code shows that after each query a flash message is generated with the<br>number of records and also if a list is empty will show that<br>the list was not loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467966-b98162ce-5948-47ec-a052-1601be053a57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows a success message with a count <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467967-044c80f0-c95e-4c40-8e1d-efae938c1d5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the error message when it is not a csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205467968-f910c5a0-d150-4fc7-acae-ecfb47cd2030.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows error when we submit without attaching a file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468037-ce0068fa-92be-4557-aafe-60423f1c3c9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows that company data is uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468036-17b6378d-9ab7-4dd5-bc5b-9e37ef5cee53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows that employee data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468179-08b69c7b-eb98-43df-9f89-087bd96c75e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot contains all the given todos: retrieving details, first and last name<br>required, company is optional, email required, insert query and user friendly message on<br>exception <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468280-9c647a0f-365e-4d2c-b17a-3631fb3ba7d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid data filled before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468360-3ca88883-5404-4deb-915e-9fa605adbdd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468282-e98bb673-8f70-4243-bae8-c46e4084aa09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows first name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468283-ef027cc9-2419-45ce-a321-104e5190577b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows last name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468278-4a3e1721-c3f3-4040-80e1-90670f6c9020.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468279-95ec12e1-47f1-4303-b3ba-93fc46e1a90c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot contains record of new added employee<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468410-c1dbc03b-e487-43ba-bde3-6a682ac0a491.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains todos 1-6: select query via left join for details, checks req<br>args for fn, ln, email etc. Append like filter for the details, append<br>equality filter for company id <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468411-9305fb45-a9e8-4a39-b9d3-ffd7bdb29374.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains 7-10 todos: append sorting, limit and a proper error message if<br>limit is not a number or out of bounds. Also a user friendly<br>mesaage flashed at exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468508-040b2220-b114-494b-aedf-5611035f4d7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with first name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468509-b190b706-ea3e-4acb-9062-d3e7a7650ff6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with last name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468511-6db4c2d4-91c5-4bad-958a-ae141007f33f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468512-2fe70955-b024-4335-9c41-41ac76145344.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468513-7bd93c06-f323-4560-8a9d-88f5ded55113.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ascending filter applied with last name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468514-4d88b545-bc21-47e4-87dc-99a231dcbc2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>descending filter applied with email<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468641-c3dc0885-c17f-42a0-a178-3ec259ce45ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot has codes for: retrieve id details from form. Firstname, last name<br>, email required. company is optional. Update query, select query <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468640-a6908546-66a5-4e08-b452-0085a7ce23a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains the user friendly exception message and employee data passed to the<br>render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468862-1f7e7f1b-ddbd-4c95-b30e-8c355e974cda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot has data before the edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468863-19a73685-8fb4-4975-9596-b310a0377195.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot has data after the edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468898-85f353f0-6a6a-4837-821f-0def3a5b06b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot has db data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468897-b6f93b4f-e2b1-49ce-b03d-60010899afaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot has db data after the edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205468979-ac1b311b-8426-49b3-a3ff-51dcd481fb4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot has all the following todos: code that retrieves form data of<br>full information. Name, address, city, state, country required with flash error message. Website<br>is optional. Insert query is given and exception user friendly message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469146-400fd591-6f8f-44a1-979f-232b98c747aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469147-b5faf223-dbbe-49df-b218-235b670ef59d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows success message after adding<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469148-a619ffcc-7d4e-4f1f-a635-34f4b8ef7033.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows name error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469149-c11ef14a-fe12-4bc0-9c86-d1e7f4a54b65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows address error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469150-0d1dbd9b-3dba-443c-bf1c-d63814e716c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows city error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469152-960a1d96-db4f-4447-b413-0c46c1f69563.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows state error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469144-b7221d15-2f63-432f-b4d1-98bc61d27a26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows country error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469244-67415c71-9501-4750-b0bc-f2b9a748b4e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the data has been added to the db record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469272-3b0cb32e-67b1-4c96-aaa4-519c08ba3249.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains the todos 1-7: select query for fetching the given details. Checks<br>request args for name, country, state, column, order and limit, Append a like<br>filter for name, equality filter for country and state. Appended sorting for asc<br>and desc. Append limit has been set<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469273-e349f9a8-654c-4c6c-8cf6-159cf0d3d1ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has the code for error message if the limit is out of<br>bounds or not a number. User friendly message is flashed on exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469278-7e3f2e96-f6c7-47e7-9d84-5328e0ee7c5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469279-2906b09a-9be2-4081-893d-b8ae53277b02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469280-4595c0e7-e047-45db-9385-e89d62a5afbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows results with state filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469282-03d75a59-60b7-42ed-8ec1-da2e4e32134b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows asc filter applied with state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469277-6d8285e8-3085-470f-aeba-4a8f44d193ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows desc filter applied with state<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469556-be2a4643-c9bc-4f87-b91a-8ae9149136ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots contains the todos: code retrieves id ,details from the form. Name ,<br>address, city, state and country is required code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469557-162a08d6-48f1-4f50-87fc-f61eadfb7731.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot code has the Update query and user friendly message for exception is<br>given along with the select query. Company data is passed to render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469561-a8b9bfca-0c82-44fb-acb4-e3ee1443ee2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has the data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469560-d1e74f34-12d7-45a9-92c1-cacaae4323ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has the data after the edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469562-9b1c39b9-2849-47dc-b462-97f5d886c66d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has the db before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469563-70133daa-d266-4a80-8408-3b0213e51a5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot has db after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469730-003ac721-94a2-4e7c-82ea-ee54b821e90c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot has code for deleting the employee by id. Redirect to employee<br>search. All request args are passed to redirect route and a success message<br>flashed if process works<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469731-17e2ac63-e2ea-4174-bcc1-51da210afb6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before deleting an employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469732-5babab4a-3232-44cb-a93b-569a2e5ee4e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after deleting an employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469735-10956be1-8902-443f-9486-51c8d088eb30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot has the code for the following : delete company by id,<br>redirect to company search, request args are passed to redirect route and success<br>message flashed if process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469738-57464287-d0e3-4e8c-9f02-0ce9705e6a8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469739-40763b9c-54c7-4df7-9bee-a78dba2bd2f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after deleting a company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/205469883-41797152-5d16-4f76-845b-567c1b9e027c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows that all the test cases have been passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I learned a lot of new things while doing this assignment. Got to<br>know more about how the deployment actually works and having a real time<br>work with database and the tables. Got a little brushed up with the<br>html coding as well. It really taught me alot and after I was<br>done I got some small errors which I resolved with professor&nbsp;<div>over discord and<br>in the class itself. I had some issues with deployment because of the<br>yml files. So made some changes in them . Also I have named<br>dev and prod as dev2 and prod2 due to some issues. Rest everything<br>was great. Had a small secret key issue that also got solved with<br>professor itself</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ab2634" target="_blank">Grading</a></td></tr></table>