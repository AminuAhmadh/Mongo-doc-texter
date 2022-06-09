import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
from pymongo import MongoClient
from dotenv import load_dotenv


# load environmental variables
load_dotenv()


uri = os.getenv('URI')
client = MongoClient(uri)
db = client.random
coll = db.excerpts


# sample of what to add
add = [

	{"type": "Excerpt:-\n",
	"value": """You might think you want an expensive car, a fancy watch, and a huge house.
What you want is respect and admiration from other people, and you think having expensive stuff will bring it.
It almost never does—especially from the people you want to respect and admire you.\n""",
	"source": "Book: The Psychology of Money by Morgan Housel."},

	{"type": "Excerpt:-\n",
	"value": """Modern capitalism is a pro at two things: generating wealth and envy.
Perhaps they go hand in hand; wanting to surpass your peers can be the fuel of hard work.
But life isn’t any fun without a sense of enough.
Happiness, as it’s said, is just results minus expectations.\n""",
	"source": "Book: The Psychology of Money by Morgan Housel."},

	{"type": "Excerpt:-\n",
	"value": """Control over doing what you want, when you want to, 
with the people you want to, is the broadest lifestyle variable that makes people happy.\n""",
	"source": "Book: The Psychology of Money by Morgan Housel."},

	{"type": "Excerpt:-\n",
	"value": """No one makes good decisions all the time.
The most impressive people are packed full of horrendous ideas that are often acted upon.
These are not delusions or failures of responsibility.
They are a smart acknowledgment of how tails drive success.\n""",
	"source": "Book: The Psychology of Money by Morgan Housel."}


	]


result = coll.insert_many(add)
# display the results of your operation
print(result.inserted_ids)

# Close the connection to MongoDB when you're done.
client.close()