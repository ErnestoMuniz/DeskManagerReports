
# DeskManagerReports
A DeskManager module for TelegramReports reports

## Instalation
First you will need to download or clone this repository and put it on the modules folder.
Then edit the following files:

keys.json
```json
{
	"cookies" : {
		"AWSELB": "YOURKEY",
	    "AWSELBCORS": "YOURKEY",
	    "deskmanager": "YOURKEY",
	    "_ga": "YOURKEY",
	    "_gid": "YOURKEY",
	    "_gat": "YOURKEY"
	},
	"Aguardando Aprovação" : "📝",
	"Aguardando Atendimento" : "⏳",
	"Andamento" : "🚶",
	"Transferência" : "🔄",
	"Aguardando Cliente" : "📆"
}
```
variables.json
```json
{
  "url": "https://myexampleurl.desk.ms/",
  "arg": "DO NOT MODIFY THIS KEY VALUE",
  "report": "DO NOT MODIFY THIS KEY VALUE"}
```
model.txt
```text
That's some example text
 - You can put some {keywords} on it -
 \ if you want it to have dinamic data from the API /

 Eg.
    The current time is {time}

 It will be displayed as:
    The current time is 03:46 (or whatever time it is when you give the command)
```
## KeyWords List
KeyWords for model.txt
```python
{day} = Returns the current day of the month
{month_name} = Returns the month name
{time} = Returns the current time in the format HH:MM
{ticket_list} = Returns the tickets list
{total_tickets} = Returns the amount of open tickets
```
## Usage
Then you just need to send the following command to receive your report:
```
/desk
```
And you're done! The bot will reply with all the data you wanted.
