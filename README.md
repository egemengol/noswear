# noswear

An api for swear detection in english language. Does not require any key or registration from the free [Purgomalum API](https://www.purgomalum.com/). 

### Usage

---
`noswear/json/This%20is%20my%20fucking%20sentence.`
```json
{
	"wasSwearing": true,
	"censored": "This is my ******* sentence."
}
```
---

`noswear/plain/This%20is%20my%20sentence.`
```
This is my ******* sentence.
```
---

`noswear/json/Pretty%20standard`
```json
{
	"wasSwearing": false,
	"censored": "Pretty standard"
}
```
---
`noswear/plain/Pretty%20standard`
```
Pretty standard
```
---
