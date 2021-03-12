## Email Word Cloud
A small little program that lets you visualize the frequency of words on email messages within a folder. The program itself connects to Yahoo or Gmail to fetch messages.

### Quick Setup
1. Clone this repo
2. ```python3 -m venv venv```
3. ```source venv/bin/activate```
4. ```pip3 install -r requirements.txt```
5. ```cp example.ini config.ini``` and *edit* with your configuration
6. *run* ```python3 email-wordcloud.py```
7. *open* cloud-results.png to visualize

> This has only been tested with Yahoo using app password. I suspect Gmail is the same process.

### Tips
* Put whatever you want to analyze into an email folder
* Cleansed emails are dumped into results.txt in case you want to analyze the messages further.
* Create a special email account/address for your email analysis. I use a separate account so I cut down on filtering. You can also use + addressing to filter these into a specific folder. Ex: my_addr+jobs@yahoo.com gets routed to a Jobs folders.

### Background
I developed this program as I was curious about market trends in the DevOps space and to have a better idea of what tech I should be looking at. What better way to get market trends then to understand what people are hiring for. So I created this little tool to basically parse recruiter emails. To ensure I'm getting email's I have my resume posted on several job sites. 

This could be used to analyze anything coming in through email. Maybe you have notifications or alerts and want to determine the most frequent type or your intrigued about the latest trends on spam. 
