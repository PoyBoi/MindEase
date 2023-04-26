import cgi
import cgitb

print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type")
print("Content-Type: text/html\n")

cgitb.enable()
form = cgi.FieldStorage()
input_field_value = form.getvalue('input-field')

# Process the input field value here
print(f"You entered: {input_field_value}")