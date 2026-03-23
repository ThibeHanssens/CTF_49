# Resources
- web server
# Approach
I first created a test account and logged in with it
![[Pasted image 20260323103129.png]]
Here we see that there is a user AdminFlag
![[Pasted image 20260323103027.png]]
We have to log in as AdminFlag but we dont know the password. However, I noticed that there is a reset password button on the login screen
![[Pasted image 20260323103614.png]]
Of course if we send a request, we dont have access to the email of the user. but if we check in the request body we see this![[Pasted image 20260323103756.png]]
If we send it to the repeater and look at the response we get 
![[Pasted image 20260323104318.png]]
We just follow this link and set a new password for the user AdminFlag
![[Pasted image 20260323104334.png]]
Then we can go back to the login screen and log in as user AdminFlag. This gives us the flag