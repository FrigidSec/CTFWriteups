### Break it
###### Description: A cybercop made a plan to fool the hacker from getting flag. Are you true hacker?

---
In this challenge, you get asked a question and have 2 radio buttons to click on before submitting: 

----
**Do you want the flag?**
- [ ] Yes
- [x] No

`Submit`
----
However, clicking on "Yes" ends up selecting "No". All you had to do was select "Yes" using JavaScript instead of clicking on it. This can be done easily using something like-
```javascript
document.querySelector("#yes").checked = true;
```
After that, you're led to an empty page (or is it?). Upon inspecting the HTML, you find a comment telling you to just send "hacker" instead of "yes" in your request.
So fire up your BurpSuite, send the request but intercept it and change the value of the data from "yes" to "hacker" instead. And you have your flag!
