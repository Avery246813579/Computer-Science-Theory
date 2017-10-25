# Restful Api

Representational state transfer, also known as Restful api, is an
architectural style and approach of communications often used in web
services development. In plain English, Restful api is a guideline that
most apis run by.

## Http Requests

A HTTP requests is called using an HTTP request. In a HTTP request we
have two big parts. We have a request, in which we send information to
the server. Then we have a response, in which the server sends
information back.

Every request and response have headers and a specific route type. Most
requests have a body, but all responses have a body. A header is
information passed to the server during every request. A route type is
the Restful route name. And the body is the information you will send or
receive to and from the server.

## Restful Routes

To understand Restful Api we have to understand Tthe five main Restful
routes are GET, POST, PATCH, PUT, and DELETE. When I refer to route it's
the VERB you send to the server. You also can send something called a
body which will contain for your request.

#### GET
The GET route (also known as read) returns back information. An example
would be how browsers call a websites get route and your browser
interprets that info.

You would call a GET request by calling a plural or single name. For
example, you can do `/dogs` to get a list of all the dogs from a server or
do `/dog/:ID` to get a single dog from your server. GET requests have no
body.


#### POST
The POST route (also know as create) creates somethings. You send
information about the item you want to create using the body of your
request. The POST request usually doesn't return anything, but if it
does it's only information on the item you create.

Along with creating things, somethings POST can be used for actions in a
server. Like if I wanted to send an email I would send a POST request to
my server.

You would send a POST request by calling a singular name without an id.
To create a new dog you would do `/dog` and pass dog parameters through
the requests body using json.

#### PATCH
The PATCH route (also known as Update/Modify) updates something. You
would send the patch to a specific element (using it's id) on your
server and in the body of your request would be the information you want
updated.

You would send a PATCH request by sending a request to the id of the
element you want in the server. If you want to change the dogs fur color
you would send a PATCH request to the `/dog/:ID` route and add fur color
to the body using json.

#### PUT
The PUT route in my opinion is the worst Restful route. Like PATCH it
updates something, but instead of taking in the element you want to
change, you have to input the full object. It's used to replace an item
while PATCH is to update. This means if you want to change the color of
a dog, you would have to send the full dog with the changed color to the
server.

Don't use this route, PATCH is better in mostly all situations.

#### DELETE
The delete Route deletes something. You would send a DELETE request to
the server for specific item, and it deletes it.

If you want to delete a dog you would send the delete to /dog/:ID and
it would delete it.

## Returning info

Restful Api is a great way of representing data, but the information
you are suppose to return back isn't always the best. For specific
routes you are suppose to return back specific error codes. I don't like
this, and other APIs don't like this. The reason I don't like this is
when I send an API call and it's rejected, I don't want my console to
be scattered with errors. That's why I (I as in I copied from some api
I used in the past) have formed conventions in returning back info.

My convention starts with every API call returning back 200 (success).
Then the response body will have a few things depending if the request
was successful or not. But everything we return back is in a json object
in the response body.

#### Successful Request
If a route is successful, which means our route does what it's suppose
to do, we first add `success: true` to our response body. If our request
requires information back we will return that information in a data
variable in our response body. If the information we want is an object
then we will return a JSON object, if it's a list of objects then we
will return a list of JSON objects.

For example if we were calling to get a singular dog (`/dog/5`) object,
our response body would be:

    {
        "success": true,
        "data": {
            "name": "Good boy",
            "color": "Blue",
            "age": 20
        }
    }

If we were requesting to GET a list of dogs (`/dogs`), our response body
would be:

    {
        "success": true,
        "data": [
          {
            "name": "Good boy",
            "color": "Blue",
            "age": 20
          },
          {
            "name": "Bad boy",
            "color": "Black",
            "age": 5
          }
        ]
    }

If we were requesting to POST a dog (`/dog`), our response body would be:

    {
        "success": true,
        "data": {
            "ID": 5
        }
    }

If we were requesting an POST action to our server ('/email/:ID'), our
response body would be:

    {
        "success": true
    }

#### Unsuccessful Request
If our request was unsuccessful, or didn't do what it was intended to,
we will first return `success: false` into our response body. We will
also return not only an error `code`, but an error `message` about why our
request was unsuccessful. These error codes will be generated by the
server, and each developer can name and number them how they like. We
can also somethings return `data` in our response body but only
indicating information which we didn't like.

What if we request to GET a dog, and can't find it:

    {
        "success": false,
        "code": 420,
        "message": "Can't find element with id"
    }

What if we try to POST a dog, but our request body is missing an
element:

    {
        "success": false,
        "code": 12,
        "message": "Missing element in request body",
        "data": {
            "element": "NAME"
        }
    }

## Constructing the best API
When constructing the best API, you want your server to make sense. With
most servers you can get long URL chains because you will have so many
routes to do so many

Say you want to get the posts that a user has. We would send a request
to the URL `/user/:ID/posts`. Now if we wanted to see a specific post
by the user, we could send a request to `/post/:ID` because we just
care about the POST, not the user.

## Authentication
You want to authenticate your user using tokens in a header, or a cookie
which is in the header. An example would be passing a jwt with a header
then in your server you would find the token with the header and
authenticate the user based on it.

Don't be passing your tokens through your body each request. That's
not called for. Headers are used from constant info and cookies are
stored and send every request. So if I were you, use cookies. You can
even return back a header called set-cookie which sets a cookie on the
client side.

We use our authentication key every time a request is send to the
server. We will be able to get the users unique id by parsing the token
in which ever way we constructed. For starters, using JWT is best
practice.

## Bad Practices
When you send a request using Restful Api, we only want to do what the
route entails. Don't be trying to return information (besides creation
info) back with a POST, and really don't try to re-render a page with
a POST. All these requests have specific purposes, so lets use them.

## Useful Tools
The best took to use for testing a Restful Api is a chrome extension
called Advanced REST client. You can also do things like connect to
sockets with it.