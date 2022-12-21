<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Akshat Mahesh Bhagat (ab2634)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 5:45:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ab2634" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209008196-2f2496cb-97d6-42d3-9380-10ff9a68ed52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for admin create item page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209008372-3533d862-2de8-41f6-8600-c456540045cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the added product in the database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The item function in shop.py receives the values when they are entered on<br>the add page. To determine if the action is to edit or add,<br>it checks if an id has been passed.&nbsp;&nbsp;<div>No id will be passed, hence<br>This is a create action, and if successful, a flash is shown. An<br>insert statement is done, passing the values to the Products table.<br style="box-sizing: border-box;<br>color: rgb(201, 209, 217); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial,<br>sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(22, 27, 34);"><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/admin/item">https://is601-ab2634-msprod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209011353-0c99d8a6-b59d-40f6-bca5-a1bc90b428a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the visible products on the shop for user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209010131-b82e70e1-5061-45db-87a7-6871defd96be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the electronics filter with price high to low<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/208852224-b1a985c0-dba1-4dff-a88a-a3d71eee58cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has the filter/sort logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>Initial data for the shop page comes from the Products table, whose visibility<br>is set to 1.</div><div>Also, the page allows for name searches, category selections, and<br>price "High to Low" or "Low to High" sort.<br></div><div>When we use one or<br>more of the following search options. We proceed to the shop.py function's shop<br>list and modify the query's where condition based on the input. and then<br>show the outcomes once more.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/shop">https://is601-ab2634-msprod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209010533-44f520ab-7be6-480a-aa8c-f38f8d0436d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the Owner product list with the visiblity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>Without applying any filters, we choose every field from the Products database and<br>feed it to the html page.</div><div>Since no conditions are stated anywhere, every product<br>will be shown regardless of visibility status.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/admin/items">https://is601-ab2634-msprod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209009514-18f6660b-7dac-4c6f-849b-0de027186df0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of admin can see edit button on the product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209011184-f988734f-b4ae-4587-a23a-3a4443007720.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for product details admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209010533-44f520ab-7be6-480a-aa8c-f38f8d0436d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the edit button on admin page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209011893-078be4af-64dd-4869-8352-fdee6023d225.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing the food item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209012076-f26fd1ef-f8d9-4293-a7ab-520cb4e47de0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed the name and description. Updated the stock and price of the item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>For the Shop page, we check the user's login status and admin status<br>at the end of each product in shop.html. If both conditions are true,<br>we display an edit button that takes the user to the item page<br>with the product details.</div><div>The edit button is displayed on the item details page<br>if the user is an admin.</div><div>Since only admin can access the page, the<br>edit button is the default on the admin items page.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/admin/item?id=14">https://is601-ab2634-msprod.herokuapp.com/admin/item?id=14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209013363-431e2dbb-f1b2-45f2-a079-badc5d62bbb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The product page, when you click on the product, it will direct to<br>the details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209013587-8e0657f7-3813-4bd8-874c-716b3f74ed4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result of the product details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>For this, I made the itemdetails.html and itemdetails function.</div><div>The product name has been<br>made clickable; when clicked, it will send the product id to the itemdetails<br>function, which will retrieve all the information from the Products database using the<br>id and display it on the item details page.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/itemdetails?id=15">https://is601-ab2634-msprod.herokuapp.com/itemdetails?id=15</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209013921-0d71ab43-b9c5-4311-b40f-a7201d2a0a04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209014034-df4d271b-559b-47a8-aafe-87e19bb9a49b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows when not logged in and cannot add to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209014261-20cd7bf7-b26b-4bdc-8731-b1bde358f169.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the cart in database <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user, having product_id &amp; user_id as composite unique key<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>By clicking the ADD button, the shop.py's cart function receives the product id<br>as a hidden field and the amount field.</div><div>And since amount is more than<br>0, we insert the product id, user id, desired quantity, and unit price<br>as soon as the product id is passed (fetching it from products table)<br></div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209014650-c88475bd-41ac-4727-92c2-b47f7683a9a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SCreenshot of cart total and items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div>When we click the cart, the function checks to see if a product<br>id is being passed and, if it isn't, it recognizes that this isn't<br>an add or update function.</div><div>It then moves to the SELECT block to get<br>the user id, id, product id, name, and desired quantity, calculates the subtotal<br>by multiplying the desired quantity by the unit price, and passes these values<br>to cart.html.</div><div>For the purpose of calculating the total, we render each item as<br>a row in a table in the HTML output, add the subtotal value<br>for each row to a variable called ns.total, and then display the total<br>at the bottom.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/cart">https://is601-ab2634-msprod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015105-55cbb307-2ceb-4622-8cf0-103c4d75a60d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating the quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015312-90abf3ba-7e5c-4932-8a2d-c24cc607b118.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated the dustbin quantity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015105-55cbb307-2ceb-4622-8cf0-103c4d75a60d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before setting the quantity of cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015700-60f70112-eedd-45d9-a079-62dcf002dbaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After setting dustbin quantity to zero<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015806-b69ffc91-73ab-4a89-ae7a-7a3c57cf3253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the negative quantity handling<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>When we click the update button in the cart, a secret product id<br>in addition to the amount field and the update button will be provided<br>to the cart function.</div><div>In the code, if the quantity is greater than 0,<br>we first retrieve the name and price from the products table before updating<br>the quantity and price in the cart table while supplying the product id<br>and user id.</div><div>As the number is less than 0, when we enter 0<br>in the quantity field, the code moves to the DELETE block, where we<br>delete the product from the cart database while passing the product id and<br>user id.</div><div>We set the minimum value for the input field in HTML to<br>0 to handle negative values in quantity fields.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209015983-bd388d39-cb69-4b52-813d-4a2ac31f3da8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before deleting an item from cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209016044-18272a70-0854-4c03-8c4a-d228699b49e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting the item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209016197-a456f35c-fdf0-40af-aefd-991e9299e584.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/114647520/209016257-de09851f-05fb-4cce-95ff-fd234454b50b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>when removing a single item in cart, when the amount is less than<br>zero, the cart function runs the Delete query while passing the product id.<br>A hidden field quantity of -1 will be submitted next to the delete<br>button.</div><div>In the cart function, if the delete all parameter is True, we delete<br>the records in the Cart table while supplying the user id when clearing<br>the total cart.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AkshatBhagat99/IS601-007/pull/20">https://github.com/AkshatBhagat99/IS601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I had a few issues with the local and remote branches, so got<br>a little stuck on that part. Got them resolved with professor.<div>Overall it was<br>quite challenging for the adding cart logic and login. Also was stuck on<br>the admin roles part due to some issue. Resolved it myself</div><div><br></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ab2634-msprod.herokuapp.com/login">https://is601-ab2634-msprod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ab2634" target="_blank">Grading</a></td></tr></table>