<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Akshat Mahesh Bhagat (ab2634)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2022 6:44:03 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ab2634" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881831-69ffe272-ac8d-4bcc-8cd4-961f6e5197e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881832-5582bd2d-ec49-43f7-a088-be95376911ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881833-a71d2276-502e-48d0-b44f-9693d73969ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows already registered email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881834-4d5f8c09-f07b-4c8a-8816-8f570d84a858.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows username is taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881835-f884fde9-5517-410b-9ab9-b9a6dd95e9a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the form is submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881925-7f2b2d35-d3a1-4388-88f4-04bbbdb4211a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows passwords dont match<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881836-8041e2af-6da0-4b2d-9a4d-338576f97b0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the added user in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>For the forms. we have several html files to carry out different operations.<br>If any mis operation is done then the page will handle those errors<br>through an error page.<div>Mysql database is used for backend. And we have used<br>flask to carry out other tasks and operations. Same way the password is<br>handled, minimum 8 characters required.</div><div>DB is utilized to store all the user, sample<br>and data.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881978-77850df1-0fa3-4b07-93ae-61ab904a489b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881979-11d52e6f-9a47-4b2d-a231-22dc6515ed9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows user does not exist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206881977-ee9d1237-01c6-4d78-ac0c-d8ae6d20262d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The user can log in into their accounts through the pages created in<br>html and if an invalid user logs in then it will throw error.<br>It uses the data from the database to check if the user is<br>valid or else will show error.<div>The DB helps the system to keep track<br>of the users and the entire data of the website.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882029-b84c5339-04eb-4ca9-8f95-7b4ede3bc44d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the user is logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882030-8423f54b-72f8-4c76-ab3c-492e039c38b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows error when logged out user tries to access the page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>flask principle is used for the session logic. When the user will log<br>in, it will process the user id to identify the user and retrieve<br>its data from the database.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882030-8423f54b-72f8-4c76-ab3c-492e039c38b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882030-8423f54b-72f8-4c76-ab3c-492e039c38b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882076-d68f3322-5c61-4a52-b901-c47109eb18bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882077-58502ee1-24da-4d4f-b6bf-8ce0ea4f6e02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User roles table screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For login protected pages, the page is accessible to the user only if<br>the user is logged in. Orelse it will show error page.&nbsp;<div>We used the<br>condition that if the user is not logged in he wont be able<br>to access certain pages.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Role protected pages are only accessible to those who actually have been assigned<br>a certain role and only the can access that page.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882211-a10ad663-9f1e-41f0-ab17-c30870aa9a26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the theme of the website<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>html is styled in a way that all the required buttons are on<br>the top left side of the webpage and easy to find. The interface<br>is user friendly and elements are basic.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882220-67a3fe33-30c3-495f-928b-2e9183f98166.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows user friendly error pt.1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882218-2e40e952-2e5d-4540-ad0c-13617959d52d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows user friendly error pt.2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882219-20218238-c01d-4198-9a99-c9992b17642e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows user friendly error pt.3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>We have been handling technical errors through a set of user friendly messages<br>which would show the user that he has landed on a wrong side.<div>Either<br>the user should be logged in or that page is role protected.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882247-c354fc07-f075-4c28-ac06-f63850d1f151.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the profile of the user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The user data is stored in the database. so when we access the<br>profile, the database will retrieve the data and display it to the user<br>on the form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882279-d8c0d736-7b78-477c-ac37-3862fb0a9c70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the username has changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882282-bac74f75-ab6a-4309-9d7c-2331ae858d60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows that the email and the password is changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882277-1d77930d-9fea-48cf-b42b-131850faa235.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the password mismatch<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882281-bc50d9c7-6f4e-4322-b350-dd60e6c71313.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the table before change<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/206882280-ed5f510a-4d23-4772-a877-e3abc9cdd122.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the table after change<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/16">https://github.com/AkshatBhagat99/IS601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The name, password and email can be modified with the flask principle, as<br>it will update the database with the new data as well.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I learned to build new forms and implement a login and register page.<br>Learned how the data is stored in the database.<div>Had a few deployment issues.<br>Got them resolved with professor</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/tree/prod2">https://github.com/AkshatBhagat99/IS601-007/tree/prod2</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ab2634" target="_blank">Grading</a></td></tr></table>