# server stat grapher
### easily graph server stats using google sheets

# instructions
1. download the repo as a .zip file and unzip it
2. create an account on [sheetdb](https://sheetdb.io/)
3. make a copy of [this spreadsheet](https://docs.google.com/spreadsheets/d/1178tFRt8Bb60Hq44sAP-8vP0zXdGTMk65Fd70hcu3KY/edit?usp=sharing) on the account you signed up to sheetdb with. it is vital that you not change any of the data in the existing columns, or the script won't work. however, you can customize the graph all you like.
4. click "Create new API" and paste the url of your newly copied spreadsheet
5. going back to the script, fill in the information in lines 4, 5, 6
6. publish all of the files in the folder to github as a **private** repo
7. go to [vercel.com](https://vercel.com/) and create an account if you don't already have one
8. on the dashboard of your account click "Add new..." and then "Project"
9. click add github account (if you didn't sign up with github), and then link your account
10. click "Import" on the repo you just created
11. on the next page, click "Deploy"
12. allow the vercel to build it, and then click on the website preview on the next page
13. finally to test if it's working, click the "push request" hyperlink.
14. you should see a message from your webhook, and there should be data in the spreadsheet
15. you're done! yipee!! please contact me with issues or questions at [my email](mailto:stat.graph@cloverbrand.xyz) or my [discord server](https://discord.gg/FXZATmh8zN).

##### with love, poppy