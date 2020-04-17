# save-external-IP-NO-DNS
instead of use Domain Name, you can save your IP on Gmail account :)

if you don't want to buy domain name, and you have to know what your external IP address (as me :),
so I had idea: why can't I save my IP on gmail (it's not that you have server or something like that, if you want to access your computer by ssh from work to home you can use this), well I created these scripts for save the IP and to get the IP.

# Instructions for the scripts will work:
the script will not be able to send the IP, so you have to enable third party app (and unsafe ;) to access to your gmail account: https://myaccount.google.com/lesssecureapps
I suggest you to create another Gmail account...

instead of send the IP to the mail every, the script save the IP on the computer, so set your path...

well after you reset the parametes on the script, you can run the script every X min/hours on the computer (by using crontab):
*/45 *    * * * root    /home/user/scripts/ip_email.py
