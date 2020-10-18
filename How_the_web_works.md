1. `HTTP`: Hyper Text Transfer Protocal	is a client-server protocol that allows the client to get or send data from the server.
2. `URL`: Uniform Resource Locator is the address of a unique resource on the web
3. 	`TCP`: This is a strandard that defines how to establish or maintain a network connection through which application programs can exchange data.
4. `IP`: Internet Protocol is the set of rules or standard that governs how data is sent from one computer to another.
5. `DNS`: The Domain Name Server is a server that translates domain names to IP addresses. It takes in a domain name as input and outputs the IP address that corresponds to the domain as output.
6. `Idempotent`: An Idempotent operation will always return the same response given the
7. `Query String`: A query sting is part of a URL that allocates values to specified parameters.
8. `Path` or `Route`: is the path to a resource on a web server.
9. 4 HTTP verbs and their use cases
- GET : This is used to request or retrieve some piece of data from a specified resource on the server. Get is Idempotent
- POST : This is used to send data to the server to create or update a specified resource 
- DELETE : This is used to delete a specified resource from the server
- PUT : This is used to replace a target resource with data sent in the request. PUT is idempotent.
10. Client : In the context of network connections, the client is a computer making requests from (an)other computer(s)
11. Server : In the context of network connections, the server is a computer that receives requests and sends responses to other computers.                                               
12. `HTTP` request : This is the message sent from a client to a server asking for a resource or asking to put data into a resource.
13. `HTTP` response : This is the response to an HTTP request sent by a client. HTTP responses typically come from servers to return some data requested from a resource or indicating the completion or failure of an operation required by the client
14. `HTTP` headers are components of the header section of HTTP requests and responses. They are used to pass additional information that define the operation parameters of the HTTP request or response.
Examples of request headers are:
- User-Agent: the user agent string of the user agent
- Referer: The address of the previous web page from which a link to the currently requested page was followed.
- If-Modified-since: allows a `304 Not Modified` to be returned if content is unchanged
- Content-Type: The media type of the body of the request
- Content-Encoding: The type of encoding used on the data
- Accept: Media type(s) that is/are acceptable for the response
Examples of response headers are:
- Allow: Valid methods for a specified resource.
- Content-Length: The length of the response body in 8-bit-bytes
- Warning: A general warning about possible problems with the entity body
- Retry-After: If an entity is temporarily unavailable, this instructs the client to try again later. Value could be a specified period of time (in seconds) or a HTTP-date.
15. `REST`: REST (REpresentations State Transfer is a software architectural style that defines a set of constraints to be used for creating Web services.
16. `JSON`: JavaScript Object Notation is a lightweight data format used for transporting and storing data
17. When a string like 'Hello World' is entered into `google.com`, a request is sent to DNS to retrieve the IP address for Google.com, then a HTTP request is sent with the `Hello World` string as a search parameter to the IP address returned from the DNS. Google.com then returns results that match the string as a response to the request. 
18. The web being stateless means that every request takes place in complete isolation from any requests that might have happened before, or will happen later. Each request relies only on information sent along with it, and does not remember or use any information from other requests
19. `curl`: curl is a command line tool that parovides the ability to issue HTTP requests from the terminal.
20. `curl -H "Accept: application/json" https://icanhazdadjoke.com/search?term=pirate`



