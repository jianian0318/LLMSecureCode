@app.route('/user')
def user_locations():
    # Retrieve the username from the request
    username = request.args.get('username')

    # Make an XPath query to find the user in the XML root
    user_xpath = f"./user[@name='{username}']/location"
    locations = root.findall(user_xpath)

    # Create a list of the locations
    location_list = [location.text for location in locations]

    # Return the list of locations
    return location_list