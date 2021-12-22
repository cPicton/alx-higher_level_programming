# Import Module
import json

# Create geeks function


def to_json_string(my_obj):

	# Define Variable
	language = "Python"
	company = "GeeksForGeeks"
	Itemid = 1
	price = 0.00

	# Create Dictionary
	value = {
		"language": language,
		"company": company,
		"Itemid": Itemid,
		"price": price
	}

	# Dictionary to JSON Object using dumps() method
	# Return JSON Object
	return json.dumps(value)

        return json.dumps(my_obj)
