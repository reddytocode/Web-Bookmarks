
Get List endpoint (Anonymous)
```bash
curl localhost:8000/v1/bookmarks/
```


Get List endpoint (Authenticated user) (./manage createsuperuser)
```bash
curl localhost:8000/v1/bookmarks/ --user "name:password"
```


Create needs authentication
```bash
curl --user "name:password" --header "Content-Type: application/json" --request POST --data '{"is_private": "false", "title": "fake-bookmark", "url": "fake-url"}' localhost:8000/v1/bookmarks/
```

Update 
```bash
curl --user "name:password" --header "Content-Type: application/json" --request PATCH --data '{"is_private": "false", "title": "fake-bookmark", "url": "fake-url"}' localhost:8000/v1/bookmarks/1
```

Update 
```bash
curl --user "name:password" --request DELETE  localhost:8000/v1/bookmarks/1
```


