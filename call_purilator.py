import requests
# structured XML
# SOAP request URL

# Development Key: 59c4ac554356438083cb7cbadc2ab10a
# Development Key password: PiszAZ[=
# Test Courier Account number: 9999999999
# Test Freight Account number: F271

url = "https://webservices.purolator.com/EWS/V2/ServiceAvailability/ServiceAvailabilityService.asmx?wsdl"

payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                        <sCountryISOCode>IN</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
            </soap:Envelope>"""
# headers


headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload)

# prints the response
print(response.text)
print(response)