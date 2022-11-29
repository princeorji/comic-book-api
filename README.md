# x-press-publishing

### Install Dependencies

1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Run the Server

To run the server, execute:

```bash
python manage.py runserver
```

### Route Paths and Functionality

`/api/`
- GET
  - Returns a 200 response containing all routes and their corresponding urls

```json
{
  "register": "/api/register/",
  "login": "/api/login/",
  "refresh_token": "/api/token/refresh/",
  "logout": "/api/logout/",
  "get_artists": "/api/get-artists/",
  "artist": "/api/artist/${id}/",
  "create_artist": "/api/create-artist/",
  "update_artist": "/api/update-artist/${id}/",
  "get_series": "/api/get-series/",
  "series": "/api/series/${id}/",
  "create_series": "/api/create-series/",
  "update_series": "/api/update-series/${id}/",
  "delete_series": "/api/delete-series/${id}/",
  "get_issues_by_series": "/api/series/${id}/issues/",
  "issue": "/api/issue/${id}/",
  "create_issue": "/api/create-issue/",
  "update_issue": "/api/update-issue/${id}/",
  "delete_issue": "/api/delete-issue/${id}/"
}
```

`/api/register/`
- POST
  - Registers new user to the database
  - Request Body:

```json
{
  "username": "example",
  "email": "example@gmail.com",
  "password": "ex@mql3"
}
```

`/api/login/`
- POST
  - Logs user into the system
  - Generates jwt token for logged in user 
  - Request Body:

```json
{
  "username": "example",
  "password": "ex@mql3"
}
```

`/api/token/refresh/`
- POST
  - Refreshes already generated token
  - Requires token generated during login 
  - Request Body:

```json
{
  "refresh": "token",
}
```

`/api/logout/`
- POST
  - Logs user out of the system
  - Returns:
  
```json
{
  "message": "Success"
}
```

`/api/get-artists`
- GET
  - Returns a 200 response containing all artists on the `artists` property of the response body
  
`/api/artist/${id}`
- GET
  - Returns a 200 response containing the artist with the supplied artist ID on the `artist` property of the response body
  - If an artist with the supplied artist ID doesn't exist, returns a 404 response
  
`/api/create-artist/`
- POST
  - Sends a post request in order to add a new artist
  - If any required fields are missing, returns a 400 response
  - Request Body:
  
```json
{
  "artist": 1,
  "biography": "a new biography string",
  "is_currently_employed": true
}
```
  
`/api/update-artist/${id}`
- PATCH
  - Updates the artist with the specified artist ID using the information from the `artist` property of the request body and saves it to the database. Returns a 200 response with the updated artist on the `artist` property of the response body
  - If any required fields are missing, returns a 400 response
  - If an artist with the supplied artist ID doesn't exist, returns a 404 response

`/api/get-series/`
- GET
  - Returns a 200 response containing all comic series on the `series` property of the response body
  
`/api/series/${id}/`
- GET
  - Returns a 200 response containing the series with the supplied artist ID on the `series` property of the response body
  - If a comic series with the supplied artist ID doesn't exist, returns a 404 response
  
`/api/create-series/`
- POST
  - Sends a post request in order to add a new series
  - If any required fields are missing, returns a 400 response
  - Request Body:
  
```json
{
  "name": "a name",
  "description": "a new description string"
}
```
  
`/api/update-series/${id}/`
- PATCH
  - Updates the comic series with the specified series ID using the information from the `series` property of the request body and saves it to the database. Returns a 200 response with the updated series on the `series` property of the response body
  - If any required fields are missing, returns a 400 response
  - If a comic series with the supplied artist ID doesn't exist, returns a 404 response
  
`/api/delete-series/${id}/`
- DELETE
  - Deletes a specified series using the id 
  - Request Arguments: `id` - integer
  - Returns:
  
```json
{
  "message": "Success"
}
```

`/api/series/${id}/issues/`
- GET
  - Returns a 200 response containing all saved issues related to the series with the supplied series ID on the `issues` property of the response body
  - If a series with the supplied series ID doesn't exist, returns a 404 response
  
`/api/issue/${id}/`
- GET
  - Returns a 200 response containing the comic issue with the supplied artist ID on the `issue` property of the response body
  - If an issue with the supplied artist ID doesn't exist, returns a 404 response
  
`/api/create-issue/`
- POST
  - Sends a post request in order to add a new issue
  - If any required fields are missing, returns a 400 response
  - Request Body:
  
```json
{
  "name": "a name",
  "issue_number": "#3",
  "publication_date": "2013-09-18",
  "artist_id": 2,
  "series_id": 2
}
```
  
`/api/update-issue/${id}/`
- PATCH
  - Updates the issue with the specified issue ID using the information from the `issue` property of the request body and saves it to the database. Returns a 200 response with the updated issue on the `issue` property of the response body
  - If any required fields are missing, returns a 400 response
  - If a series with the supplied series ID doesn't exist, returns a 404 response
  - If an issue with the supplied issue ID doesn't exist, returns a 404 response
  
`/api/delete-issue/${id}/`
- DELETE
  - Deletes a specified issue using the id 
  - Request Arguments: `id` - integer
  - Returns:
  
```json
{
  "message": "Success"
}
```

## Testing

To deploy the tests, run:

```bash
python manage.py test
```