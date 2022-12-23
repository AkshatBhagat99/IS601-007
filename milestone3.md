<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Akshat Mahesh Bhagat (ab2634)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 11:42:17 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-bank-project/grade/ab2634" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209091284-a0fe76a2-83a7-44d9-9084-d0ef43ef5498.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the transfer page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209091417-f5389173-34a4-4b3f-a6de-0f3f496bff69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the dropdown values with balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209091599-197095d8-01aa-4f41-9e4a-87577084553e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows error that cant transfer funds more than they have<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209091963-42e4c3b6-a71b-405f-a43a-252cfcad3ebb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows that we cant transfer to same account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209092596-01e80646-1db9-4266-b541-7265c65ac90f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code that shows the above logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209092802-029f4b8f-5c60-44e0-a8f7-9bc38b5396b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the following cannot transfer negative balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209270512-7d8549e6-0d59-423e-9f5b-f432c83ece73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the code for the following logic where we cant transfer<br>negative balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209094023-0cfc84e8-7194-42ea-b369-62b6c0c78309.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the generated transaction history<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209094820-7e0b72d3-50fa-41ce-9daf-0182577f1dc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the transaction history in db<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209094570-fb61ecea-2e5a-4e86-9515-1b5e4931fd88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The accounts table of the user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p>the list dropdown shows the available accounts for a user with the balances<br>of their account.<div>The balances are fetched from the accounts database and any transaction<br>record is stored in the transaction history.</div><div>And the database gets updated accordingly</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/26">https://github.com/AkshatBhagat99/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-prod3.herokuapp.com/accounts/transfer">https://is601-ab2634-prod3.herokuapp.com/accounts/transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209095611-9c527367-bbcb-4bba-974f-f0ed0069cf68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the transaction history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209095956-de825f6a-15eb-430d-ae72-79d3c0dcd6dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the transfer filter <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209096087-c8b297df-108d-4787-918b-1698596dedc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the withdraw filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209096222-277cb464-7177-4f57-bd98-d8a45415a00d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the date filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>The filters are used according to sort them with dates.<div>And also according to<br>deposits, withdrawals and transfers with the sorting filter</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/26">https://github.com/AkshatBhagat99/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-prod3.herokuapp.com/accounts/list">https://is601-ab2634-prod3.herokuapp.com/accounts/list</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209096863-6a638aff-4910-4dd9-b452-dae7ba2c3f64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the users profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/26">https://github.com/AkshatBhagat99/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-prod3.herokuapp.com/profile">https://is601-ab2634-prod3.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209097129-06cc2dd5-1c89-4dd8-9cf0-e0239fbb74b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>External transfer screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209097520-01522f5f-160b-4fef-bf1c-5fd39242c8ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows transfer exceeds the balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209097959-1a56a43e-84aa-4b32-8405-166ff4630946.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the following logic where the cannot exceed the limit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209098094-676cbbe5-28f7-474e-80b7-422161a27a2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the user cannot send negative amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209270110-0c37043e-b729-4468-8f7d-5b49a9afbeca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the code where they cant send a negative amount<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209098313-67864391-ff4f-4123-a271-06ca1515a475.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the user is not found<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209270309-0e690897-2207-4122-abd8-f7255dfbb7de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the logic if user doesnt exist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209098961-aeeb387a-bcf1-4846-8a53-e607264d5e20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the external transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209099360-c78f2ad5-dd15-445e-a85b-9e8bc21e74c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB shows the updated account balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>The account number is the unique id for the user which defines its<br>account. Last name is mandatory while making an external transfer.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/26">https://github.com/AkshatBhagat99/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-prod3.herokuapp.com/accounts/ext_transfer">https://is601-ab2634-prod3.herokuapp.com/accounts/ext_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Had got stuck on the transfer logic for a while, Fixed it with<br>adding the correct query. Rest was all great, had a few git branch<br>issues which got resolved with professor on discord<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-bank-project/grade/ab2634" target="_blank">Grading</a></td></tr></table>