@app.route('/user')
def user_locations():
    username = request.args.get('username') # Retrieve the username from the request

    user_locations = []

    # loop through each user element in the XML root
    for user in root.findall('user'):
        # check if the name attribute of the user element matches the given username
        if user.get('name') == username:
            # find all location elements within the found user element
            locations = user.findall('location')
            # loop through each location element and add its text value to the list of user locations
            for location in locations:
                user_locations.append(location.text)

    return user_locations # return the list of locations of the user