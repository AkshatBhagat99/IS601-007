<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Akshat Mahesh Bhagat (ab2634)</td></tr>
<tr><td> <em>Generated: </em> 10/24/2022 7:37:46 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ab2634" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197649047-f3004c31-c648-43bb-a66a-4176a0d931b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows code which is used to calculate the cost of the icecream<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197438775-a5e9ac88-9aa1-44c3-914a-84bd0ed83113.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The output where it shows the calculated cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>For the following code, the cost of the toppings and scoops was defined<br>earlier. Used if else loop, if the user chooses waffle cone, the price<br>will be $1.5, or else $1 for normal cone.<div><div>We have already defined the<br>price amount for each of the container, toppings and its flavors. It is<br>easy to calculate the total amount after taking the input from the user.<br>for eg: The user is chose cup as a container for his Icecream,<br>cost for one cup is 1$ and for flavor its 2$(vanilla, chocolate) and<br>lastly for toppings its 0.50$(Chocolate chips, m&amp;m&#39;s). Now we&#39;&#39;ll sum it all up<br>using &quot;cost=cone_price+(number_of_scoops)(flavor_price)+(number_of_toppings)(toppings_price)&quot;. cost= 1+2<em>1+2</em>0.25= 3.5. The total cost for the user&#39;s Icecream will<br>be $3.5.</div><div>The user will be asked to choose their desired container, flavor and<br>toppings, they can add more than one of those and then in the<br>end an exact price amount for the icecream will be asked as input<br>to complete the procedure.</div><div><br><div><br><div><br></div></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197462809-3388b89d-9eec-4934-8f35-4f02d05be6fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows that the topping is out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197462810-0625cd53-bfca-4781-8c9c-3b04330f2be6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for out of stock exception pt.1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197462811-d8ae1a17-74fa-4e1f-9626-27eb30d4d6e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for out of stock exception pt.2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197462893-3989ddba-45ea-4381-b9e4-a09ab176d191.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the machine needs cleaning part<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197462894-e519f837-2ed8-42d8-89c8-f35e8eadd5d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output where the program asks for cleaning<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463132-f5e7d865-4dc0-4de0-b171-10f8250a99c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the invalid choice exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463134-fe235737-b7b9-4df2-b7f9-2bd7caeb2a9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for invalid choice exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463207-be1f7bf5-0f40-4666-9e7c-98759ee32386.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for exceeded choices for the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463208-d6899416-d293-4465-92c7-14f78defda72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for exceeded choices for the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463010-f78df05c-054e-4f5a-9a9a-47ff51c1e8ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for invalid payment<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197463009-286b29f0-24ff-4c22-aedb-1c659f1ab5b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for invalid payment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">&nbsp;OutOfStockException: This exception occurs when a particular topping or a scoop<br>is out of stock</span><div><span style="font-size: 13px;">NeedsCleaningException:&nbsp;</span><span style="font-size: 13px;">This exception occurs when the machine<br>needs to go under cleaning after a certain amount of rounds</span><span style="font-size: 13px;"><br></span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;InvalidChoiceException:&nbsp;</span><span style="font-size: 13px;">This exception occurs when the user enters a choice which<br>is not available in the given options&nbsp;</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">ExceededRemainingChoicesException:&nbsp;</span><span style="font-size: 13px;">This<br>exception occurs when the user exceeds the number of given choices</span><span style="font-size: 13px;"><br></span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;InvalidPaymentException:&nbsp;</span><span style="font-size: 13px;">This exception occurs when the user puts in the wrong<br>amount</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648573-88d8c474-5d8a-4f51-8360-aefe08a35772.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 1 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648574-e628074d-91b8-464d-b05f-36987483cf11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 2 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648575-1174c19c-6cbf-4c48-80e7-9412219a3a9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 3 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648577-8bcbc32e-708e-46e7-b314-85204156428c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 4 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648578-b6b4b7c6-0cc2-44bb-a7a9-e938f20f9baf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 5 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648580-373e08af-69e1-496a-a3bb-75e431926456.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 6 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648581-d0d3f1cd-2581-454b-8e29-d84280ac03a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 7 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197648570-4bf01eb8-c903-4436-9dfe-deac21865c9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test case 8 code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197649837-326d6ac7-4f17-49fd-9ea1-5a40f631fcfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot where all test cases are passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test 1: the container must be the first selection in which we can&#39;t<br>add flavors/toppings without a container choice<div><div><div><div><div><div><div><div><div>Test2: flavors can only be added if they&#39;re<br>in stock</div><div>Test3: toppings can only be added if they&#39;re in stock</div><div>Test4: user can<br>add up to 3 flavors/scoops</div><div>Test5:User can add up to 3 toppings</div><div>Test6: cost is<br>calculated properly based on the input given by user</div><div>Test7: Sum of costs is<br>calculated properly by including a few Icecream combinations</div><div>Test8:Total Icecream is properly incremented for<br>each purchase</div></div></div></div></div></div></div></div><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/3">https://github.com/AkshatBhagat99/IS601-007/pull/3</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>From this miniproject, i learned how to use the exception handling and testcases<br>for the ice cream machine.<div>I had difficulties with the testcases as I could<br>not run them, But then got them resolved with the professor&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197469271-12fbbd94-a391-4fa6-92a7-ecb13f1d2743.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful output screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/197469276-6e7e162e-11b1-45eb-a32d-3802a0f5f697.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful output screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ab2634" target="_blank">Grading</a></td></tr></table>