# Ubidots API Usage

## Get variable

Get the variable state recently.
```
curl -H "Content-Type: application/json" "http://things.ubidots.com/api/v1.6/variables/573fbb1f7625423b1d1c0523/values/?token=BQVCK7vEK1t59qPNFGVgCdyZ8HRogc&page_size=2"
```
Response
```
{
  "count": 68,
  "next": "http://things.ubidots.com/api/v1.6/variables/573fbb1f7625423b1d1c0523/values/?token=BQVCK7vEK1t59qPNFGVgCdyZ8HRogc&page=2&page_size=2",
  "previous": null,
  "results": [
    {
      "url": "http://things.ubidots.com/api/v1.6/values/574015b7762542230698f822",
      "value": 0,
      "timestamp": 1463817655429,
      "context": {},
      "created_at": "2016-05-21T08:00:55.429"
    },
    {
      "url": "http://things.ubidots.com/api/v1.6/values/574015ad762542230698f813",
      "value": 0,
      "timestamp": 1463817645880,
      "context": {},
      "created_at": "2016-05-21T08:00:45.880"
    }
  ]
}
```

## Update variable

Update the variable, the API document show as following command, but the value update will delay about 5 minutes, is it a bug?
```
curl -X POST -H "Content-Type: application/json" -d '{"value":1}' http://things.ubidots.com/api/v1.6/variables/573fbb1f7625423b1d1c0523/values/?token=BQVCK7vEK1t59qPNFGVgCdyZ8HRogc
```


Update the variable, the SDK use following command and it can update immediately.
```
curl -X POST -H "Content-Type: application/json" -H "X-AUTH-TOKEN: BQVCK7vEK1t59qPNFGVgCdyZ8HRogc" -d '{"value":1}' http://things.ubidots.com/api/v1.6/variables/573fbb1f7625423b1d1c0523/values
```
