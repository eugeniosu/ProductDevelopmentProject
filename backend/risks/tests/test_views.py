from rest_framework.test import APIClient
from rest_framework import status


class ViewTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_api_can_create_field(self):
        field = {"name": "DOB", "type": "date", "enumValues": ""}
        response = self.client.post('/api/field/', field, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        getResponse = self.client.get("/api/field/%s/" % response.data['pk'])
        self.assertEqual(field['name'], getResponse.data['name'])
        self.assertEqual(field['type'], getResponse.data['type'])
        self.assertEqual(field['enumValues'], getResponse.data['enumValues'])

    def test_api_can_create_field_with_bad_request(self):
        wrongFormat = {"name": {"name": "1"}}
        response = self.client.post('/api/field/', wrongFormat, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_edit_field(self):
        field = {"name": "DOB", "type": "date"}
        response = self.client.post('/api/field/', field, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        field = {"name": "options", "type": "enum", "enumValues": "A,B"}
        responseEdit = self.client.put(
                            "/api/field/" + str(response.data['pk']) + '/',
                            field,
                            format="json"
                            )
        self.assertEqual(responseEdit.status_code, status.HTTP_200_OK)

        getResponse = self.client.get("/api/field/%s/" % response.data['pk'])

        self.assertEqual(field['name'], getResponse.data['name'])
        self.assertEqual(field['type'], getResponse.data['type'])
        self.assertEqual(field['enumValues'], getResponse.data['enumValues'])

    def test_api_can_create_riskType(self):
        field = {"name": "DOB", "type": "date"}
        responseField = self.client.post('/api/field/', field, format="json")

        riskType = {"name": "Houses", "field": [responseField.data['url']]}
        response = self.client.post('/api/risktype/', riskType, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        getResponse = self.client.get(
                                    "/api/risktype/%s/" % response.data['pk']
                                    )
        self.assertEqual(riskType['name'], getResponse.data['name'])

    def test_api_can_create_riskType_with_bad_request(self):
        wrongFormat = {"name": {"name": "1"}}
        response = self.client.post(
                                '/api/risktype/', wrongFormat, format="json"
                                    )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_edit_riskType(self):
        field = {"name": "DOB", "type": "date"}
        responseField = self.client.post('/api/field/', field, format="json")

        riskType = {"name": "Houses", "field": [responseField.data['url']]}
        response = self.client.post('/api/risktype/', riskType, format="json")

        riskType = {"name": "Mansions", "field": [responseField.data['url']]}
        responseEdit = self.client.put(
                            "/api/risktype/" + str(response.data['pk']) + '/',
                            riskType,
                            format="json"
                            )
        self.assertEqual(responseEdit.status_code, status.HTTP_200_OK)

        getResponse = self.client.get(
                                    "/api/risktype/%s/" % response.data['pk']
                                    )
        self.assertEqual(riskType['name'], getResponse.data['name'])

    def test_api_can_create_risk(self):
        field = {"name": "DOB", "type": "date"}
        responseField1 = self.client.post('/api/field/', field, format="json")

        field = {"name": "Full Name", "type": "text"}
        responseField2 = self.client.post(
                                        '/api/field/', field, format="json"
                                        )
        riskType = {
          "name": "Houses",
          "field": [
            responseField1.data['url'],
            responseField2.data['url']
          ]
        }
        responseRiskType = self.client.post(
                                    '/api/risktype/', riskType, format="json"
                                    )

        risk = {
          "risk": {
            "name": "House A",
            "risk_type": responseRiskType.data['url']
          },
          "fieldRisk": [{
              "value": "2018-01-01",
              "field": responseField1.data['url'],
            },
            {
              "value": "Eugenio Suarez",
              "field": responseField2.data['url'],
            }
          ]
        }
        response = self.client.post('/api/risk/', risk, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        getResponse = self.client.get("/api/risk/%s/" % response.data['pk'])
        self.assertEqual(
                        risk['risk']['name'],
                        getResponse.data['risk']['name'])
        self.assertEqual(
                        risk['fieldRisk'][0]['value'],
                        getResponse.data['fieldRisk'][0]['value']
                        )
        self.assertEqual(
                        risk['fieldRisk'][1]['value'],
                        getResponse.data['fieldRisk'][1]['value']
                        )

    def test_api_can_create_risk_with_bad_request(self):
        wrongFormat = {"risk": {"name": "Eugenio"}}
        response = self.client.post('/api/risk/', wrongFormat, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
