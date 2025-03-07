# Pending improvements

- DB backend: Allows to cache results and must improve regex search over the content.
Must be a relational DB because the structure is well-defined (gist 1-N file) but must support
very long text field.
- The Api can be protected setting limit over the number of gist and file size that a user can download
- The app can be deployed in any cloud via Kubernetes. In this way scalability and resilience can be achieved
- Using Kubernetes a health check can be implemented and when a server is not healthy it will be replaced
Also an alert system must be implemented to alert when ths problem happens to solve it
- This kind of service that need to wait for another api calls is more efficient to implement using async
to avoid exhausting the kernel threads
