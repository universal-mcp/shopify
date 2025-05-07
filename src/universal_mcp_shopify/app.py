from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class ShopifyApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='shopify', integration=integration, **kwargs)
        self.base_url = "https://{{store_name}}.myshopify.com"

    def retrieves_alist_of_access_scopes_associated_to_the_access_token(self) -> dict[str, Any]:
        """
        Retrieves the list of OAuth access scopes (permissions) granted to an application using the Shopify Admin REST API.

        Returns:
            dict[str, Any]: List all scopes

        Tags:
            Access, AccessScope
        """
        url = f"{self.base_url}/admin/oauth/access_scopes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_storefront_access_tokens_that_have_been_issued(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of storefront access tokens, which are used to authenticate requests to the Shopify Storefront API, allowing access to data such as products and checkout functionality.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of storefront access tokens that have been issued

        Tags:
            Access, StorefrontAccessToken
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/storefront_access_tokens.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_storefrontaccesstoken(self, api_version, storefront_access_token=None) -> dict[str, Any]:
        """
        Creates a Shopify Storefront API access token for client-side GraphQL requests, enabling access to store data like products, collections, and checkout.

        Args:
            api_version (string): api_version
            storefront_access_token (object): storefront_access_token
                Example:
                ```json
                {
                  "storefront_access_token": {
                    "title": "Test"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new storefront access token

        Tags:
            Access, StorefrontAccessToken
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'storefront_access_token': storefront_access_token,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/storefront_access_tokens.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_existing_storefront_access_token(self, api_version, storefront_access_token_id) -> Any:
        """
        Deletes a storefront access token and returns a success status upon completion.

        Args:
            api_version (string): api_version
            storefront_access_token_id (string): storefront_access_token_id

        Returns:
            Any: Delete an existing storefront access token

        Tags:
            Access, StorefrontAccessToken
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if storefront_access_token_id is None:
            raise ValueError("Missing required parameter 'storefront_access_token_id'")
        url = f"{self.base_url}/admin/api/{api_version}/storefront_access_tokens/{storefront_access_token_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_reports(self, api_version, ids=None, limit=None, since_id=None, updated_at_min=None, updated_at_max=None, fields=None) -> dict[str, Any]:
        """
        Retrieves reports data for specified parameters, such as IDs, limit, and date ranges, using the GET method.

        Args:
            api_version (string): api_version
            ids (string): A comma-separated list of report IDs.
            limit (string): The amount of results to return.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            updated_at_min (string): Show reports last updated after date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show reports last updated before date. (format: 2014-04-25T16:15:47-04:00)
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a list reports last updated after 2005-07-31 15:57:11 in the EDT timezone / Retrieve a list of all reports / Retrieve a list all reports after the specified ID / Retrieve a list of all reports, showing only some attributes / Retrieve a list of specific reports

        Tags:
            Analytics, Report
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/reports.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit), ('since_id', since_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_report(self, api_version, report=None) -> dict[str, Any]:
        """
        Submits a report generation request and returns a success status upon creation.

        Args:
            api_version (string): api_version
            report (object): report
                Example:
                ```json
                {
                  "report": {
                    "name": "A new app report",
                    "shopify_ql": "SHOW total_sales BY order_id FROM sales SINCE -1m UNTIL today ORDER BY total_sales"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new report

        Tags:
            Analytics, Report, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'report': report,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/reports.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_report(self, api_version, report_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a report by its ID using the specified API version and optionally includes additional fields in the response.

        Args:
            api_version (string): api_version
            report_id (string): report_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a single report / Retrieve a single report, showing only particular fields

        Tags:
            Analytics, Report, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if report_id is None:
            raise ValueError("Missing required parameter 'report_id'")
        url = f"{self.base_url}/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_areport(self, api_version, report_id, report=None) -> dict[str, Any]:
        """
        Updates or replaces a specific report resource at the specified report ID in JSON format using the PUT method.

        Args:
            api_version (string): api_version
            report_id (string): report_id
            report (object): report
                Example:
                ```json
                {
                  "report": {
                    "id": 517154478,
                    "name": "Changed Report Name",
                    "shopify_ql": "SHOW total_sales BY order_id FROM sales SINCE -12m UNTIL today ORDER BY total_sales"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an existing report

        Tags:
            Analytics, Report, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if report_id is None:
            raise ValueError("Missing required parameter 'report_id'")
        request_body = {
            'report': report,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_areport(self, api_version, report_id) -> dict[str, Any]:
        """
        Deletes the specified report using the DELETE method and returns a successful status upon completion.

        Args:
            api_version (string): api_version
            report_id (string): report_id

        Returns:
            dict[str, Any]: Delete an existing report

        Tags:
            Analytics, Report
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if report_id is None:
            raise ValueError("Missing required parameter 'report_id'")
        url = f"{self.base_url}/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_application_charges(self, api_version, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of application charges in JSON format, allowing filtering by specific fields and starting from a given ID.

        Args:
            api_version (string): api_version
            since_id (string): Restrict results to after the specified ID.
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve all application charges / Retrieve all application charges since a specified ID

        Tags:
            Billing, ApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/application_charges.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_an_application_charge(self, api_version, application_charge=None) -> dict[str, Any]:
        """
        Creates a new application charge through the API, returning a success response upon creation or an error if validation fails.

        Args:
            api_version (string): api_version
            application_charge (object): application_charge
                Example:
                ```json
                {
                  "application_charge": {
                    "name": "Super Duper Expensive action",
                    "price": 100,
                    "return_url": "http://super-duper.shopifyapps.com",
                    "test": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an application charge / Create a test charge that will not cause a credit card to be charged

        Tags:
            Billing, ApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'application_charge': application_charge,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/application_charges.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_an_application_charge(self, api_version, application_charge_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details of a specific application charge transaction using specified fields from the Stripe Connect API.

        Args:
            api_version (string): api_version
            application_charge_id (string): application_charge_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve an application charge

        Tags:
            Billing, ApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if application_charge_id is None:
            raise ValueError("Missing required parameter 'application_charge_id'")
        url = f"{self.base_url}/admin/api/{api_version}/application_charges/{application_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activates_an_application_charge(self, api_version, application_charge_id, application_charge=None) -> dict[str, Any]:
        """
        Activates a previously created application charge using the specified ID and returns a success status upon completion.

        Args:
            api_version (string): api_version
            application_charge_id (string): application_charge_id
            application_charge (object): application_charge
                Example:
                ```json
                {
                  "application_charge": {
                    "api_client_id": 755357713,
                    "charge_type": null,
                    "created_at": "2020-01-14T10:41:30-05:00",
                    "decorated_return_url": "http://google.com?charge_id=675931192",
                    "id": 675931192,
                    "name": "iPod Cleaning",
                    "price": "5.00",
                    "return_url": "http://google.com",
                    "status": "accepted",
                    "test": null,
                    "updated_at": "2020-01-14T10:41:30-05:00"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Activate an application charge

        Tags:
            Billing, ApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if application_charge_id is None:
            raise ValueError("Missing required parameter 'application_charge_id'")
        request_body = {
            'application_charge': application_charge,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/application_charges/{application_charge_id}/activate.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_all_application_credits(self, api_version, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of application credits issued to merchants through the Shopify API, allowing optional field filtering via query parameters.

        Args:
            api_version (string): api_version
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve all application credits

        Tags:
            Billing, ApplicationCredit
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/application_credits.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_an_application_credit(self, api_version, application_credit=None) -> dict[str, Any]:
        """
        Issues application credits to merchants, which can be used towards future app purchases in Shopify, using the POST method at "/admin/api/{api_version}/application_credits.json".

        Args:
            api_version (string): api_version
            application_credit (object): application_credit
                Example:
                ```json
                {
                  "application_credit": {
                    "amount": 5,
                    "description": "application credit for refund"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new credit / Create a test application credit that will not issue a credit to the merchant

        Tags:
            Billing, ApplicationCredit
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'application_credit': application_credit,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/application_credits.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_application_credit(self, api_version, application_credit_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific application credit from Shopify's admin API, including optional field filtering parameters.

        Args:
            api_version (string): api_version
            application_credit_id (string): application_credit_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a single application credit

        Tags:
            Billing, ApplicationCredit
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if application_credit_id is None:
            raise ValueError("Missing required parameter 'application_credit_id'")
        url = f"{self.base_url}/admin/api/{api_version}/application_credits/{application_credit_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_recurring_application_charges(self, api_version, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of recurring application charges with optional filtering by ID and field selection.

        Args:
            api_version (string): api_version
            since_id (string): Restrict results to after the specified ID.
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve all recurring charges since a specified ID / Retrieve all recurring application charges

        Tags:
            Billing, RecurringApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_arecurring_application_charge(self, api_version, recurring_application_charge=None) -> dict[str, Any]:
        """
        Creates a new recurring application charge using the API, handling the setup and management of periodic billing.

        Args:
            api_version (string): api_version
            recurring_application_charge (object): recurring_application_charge
                Example:
                ```json
                {
                  "recurring_application_charge": {
                    "capped_amount": 100,
                    "name": "Super Duper Plan",
                    "price": 10,
                    "return_url": "http://super-duper.shopifyapps.com",
                    "terms": "$1 for 1000 emails"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a recurring application charge / Create a recurring test charge that will not cause a credit card to be charged / Create a new charge with a trial period. The trial period will go into effect at the time the recurring charge is activated. / Create a new charge with terms and a capped amount

        Tags:
            Billing, RecurringApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'recurring_application_charge': recurring_application_charge,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_charge(self, api_version, recurring_application_charge_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details for a specific recurring application charge by ID using the "GET" method, optionally including additional fields specified in the query parameters.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a single charge

        Tags:
            Billing, RecurringApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancels_arecurring_application_charge(self, api_version, recurring_application_charge_id) -> Any:
        """
        Cancels an existing recurring application charge for a Shopify store.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id

        Returns:
            Any: Cancel the current recurring charge for a shop

        Tags:
            Billing, RecurringApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def activates_arecurring_application_charge(self, api_version, recurring_application_charge_id, recurring_application_charge=None) -> dict[str, Any]:
        """
        Activates a recurring application charge using the API and returns a status message in response.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id
            recurring_application_charge (object): recurring_application_charge
                Example:
                ```json
                {
                  "recurring_application_charge": {
                    "activated_on": null,
                    "api_client_id": 755357713,
                    "billing_on": "2020-01-14",
                    "cancelled_on": null,
                    "created_at": "2020-01-14T10:26:56-05:00",
                    "decorated_return_url": "http://yourapp.com?charge_id=455696195",
                    "id": 455696195,
                    "name": "Super Mega Plan",
                    "price": "15.00",
                    "return_url": "http://yourapp.com",
                    "status": "accepted",
                    "test": null,
                    "trial_days": 0,
                    "trial_ends_on": null,
                    "updated_at": "2020-01-13T19:00:00-05:00"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Activate a recurring application charge

        Tags:
            Billing, RecurringApplicationCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        request_body = {
            'recurring_application_charge': recurring_application_charge,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/activate.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_usage_charges(self, api_version, recurring_application_charge_id, fields=None) -> dict[str, Any]:
        """
        Retrieves usage charges for a specific recurring application charge via the Shopify Admin API, filtering results based on specified fields.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve all usage charges

        Tags:
            Billing, UsageCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_ausage_charge(self, api_version, recurring_application_charge_id, usage_charge=None) -> dict[str, Any]:
        """
        Creates a usage-based charge on a recurring billing subscription and returns the charge details upon success.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id
            usage_charge (object): usage_charge
                Example:
                ```json
                {
                  "usage_charge": {
                    "description": "Super Mega Plan 1000 emails",
                    "price": 1
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new usage charge

        Tags:
            Billing, UsageCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        request_body = {
            'usage_charge': usage_charge,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_charge1(self, api_version, recurring_application_charge_id, usage_charge_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific usage charge associated with a recurring application charge for tracking and billing purposes.

        Args:
            api_version (string): api_version
            recurring_application_charge_id (string): recurring_application_charge_id
            usage_charge_id (string): usage_charge_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a single charge

        Tags:
            Billing, UsageCharge
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if recurring_application_charge_id is None:
            raise ValueError("Missing required parameter 'recurring_application_charge_id'")
        if usage_charge_id is None:
            raise ValueError("Missing required parameter 'usage_charge_id'")
        url = f"{self.base_url}/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges/{usage_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_addresses_for_acustomer(self, api_version, customer_id) -> dict[str, Any]:
        """
        Retrieves a list of customer addresses associated with a specific customer ID.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id

        Returns:
            dict[str, Any]: Retrieve all of a customer’s addresses / Retrieve a limited number of addresses for a customer

        Tags:
            Customers, Customer Address
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/addresses.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_address_for_acustomer(self, api_version, customer_id, address=None) -> dict[str, Any]:
        """
        Creates a new address for a specified customer using the POST method.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            address (object): address
                Example:
                ```json
                {
                  "address": {
                    "address1": "1 Rue des Carrieres",
                    "address2": "Suite 1234",
                    "city": "Montreal",
                    "company": "Fancy Co.",
                    "country": "Canada",
                    "country_code": "CA",
                    "country_name": "Canada",
                    "first_name": "Samuel",
                    "last_name": "de Champlain",
                    "name": "Samuel de Champlain",
                    "phone": "819-555-5555",
                    "province": "Quebec",
                    "province_code": "QC",
                    "zip": "G1R 4P5"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new address for a customer

        Tags:
            Customers, Customer Address
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        request_body = {
            'address': address,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/addresses.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_details_for_asingle_customer_address(self, api_version, customer_id, address_id) -> dict[str, Any]:
        """
        Retrieves a specific customer address using the provided customer ID and address ID, returning details about the address.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            address_id (string): address_id

        Returns:
            dict[str, Any]: Retrieve a single customer address

        Tags:
            Customers, Customer Address
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        if address_id is None:
            raise ValueError("Missing required parameter 'address_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_customer_address(self, api_version, customer_id, address_id, address=None) -> dict[str, Any]:
        """
        Updates an existing customer address using the HTTP PUT method at a specified API path, returning a successful status message upon completion.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            address_id (string): address_id
            address (object): address
                Example:
                ```json
                {
                  "address": {
                    "id": 207119551,
                    "zip": "90210"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the postal code of a customer address

        Tags:
            Customers, Customer Address
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        if address_id is None:
            raise ValueError("Missing required parameter 'address_id'")
        request_body = {
            'address': address,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_an_address_from_acustomer_saddress_list(self, api_version, customer_id, address_id) -> dict[str, Any]:
        """
        Deletes a customer's address specified by the customer ID and address ID using a DELETE request.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            address_id (string): address_id

        Returns:
            dict[str, Any]: Remove a customer address

        Tags:
            Customers, Customer Address
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        if address_id is None:
            raise ValueError("Missing required parameter 'address_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_customers(self, api_version, ids=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, limit=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of customers with optional filtering by IDs, creation/update timestamps, and field selection.

        Args:
            api_version (string): api_version
            ids (string): Restrict results to customers specified by a comma-separated list of IDs.
            since_id (string): Restrict results to those after the specified ID.
            created_at_min (string): Show customers created after a specified date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show customers created before a specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show customers last updated after a specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show customers last updated before a specified date. (format: 2014-04-25T16:15:47-04:00)
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all customers for a shop / Retrieve a list of specific customers / Retrieve all customers after a specified ID / Retrieve all customers changed after a certain date

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/customers.json"
        query_params = {k: v for k, v in [('ids', ids), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acustomer(self, api_version, customer=None) -> dict[str, Any]:
        """
        Creates a new customer resource using the API and returns a status message upon successful creation.

        Args:
            api_version (string): api_version
            customer (object): customer
                Example:
                ```json
                {
                  "customer": {
                    "addresses": [
                      {
                        "address1": "123 Oak St",
                        "city": "Ottawa",
                        "country": "CA",
                        "first_name": "Mother",
                        "last_name": "Lastnameson",
                        "phone": "555-1212",
                        "province": "ON",
                        "zip": "123 ABC"
                      }
                    ],
                    "email": "steve.lastnameson@example.com",
                    "first_name": "Steve",
                    "last_name": "Lastnameson",
                    "phone": "+15142546011",
                    "verified_email": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a customer with <code>send_email_invite</code> / Create a customer with a metafield / Create a customer with <code>password</code> and <code>password_confirmation</code> and skip sending the welcome email / Create a new customer record

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'customer': customer,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customers.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def searches_for_customers_that_match_asupplied_query(self, api_version, order=None, query=None, limit=None, fields=None) -> dict[str, Any]:
        """
        Searches customer records using specified filters, sorting options, and field selections, returning matching results in a structured format.

        Args:
            api_version (string): api_version
            order (string): Set the field and direction by which to order results.(default: last\_order\_date DESC)
            query (string): Text to search for in the shop\'s customer data.
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all customers with an address in the United States and the name "Bob"

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/search.json"
        query_params = {k: v for k, v in [('order', order), ('query', query), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_customer(self, api_version, customer_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a customer's details in JSON format using the specified API version and customer ID, with optional fields specified via the query parameters.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single customer by their ID

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_acustomer(self, api_version, customer_id, customer=None) -> dict[str, Any]:
        """
        Updates or replaces the customer resource at the specified ID and returns the updated entity.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            customer (object): customer
                Example:
                ```json
                {
                  "customer": {
                    "id": 207119551,
                    "metafields": [
                      {
                        "key": "new",
                        "namespace": "global",
                        "value": "newvalue",
                        "value_type": "string"
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update details for a customer / Update a customer's marketing opt-in state / Update a customer's tags / Add metafield to an existing customer

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        request_body = {
            'customer': customer,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_acustomer(self, api_version, customer_id) -> Any:
        """
        Deletes a customer's data permanently using the "DELETE" method at the specified API path, immediately canceling any active subscriptions and preventing further operations.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id

        Returns:
            Any: API response data.

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def sends_an_account_invite_to_acustomer(self, api_version, customer_id, customer_invite=None) -> dict[str, Any]:
        """
        Sends an invitation to a specified customer using the "POST" method.

        Args:
            api_version (string): api_version
            customer_id (string): customer_id
            customer_invite (object): customer_invite
                Example:
                ```json
                {
                  "customer_invite": {
                    "bcc": [
                      "noaccesssteve@jobs.com"
                    ],
                    "custom_message": "My awesome new store",
                    "from": "noaccesssteve@jobs.com",
                    "subject": "Welcome to my new shop",
                    "to": "new_test_email@shopify.com"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Send the default invite / Send a customized invite

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        request_body = {
            'customer_invite': customer_invite,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/send_invite.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_customers(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of customers using the specified API version.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a count of all customers

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_all_orders_belonging_to_acustomer(self, api_version, customer_id) -> dict[str, Any]:
        """
        Retrieves a list of orders for a specified customer using the "GET" method via the API endpoint "/admin/api/{api_version}/customers/{customer_id}/orders.json".

        Args:
            api_version (string): api_version
            customer_id (string): customer_id

        Returns:
            dict[str, Any]: Retrieve all orders from a customer

        Tags:
            Customers, Customer
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_id is None:
            raise ValueError("Missing required parameter 'customer_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customers/{customer_id}/orders.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_customer_saved_searches(self, api_version, limit=None, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of customer-saved searches in JSON format, allowing for optional filtering by limit, since_id, and specific fields.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all customer saved searches for a shop / Retrieve all customer saved searches for a shop after a specified ID

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acustomer_saved_search(self, api_version, customer_saved_search=None) -> dict[str, Any]:
        """
        Creates a new customer saved search entry via the specified API version and returns an empty response on success or validation errors.

        Args:
            api_version (string): api_version
            customer_saved_search (object): customer_saved_search
                Example:
                ```json
                {
                  "customer_saved_search": {
                    "body": "foobar"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a customer saved search with multiple terms / Create a customer saved search

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'customer_saved_search': customer_saved_search,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_all_customer_saved_searches(self, api_version, since_id=None) -> dict[str, Any]:
        """
        Retrieves a count of customer saved searches with optional filtering by creation time using the "since_id" parameter.

        Args:
            api_version (string): api_version
            since_id (string): Restrict results to after the specified ID

        Returns:
            dict[str, Any]: Retrieve a count of all customer saved searches after a specified ID / Retrieve a count all customer saved searches

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches/count.json"
        query_params = {k: v for k, v in [('since_id', since_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_customer_saved_search(self, api_version, customer_saved_search_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a customer saved search by ID using the Shopify API, optionally specifying fields to include in the response.

        Args:
            api_version (string): api_version
            customer_saved_search_id (string): customer_saved_search_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Get one customer saved search by ID

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_saved_search_id is None:
            raise ValueError("Missing required parameter 'customer_saved_search_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_acustomer_saved_search(self, api_version, customer_saved_search_id, customer_saved_search=None) -> dict[str, Any]:
        """
        Updates a customer's saved search identified by the `{customer_saved_search_id}` at the specified `{api_version}`, allowing modifications to its details.

        Args:
            api_version (string): api_version
            customer_saved_search_id (string): customer_saved_search_id
            customer_saved_search (object): customer_saved_search
                Example:
                ```json
                {
                  "customer_saved_search": {
                    "id": 789629109,
                    "name": "This Name Has Been Changed"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an existing customer saved search

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_saved_search_id is None:
            raise ValueError("Missing required parameter 'customer_saved_search_id'")
        request_body = {
            'customer_saved_search': customer_saved_search,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_acustomer_saved_search(self, api_version, customer_saved_search_id) -> dict[str, Any]:
        """
        Deletes a specified customer saved search using its unique identifier and returns a success status upon completion.

        Args:
            api_version (string): api_version
            customer_saved_search_id (string): customer_saved_search_id

        Returns:
            dict[str, Any]: Delete an existing Customer Saved Search

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_saved_search_id is None:
            raise ValueError("Missing required parameter 'customer_saved_search_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_all_customers_returned_by_acustomer_saved_search(self, api_version, customer_saved_search_id, order=None, limit=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of customers associated with a specific customer saved search, allowing for optional filtering by order, limited results, and customizable fields.

        Args:
            api_version (string): api_version
            customer_saved_search_id (string): customer_saved_search_id
            order (string): Set the field and direction by which to order results.(default: last\_order\_date DESC)
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve customers who match the query for the specified customer saved search

        Tags:
            Customers, CustomerSavedSearch
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if customer_saved_search_id is None:
            raise ValueError("Missing required parameter 'customer_saved_search_id'")
        url = f"{self.base_url}/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}/customers.json"
        query_params = {k: v for k, v in [('order', order), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_discount_codes(self, api_version, price_rule_id) -> dict[str, Any]:
        """
        Retrieves discount codes associated with a specific price rule using the specified API version.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id

        Returns:
            dict[str, Any]: Retrieve a list of all discount codes

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_adiscount_code(self, api_version, price_rule_id, discount_code=None) -> dict[str, Any]:
        """
        Creates a discount code associated with a specific price rule in Shopify and returns the created resource.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            discount_code (object): discount_code
                Example:
                ```json
                {
                  "discount_code": {
                    "code": "SUMMERSALE10OFF"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a discount code

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        request_body = {
            'discount_code': discount_code,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_discount_code(self, api_version, price_rule_id, discount_code_id) -> dict[str, Any]:
        """
        Retrieves information about a specific discount code for a given price rule using the API.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            discount_code_id (string): discount_code_id

        Returns:
            dict[str, Any]: Retrieve a single discount code

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        if discount_code_id is None:
            raise ValueError("Missing required parameter 'discount_code_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_discount_code(self, api_version, price_rule_id, discount_code_id, discount_code=None) -> dict[str, Any]:
        """
        Updates an existing discount code associated with a specified price rule in Shopify, allowing merchants to modify the discount code details within the defined price rule.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            discount_code_id (string): discount_code_id
            discount_code (object): discount_code
                Example:
                ```json
                {
                  "discount_code": {
                    "code": "WINTERSALE20OFF",
                    "created_at": "2020-01-14T10:35:09-05:00",
                    "id": 507328175,
                    "updated_at": "2020-01-14T10:35:09-05:00",
                    "usage_count": 0
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the code for a discount

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        if discount_code_id is None:
            raise ValueError("Missing required parameter 'discount_code_id'")
        request_body = {
            'discount_code': discount_code,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_adiscount_code(self, api_version, price_rule_id, discount_code_id) -> Any:
        """
        Deletes a specific discount code associated with a price rule.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            discount_code_id (string): discount_code_id

        Returns:
            Any: Delete a discount code

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        if discount_code_id is None:
            raise ValueError("Missing required parameter 'discount_code_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_the_location_of_adiscount_code(self, api_version) -> Any:
        """
        Retrieves discount code information using the "GET" method at the "/admin/api/{api_version}/discount_codes/lookup.json" endpoint.

        Args:
            api_version (string): api_version

        Returns:
            Any: API response data.

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/discount_codes/lookup.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_adiscount_code_creation_job(self, api_version, price_rule_id, discount_codes=None) -> dict[str, Any]:
        """
        Applies batch operations to a specific price rule using the POST method, allowing for efficient management of price rules in bulk.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            discount_codes (array): discount_codes
                Example:
                ```json
                {
                  "discount_codes": [
                    {
                      "code": "SUMMER1"
                    },
                    {
                      "code": "SUMMER2"
                    },
                    {
                      "code": "SUMMER3"
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Create a discount code creation job

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        request_body = {
            'discount_codes': discount_codes,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/batch.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_adiscount_code_creation_job(self, api_version, price_rule_id, batch_id) -> dict[str, Any]:
        """
        Retrieves a batch of price rule details for a specific batch and price rule ID using the specified API version.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            batch_id (string): batch_id

        Returns:
            dict[str, Any]: Retrieve a discount code creation job

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/batch/{batch_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_discount_codes_for_adiscount_code_creation_job(self, api_version, price_rule_id, batch_id) -> dict[str, Any]:
        """
        Retrieves a list of discount codes associated with a specific batch under a price rule using the "GET" method.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            batch_id (string): batch_id

        Returns:
            dict[str, Any]: Retrieve a list of discount codes for a discount code creation job

        Tags:
            Discounts, DiscountCode
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        if batch_id is None:
            raise ValueError("Missing required parameter 'batch_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_price_rules(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, starts_at_min=None, starts_at_max=None, ends_at_min=None, ends_at_max=None, times_used=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of price rules with optional filters for time ranges, usage, and creation/modification dates.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Show price rules created after date (format 2017-03-25T16:15:47-04:00).
            created_at_max (string): Show price rules created before date (format 2017-03-25T16:15:47-04:00).
            updated_at_min (string): Show price rules last updated after date (format 2017-03-25T16:15:47-04:00).
            updated_at_max (string): Show price rules last updated before date (format 2017-03-25T16:15:47-04:00).
            starts_at_min (string): Show price rules starting after date (format 2017-03-25T16:15:47-04:00).
            starts_at_max (string): Show price rules starting before date (format 2017-03-25T16:15:47-04:00).
            ends_at_min (string): Show price rules ending after date (format 2017-03-25T16:15:47-04:00).
            ends_at_max (string): Show price rules ending before date (format 2017-03-25T16:15:47-04:00).
            times_used (string): Show price rules with times used.

        Returns:
            dict[str, Any]: Retrieve all price rules

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('starts_at_min', starts_at_min), ('starts_at_max', starts_at_max), ('ends_at_min', ends_at_min), ('ends_at_max', ends_at_max), ('times_used', times_used)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_aprice_rule(self, api_version, price_rule=None) -> dict[str, Any]:
        """
        Creates a new price rule using the POST method, enabling the management of pricing configurations for specific products or customer groups at the specified API endpoint.

        Args:
            api_version (string): api_version
            price_rule (object): price_rule
                Example:
                ```json
                {
                  "price_rule": {
                    "allocation_method": "across",
                    "customer_selection": "all",
                    "starts_at": "2017-01-19T17:59:10Z",
                    "target_selection": "all",
                    "target_type": "line_item",
                    "title": "SUMMERSALE10OFF",
                    "value": "-10.0",
                    "value_type": "fixed_amount"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a price rule that gives the buyer 15% off a specific collection / Create a price rule that gives a select group of customers $5 off their order / Create a price rule that gives the buyer free shipping on orders
                over $50.00 that can be used up to 20 times / Create a Buy X Get Y price rule that gives one free ipod touch if customer buys 2 ipods  / Create a price rule that gives the buyer $10.00 off an order

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'price_rule': price_rule,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/price_rules.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_price_rule(self, api_version, price_rule_id) -> dict[str, Any]:
        """
        Retrieves a specific price rule's details including entitlements, prerequisites, and discount conditions from the store's pricing system.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id

        Returns:
            dict[str, Any]: Retrieve a single price rule by its ID

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_aprice_rule(self, api_version, price_rule_id, price_rule=None) -> dict[str, Any]:
        """
        Updates a price rule configuration for a specific ID using the Shopify Admin REST API.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id
            price_rule (object): price_rule
                Example:
                ```json
                {
                  "price_rule": {
                    "id": 507328175,
                    "title": "WINTER SALE"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the title of a price rule

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        request_body = {
            'price_rule': price_rule,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_pricerule(self, api_version, price_rule_id) -> Any:
        """
        Deletes a specified price rule with the provided ID using the "DELETE" method, returning a successful response with a 204 status code.

        Args:
            api_version (string): api_version
            price_rule_id (string): price_rule_id

        Returns:
            Any: Delete a price rule

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if price_rule_id is None:
            raise ValueError("Missing required parameter 'price_rule_id'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_all_price_rules(self, api_version) -> dict[str, Any]:
        """
        Retrieves the total count of price rules configured in the system.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a count of all price rules

        Tags:
            Discounts, PriceRule
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/price_rules/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_events(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, filter=None, verb=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a filtered list of administrative events with parameters for date ranges, pagination, and field selection.

        Args:
            api_version (string): api_version
            limit (string): The number of results to show.(default: 50)(maximum: 250)
            since_id (string): Show only results after the specified ID.
            created_at_min (string): Show events created at or after this date and time. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show events created at or before this date and time. (format: 2014-04-25T16:15:47-04:00)
            filter (string): Show events specified in this filter.
            verb (string): Show events of a certain type.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a list of events related to products that were deleted / Retrieve a list of all events from a specific order / Retrieve all events after the specified ID / Retrieve an event after a specific ID using <code>since_id</code> / Retrieve a list of all events related to products and orders / Retrieve all events from a specific product / Retrieve a list of events that occured at the specified time / Retrieve a list of all events for a shop

        Tags:
            Events, Event
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/events.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('filter', filter), ('verb', verb), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_event(self, api_version, event_id, fields=None) -> dict[str, Any]:
        """
        Retrieves event details in JSON format from the admin API for a specified event ID and API version with optional field filtering.

        Args:
            api_version (string): api_version
            event_id (string): event_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieves a single event by its ID

        Tags:
            Events, Event
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/admin/api/{api_version}/events/{event_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_events(self, api_version, created_at_min=None, created_at_max=None) -> dict[str, Any]:
        """
        Retrieves the count of events using the "GET" method, allowing filtering by creation date range via "created_at_min" and "created_at_max" query parameters.

        Args:
            api_version (string): api_version
            created_at_min (string): Count only events created at or after this date and time. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Count only events created at or before this date and time. (format: 2014-04-25T16:15:47-04:00)

        Returns:
            dict[str, Any]: Count all events / Count of the number of events since a particular time

        Tags:
            Events, Event
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/events/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_webhooks(self, api_version, address=None, created_at_max=None, created_at_min=None, fields=None, limit=None, since_id=None, topic=None, updated_at_min=None, updated_at_max=None) -> dict[str, Any]:
        """
        Retrieves a list of webhooks in JSON format, allowing filtering by address, creation and update times, specific fields, limit, and topic, using the "GET" method.

        Args:
            api_version (string): api_version
            address (string): Retrieve webhook subscriptions that send the POST request to this URI.
            created_at_max (string): Retrieve webhook subscriptions that were created before a given date and time (format: 2014-04-25T16:15:47-04:00).
            created_at_min (string): Retrieve webhook subscriptions that were created after a given date and time (format: 2014-04-25T16:15:47-04:00).
            fields (string): Comma-separated list of the properties you want returned for each item in the result list. Use this parameter to restrict the returned list of items to only those properties you specify.
            limit (string): Maximum number of webhook subscriptions that should be returned. Setting this parameter outside the maximum range will return an error.(default: 50)(maximum: 250)
            since_id (string): Restrict the returned list to webhook subscriptions whose id is greater than the specified since\_id.
            topic (string): Show webhook subscriptions with a given topic. For a list of valid values, refer to the [`topic` property](#topic-property-).>
            updated_at_min (string): Retrieve webhooks that were updated before a given date and time (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Retrieve webhooks that were updated after a given date and time (format: 2014-04-25T16:15:47-04:00).

        Returns:
            dict[str, Any]: Retrieve a list of all webhook subscriptions for your shop / Retrieve a list of all webhook subscriptions for your shop after a specified <code>id</code>

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/webhooks.json"
        query_params = {k: v for k, v in [('address', address), ('created_at_max', created_at_max), ('created_at_min', created_at_min), ('fields', fields), ('limit', limit), ('since_id', since_id), ('topic', topic), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_webhook(self, api_version, webhook=None) -> dict[str, Any]:
        """
        Creates a new webhook subscription for event notifications from the admin API.

        Args:
            api_version (string): api_version
            webhook (object): webhook
                Example:
                ```json
                {
                  "webhook": {
                    "address": "https://whatever.hostname.com/",
                    "format": "json",
                    "topic": "orders/create"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Subscribe to order creation webhooks

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'webhook': webhook,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/webhooks.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_acount_of_all_webhooks(self, api_version, address=None, topic=None) -> dict[str, Any]:
        """
        Retrieves the count of webhooks for a specified address and topic using the GET method.

        Args:
            api_version (string): api_version
            address (string): Retrieve webhook subscriptions that send the POST request to this URI.
            topic (string): Show webhook subscriptions with a given topic. For a list of valid values, refer to the [`topic` property](#topic-property-).>

        Returns:
            dict[str, Any]: Count all of the webhook subscriptions for the topic <code>orders/create</code> / Count all of the webhook subscriptions for your shop

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/webhooks/count.json"
        query_params = {k: v for k, v in [('address', address), ('topic', topic)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_webhook(self, api_version, webhook_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific webhook's details in JSON format using the specified API version and webhook ID from the admin API.

        Args:
            api_version (string): api_version
            webhook_id (string): webhook_id
            fields (string): Comma-separated list of the properties you want returned for each item in the result list. Use this parameter to restrict the returned list of items to only those properties you specify.

        Returns:
            dict[str, Any]: Retrieve a single webhook by its <code>id</code>

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        url = f"{self.base_url}/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_webhook(self, api_version, webhook_id, webhook=None) -> dict[str, Any]:
        """
        Updates the specified webhook's configuration using the provided data and returns a success status upon completion.

        Args:
            api_version (string): api_version
            webhook_id (string): webhook_id
            webhook (object): webhook
                Example:
                ```json
                {
                  "webhook": {
                    "address": "https://somewhere-else.com/",
                    "id": 4759306
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a webhook subscription so that it POSTs to a different address

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        request_body = {
            'webhook': webhook,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_webhook(self, api_version, webhook_id) -> dict[str, Any]:
        """
        Deletes a webhook identified by its ID using the DELETE method, effectively removing the webhook endpoint.

        Args:
            api_version (string): api_version
            webhook_id (string): webhook_id

        Returns:
            dict[str, Any]: Delete an existing webhook from a shop

        Tags:
            Events, Webhook
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if webhook_id is None:
            raise ValueError("Missing required parameter 'webhook_id'")
        url = f"{self.base_url}/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_inventory_items(self, api_version, ids=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of inventory items with support for filtering by IDs and limiting results.

        Args:
            api_version (string): api_version
            ids (string): Show only inventory items specified by a comma-separated list of IDs.(maximum: 100)
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)

        Returns:
            dict[str, Any]: Retrieve a list of inventory items

        Tags:
            Inventory, InventoryItem
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/inventory_items.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_inventory_item_by_id(self, api_version, inventory_item_id) -> dict[str, Any]:
        """
        Retrieves inventory item details using the API at the specified version, returning information for the specified inventory item ID.

        Args:
            api_version (string): api_version
            inventory_item_id (string): inventory_item_id

        Returns:
            dict[str, Any]: Retrieve an inventory item by ID

        Tags:
            Inventory, InventoryItem
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if inventory_item_id is None:
            raise ValueError("Missing required parameter 'inventory_item_id'")
        url = f"{self.base_url}/admin/api/{api_version}/inventory_items/{inventory_item_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_inventory_item(self, api_version, inventory_item_id, inventory_item=None) -> dict[str, Any]:
        """
        Updates an inventory item with the specified ID by modifying its characteristics or details using the PUT method at the "/admin/api/{api_version}/inventory_items/{inventory_item_id}.json" endpoint.

        Args:
            api_version (string): api_version
            inventory_item_id (string): inventory_item_id
            inventory_item (object): inventory_item
                Example:
                ```json
                {
                  "inventory_item": {
                    "cost": "25.00",
                    "id": 808950810
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an inventory item's SKU / Update an inventory item's unit cost

        Tags:
            Inventory, InventoryItem
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if inventory_item_id is None:
            raise ValueError("Missing required parameter 'inventory_item_id'")
        request_body = {
            'inventory_item': inventory_item,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/inventory_items/{inventory_item_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_inventory_levels(self, api_version, inventory_item_ids=None, location_ids=None, limit=None, updated_at_min=None) -> dict[str, Any]:
        """
        Retrieves inventory level information for specified inventory items and locations using the "GET" method, allowing for filtering by item IDs, location IDs, and update time, and returns the data in JSON format.

        Args:
            api_version (string): api_version
            inventory_item_ids (string): A comma-separated list of inventory item IDs.(maximum: 50)
            location_ids (string): A comma-separated list of location IDs. To find the ID of a location, use the [Location resource](/api/reference/location).(maximum: 50)
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            updated_at_min (string): Show inventory levels updated at or after date (format: 2019-03-19T01:21:44-04:00).

        Returns:
            dict[str, Any]: Retrieve inventory levels for the specified inventory items and locations / Retrieve inventory levels at a single location / Retrieve inventory levels for a single inventory item

        Tags:
            Inventory, InventoryLevel
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/inventory_levels.json"
        query_params = {k: v for k, v in [('inventory_item_ids', inventory_item_ids), ('location_ids', location_ids), ('limit', limit), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_inventory_level_from_alocation(self, api_version) -> Any:
        """
        Deletes inventory levels from the system and returns a success status without content.

        Args:
            api_version (string): api_version

        Returns:
            Any: Delete an inventory level

        Tags:
            Inventory, InventoryLevel
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/inventory_levels.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def adjusts_the_inventory_level_of_an_inventory_item_at_alocation(self, api_version, available_adjustment=None, inventory_item_id=None, location_id=None) -> dict[str, Any]:
        """
        Adjusts the inventory level for a specific item at a location using a relative quantity change.

        Args:
            api_version (string): api_version
            available_adjustment (number): available_adjustment Example: '5'.
            inventory_item_id (number): inventory_item_id Example: '808950810'.
            location_id (number): location_id
                Example:
                ```json
                {
                  "available_adjustment": 5,
                  "inventory_item_id": 808950810,
                  "location_id": 905684977
                }
                ```

        Returns:
            dict[str, Any]: Adjust the available quantity of an inventory item by 5 at a single location

        Tags:
            Inventory, InventoryLevel
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'available_adjustment': available_adjustment,
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/inventory_levels/adjust.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def connects_an_inventory_item_to_alocation(self, api_version, inventory_item_id=None, location_id=None) -> dict[str, Any]:
        """
        Connects inventory levels to a specified location or system and returns a success status upon creation.

        Args:
            api_version (string): api_version
            inventory_item_id (number): inventory_item_id Example: '457924702'.
            location_id (number): location_id
                Example:
                ```json
                {
                  "inventory_item_id": 457924702,
                  "location_id": 192722535
                }
                ```

        Returns:
            dict[str, Any]: Connect an inventory item to a location

        Tags:
            Inventory, InventoryLevel
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/inventory_levels/connect.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sets_the_inventory_level_for_an_inventory_item_at_alocation(self, api_version, available=None, inventory_item_id=None, location_id=None) -> dict[str, Any]:
        """
        Updates inventory levels for specific items and returns a success status.

        Args:
            api_version (string): api_version
            available (number): available Example: '42'.
            inventory_item_id (number): inventory_item_id Example: '808950810'.
            location_id (number): location_id
                Example:
                ```json
                {
                  "available": 42,
                  "inventory_item_id": 808950810,
                  "location_id": 905684977
                }
                ```

        Returns:
            dict[str, Any]: Set the available inventory at a location

        Tags:
            Inventory, InventoryLevel
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'available': available,
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/inventory_levels/set.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_locations(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of locations accessible through the admin API and returns them in JSON format.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of all locations

        Tags:
            Inventory, Location
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/locations.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_location_by_its_id(self, api_version, location_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific location by its ID from the admin API.

        Args:
            api_version (string): api_version
            location_id (string): location_id

        Returns:
            dict[str, Any]: Retrieve a single location

        Tags:
            Inventory, Location
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if location_id is None:
            raise ValueError("Missing required parameter 'location_id'")
        url = f"{self.base_url}/admin/api/{api_version}/locations/{location_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_locations(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of locations in JSON format using the specified API version.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Count all store locations

        Tags:
            Inventory, Location
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/locations/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_inventory_levels_for_alocation(self, api_version, location_id) -> dict[str, Any]:
        """
        Retrieves the current inventory levels for products at a specified store location using the GET method and returns this information in JSON format.

        Args:
            api_version (string): api_version
            location_id (string): location_id

        Returns:
            dict[str, Any]: Retrieve a list of all inventory for a location by its ID

        Tags:
            Inventory, Location
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if location_id is None:
            raise ValueError("Missing required parameter 'location_id'")
        url = f"{self.base_url}/admin/api/{api_version}/locations/{location_id}/inventory_levels.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_marketing_events(self, api_version, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of marketing events using the specified limit and offset parameters.

        Args:
            api_version (string): api_version
            limit (string): The amount of results to return.(default: 50)(maximum: 250)
            offset (string): The number of marketing events to skip.

        Returns:
            dict[str, Any]: Retrieve all marketing events

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events.json"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_amarketing_event(self, api_version, marketing_event=None) -> dict[str, Any]:
        """
        Creates a marketing event using the specified API version and returns a status message upon successful creation.

        Args:
            api_version (string): api_version
            marketing_event (object): marketing_event
                Example:
                ```json
                {
                  "marketing_event": {
                    "event_type": "ad",
                    "marketing_channel": "social",
                    "paid": true,
                    "referring_domain": "facebook.com",
                    "started_at": "2020-12-15",
                    "utm_campaign": "Christmas2020",
                    "utm_medium": "cpc",
                    "utm_source": "facebook"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a marketing event

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'marketing_event': marketing_event,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_all_marketing_events(self, api_version) -> dict[str, Any]:
        """
        Retrieves the total count of marketing events matching specified criteria using filtering parameters.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a count all marketing events

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_marketing_event(self, api_version, marketing_event_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific marketing event by its ID from the Shopify API.

        Args:
            api_version (string): api_version
            marketing_event_id (string): marketing_event_id

        Returns:
            dict[str, Any]: Retrieve a single marketing event by its ID

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if marketing_event_id is None:
            raise ValueError("Missing required parameter 'marketing_event_id'")
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_amarketing_event(self, api_version, marketing_event_id, marketing_event=None) -> dict[str, Any]:
        """
        Updates a marketing event's details via the specified marketing_event_id and returns a success status upon completion.

        Args:
            api_version (string): api_version
            marketing_event_id (string): marketing_event_id
            marketing_event (object): marketing_event
                Example:
                ```json
                {
                  "marketing_event": {
                    "budget": "11.1",
                    "budget_type": "daily",
                    "currency": "CAD",
                    "ended_at": "2020-02-03T00:00 +00:00",
                    "event_type": "ad",
                    "id": 998730532,
                    "referring_domain": "instagram.com",
                    "remote_id": "1000:2000",
                    "scheduled_to_end_at": "2020-02-04T00:00 +00:00",
                    "started_at": "2020-02-02T00:00 +00:00",
                    "utm_campaign": "other",
                    "utm_medium": "other",
                    "utm_source": "other"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a marketing event. Can modify only timestamps, remote_id, and budget/currency.

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if marketing_event_id is None:
            raise ValueError("Missing required parameter 'marketing_event_id'")
        request_body = {
            'marketing_event': marketing_event,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_amarketing_event(self, api_version, marketing_event_id) -> dict[str, Any]:
        """
        Deletes a specific marketing event using its unique identifier and returns a success status upon removal.

        Args:
            api_version (string): api_version
            marketing_event_id (string): marketing_event_id

        Returns:
            dict[str, Any]: Delete a marketing event

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if marketing_event_id is None:
            raise ValueError("Missing required parameter 'marketing_event_id'")
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_marketing_engagements_on_amarketing_event(self, api_version, marketing_event_id, engagements=None) -> dict[str, Any]:
        """
        Creates an engagement record for a specified marketing event using the POST method.

        Args:
            api_version (string): api_version
            marketing_event_id (string): marketing_event_id
            engagements (array): engagements
                Example:
                ```json
                {
                  "engagements": [
                    {
                      "ad_spend": 10,
                      "clicks_count": 0,
                      "favorites_count": 0,
                      "is_cumulative": true,
                      "occurred_on": "2020-01-15",
                      "views_count": 0
                    },
                    {
                      "clicks_count": 50,
                      "is_cumulative": true,
                      "occurred_on": "2020-01-16",
                      "views_count": 100
                    },
                    {
                      "clicks_count": 100,
                      "is_cumulative": true,
                      "occurred_on": "2020-01-17",
                      "views_count": 200
                    }
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Add engagements to a marketing engagement

        Tags:
            Marketingevent, MarketingEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if marketing_event_id is None:
            raise ValueError("Missing required parameter 'marketing_event_id'")
        request_body = {
            'engagements': engagements,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/marketing_events/{marketing_event_id}/engagements.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_metafields_that_belong_to_aresource(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, namespace=None, key=None, value_type=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of metafields across all resources with optional filters like namespace, key, value type, and date ranges.

        Args:
            api_version (string): api_version
            limit (string): Amount of results(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID
            created_at_min (string): Show metafields created after date (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show metafields created before date (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show metafields last updated after date (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show metafields last updated before date (format: 2014-04-25T16:15:47-04:00)
            namespace (string): Show metafields with given namespace
            key (string): Show metafields with given key
            value_type (string): Specifies the metafield value type to filter results (deprecated in favor of 'type' parameter for API versions after 2022-01).
            fields (string): comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Retrieve metafields that belong to a Shop resource / Retrieve a list of metafields that belong to a Product resource / Retrieve metafields after the specified ID that belong to a Shop resource / Retrieve a list of metafields that belong to a Product Image resource

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/metafields.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('namespace', namespace), ('key', key), ('value_type', value_type), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_metafield_for_aresource(self, api_version, metafield=None) -> dict[str, Any]:
        """
        Creates a new metafield entry in Shopify's system for storing custom data associated with various resources.

        Args:
            api_version (string): api_version
            metafield (object): metafield
                Example:
                ```json
                {
                  "metafield": {
                    "key": "warehouse",
                    "namespace": "inventory",
                    "value": 25,
                    "value_type": "integer"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new metafield for a Product resource / Create a new metafield for a Shop resource

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'metafield': metafield,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/metafields.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_aresource_smetafields(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of metafields for a specified resource using the "GET" method at the "/admin/api/{api_version}/metafields/count.json" endpoint.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a count of metafields that belong to a Shop resource / Retrieve a count of metafields that belong to a Product resource

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/metafields/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_metafield_from_aresource_by_its_id(self, api_version, metafield_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific metafield by its ID using the Shopify API, allowing for optional filtering of returned fields.

        Args:
            api_version (string): api_version
            metafield_id (string): metafield_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single metafield by its ID / Retrieve a single metafield by its ID

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if metafield_id is None:
            raise ValueError("Missing required parameter 'metafield_id'")
        url = f"{self.base_url}/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_ametafield(self, api_version, metafield_id, metafield=None) -> dict[str, Any]:
        """
        Updates an existing metafield's data in Shopify via the specified API endpoint.

        Args:
            api_version (string): api_version
            metafield_id (string): metafield_id
            metafield (object): metafield
                Example:
                ```json
                {
                  "metafield": {
                    "id": 721389482,
                    "value": "something new",
                    "value_type": "string"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a metafield. The namespace and key of an existing metafield can't be changed. / Update a metafield. The namespace and key of an existing metafield can't be changed.

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if metafield_id is None:
            raise ValueError("Missing required parameter 'metafield_id'")
        request_body = {
            'metafield': metafield,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_ametafield_by_its_id(self, api_version, metafield_id) -> dict[str, Any]:
        """
        Deletes a metafield by its ID using the Shopify API, removing the specified metafield's data from a store.

        Args:
            api_version (string): api_version
            metafield_id (string): metafield_id

        Returns:
            dict[str, Any]: Delete a metafield by its ID / Delete a metafield by its ID

        Tags:
            Metafield, Metafield1
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if metafield_id is None:
            raise ValueError("Missing required parameter 'metafield_id'")
        url = f"{self.base_url}/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_articles_from_ablog(self, api_version, blog_id, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None, handle=None, tag=None, author=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of articles from a specified blog using the GET method with optional filtering by parameters such as creation date, publication status, author, and tags.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Show articles created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Show articles created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Show articles last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Show articles last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Show articles published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Show articles published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Retrieve results based on their published status.(default: any)
            handle (string): Retrieve an article with a specific handle.
            tag (string): Filter articles with a specific tag.
            author (string): Filter articles by article author.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all articles from a blog after a specified ID / Retrieve a list of articles from a blog

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('handle', handle), ('tag', tag), ('author', author), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_an_article_for_ablog(self, api_version, blog_id, article=None) -> dict[str, Any]:
        """
        Creates a new article in the specified blog using the Blogger API and returns the created article on success.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            article (object): article
                Example:
                ```json
                {
                  "article": {
                    "author": "John Smith",
                    "body_html": "<h1>I like articles</h1>\n<p><strong>Yea</strong>, I like posting them through <span class=\"caps\">REST</span>.</p>",
                    "published": false,
                    "tags": "This Post, Has Been Tagged",
                    "title": "My new Article title"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an article with a metafield / Create an article with an image, which will be downloaded by Shopify / Create an article with HTML markup for a blog / Create an article with a base64 encoded image / Create an unpublished article for a blog

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        request_body = {
            'article': article,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_all_articles_from_ablog(self, api_version, blog_id, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves the count of articles in a specific blog with optional time-based and status filters.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            created_at_min (string): Count articles created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Count articles created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Count articles last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Count articles last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Count articles published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Count articles published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Count articles with a given published status.(default: any)

        Returns:
            dict[str, Any]: Count all a blog's articles

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_article(self, api_version, blog_id, article_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific article from a blog by its ID, returning the requested fields in the response.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            article_id (string): article_id
            fields (string): Show only certain fields, specifed by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single article

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        if article_id is None:
            raise ValueError("Missing required parameter 'article_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_article(self, api_version, blog_id, article_id, article=None) -> dict[str, Any]:
        """
        Updates an article in a blog using the "PUT" method, replacing the existing resource with a new representation at the specified API path.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            article_id (string): article_id
            article (object): article
                Example:
                ```json
                {
                  "article": {
                    "id": 134645308,
                    "metafields": [
                      {
                        "key": "new",
                        "namespace": "global",
                        "value": "newvalue",
                        "value_type": "string"
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an article's image / Hide a published article / Update the alt text for an article image / Update an existing article of a blog / Publish a hidden article / Remove the image from an article / Add a metafield to an existing article

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        if article_id is None:
            raise ValueError("Missing required parameter 'article_id'")
        request_body = {
            'article': article,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_article(self, api_version, blog_id, article_id) -> dict[str, Any]:
        """
        Deletes a specific article from a blog using the provided blog and article identifiers and returns a success status upon completion.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            article_id (string): article_id

        Returns:
            dict[str, Any]: Delete an existing article from a blog

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        if article_id is None:
            raise ValueError("Missing required parameter 'article_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_article_authors(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of article authors in JSON format using the specified API version.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of all article authors

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/articles/authors.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_article_tags(self, api_version, limit=None, popular=None) -> dict[str, Any]:
        """
        Retrieves article tags with optional parameters for limiting results and filtering by popularity.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of tags to retrieve.
            popular (string): A flag for ordering retrieved tags. If present in the request, then the results will be ordered by popularity, starting with the most popular tag.

        Returns:
            dict[str, Any]: Retrieve a list of all tags from a specific blog / Retrieve a list of the most popular tags / Retrieve a list of all tags for all articles / Retrieve a list of the most popular tags from a specific blog

        Tags:
            Online store, Article
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/articles/tags.json"
        query_params = {k: v for k, v in [('limit', limit), ('popular', popular)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_assets_for_atheme(self, api_version, theme_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of theme assets for a specified theme in Shopify using the GET method at the "/admin/api/{api_version}/themes/{theme_id}/assets.json" endpoint, optionally filtering the response by fields specified in the query parameters.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names

        Returns:
            dict[str, Any]: Retrieve a list of all assets for a theme / Retrieve a theme image / Retrieve a Liquid template

        Tags:
            Online store, Asset
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_or_updates_an_asset_for_atheme(self, api_version, theme_id, asset=None) -> dict[str, Any]:
        """
        Updates or creates theme assets in Shopify stores using the Asset REST API, enabling modification of theme files like Liquid templates or CSS.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id
            asset (object): asset
                Example:
                ```json
                {
                  "asset": {
                    "key": "layout/alternate.liquid",
                    "source_key": "layout/theme.liquid"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an image asset by providing a base64-encoded attachment / Create an image asset by providing a source URL from which to upload the image / Change an existing Liquid template's value / Duplicate an existing asset by providing a source key

        Tags:
            Online store, Asset
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        request_body = {
            'asset': asset,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_asset_from_atheme(self, api_version, theme_id) -> dict[str, Any]:
        """
        Deletes a theme asset in a Shopify store using the "DELETE" method at the specified API path, returning a status message based on the outcome of the deletion request.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id

        Returns:
            dict[str, Any]: Delete an image from a theme

        Tags:
            Online store, Asset
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_alist_of_all_blogs(self, api_version, limit=None, since_id=None, handle=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of blogs with configurable filters (limit, handle, etc.) and optional field selection in the specified API version.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID
            handle (string): Filter by blog handle
            fields (string): comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Get all blogs for a shop after a specified ID / Get all blogs for a shop

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('handle', handle), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_blog(self, api_version, blog=None) -> dict[str, Any]:
        """
        Creates a new blog using the API at "/admin/api/{api_version}/blogs.json" with the "POST" method, returning a status indicating success or failure.

        Args:
            api_version (string): api_version
            blog (object): blog
                Example:
                ```json
                {
                  "blog": {
                    "metafields": [
                      {
                        "key": "new",
                        "namespace": "global",
                        "value": "newvalue",
                        "value_type": "string"
                      }
                    ],
                    "title": "Apple main blog"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new empty blog / Create a new empty blog with a metafield

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'blog': blog,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/blogs.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_acount_of_all_blogs(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of blogs using the "GET" method at the specified API endpoint.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Get all blogs for a shop

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_blog(self, api_version, blog_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a blog with the specified ID and optional fields using the "GET" method.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            fields (string): comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Get a single blog

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_blog(self, api_version, blog_id, blog=None) -> dict[str, Any]:
        """
        Updates or replaces an entire blog entry at the specified blog ID using the provided data and returns a success status.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id
            blog (object): blog
                Example:
                ```json
                {
                  "blog": {
                    "id": 241253187,
                    "title": "IPod Updates"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Add a metafield to an existing blog / Update an existing blog title and handle and also activate comments / Update an existing blog title

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        request_body = {
            'blog': blog,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_blog(self, api_version, blog_id) -> dict[str, Any]:
        """
        Deletes a blog with the specified ID using the DELETE method via the API endpoint "/admin/api/{api_version}/blogs/{blog_id}.json" and returns a successful status message if the operation is completed.

        Args:
            api_version (string): api_version
            blog_id (string): blog_id

        Returns:
            dict[str, Any]: Remove an existing blog from a shop

        Tags:
            Online store, Blog
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if blog_id is None:
            raise ValueError("Missing required parameter 'blog_id'")
        url = f"{self.base_url}/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_comments(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, fields=None, published_status=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of comments with filtering by date ranges, status, and field selection parameters via a GET request.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Show comments created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Show comments created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Show comments last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Show comments last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Show comments published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Show comments published before date (format: 2014-04-25T16:15:47-04:00).
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            published_status (string): Filter results by their published status.(default: any)
            status (string): Filter results by their status.

        Returns:
            dict[str, Any]: Retrieve all the comments for a certain article of a blog / Retrieve all the comments for this shop / Retrieve all comments for this shop after the specified ID / Retrieve all the comments for all the articles of a blog

        Tags:
            Online store, Comment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/comments.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('fields', fields), ('published_status', published_status), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acomment_for_an_article(self, api_version, comment=None) -> dict[str, Any]:
        """
        Creates comments through an administrative API endpoint.

        Args:
            api_version (string): api_version
            comment (object): comment
                Example:
                ```json
                {
                  "comment": {
                    "article_id": 134645308
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a comment for an article of a blog using basic Textile markup

        Tags:
            Online store, Comment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'comment': comment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/comments.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_comments(self, api_version, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None, status=None) -> dict[str, Any]:
        """
        Retrieves the count of comments filtered by creation, update, and publication timestamps or status using specific query parameters.

        Args:
            api_version (string): api_version
            created_at_min (string): Count comments created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Count comments created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Count comments last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Count comments last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Count comments published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Count comments published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Retrieve a count of comments with a given published status.(default: any)
            status (string): Retrieve a count of comments with a given status.

        Returns:
            dict[str, Any]: Count all comments for a certain article of a blog / Count all the comments for all the articles of a blog / Count all the comments for this shop

        Tags:
            Online store, Comment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/comments/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_comment_by_its_id(self, api_version, comment_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific comment's details by its ID in the GitHub API, supporting optional field filtering.

        Args:
            api_version (string): api_version
            comment_id (string): comment_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single comment

        Tags:
            Online store, Comment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        url = f"{self.base_url}/admin/api/{api_version}/comments/{comment_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_acomment_of_an_article(self, api_version, comment_id, comment=None) -> dict[str, Any]:
        """
        Updates a comment identified by `{comment_id}` using the "PUT" method, enabling modifications to existing comments in a structured API environment.

        Args:
            api_version (string): api_version
            comment_id (string): comment_id
            comment (object): comment
                Example:
                ```json
                {
                  "comment": {
                    "author": "Your new name",
                    "body": "You can even update through a web service.",
                    "email": "your@updated-email.com",
                    "id": 118373535,
                    "published_at": "2020-01-14T15:42:13.430Z"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the body of an existing comment

        Tags:
            Online store, Comment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if comment_id is None:
            raise ValueError("Missing required parameter 'comment_id'")
        request_body = {
            'comment': comment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/comments/{comment_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_pages(self, api_version, limit=None, since_id=None, title=None, handle=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, fields=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves a list of pages in JSON format using the Shopify API, allowing filtering by parameters such as limit, title, handle, creation and update dates, and publication status.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            title (string): Retrieve pages with a given title.
            handle (string): Retrieve a page with a given handle.
            created_at_min (string): Show pages created after date (format: 2008-12-31).
            created_at_max (string): Show pages created before date (format: 2008-12-31).
            updated_at_min (string): Show pages last updated after date (format: 2008-12-31).
            updated_at_max (string): Show pages last updated before date (format: 2008-12-31).
            published_at_min (string): Show pages published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Show pages published before date (format: 2014-04-25T16:15:47-04:00).
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            published_status (string): Restrict results to pages with a given published status:(default: any)

        Returns:
            dict[str, Any]: Retrieve a list of all pages after the specified ID / Get all pages for a shop

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/pages.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('title', title), ('handle', handle), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('fields', fields), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_page(self, api_version, page=None) -> dict[str, Any]:
        """
        Creates a new page in the Shopify admin using the POST method and returns a status message.

        Args:
            api_version (string): api_version
            page (object): page
                Example:
                ```json
                {
                  "page": {
                    "body_html": "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>",
                    "published": false,
                    "title": "Warranty information"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a page with a metafield / Create a page with HTML markup / Create an unpublished page

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'page': page,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/pages.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_apage_count(self, api_version, title=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves the count of pages in a Shopify store based on specified criteria such as title, creation date, update date, publication date, and publication status using the GET method.

        Args:
            api_version (string): api_version
            title (string): Count pages with a given title.
            created_at_min (string): Count pages created after date (format: 2008-12-31).
            created_at_max (string): Count pages created before date (format: 2008-12-31).
            updated_at_min (string): Count pages last updated after date (format: 2008-12-31).
            updated_at_max (string): Count pages last updated before date (format: 2008-12-31).
            published_at_min (string): Show pages published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Show pages published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Count pages with a given published status:(default: any)

        Returns:
            dict[str, Any]: Retrieve a count of all pages

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/pages/count.json"
        query_params = {k: v for k, v in [('title', title), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_page_by_its_id(self, api_version, page_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific page's details from the admin API, filtered by the requested fields, and returns the structured data in JSON format.

        Args:
            api_version (string): api_version
            page_id (string): page_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single page

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if page_id is None:
            raise ValueError("Missing required parameter 'page_id'")
        url = f"{self.base_url}/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_apage(self, api_version, page_id, page=None) -> dict[str, Any]:
        """
        Updates a specific page with the given ID using the PUT method, replacing its existing content with new data.

        Args:
            api_version (string): api_version
            page_id (string): page_id
            page (object): page
                Example:
                ```json
                {
                  "page": {
                    "id": 131092082,
                    "published": false
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an existing page completely / Add a metafield to a page / Show a hidden page / Update the body HTML of an existing page / Hide a published page

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if page_id is None:
            raise ValueError("Missing required parameter 'page_id'")
        request_body = {
            'page': page,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_apage(self, api_version, page_id) -> dict[str, Any]:
        """
        Deletes a page identified by the given page ID using the DELETE method, returning a status message upon successful deletion.

        Args:
            api_version (string): api_version
            page_id (string): page_id

        Returns:
            dict[str, Any]: Delete a page

        Tags:
            Online store, Page
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if page_id is None:
            raise ValueError("Missing required parameter 'page_id'")
        url = f"{self.base_url}/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_url_redirects(self, api_version, limit=None, since_id=None, path=None, target=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of redirects in JSON format using the "GET" method at the "/admin/api/{api_version}/redirects.json" endpoint, allowing filtering by parameters such as limit, since_id, path, target, and fields.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            path (string): Show redirects with a given path.
            target (string): Show redirects with a given target.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a list of URL redirects after a specified ID / Retrieve a list of all redirects

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/redirects.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('path', path), ('target', target), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_aredirect(self, api_version, redirect=None) -> dict[str, Any]:
        """
        Creates a new URL redirect using the API, returning a successful response with a status code of 201 upon completion, or an error response with a status code of 422 if validation fails.

        Args:
            api_version (string): api_version
            redirect (object): redirect
                Example:
                ```json
                {
                  "redirect": {
                    "body": "foobar"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a redirect using a full URL for the path, which will be saved as an absolute path without a domain / Create a redirect

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'redirect': redirect,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/redirects.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_url_redirects(self, api_version, path=None, target=None) -> dict[str, Any]:
        """
        Retrieves the count of redirects for a specified path using the GET method at "/admin/api/{api_version}/redirects/count.json".

        Args:
            api_version (string): api_version
            path (string): Count redirects with given path.
            target (string): Count redirects with given target.

        Returns:
            dict[str, Any]: Count all redirects

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/redirects/count.json"
        query_params = {k: v for k, v in [('path', path), ('target', target)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_redirect(self, api_version, redirect_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details of a specific redirect ID in JSON format, allowing optional field selection via query parameters.

        Args:
            api_version (string): api_version
            redirect_id (string): redirect_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single redirect by its ID

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if redirect_id is None:
            raise ValueError("Missing required parameter 'redirect_id'")
        url = f"{self.base_url}/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_redirect(self, api_version, redirect_id, redirect=None) -> dict[str, Any]:
        """
        Updates or replaces a specific redirect resource identified by `{redirect_id}` using the REST API, returning a status message if successful.

        Args:
            api_version (string): api_version
            redirect_id (string): redirect_id
            redirect (object): redirect
                Example:
                ```json
                {
                  "redirect": {
                    "id": 950115854,
                    "path": "/powermac",
                    "target": "/pages/macpro"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the path URI of a redirect / Update both the path and target URIs of a redirect

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if redirect_id is None:
            raise ValueError("Missing required parameter 'redirect_id'")
        request_body = {
            'redirect': redirect,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_aredirect(self, api_version, redirect_id) -> dict[str, Any]:
        """
        Deletes a specific URL redirect identified by the provided `redirect_id`, removing the associated redirection rule from the system.

        Args:
            api_version (string): api_version
            redirect_id (string): redirect_id

        Returns:
            dict[str, Any]: Delete an existing redirect

        Tags:
            Online store, Redirect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if redirect_id is None:
            raise ValueError("Missing required parameter 'redirect_id'")
        url = f"{self.base_url}/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_script_tags(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, src=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of script tags using the Shopify API, allowing filtering by parameters such as creation and update times, source URL, and specific fields.

        Args:
            api_version (string): api_version
            limit (string): The number of results to return.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Show script tags created after this date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show script tags created before this date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show script tags last updated after this date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show script tags last updated before this date. (format: 2014-04-25T16:15:47-04:00)
            src (string): Show script tags with this URL.
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a list of all script tags after the specified ID / Retrieve a list of all script tags / Retrieve a list of all script tags with a particular URL

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/script_tags.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('src', src), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_script_tag(self, api_version, script_tag=None) -> dict[str, Any]:
        """
        Creates a script tag for loading remote JavaScript into a storefront or checkout page via the Shopify Admin API.

        Args:
            api_version (string): api_version
            script_tag (object): script_tag
                Example:
                ```json
                {
                  "script_tag": {
                    "body": "foobar"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new script tag

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'script_tag': script_tag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/script_tags.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_all_script_tags(self, api_version, src=None) -> dict[str, Any]:
        """
        Retrieves the count of script tags using the "GET" method, with an optional query parameter "src" to refine the request.

        Args:
            api_version (string): api_version
            src (string): Count only script tags with a given URL.

        Returns:
            dict[str, Any]: Retrieve a count of all script tags for your shop

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/script_tags/count.json"
        query_params = {k: v for k, v in [('src', src)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_script_tag(self, api_version, script_tag_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a script tag by its ID using the API, allowing for optional specification of fields to include in the response.

        Args:
            api_version (string): api_version
            script_tag_id (string): script_tag_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a single script tag by its ID

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if script_tag_id is None:
            raise ValueError("Missing required parameter 'script_tag_id'")
        url = f"{self.base_url}/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_ascript_tag(self, api_version, script_tag_id, script_tag=None) -> dict[str, Any]:
        """
        Updates a script tag by its ID using the PUT method and returns a successful response with a status code of 200.

        Args:
            api_version (string): api_version
            script_tag_id (string): script_tag_id
            script_tag (object): script_tag
                Example:
                ```json
                {
                  "script_tag": {
                    "id": 596726825,
                    "src": "https://somewhere-else.com/another.js"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a script tag's URL

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if script_tag_id is None:
            raise ValueError("Missing required parameter 'script_tag_id'")
        request_body = {
            'script_tag': script_tag,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_ascript_tag(self, api_version, script_tag_id) -> dict[str, Any]:
        """
        Deletes a specified script tag from a Shopify store using the provided script tag ID.

        Args:
            api_version (string): api_version
            script_tag_id (string): script_tag_id

        Returns:
            dict[str, Any]: Delete an existing script tag

        Tags:
            Online store, ScriptTag
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if script_tag_id is None:
            raise ValueError("Missing required parameter 'script_tag_id'")
        url = f"{self.base_url}/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_themes(self, api_version, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of store themes (including active, unpublished, and legacy themes) with optional field filtering via query parameters.

        Args:
            api_version (string): api_version
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a list of themes

        Tags:
            Online store, Theme
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/themes.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_atheme(self, api_version, theme=None) -> dict[str, Any]:
        """
        Creates a new theme in a Shopify store via the Admin API, returning a success status on creation or validation errors.

        Args:
            api_version (string): api_version
            theme (object): theme
                Example:
                ```json
                {
                  "theme": {
                    "body": "foobar"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a theme that has a custom name and is published

        Tags:
            Online store, Theme
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'theme': theme,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/themes.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_theme(self, api_version, theme_id, fields=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific theme by ID from the Shopify admin, including customizable fields.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single theme

        Tags:
            Online store, Theme
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_theme(self, api_version, theme_id, theme=None) -> dict[str, Any]:
        """
        Updates a theme resource by replacing or modifying it using the provided JSON data.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id
            theme (object): theme
                Example:
                ```json
                {
                  "theme": {
                    "id": 752253240,
                    "name": "Experimental"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Publish an unpublished theme / Update a theme's name

        Tags:
            Online store, Theme
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        request_body = {
            'theme': theme,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_theme(self, api_version, theme_id) -> dict[str, Any]:
        """
        Deletes a specified theme and returns a success status upon completion.

        Args:
            api_version (string): api_version
            theme_id (string): theme_id

        Returns:
            dict[str, Any]: Delete a theme

        Tags:
            Online store, Theme
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if theme_id is None:
            raise ValueError("Missing required parameter 'theme_id'")
        url = f"{self.base_url}/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_checkouts(self, api_version, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, status=None) -> dict[str, Any]:
        """
        Retrieves the count of checkouts using the "GET" method at "/admin/api/{api_version}/checkouts/count.json", allowing filtering by parameters such as since_id, creation date, update date, and status.

        Args:
            api_version (string): api_version
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Count checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Count checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Count checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Count checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00)
            status (string): Count checkouts with a given status.(default: open)

        Returns:
            dict[str, Any]: Count all checkouts

        Tags:
            Orders, Abandoned checkouts
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/count.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_abandoned_checkouts(self, api_version, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of checkouts with optional filters like date ranges, status, and pagination controls.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            created_at_min (string): Show checkouts created after the specified date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show checkouts created before the specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show checkouts last updated after the specified date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show checkouts last updated before the specified date. (format: 2014-04-25T16:15:47-04:00)
            status (string): Show only checkouts with a given status.(default: open)

        Returns:
            dict[str, Any]: Retrieve all abandoned checkouts

        Tags:
            Orders, Abandoned checkouts
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acheckout(self, api_version, checkout=None) -> dict[str, Any]:
        """
        Creates a new checkout session for processing payments and managing order details.

        Args:
            api_version (string): api_version
            checkout (object): checkout
                Example:
                ```json
                {
                  "checkout": {
                    "email": "me@example.com"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a checkout with a product variant and quantity / Create a checkout without any line items

        Tags:
            Sales channels, Checkout
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'checkout': checkout,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/checkouts.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_draft_orders(self, api_version, fields=None, limit=None, since_id=None, updated_at_min=None, updated_at_max=None, ids=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of draft orders from a Shopify store, allowing specification of fields, limits, and filters by ID, status, and update time, using the GET method.

        Args:
            api_version (string): api_version
            fields (string): A comma-separated list of fields to include in the response
            limit (string): Amount of results(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID
            updated_at_min (string): Show orders last updated after date (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show orders last updated before date (format: 2014-04-25T16:15:47-04:00)
            ids (string): Filter by list of IDs
            status (string): Filter draft orders by their status.

        Returns:
            dict[str, Any]: List all draft orders

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders.json"
        query_params = {k: v for k, v in [('fields', fields), ('limit', limit), ('since_id', since_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('ids', ids), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_draftorder(self, api_version, draft_order=None) -> dict[str, Any]:
        """
        Creates a new draft order in a Shopify store, allowing merchants to generate provisional sales transactions for custom or wholesale purchases, manage inventory, and facilitate secure payment processing when the order is finalized.

        Args:
            api_version (string): api_version
            draft_order (object): draft_order
                Example:
                ```json
                {
                  "draft_order": {
                    "line_items": [
                      {
                        "applied_discount": {
                          "amount": "10.0",
                          "description": "Custom discount",
                          "title": "Custom",
                          "value": "10.0",
                          "value_type": "fixed_amount"
                        },
                        "price": "20.00",
                        "quantity": 1,
                        "title": "Custom Tee"
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: <span id="create-a-percent-discount-on-a-line-item-{{ current_version }}">Create a draft order with a percent discount on a line item</span> / Create a simple draft order with only a product variant ID. / <span id="create-a-draft-order-with-a-discount-{{ current_version }}">Create a draft order with a discount</span> / <span id="create-custom-draft-order-{{ current_version }}">Create custom draft order</span> / Create a draft order with a discounted line item

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'draft_order': draft_order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_draftorder(self, api_version, draft_order_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific draft order by its ID using the GET method, allowing optional filtering by specific fields to customize the response.

        Args:
            api_version (string): api_version
            draft_order_id (string): draft_order_id
            fields (string): A comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Get a representation of a single draft order

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if draft_order_id is None:
            raise ValueError("Missing required parameter 'draft_order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_draftorder(self, api_version, draft_order_id, draft_order=None) -> dict[str, Any]:
        """
        Updates a specific draft order using the Shopify Draft Order API, allowing for modifications such as changing products, quantities, or applying discounts.

        Args:
            api_version (string): api_version
            draft_order_id (string): draft_order_id
            draft_order (object): draft_order
                Example:
                ```json
                {
                  "draft_order": {
                    "id": 994118539,
                    "note": "Customer contacted us about a custom engraving on this iPod"
                  }
                }
                ```

        Returns:
            dict[str, Any]: <span id="set-discount-on-a-draft-order-{{ current_version }}">Set a discount on a draft order</span> / Add a note to a draft order

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if draft_order_id is None:
            raise ValueError("Missing required parameter 'draft_order_id'")
        request_body = {
            'draft_order': draft_order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_draftorder(self, api_version, draft_order_id) -> dict[str, Any]:
        """
        Deletes a draft order specified by its ID using the DELETE method, removing it from the system.

        Args:
            api_version (string): api_version
            draft_order_id (string): draft_order_id

        Returns:
            dict[str, Any]: Permanently delete a draft order

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if draft_order_id is None:
            raise ValueError("Missing required parameter 'draft_order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_acount_of_all_draftorders(self, api_version, since_id=None, status=None, updated_at_max=None, updated_at_min=None) -> dict[str, Any]:
        """
        Retrieves the count of draft orders matching specified conditions, such as status, update time, and since ID, using the Shopify API.

        Args:
            api_version (string): api_version
            since_id (string): Count draft orders after the specified ID.
            status (string): Count draft orders that have a given status.(default: open)
            updated_at_max (string): Count draft orders last updated before the specified date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Count draft orders last updated after the specified date (format: 2014-04-25T16:15:47-04:00).

        Returns:
            dict[str, Any]: Count all draft orders

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders/count.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('status', status), ('updated_at_max', updated_at_max), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_an_invoice(self, api_version, draft_order_id, draft_order_invoice=None) -> dict[str, Any]:
        """
        Sends an email invoice for a specified draft order using the Shopify Admin API.

        Args:
            api_version (string): api_version
            draft_order_id (string): draft_order_id
            draft_order_invoice (object): draft_order_invoice
                Example:
                ```json
                {
                  "draft_order_invoice": {}
                }
                ```

        Returns:
            dict[str, Any]: Send a customized invoice / Send the default invoice

        Tags:
            Orders, DraftOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if draft_order_id is None:
            raise ValueError("Missing required parameter 'draft_order_id'")
        request_body = {
            'draft_order_invoice': draft_order_invoice,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/draft_orders/{draft_order_id}/send_invoice.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_order_risks_for_an_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves the risk assessment details for a specific order using the "GET" method.

        Args:
            api_version (string): api_version
            order_id (string): order_id

        Returns:
            dict[str, Any]: Retrieve all order risks for an order

        Tags:
            Orders, Order Risk
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/risks.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_an_order_risk_for_an_order(self, api_version, order_id, risk=None) -> dict[str, Any]:
        """
        Submits a fraud risk assessment for an order to Shopify's deprecated legacy API, returning a 201 status upon creation.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            risk (object): risk
                Example:
                ```json
                {
                  "risk": {
                    "cause_cancel": true,
                    "display": true,
                    "message": "This order came from an anonymous proxy",
                    "recommendation": "cancel",
                    "score": 1,
                    "source": "External"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an order risk showing a fraud risk for proxy detection

        Tags:
            Orders, Order Risk
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'risk': risk,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/risks.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_order_risk_by_its_id(self, api_version, order_id, risk_id) -> dict[str, Any]:
        """
        Retrieves a specific risk associated with an order using the specified API version.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            risk_id (string): risk_id

        Returns:
            dict[str, Any]: Retrieve a single order risk

        Tags:
            Orders, Order Risk
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if risk_id is None:
            raise ValueError("Missing required parameter 'risk_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_order_risk(self, api_version, order_id, risk_id, risk=None) -> dict[str, Any]:
        """
        Updates or replaces a specific risk associated with an order in the system using the PUT method.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            risk_id (string): risk_id
            risk (object): risk
                Example:
                ```json
                {
                  "risk": {
                    "cause_cancel": false,
                    "id": 284138680,
                    "message": "After further review, this is a legitimate order",
                    "recommendation": "accept",
                    "score": 0,
                    "source": "External"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update an existing order risk for an order

        Tags:
            Orders, Order Risk
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if risk_id is None:
            raise ValueError("Missing required parameter 'risk_id'")
        request_body = {
            'risk': risk,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_order_risk_for_an_order(self, api_version, order_id, risk_id) -> dict[str, Any]:
        """
        Deletes a specific risk associated with an order using the API endpoint at "/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json" via the DELETE method.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            risk_id (string): risk_id

        Returns:
            dict[str, Any]: Delete an order risk for an order

        Tags:
            Orders, Order Risk
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if risk_id is None:
            raise ValueError("Missing required parameter 'risk_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_orders(self, api_version, ids=None, name=None, limit=None, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, processed_at_min=None, processed_at_max=None, attribution_app_id=None, status=None, financial_status=None, fulfillment_status=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of Shopify orders using the "GET" method at "/admin/api/{api_version}/orders.json," allowing for filtering by various criteria such as order IDs, creation and update times, status, and more.

        Args:
            api_version (string): api_version
            ids (string): Retrieve only orders specified by a comma-separated list of order IDs.
            name (string): Filters orders by name; optional query parameter (name=value format). Example: 'EB5-155256'.
            limit (string): The maximum number of results to show on a page.(default: 50)(maximum: 250)
            since_id (string): Show orders after the specified ID.
            created_at_min (string): Show orders created at or after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Show orders created at or before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Show orders last updated at or after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Show orders last updated at or before date (format: 2014-04-25T16:15:47-04:00).
            processed_at_min (string): Show orders imported at or after date (format: 2014-04-25T16:15:47-04:00).
            processed_at_max (string): Show orders imported at or before date (format: 2014-04-25T16:15:47-04:00).
            attribution_app_id (string): Show orders attributed to a certain app, specified by the app ID. Set as `current` to show orders for the app currently consuming the API.
            status (string): Filter orders by their status.(default: open) Example: 'any'.
            financial_status (string): Filter orders by their financial status.(default: any)
            fulfillment_status (string): Filter orders by their fulfillment status.(default: any)
            fields (string): Retrieve only certain fields, specified by a comma-separated list of fields names.

        Returns:
            dict[str, Any]: Retrieve all orders but show only certain properties / Retrieve specific orders / Retrieve orders that have authorized payments ready to be captured / Retrieve all orders / Retrieve orders last updated after 2005-07-31 15:57:11 in the EDT timezone / Retrieve all orders after the specified ID

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/orders.json"
        query_params = {k: v for k, v in [('ids', ids), ('name', name), ('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('processed_at_min', processed_at_min), ('processed_at_max', processed_at_max), ('attribution_app_id', attribution_app_id), ('status', status), ('financial_status', financial_status), ('fulfillment_status', fulfillment_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_an_order(self, api_version, order=None) -> dict[str, Any]:
        """
        Creates a new order in a Shopify store using the Admin API, returning a response with a status code based on the operation's success or failure.

        Args:
            api_version (string): api_version
            order (object): order
                Example:
                ```json
                {
                  "order": {
                    "email": "foo@example.com",
                    "fulfillment_status": "fulfilled",
                    "fulfillments": [
                      {
                        "location_id": 905684977
                      }
                    ],
                    "line_items": [
                      {
                        "quantity": 1,
                        "variant_id": 447654529
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a partially paid order with a new customer and addresses / Create a comprehensive order / Create an order with tax lines split across taxable line items / Create a simple order with only a product variant ID / Create a simple order without sending an order receipt or a fulfillment receipt / Create a simple order, sending an order confirmation and a shipping confirmation to the customer / Create a pending order with an existing customer / Create a simple order and fulfill it

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'order': order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves details for a specific order using the specified API version and order ID in the admin API.

        Args:
            api_version (string): api_version
            order_id (string): order_id

        Returns:
            dict[str, Any]: Retrieve a single order / Get only particular fields

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_order(self, api_version, order_id, order=None) -> dict[str, Any]:
        """
        Updates an existing order or creates a new one at the specified order ID using the PUT method.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            order (object): order
                Example:
                ```json
                {
                  "order": {
                    "buyer_accepts_marketing": true,
                    "id": 450789469
                  }
                }
                ```

        Returns:
            dict[str, Any]: Add note attributes to an order / Update the shipping address of an order / Update an order's tags / Add a note to order / Change an order's phone number / Add a metafield to an order / Change an order's email address / Remove the customer from an order / Change whether the buyer accepts marketing

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'order': order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_an_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Deletes a specified order using the provided order ID, returning a successful status if the operation is completed.

        Args:
            api_version (string): api_version
            order_id (string): order_id

        Returns:
            dict[str, Any]: Delete an order

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_an_order_count(self, api_version, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, status=None, financial_status=None, fulfillment_status=None) -> dict[str, Any]:
        """
        Retrieves the count of orders from a Shopify store with optional filters for date ranges, status, and fulfillment/financial states.

        Args:
            api_version (string): api_version
            created_at_min (string): Count orders created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Count orders created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Count orders last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Count orders last updated before date (format: 2014-04-25T16:15:47-04:00).
            status (string): Count orders of a given status.(default: open)
            financial_status (string): Count orders of a given financial status.(default: any)
            fulfillment_status (string): Filter orders by their fulfillment status.(default: any)

        Returns:
            dict[str, Any]: Count orders that have authorized payments ready to be captured / Count all orders

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status), ('financial_status', financial_status), ('fulfillment_status', fulfillment_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancels_an_order(self, api_version, order_id, amount=None, currency=None, note=None) -> dict[str, Any]:
        """
        Cancels a specified order using a POST request and returns status codes for success (200) or invalid request (422).

        Args:
            api_version (string): api_version
            order_id (string): order_id
            amount (string): amount Example: '10.00'.
            currency (string): currency Example: 'USD'.
            note (string): note
                Example:
                ```json
                {
                  "amount": "10.00",
                  "currency": "USD",
                  "note": "Broke in shipping"
                }
                ```

        Returns:
            dict[str, Any]: Cancel and refund an order using the <code>refund</code> property / Cancel an order / Cancel and refund an order using the <code>amount</code> property

        Tags:
            Orders, Order
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'amount': amount,
            'currency': currency,
            'note': note,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/cancel.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_refunds_for_an_order(self, api_version, order_id, limit=None, fields=None, in_shop_currency=None) -> dict[str, Any]:
        """
        Retrieves a list of refunds for a specified order, allowing optional filtering by the number of results, specific fields, and currency.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            in_shop_currency (string): Show amounts in the shop currency for the underlying transaction.(default: false)

        Returns:
            dict[str, Any]: Retrieve all refunds from a specific order

        Tags:
            Orders, Refund
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/refunds.json"
        query_params = {k: v for k, v in [('limit', limit), ('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_arefund(self, api_version, order_id, refund=None) -> dict[str, Any]:
        """
        Creates a refund for an order using the specified order ID, allowing merchants to process partial or full refunds through the API.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            refund (object): refund
                Example:
                ```json
                {
                  "refund": {
                    "currency": "USD",
                    "shipping": {
                      "amount": 5
                    },
                    "transactions": [
                      {
                        "amount": 5,
                        "gateway": "bogus",
                        "kind": "refund",
                        "parent_id": 801038806
                      }
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a refund for an order / Refund a specific amount of shipping

        Tags:
            Orders, Refund
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'refund': refund,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/refunds.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_refund(self, api_version, order_id, refund_id, fields=None, in_shop_currency=None) -> dict[str, Any]:
        """
        Retrieves a specific refund associated with an order by its ID, allowing customization of the response with optional fields and currency settings.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            refund_id (string): refund_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            in_shop_currency (string): Show amounts in the shop currency for the underlying transaction.(default: false)

        Returns:
            dict[str, Any]: Retrieve a specific refund

        Tags:
            Orders, Refund
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if refund_id is None:
            raise ValueError("Missing required parameter 'refund_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/refunds/{refund_id}.json"
        query_params = {k: v for k, v in [('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def calculates_arefund(self, api_version, order_id, refund=None) -> dict[str, Any]:
        """
        Calculates refund amounts for an order, including line items, shipping, and taxes, based on specified criteria.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            refund (object): refund
                Example:
                ```json
                {
                  "refund": {
                    "refund_line_items": [
                      {
                        "line_item_id": 518995019,
                        "quantity": 1,
                        "restock_type": "no_restock"
                      }
                    ],
                    "shipping": {
                      "full_refund": true
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: Calculate the refund for a line item and shipping / Calculate a refund for a partial amount of shipping / Calculate the refund without specifying currency

        Tags:
            Orders, Refund
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'refund': refund,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/refunds/calculate.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_transactions(self, api_version, order_id, since_id=None, fields=None, in_shop_currency=None) -> dict[str, Any]:
        """
        Retrieves a list of transactions for a specified order using the Shopify API, optionally filtered by since_id, specified fields, and currency.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            since_id (string): Retrieve only transactions after the specified ID.
            fields (string): Show only certain fields, specifed by a comma-separated list of fields names.
            in_shop_currency (string): Show amounts in the shop currency.(default: false)

        Returns:
            dict[str, Any]: Retrieve an order's transactions / Retrieve an order's transactions after a specified ID

        Tags:
            Orders, Transaction
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/transactions.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_atransaction_for_an_order(self, api_version, order_id, transaction=None) -> dict[str, Any]:
        """
        Creates a new transaction for a specified order using the Shopify Admin API and returns the result with a 201 Created status.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            transaction (object): transaction
                Example:
                ```json
                {
                  "transaction": {
                    "amount": "10.00",
                    "currency": "USD",
                    "kind": "capture",
                    "parent_id": 389404469
                  }
                }
                ```

        Returns:
            dict[str, Any]: Capture the full amount for an authorized order, and associate the capture with an authorization by including its authorization code / Create a test transaction. / Capture a specified amount on an authorized order, and associate the capture with an authorization by including its ID

        Tags:
            Orders, Transaction
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'transaction': transaction,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/transactions.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_an_order_stransactions(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves the transaction count for a specific order using the "GET" method.

        Args:
            api_version (string): api_version
            order_id (string): order_id

        Returns:
            dict[str, Any]: Count an order's transactions

        Tags:
            Orders, Transaction
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/transactions/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_transaction(self, api_version, order_id, transaction_id, fields=None, in_shop_currency=None) -> dict[str, Any]:
        """
        Retrieves a specific transaction from an order, optionally filtering response fields and currency format using query parameters.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            transaction_id (string): transaction_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            in_shop_currency (string): Show amounts in the shop currency.(default: false)

        Returns:
            dict[str, Any]: Retrieve a specific transaction for an order

        Tags:
            Orders, Transaction
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if transaction_id is None:
            raise ValueError("Missing required parameter 'transaction_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/transactions/{transaction_id}.json"
        query_params = {k: v for k, v in [('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_gift_cards(self, api_version, status=None, limit=None, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of gift cards in JSON format, allowing filtering by status, limiting the number of results, specifying a starting point with an ID, and selecting specific fields for the response.

        Args:
            api_version (string): api_version
            status (string): Retrieve gift cards with a given status. Valid values:
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a list of all gift cards / Retrieve a list of all enabled gift cards

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards.json"
        query_params = {k: v for k, v in [('status', status), ('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_agift_card(self, api_version, gift_card=None) -> dict[str, Any]:
        """
        Creates a new gift card and returns the created resource with a 201 status code.

        Args:
            api_version (string): api_version
            gift_card (object): gift_card
                Example:
                ```json
                {
                  "gift_card": {
                    "initial_value": 25
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a gift card with a custom code / Create a gift card with an automatically generated code

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'gift_card': gift_card,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_gift_card(self, api_version, gift_card_id) -> dict[str, Any]:
        """
        Retrieves information about a specific gift card using the provided gift card ID.

        Args:
            api_version (string): api_version
            gift_card_id (string): gift_card_id

        Returns:
            dict[str, Any]: Retrieve a single gift card

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if gift_card_id is None:
            raise ValueError("Missing required parameter 'gift_card_id'")
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards/{gift_card_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_gift_card(self, api_version, gift_card_id, gift_card=None) -> dict[str, Any]:
        """
        Updates the details of a specific gift card using the PUT method at the "/admin/api/{api_version}/gift_cards/{gift_card_id}.json" endpoint.

        Args:
            api_version (string): api_version
            gift_card_id (string): gift_card_id
            gift_card (object): gift_card
                Example:
                ```json
                {
                  "gift_card": {
                    "id": 48394658,
                    "note": "Updating with a new note"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the expiry date of a gift card / Update the note of a gift card

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if gift_card_id is None:
            raise ValueError("Missing required parameter 'gift_card_id'")
        request_body = {
            'gift_card': gift_card,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards/{gift_card_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_gift_cards(self, api_version, status=None) -> dict[str, Any]:
        """
        Retrieves the count of gift cards filtered by status using the Shopify Admin REST API.

        Args:
            api_version (string): api_version
            status (string): Count gift cards with a given status. Valid values:

        Returns:
            dict[str, Any]: Retrieve a count of enabled gift cards / Retrieve a count of all gift cards

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards/count.json"
        query_params = {k: v for k, v in [('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def disables_agift_card(self, api_version, gift_card_id, gift_card=None) -> dict[str, Any]:
        """
        Deactivates a gift card and invalidates its remaining balance via a POST request.

        Args:
            api_version (string): api_version
            gift_card_id (string): gift_card_id
            gift_card (object): gift_card
                Example:
                ```json
                {
                  "gift_card": {
                    "id": 48394658
                  }
                }
                ```

        Returns:
            dict[str, Any]: Disable a gift card

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if gift_card_id is None:
            raise ValueError("Missing required parameter 'gift_card_id'")
        request_body = {
            'gift_card': gift_card,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards/{gift_card_id}/disable.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def searches_for_gift_cards(self, api_version, order=None, query=None, limit=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of gift cards matching specified criteria such as search query, order, limit, and requested fields.

        Args:
            api_version (string): api_version
            order (string): The field and direction to order results by.(default: disabled\_at DESC)
            query (string): The text to search for.
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all gift cards with the last characters "mnop"

        Tags:
            Plus, Gift Card
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/gift_cards/search.json"
        query_params = {k: v for k, v in [('order', order), ('query', query), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_all_users(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of users in the system as JSON data using the "GET" method.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of all users

        Tags:
            Plus, User
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/users.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_user(self, api_version, user_id) -> dict[str, Any]:
        """
        Retrieves a specific user's details from the administrative API in JSON format for the specified API version and user ID.

        Args:
            api_version (string): api_version
            user_id (string): user_id

        Returns:
            dict[str, Any]: Retrieve a single user

        Tags:
            Plus, User
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if user_id is None:
            raise ValueError("Missing required parameter 'user_id'")
        url = f"{self.base_url}/admin/api/{api_version}/users/{user_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_the_currently_logged_in_user(self, api_version) -> dict[str, Any]:
        """
        Retrieves the current authenticated user's details in the specified API version.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve the the currently logged-in user

        Tags:
            Plus, User
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/users/current.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_collects(self, api_version, limit=None, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of data collections in JSON format, allowing filtering by limit, since_id, and specific fields.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to show.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve only collects for a certain product / Retrieve all collects for the shop / Retrieve only collects for a certain collection

        Tags:
            Products, Collect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/collects.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def adds_aproduct_to_acustom_collection(self, api_version, collect=None) -> dict[str, Any]:
        """
        Creates a new collection in a store using the POST method, returning a status message upon successful creation or an error response if the request is invalid.

        Args:
            api_version (string): api_version
            collect (object): collect
                Example:
                ```json
                {
                  "collect": {
                    "collection_id": 841564295,
                    "product_id": 921728736
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new link between an existing product and an existing collection

        Tags:
            Products, Collect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'collect': collect,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/collects.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_collect_by_its_id(self, api_version, collect_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific collect entry from the Shopify admin API, returning JSON data with fields optionally filtered by the request.

        Args:
            api_version (string): api_version
            collect_id (string): collect_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a collect with a certain ID

        Tags:
            Products, Collect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collect_id is None:
            raise ValueError("Missing required parameter 'collect_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collects/{collect_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_aproduct_from_acollection(self, api_version, collect_id) -> dict[str, Any]:
        """
        Deletes a specific collect entry by ID using the specified API version and returns a success status.

        Args:
            api_version (string): api_version
            collect_id (string): collect_id

        Returns:
            dict[str, Any]: Delete the link between a product an a collection

        Tags:
            Products, Collect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collect_id is None:
            raise ValueError("Missing required parameter 'collect_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collects/{collect_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_collects(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of collections using the GET method at the specified API endpoint "/admin/api/{api_version}/collects/count.json".

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Count only collects for a certain collection / Count only collects for a certain product / Count all collects for the shop / Count only collects for a certain product / Count only collects for a certain collection / Count all collects for the shop

        Tags:
            Products, Collect
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/collects/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_collection(self, api_version, collection_id, fields=None) -> dict[str, Any]:
        """
        Retrieves information about a specific collection using the "GET" method, allowing optional filtering through the "fields" query parameter.

        Args:
            api_version (string): api_version
            collection_id (string): collection_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a specific collection by its ID

        Tags:
            Products, Collection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_id is None:
            raise ValueError("Missing required parameter 'collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collections/{collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_alist_of_products_belonging_to_acollection(self, api_version, collection_id, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of products from a specific collection using the "GET" method, allowing optional filtering by a limit parameter.

        Args:
            api_version (string): api_version
            collection_id (string): collection_id
            limit (string): The number of products to retrieve.(default: 50)(maximum: 250)

        Returns:
            dict[str, Any]: Retrieve a list of products belonging to a collection

        Tags:
            Products, Collection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_id is None:
            raise ValueError("Missing required parameter 'collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collections/{collection_id}/products.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_custom_collections(self, api_version, limit=None, ids=None, since_id=None, title=None, product_id=None, handle=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of custom collections (manually curated product groupings) with optional filtering by parameters like IDs, titles, product associations, and publication status.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            ids (string): Show only collections specified by a comma-separated list of IDs.
            since_id (string): Restrict results to after the specified ID.
            title (string): Show custom collections with a given title.
            product_id (string): Show custom collections that include a given product.
            handle (string): Filter by custom collection handle.
            updated_at_min (string): Show custom collections last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Show custom collections last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Show custom collections published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Show custom collections published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Show custom collectsion with a given published status.(default: any)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all collections / Retrieve all collections after the specified ID / Retrieve a list of specific custom collections / Retrieve all custom collections that contain a given product

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections.json"
        query_params = {k: v for k, v in [('limit', limit), ('ids', ids), ('since_id', since_id), ('title', title), ('product_id', product_id), ('handle', handle), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acustom_collection(self, api_version, custom_collection=None) -> dict[str, Any]:
        """
        Creates a new custom collection in a Shopify store using the API, allowing merchants to group products together for easier navigation.

        Args:
            api_version (string): api_version
            custom_collection (object): custom_collection
                Example:
                ```json
                {
                  "custom_collection": {
                    "image": {
                      "alt": "Rails Logo",
                      "src": "http://example.com/rails_logo.gif"
                    },
                    "title": "Macbooks"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an unpublished custom collection / Create a custom collection / Create a collection that contains a product by including a collect / Create a custom collection with a base64-encoded image / Create a custom collection with a metafield / Create a custom collection with an image, which will be uploaded to Shopify

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'custom_collection': custom_collection,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_custom_collections(self, api_version, title=None, product_id=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves a count of custom collections in a Shopify store, optionally filtered by title, product association, or publication timestamps.

        Args:
            api_version (string): api_version
            title (string): Count custom collections with given title.
            product_id (string): Count custom collections that include a given product.
            updated_at_min (string): Count custom collections last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Count custom collections last updated before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min (string): Count custom collections published after date (format: 2014-04-25T16:15:47-04:00).
            published_at_max (string): Count custom collections published before date (format: 2014-04-25T16:15:47-04:00).
            published_status (string): Count custom collections with a given published status.(default: any)

        Returns:
            dict[str, Any]: Count all custom collections that contain a given product / Count all custom collections

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections/count.json"
        query_params = {k: v for k, v in [('title', title), ('product_id', product_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_custom_collection(self, api_version, custom_collection_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific custom collection and optionally includes specified fields in the response, using the Shopify API.

        Args:
            api_version (string): api_version
            custom_collection_id (string): custom_collection_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a specific collection by its ID

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if custom_collection_id is None:
            raise ValueError("Missing required parameter 'custom_collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_custom_collection(self, api_version, custom_collection_id, custom_collection=None) -> dict[str, Any]:
        """
        Updates an existing custom collection by replacing it with the new data provided in the request body, allowing modifications to its attributes such as title and collected products.

        Args:
            api_version (string): api_version
            custom_collection_id (string): custom_collection_id
            custom_collection (object): custom_collection
                Example:
                ```json
                {
                  "custom_collection": {
                    "id": 841564295,
                    "published": false
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the description of a custom collection / Update a collection to remove its image / Update a collection with a new collection image / Update a collection with new alt text for its image / Publish a hidden collection / Add a collect to an existing collection by providing a product ID, and update an existing collect by its own ID to change its sort position / Add a metafield to an existing collection / Hide a published collection

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if custom_collection_id is None:
            raise ValueError("Missing required parameter 'custom_collection_id'")
        request_body = {
            'custom_collection': custom_collection,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_acustom_collection(self, api_version, custom_collection_id) -> dict[str, Any]:
        """
        Deletes a custom product collection in Shopify using the specified collection ID.

        Args:
            api_version (string): api_version
            custom_collection_id (string): custom_collection_id

        Returns:
            dict[str, Any]: Delete a custom collection

        Tags:
            Products, CustomCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if custom_collection_id is None:
            raise ValueError("Missing required parameter 'custom_collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_alist_of_all_product_images(self, api_version, product_id, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of product images for a specified product using the "GET" method at the "/admin/api/{api_version}/products/{product_id}/images.json" path, allowing optional filters by "since_id" and customizable fields.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            since_id (string): Restrict results to after the specified ID
            fields (string): comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Get all product images for a product / Get all product images for a product after a specified ID

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_product_image(self, api_version, product_id, image=None) -> dict[str, Any]:
        """
        Creates and manages product images by uploading new images for a specified product using the POST method.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            image (object): image
                Example:
                ```json
                {
                  "image": {
                    "attachment": "R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\nU7Mq2Mq1K9cUW8GKTUG2rNkUHNByWMuWLdWva7t1W7UKG4S7eO/ycEhQHgaK\nsL4VGGyocGE3br5929KuxQFFkEtIlgypsuUDmDMfWGRmUZvPoEHfGU36jgDT\nLQSoVt3IQ2sPsL0IUNZGlZ0H0lo00jEkCytWMspdGzBgn/F9EBIWnKIQlqHB\nhA0bQpx48Z7UAkoEcMTdUeTJJSxf/4akOTNnzqHb3GkjrUdp0gKwq77jWdod\nO7dNKWvhRUcWT6zYQI82xB03AAQNCdTKX/xAAB10hfVCnRtbVIhIAy14oJoZ\nAXS4XXfdQaYIeOGJRx555Z1nRnrqqUeaMtIYY8dmn7Vg2yK57TYEgAzIQGBx\nxyXHj0A0OOTggxFKSN1iWwTTAIYanpYdMtFE4+GVIHrn3XeUmVhZeWiIMoOY\nnVQDGiTgKALJjIssIsADt0mjjI6+AXcDgQYi2M8/7ijEwzRIFmBIL9NVV+EW\nVzyZ4Wqj9RBABchQWeWkV3aY5ZYjjgieeKL446mnjxwAiZVpliAjZqblt19/\n/7HCwIAFGv+X3J4s9fMckoYhphiTQTwJ5Wqn9dDDAWuMUUEFviTrS6STVlmp\npVmKqCkOn34aB6TIBAAOJeHZAYl6ptixSCL8edGbq8HFeqBDcygEyIOCGqYk\nkxUW4euiq7knbA/gUDHGv//ec2wFayQbaQWinOCslVhmSUq1/gCDLJXacgtJ\nCYu4J66cjbAKoA3CxapnOgm9g+ughdK7xYX3Rinlvj2YYcYanVBBhTg2Axzw\nG4/4k4bBzDZbKRUQP1LIsRSX6sgBZtwhzQP68ccbj7AWty4/5igEoaC9dK3r\noVtgs4evvzKqb8wyQ0JFJzXXbDMVcQBQLTDGVmCssstKGs09oPT/jQcRoBw9\nMamKgEOeeg/gqBtvdVZSDnHFIQgRD4RxXWhiYEOQKNn4zncHzDIzHc0ZpHdy\nRicIQOypKDf7q3Pd96ABzSab+E1EIYIvS2o0ijA92gPZiCB1qwL+iJxL78Z7\n2NeHQrAK2YrCZva+bcgcujFUQIEG6WigonoCdLT9tr9UbIIAMMCEkkYacvvT\nxSgsBPKGJKBEAw4yjhx+hyn+PAJFfztyVdWOt5B3RehyimneFuwFvQxFyTSf\n25f1zCAqSFACDXTQ3gwSoDoElI5tZyBAINqnuhJ+Kg9vOIOaVnSHT5ECHucK\n0OMiBxJAPCdXmGseBLoBvei5rFEStB5m/yBhjFJUIw50oIMoLvCpFRAADduj\nwxvUYMIqmvARCBiDeiwRBk+lQQTEq5qQ3CWdJSkGAlu4y9h66EBgAbF6QhSV\nMUpQilKcQRNLwIenfpFEJebBioC0ohrQQJ8QhMIfSwhgj2YouYTYUEmGqhBe\nFNBDH5otgmgLnRyLWMdq0GEGCMCHJjSBjzQE8pSChMLTCJBI4pXDBeuiiA1T\nprK7PK+SUPphsIQ1wSEag5OUKIUlyiAmAowClci0YizKILUAFi+WDQEEJOmF\nxlnMYnOVbOP0gkjBTdZRmDiwhCuywcRkmtOEpHjC1DzBABto4xqN5AcgdEXN\nNO4Ql0+CB2xctv9LM2SSgpXhZB0t0QlT+iMUkzinQquFihD452P0gGdGAPGN\nHKYxjbOAwBpxqU9+ApGXQgyoQDWRgASwoAMGMMAHDrnQhc5AkQPSU0NgYVF7\nQmAWKcBnPvc5HwGcbUVxJCInEfACQXQACUhFQkqRwAIOttScv9ABO21wA8k1\np5Z3mYXYdNqAjvLzbHDUpFCNIQoUdGAdHUhrUg2gVAOg4AXmvEAaOPEGaCCA\nAASQxBtIYYIq5kEHAaKHVfsRGB3eNBPYxKdXGVWGUnAzdOSxgyg+MIxhoDWt\nal3rUlXABEBeYBQIiMMm0AAKPBBAE1A4nTjWEIAzvGEFqsvDEHqEjZj/wMKw\n1rwlVxerGkv4AxVoAOkEmXGMOKDgA8i1LFrRioSjKrWtKRVEQlXHBBSKQhLQ\nEG3tCHCLJaSWClD0zgHO8LBqDeIYNsDGTG4ryZtak4G7lZ6G2sBSfyCAaTK7\nAzfgQIEzoOC/yKVsZS+bWeim1BsdqEG10oCANxDgDZwIRHa3O4hbaA91nlKB\nKA7QBhHo0VPwCFBtAdNea86CZVztKk8FUN5PjQIHxKWABihQBkHY+L/HTa5l\nMetcAxvAG94wQAQAkA1SIIAUBvUHdkVLgBkMwrvkPSEkVtSCJ/yCAJ5gZ20l\nwgObziITGk3xTqUHhWoxYQVdAIYINMBmO0TA/8aCwHGOBbwOAvc4pXj2RieY\nIY69ttgfpJBEHOLQ5ArTAQ2SaPAb4lAC33XsoaxYhUx4kFVrZoKSYlYxbOzg\nPX8kAM1d6AILOuEDDQzBBCaIwJvhjOMAU7bOmE0qdMUhhFozQhVxiMWnuiAJ\nQTfZyahFQydWGwA1cbiZAJL0Qiht6UzoVsxetUQaJhEKZzhDBdh+A5s9AQxU\nq3rVN241ne0sa1rXWgjbqLUd3uqPUYhCFNDAxwzm3d3vjgF/vTvAHegUaYbw\nwMSZyAR8oX0I2BwiC2eoQQ2srYJA6IDNb2ABqr39bVYDWMfkRgIVzs1xdEOD\nCjhQ4nXlPe9BaOLQNf+rRjQc0eg2DM8TyvZTs3mY6Xwy4xI2YLMGdIAAhTvD\nFWzuhKhZIHGKq9riF381rDtQho53/Bjpboc1OiEJktMbtaplrbHboCOYT9rS\nOdhopocwgiRowOw6L0MNCKCBKjwA26IW9cRTXfE4i1vAlpUEHJze8XTXehvc\n2AQ05k3vDHaiDGNYeaPNoAzGxbwf/86EHDCd4kbsyBMySII2NH92nevg4TbI\nA7ZVEGqiF93ocLb7nIdhgGMIoROW4Dvft2GHOqQiDoM3+YWJnT8O7yYL3fgI\nDwK+CrFX0lwBctUxtLH55qNd5xkYxMKvDffSn/7b4L47JYQgjnW0XvZOv0L/\nKmz/BS5sIg5QvtkavDPlO/Am+FzOBCBqgU8veEJA9LCBDRjQznIw3/lJEIBs\n5gqhUIALN3rWR3QTh31IFwcUkAiV1QEOCH4ddw8LkAqpUH5cgAtnIGzikHgs\nxzSW1w3+Jgc0Bz32Rw8DoA3lQA8yIAP6xwoj4H//B4BJYAOjoAZqYIDWRn0J\nuIB1Z3fHQAGdgHeJQIEcxwwLQH5csIHEQARE4C9aRx49oAPw5ydyIHaANUPE\nwXwtmH/6Vw5iKIb/F4DaoAGisAIroIM7WG0MR3pDd3qoJwjVQAEUAAdvEGAG\nsHcUgITFgAtLmIFNiAtQeAInMAa+UGwiyAEW8QMc//AkgKUNx7EPkLOCLOiC\nNiADIzCDY0iDm2cHLxCKbNiGPueDcVh02McJ/GWHjfABxyUJdigEfUiB+pAL\ndVAHX1B+uPCERHAChSAw8QAOHMaIE6EF3MAKkjiJxlGJljgC+UcPm7iJnch8\nDJAHoRiKaqiDBRgK01d9LDB0QFiHdmiH1YACSDCE4ziLsscIdRCIGriLhfiL\naxAPOKAKtbARPFAFQKKMywg5XuiC9ACN0TiNOwAAAHCNL5CN2siN3QiHcYhq\nwCAD6WiHomAJEzmO4LcGueCOG4gLf2OIAjOPOHCPEEFT/KiMzKgNLigDABmN\nnKgL02aQB3mNCkmKB+iNCv+IBjI2Y+O4ihcZi063DcywkReYi04Yj/ewBmuA\nAyRYEbAAAVVwkv3oj9rwgizJks4okCMwCI+ACqgwCQaJkGq4hm3IjW8YakPn\nCWxmhzz5kxfJd3iwkUx4lL0ojw/QlAnxlG4glQYCOStplS8YkJuoCwnwCIY5\nCYgZljRJlqTYg9WnbTq3lm3plrGojrVWixuJgRpIDB95AgLTCCRYkjeVAXw5\nlfqXiVa5ks64QSVlmF8JljO5mAtplj4IdJE5YzpHmenYcXCwAHKJi7rIi74Y\nD7oQms1xU71QmpQ4AOVwmvoHmAH5ABcwna3pmompmAnJmDzIcGp5m2upmxMp\ni+f/Zg9AIJeCeJSG+ACHAH8OwWyzoJyUCIOnCYOAKQP4wATTeQElVZio8AiI\nCZtiSZbbuHAIUAXemZu5CZ4YyQ250KAXeJ6c2YsCYIUYwWyZUADK6QoEwAfO\nOZ8yoANSwAT4SZ37eZjXGZtjOZshoAFQ8HAHOo6TCZ5CgAfluYS4OIhPGA8C\n4AXBtxBP+WXvWZrZ4ClhYAkdmokzgAkhKqIjqp+GaaIyGaAL+XDOEAEueqC4\nGaNuKQTWAAQ1OpceCQktcAgcYFuHJQc+wJfhADFpsAPhcJpewAZKKgVL2qTV\n2ZUnKptqMApJ8ADVZqVYKpkKaodwEAflaYvAuYFE4HIe/8CIEWGhchCkJ7kE\nJQQAHGoDZcYGckqnTGqnhWmiALqYS5AEdGCAVmqgBvqiMqagquANX3qe8cCo\njpqX1iQHsAALaWogx5FkEBMO7URCmjqnTJqfJQql2LkClpAEwNCGahABapmq\nqqqgjAAE3uCgTFgC6tEIZVoRzCYHckBpJ+kBJoQA+xcCqrOpdeqpT/qf2JkF\nSQAPOdiGLoqq0QqeVOCqDUp+RMBh+7atDgELX+atPJCPKOkAJmQJ7fRH54oJ\nc7qk+amfn+qfsAkAKqB5SeAFo7CGwBCo3smWlMkMQPaqyAAJi2AaKTBpECB5\nUdFlKJk6qoMK/McHVsSwdFqnxP9aUv3JrgRghhcbCCswqp0XmdAamTtJmXHg\nqjWaCmqCIwJwsg/RrSvLA6R5HDIAAyJAAJ3mKQQAAwxwC4Akp8Iqog9bna+5\nA2V4g+kUgM/HZlUwtB2rparwYzWKB/nzAG3QtBVaq1HxA5+wl8cBA1iABTCg\nCyGgsK7Af1lrReiariTKn6ggAmTIfDfIAJuntt7pth2bjnAABHKbC74ADi13\nByfLrQG7sp/AA8dBD4EruIILAy0ABboAA66ATMHKqcMKsZ/aCNMouWrbu2vb\nthw7kdUgt3VgP41WsinwEPzwb7NgqzzwA3xrCMYBuKu7ujBwvTBAAOYEtrbr\nqQkwg5z/GLmVa7GWy7EJmo7ccGB4gAxp8i3SMLoNEXnOywOf8AmwsA/aUL3V\ni726QELJtLi3W1ICWQ7SGLm+67tCi6UeSwGb8GOFkC1L+74uAbAq+7z1Sw0F\nwACXcAmBy8H6O7sLxb22O52k4IwD2Yk0SL69a763KWOJgAQLACnFBgl267Qy\nV8H0+wnUgAEb3MMbrL/a+1SaWrNMSgpYqZUEPIY1qMICyMJtCQSB4wv2czjw\nC3mla8E6nAzcEA4+jAU/HLiJG8IAbMRW6ZLgq8S8e8BOPGM4cDtSDLqboQD4\neMV8m8VXkAV47MMeDMJP9SmLiw82oAOpicThm8IHXL6BSgEn/4AHhbAsaRLH\nMSG/e3vBjojHWRADeowFg9DHEMO9DmADDjAK1ZCaLknAhZzGaoyl3IALXHAC\nMry0cjwR8juwz0sN1OBs3HDJlpwFl8DLvMrJnqKpUADKIUoKD1DGpVzAZ3vI\nWKoIxNDKr0yysRy/dKzDP3BTChADunzJlxAOygDMJkQANlAGmMCk+CDI0KiV\nBYzGh9zEOmcDRPCEjEwlI3IACtARkmzB1JBRs9AN3KDN2mzJZQDOJRQGNmAH\nDSuiyhCYL2jGKIzKCMxmdwCFRMDIb9xo07y8V1y/14wXVxADIA3QWRDEBF0t\nBi0CAOwKgDkCmmjGpzy+anwPvbjIJ//gyBitvLNswRmVVewQ0iL9yyVt0PVA\nAIsLBfVJytK4zuXQzknADIZoiIVABNEsx8vWvN/6vJRmU6vw0T4tsyWtOvxn\nA+EABQCgpID8gqh5lQ6dxGR4yIrgi78o01MdyVY9sJ+QCd+ARlmVzT490F8N\nMTEQ1gwQDiGwPh260i2dzJ3Yu8eAO/fw2BVwD408w7UAEv9mqyubQBe1Q/98\nCCA9A38NMSLAf4JtAyFw2Gnd0Il9wmKotm0Q10o5j41svFQtc/M7CwmU1/ZU\nC559CLrwC6FdLSFA2sR9pB5anw4dvlUZDyE5j/SINKBb2RRx2ZldHUxyFxwQ\nA70d3NUCBa7/QtyljdrIvdZj6AFKGQ/oTY84YA8PnCb3ON11PQv0dN0QgA1X\noAuH4Fvc7SkIwABcC97hfdiIvdrgSwnOrd72QAkGDsHSnRDD57wS0g4NcAVb\ncN1bkAKHcAh+vd95cL3+DeABPp+pjcybeAnojQMobg8JTgmqQAlSrAjSHb8q\nOwvT0QDocOMTQAJ6UARk4M+HANr77SnY6+Egrn/tdKTjHY2LkOIqruCq8OR2\n8MYk6ScqSyiGQAI3fuNRsOVRMAEKcAjAHeT+cARD/t8g3k5HLuJHLQMMYA/r\nreAsbhv48QCUYD8NDnmSR+MF0At/YARGoOXoEAW8QAscMARhHNwh/1DmHm7m\nxZ3mxw2Y1rDicY4ft/EAlp4tlS3LkndD3ODnfp7lW14EW7AHYu4pg9C6Zc5/\njE7a+4fkad3iTy7nlW4KtC4N9hAAU47nR1IAwtAMno4Of77labQHrVDqYWC9\nis61qx7i83kIsU7plk7rppAI1G4K0UCSDp4JbgAdJNAMvv7pOL4YViAPpe4P\n+pvsy87qrT6ftQHtiUPr1K4M+9EC9nDnlOYDg+EDf+Dt3/7n6EALi0EL+VDu\nD4DsqI69ql7kjo4F7r4IpiAN8T7vjdAIdmDv74DvPsAN/O7tv14EiUECUQAC\npV4G+ovsqf7hAH6a1jDr8E7tLaAbE+8FMv//3n6S79MwBDuw7xzv6e2gGBMQ\nBadQ6gSABQ5AAA4gAodg8kOe8GduCu8O8S7/8jHfH5/HDiWRDH6QA9hwK4PB\nDfbyBLRAAtPxDbaw5X0g5mlwCXzsMwgABUdw8Aif7ocg7fEu9VP/eUPwCmDw\nAzPxA+TgBxgQ+BBgMpUjKNQR6FEwB6WuDJdw6AAQuMnO9KQNI3UP8x0DQHoP\nBmBABnuxEH4f+KAP+LitPNNRDFq+DCN/CSQt3Psb+fyXBZU/8ZevA5mv+Zqf\nAz/AED+gBeQA+r4f+DkAAShTBKAu8kFOAOFQDQV97oqu6o0g8TFP+7Vv+5Ug\nC9+q+1PQ+7//+1n/DwFF4O/osAFiDgB4DNT+UPDWC/lljgV23zF5b/vwXwny\njw3f+hE/kP1TsP36/wxNABBNeEVBp87fQYQJFS5k2NBOjGoEwvxKSOASFowZ\nscDgyHFIo0ZehrwCU9JkyUopK8nKlIkHP379+P2YMoUcBpw5deZ8RohQE6Cn\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n",
                    "filename": "rails_logo.gif",
                    "metafields": [
                      {
                        "key": "new",
                        "namespace": "global",
                        "value": "newvalue",
                        "value_type": "string"
                      }
                    ],
                    "position": 1
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new product image with included image data as attachment / Create a new product image and make it the main image / Create a new product image using a source URL that will be downloaded by Shopify / Create a new product image and attach it to product variants / <span id="metafield">Create a new product image with a metafield</span>

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        request_body = {
            'image': image,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_acount_of_all_product_images(self, api_version, product_id, since_id=None) -> dict[str, Any]:
        """
        Retrieves the count of product images associated with a specific product using the GET method, optionally filtering by a since_id parameter.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            since_id (string): Restrict results to after the specified ID

        Returns:
            dict[str, Any]: Get a count all product images / Get a count of all product images after a specified ID

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images/count.json"
        query_params = {k: v for k, v in [('since_id', since_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_product_image(self, api_version, product_id, image_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific product image by ID with optional field selection for the API version.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            image_id (string): image_id
            fields (string): comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Show product image

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_product_image(self, api_version, product_id, image_id, image=None) -> dict[str, Any]:
        """
        Updates an existing product image specified by the product ID and image ID using the PUT method, allowing for modifications to image attributes such as source or metadata.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            image_id (string): image_id
            image (object): image
                Example:
                ```json
                {
                  "image": {
                    "id": 850703190,
                    "variant_ids": [
                      808950810,
                      457924702
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Modify an image; add a metafield / Modify an image; change its position and alt tag content / Modify an image; add it to product variants

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'")
        request_body = {
            'image': image,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_product_image(self, api_version, product_id, image_id) -> dict[str, Any]:
        """
        Deletes a specific product image identified by the `image_id` from a product specified by the `product_id` using the HTTP DELETE method.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            image_id (string): image_id

        Returns:
            dict[str, Any]: Delete a product image

        Tags:
            Products, Product Image
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        if image_id is None:
            raise ValueError("Missing required parameter 'image_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_product_variants(self, api_version, product_id, limit=None, presentment_currencies=None, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of product variants for a specified product with optional pagination, currency display, and field filtering.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            limit (string): Return up to this many results per page(default: 50)(maximum: 250)
            presentment_currencies (string): Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217][1] currency codes. [1]:
            since_id (string): Restrict results to after the specified ID
            fields (string): A comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Retrieve all variants for a product / Retrieve all variants for a product with prices in specified presentment currencies / Retrieve all variants for a product after a specified ID

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/variants.json"
        query_params = {k: v for k, v in [('limit', limit), ('presentment_currencies', presentment_currencies), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_product_variant(self, api_version, product_id, variant=None) -> dict[str, Any]:
        """
        Creates a new product variant within a specified product using the POST method, returning a successful response when the variant is added.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            variant (object): variant
                Example:
                ```json
                {
                  "variant": {
                    "option1": "Yellow",
                    "price": "1.00"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new product variant with an image / Create a new product variant with a metafield / Create a new product variant

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        request_body = {
            'variant': variant,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/variants.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_acount_of_all_product_variants(self, api_version, product_id) -> dict[str, Any]:
        """
        Retrieves the count of variants for a specific product in Shopify's inventory.

        Args:
            api_version (string): api_version
            product_id (string): product_id

        Returns:
            dict[str, Any]: Retrieve a count all variants for a product

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/variants/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_product_variant(self, api_version, variant_id, fields=None) -> dict[str, Any]:
        """
        Retrieves variant details using the specified API version and variant ID, optionally filtering by specified fields.

        Args:
            api_version (string): api_version
            variant_id (string): variant_id
            fields (string): A comma-separated list of fields to include in the response

        Returns:
            dict[str, Any]: Retrieve a product variant by ID

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if variant_id is None:
            raise ValueError("Missing required parameter 'variant_id'")
        url = f"{self.base_url}/admin/api/{api_version}/variants/{variant_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_product_variant(self, api_version, variant_id, variant=None) -> dict[str, Any]:
        """
        Updates the variant with the specified ID in the API, replacing its current state with the data provided in the request body.

        Args:
            api_version (string): api_version
            variant_id (string): variant_id
            variant (object): variant
                Example:
                ```json
                {
                  "variant": {
                    "id": 808950810,
                    "option1": "Not Pink",
                    "price": "99.00"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Add a metafield to an existing variant / Add an existing image to an existing variant / Update the title and price of an existing variant

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if variant_id is None:
            raise ValueError("Missing required parameter 'variant_id'")
        request_body = {
            'variant': variant,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/variants/{variant_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_product_variant(self, api_version, product_id, variant_id) -> dict[str, Any]:
        """
        Deletes a product variant using the Shopify Admin API.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            variant_id (string): variant_id

        Returns:
            dict[str, Any]: Delete a product variant

        Tags:
            Products, Product Variant
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        if variant_id is None:
            raise ValueError("Missing required parameter 'variant_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}/variants/{variant_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_products(self, api_version, ids=None, limit=None, since_id=None, title=None, vendor=None, handle=None, product_type=None, collection_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None, fields=None, presentment_currencies=None) -> dict[str, Any]:
        """
        Retrieves a list of products from a Shopify store using the Admin API, allowing for filtering based on parameters such as product IDs, title, vendor, and creation or publication dates.

        Args:
            api_version (string): api_version
            ids (string): Return only products specified by a comma-separated list of product IDs.
            limit (string): Return up to this many results per page.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            title (string): Filter results by product title.
            vendor (string): Filter results by product vendor.
            handle (string): Filter results by product handle.
            product_type (string): Filter results by product type.
            collection_id (string): Filter results by product collection ID.
            created_at_min (string): Show products created after date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show products created before date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show products last updated after date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show products last updated before date. (format: 2014-04-25T16:15:47-04:00)
            published_at_min (string): Show products published after date. (format: 2014-04-25T16:15:47-04:00)
            published_at_max (string): Show products published before date. (format: 2014-04-25T16:15:47-04:00)
            published_status (string): Return products by their published status(default: any)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.
            presentment_currencies (string): Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217][1] currency codes. [1]:

        Returns:
            dict[str, Any]: Retrieve all products, showing only some attributes / Retrieve all products with prices in selected presentment currencies / Retrieve all products that belong to a certain collection / Retrieve all products / Retrieve all products after the specified ID / Retrieve a list of specific products.

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/products.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit), ('since_id', since_id), ('title', title), ('vendor', vendor), ('handle', handle), ('product_type', product_type), ('collection_id', collection_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields), ('presentment_currencies', presentment_currencies)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_product(self, api_version, product=None) -> dict[str, Any]:
        """
        Creates a new product in Shopify via the REST Admin API and returns the product details upon successful creation.

        Args:
            api_version (string): api_version
            product (object): product
                Example:
                ```json
                {
                  "product": {
                    "body_html": "<strong>Good snowboard!</strong>",
                    "product_type": "Snowboard",
                    "published": false,
                    "title": "Burton Custom Freestyle 151",
                    "vendor": "Burton"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new product with multiple product variants and multiple options / Create a new product with multiple product variants / Create a new product with the default variant and base64 encoded image / Create a product with a metafield / Create a new product with the default product variant / Create a new product with the default variant and a product image that will be downloaded by Shopify / Create a new unpublished product

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'product': product,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/products.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_products(self, api_version, vendor=None, product_type=None, collection_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves the count of products in a Shopify store using the specified API version, allowing optional filtering by vendor, product type, collection ID, creation date, update date, publication date, and publication status.

        Args:
            api_version (string): api_version
            vendor (string): Filter results by product vendor.
            product_type (string): Filter results by product type.
            collection_id (string): Filter results by collection ID.
            created_at_min (string): Show products created after date. (format: 2014-04-25T16:15:47-04:00)
            created_at_max (string): Show products created before date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_min (string): Show products last updated after date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show products last updated before date. (format: 2014-04-25T16:15:47-04:00)
            published_at_min (string): Show products published after date. (format: 2014-04-25T16:15:47-04:00)
            published_at_max (string): Show products published before date. (format: 2014-04-25T16:15:47-04:00)
            published_status (string): Return products by their published status(default: any)

        Returns:
            dict[str, Any]: Retrieve a count of all products of a given collection / Retrieve a count of all products

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/products/count.json"
        query_params = {k: v for k, v in [('vendor', vendor), ('product_type', product_type), ('collection_id', collection_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_product(self, api_version, product_id, fields=None) -> dict[str, Any]:
        """
        Retrieves product details in JSON format for a specified product using the "GET" method, allowing optional filtering by specifying fields via query parameters.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve only particular fields / Retrieve a single product by ID

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_aproduct(self, api_version, product_id, product=None) -> dict[str, Any]:
        """
        Replaces an entire product entry in the admin system with a new version, returning a success status upon completion.

        Args:
            api_version (string): api_version
            product_id (string): product_id
            product (object): product
                Example:
                ```json
                {
                  "product": {
                    "id": 632910392,
                    "tags": "Barnes & Noble, John's Fav"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Add a metafield to an existing product / Update a product by adding a new product image / Update a product by reordering product image / Update a product's title / Update a product by clearing product images / Hide a published product by changing the published attribute to false / Update a product's SEO title and description / Update a product and one of its variants / Update a product by reordering the product variants / Show a hidden product by changing the published attribute to true / Update a product's tags

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        request_body = {
            'product': product,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_aproduct(self, api_version, product_id) -> dict[str, Any]:
        """
        Deletes a product along with its associated variants and media from the system using the provided product ID.

        Args:
            api_version (string): api_version
            product_id (string): product_id

        Returns:
            dict[str, Any]: Delete a product along with all its variants and images

        Tags:
            Products, Product
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_id is None:
            raise ValueError("Missing required parameter 'product_id'")
        url = f"{self.base_url}/admin/api/{api_version}/products/{product_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_smart_collections(self, api_version, limit=None, ids=None, since_id=None, title=None, product_id=None, handle=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of smart collections from a Shopify store, allowing for filtering by various parameters such as IDs, titles, product IDs, and publication status.

        Args:
            api_version (string): api_version
            limit (string): The number of results to show.(default: 50)(maximum: 250)
            ids (string): Show only the smart collections specified by a comma-separated list of IDs.
            since_id (string): Restrict results to after the specified ID.
            title (string): Show smart collections with the specified title.
            product_id (string): Show smart collections that includes the specified product.
            handle (string): Filter results by smart collection handle.
            updated_at_min (string): Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00)
            published_at_min (string): Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00)
            published_at_max (string): Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00)
            published_status (string): Filter results based on the published status of smart collections.(default: any)
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a list of all smart collections for a certain product_id / Retrieve a list of specific smart collections / Retrieve a list of all smart collections / Retrieve a list all smart collections after a specified ID

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections.json"
        query_params = {k: v for k, v in [('limit', limit), ('ids', ids), ('since_id', since_id), ('title', title), ('product_id', product_id), ('handle', handle), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_asmart_collection(self, api_version, smart_collection=None) -> dict[str, Any]:
        """
        Creates a new Shopify smart collection with automated product inclusion rules and returns the collection details upon successful creation.

        Args:
            api_version (string): api_version
            smart_collection (object): smart_collection
                Example:
                ```json
                {
                  "smart_collection": {
                    "published": false,
                    "rules": [
                      {
                        "column": "vendor",
                        "condition": "Apple",
                        "relation": "equals"
                      }
                    ],
                    "title": "Macbooks"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a new smart collection with a base64 encoded image / Create a smart collection of all products starting with the specified term / Create a smart collection with a specified title / Create a new smart collection with an image that will be downloaded by Shopify / Create a new unpublished smart collection

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'smart_collection': smart_collection,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_smart_collections(self, api_version, title=None, product_id=None, updated_at_min=None, updated_at_max=None, published_at_min=None, published_at_max=None, published_status=None) -> dict[str, Any]:
        """
        Retrieves a count of smart collections in a Shopify store, optionally filtered by title, product ID, update or publication dates, and publication status.

        Args:
            api_version (string): api_version
            title (string): Show smart collections with the specified title.
            product_id (string): Show smart collections that include the specified product.
            updated_at_min (string): Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00)
            updated_at_max (string): Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00)
            published_at_min (string): Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00)
            published_at_max (string): Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00)
            published_status (string): Filter results based on the published status of smart collections.(default: any)

        Returns:
            dict[str, Any]: Retrieve a count of all smart collections for a certain product_id / Retrieve a count of all smart collections

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections/count.json"
        query_params = {k: v for k, v in [('title', title), ('product_id', product_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_smart_collection(self, api_version, smart_collection_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a smart collection by its ID using the Shopify API, optionally specifying fields to include in the response.

        Args:
            api_version (string): api_version
            smart_collection_id (string): smart_collection_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a specific collection by ID

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if smart_collection_id is None:
            raise ValueError("Missing required parameter 'smart_collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_smart_collection(self, api_version, smart_collection_id, smart_collection=None) -> dict[str, Any]:
        """
        Updates a specific smart collection's configuration and rules via the Shopify Admin API, returning a success status on completion.

        Args:
            api_version (string): api_version
            smart_collection_id (string): smart_collection_id
            smart_collection (object): smart_collection
                Example:
                ```json
                {
                  "smart_collection": {
                    "id": 482865238,
                    "image": {
                      "alt": "Rails logo",
                      "attachment": "R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\nU7Mq2Mq1K9cUW8GKTUG2rNkUHNByWMuWLdWva7t1W7UKG4S7eO/ycEhQHgaK\nsL4VGGyocGE3br5929KuxQFFkEtIlgypsuUDmDMfWGRmUZvPoEHfGU36jgDT\nLQSoVt3IQ2sPsL0IUNZGlZ0H0lo00jEkCytWMspdGzBgn/F9EBIWnKIQlqHB\nhA0bQpx48Z7UAkoEcMTdUeTJJSxf/4akOTNnzqHb3GkjrUdp0gKwq77jWdod\nO7dNKWvhRUcWT6zYQI82xB03AAQNCdTKX/xAAB10hfVCnRtbVIhIAy14oJoZ\nAXS4XXfdQaYIeOGJRx555Z1nRnrqqUeaMtIYY8dmn7Vg2yK57TYEgAzIQGBx\nxyXHj0A0OOTggxFKSN1iWwTTAIYanpYdMtFE4+GVIHrn3XeUmVhZeWiIMoOY\nnVQDGiTgKALJjIssIsADt0mjjI6+AXcDgQYi2M8/7ijEwzRIFmBIL9NVV+EW\nVzyZ4Wqj9RBABchQWeWkV3aY5ZYjjgieeKL446mnjxwAiZVpliAjZqblt19/\n/7HCwIAFGv+X3J4s9fMckoYhphiTQTwJ5Wqn9dDDAWuMUUEFviTrS6STVlmp\npVmKqCkOn34aB6TIBAAOJeHZAYl6ptixSCL8edGbq8HFeqBDcygEyIOCGqYk\nkxUW4euiq7knbA/gUDHGv//ec2wFayQbaQWinOCslVhmSUq1/gCDLJXacgtJ\nCYu4J66cjbAKoA3CxapnOgm9g+ughdK7xYX3Rinlvj2YYcYanVBBhTg2Axzw\nG4/4k4bBzDZbKRUQP1LIsRSX6sgBZtwhzQP68ccbj7AWty4/5igEoaC9dK3r\noVtgs4evvzKqb8wyQ0JFJzXXbDMVcQBQLTDGVmCssstKGs09oPT/jQcRoBw9\nMamKgEOeeg/gqBtvdVZSDnHFIQgRD4RxXWhiYEOQKNn4zncHzDIzHc0ZpHdy\nRicIQOypKDf7q3Pd96ABzSab+E1EIYIvS2o0ijA92gPZiCB1qwL+iJxL78Z7\n2NeHQrAK2YrCZva+bcgcujFUQIEG6WigonoCdLT9tr9UbIIAMMCEkkYacvvT\nxSgsBPKGJKBEAw4yjhx+hyn+PAJFfztyVdWOt5B3RehyimneFuwFvQxFyTSf\n25f1zCAqSFACDXTQ3gwSoDoElI5tZyBAINqnuhJ+Kg9vOIOaVnSHT5ECHucK\n0OMiBxJAPCdXmGseBLoBvei5rFEStB5m/yBhjFJUIw50oIMoLvCpFRAADduj\nwxvUYMIqmvARCBiDeiwRBk+lQQTEq5qQ3CWdJSkGAlu4y9h66EBgAbF6QhSV\nMUpQilKcQRNLwIenfpFEJebBioC0ohrQQJ8QhMIfSwhgj2YouYTYUEmGqhBe\nFNBDH5otgmgLnRyLWMdq0GEGCMCHJjSBjzQE8pSChMLTCJBI4pXDBeuiiA1T\nprK7PK+SUPphsIQ1wSEag5OUKIUlyiAmAowClci0YizKILUAFi+WDQEEJOmF\nxlnMYnOVbOP0gkjBTdZRmDiwhCuywcRkmtOEpHjC1DzBABto4xqN5AcgdEXN\nNO4Ql0+CB2xctv9LM2SSgpXhZB0t0QlT+iMUkzinQquFihD452P0gGdGAPGN\nHKYxjbOAwBpxqU9+ApGXQgyoQDWRgASwoAMGMMAHDrnQhc5AkQPSU0NgYVF7\nQmAWKcBnPvc5HwGcbUVxJCInEfACQXQACUhFQkqRwAIOttScv9ABO21wA8k1\np5Z3mYXYdNqAjvLzbHDUpFCNIQoUdGAdHUhrUg2gVAOg4AXmvEAaOPEGaCCA\nAASQxBtIYYIq5kEHAaKHVfsRGB3eNBPYxKdXGVWGUnAzdOSxgyg+MIxhoDWt\nal3rUlXABEBeYBQIiMMm0AAKPBBAE1A4nTjWEIAzvGEFqsvDEHqEjZj/wMKw\n1rwlVxerGkv4AxVoAOkEmXGMOKDgA8i1LFrRioSjKrWtKRVEQlXHBBSKQhLQ\nEG3tCHCLJaSWClD0zgHO8LBqDeIYNsDGTG4ryZtak4G7lZ6G2sBSfyCAaTK7\nAzfgQIEzoOC/yKVsZS+bWeim1BsdqEG10oCANxDgDZwIRHa3O4hbaA91nlKB\nKA7QBhHo0VPwCFBtAdNea86CZVztKk8FUN5PjQIHxKWABihQBkHY+L/HTa5l\nMetcAxvAG94wQAQAkA1SIIAUBvUHdkVLgBkMwrvkPSEkVtSCJ/yCAJ5gZ20l\nwgObziITGk3xTqUHhWoxYQVdAIYINMBmO0TA/8aCwHGOBbwOAvc4pXj2RieY\nIY69ttgfpJBEHOLQ5ArTAQ2SaPAb4lAC33XsoaxYhUx4kFVrZoKSYlYxbOzg\nPX8kAM1d6AILOuEDDQzBBCaIwJvhjOMAU7bOmE0qdMUhhFozQhVxiMWnuiAJ\nQTfZyahFQydWGwA1cbiZAJL0Qiht6UzoVsxetUQaJhEKZzhDBdh+A5s9AQxU\nq3rVN241ne0sa1rXWgjbqLUd3uqPUYhCFNDAxwzm3d3vjgF/vTvAHegUaYbw\nwMSZyAR8oX0I2BwiC2eoQQ2srYJA6IDNb2ABqr39bVYDWMfkRgIVzs1xdEOD\nCjhQ4nXlPe9BaOLQNf+rRjQc0eg2DM8TyvZTs3mY6Xwy4xI2YLMGdIAAhTvD\nFWzuhKhZIHGKq9riF381rDtQho53/Bjpboc1OiEJktMbtaplrbHboCOYT9rS\nOdhopocwgiRowOw6L0MNCKCBKjwA26IW9cRTXfE4i1vAlpUEHJze8XTXehvc\n2AQ05k3vDHaiDGNYeaPNoAzGxbwf/86EHDCd4kbsyBMySII2NH92nevg4TbI\nA7ZVEGqiF93ocLb7nIdhgGMIoROW4Dvft2GHOqQiDoM3+YWJnT8O7yYL3fgI\nDwK+CrFX0lwBctUxtLH55qNd5xkYxMKvDffSn/7b4L47JYQgjnW0XvZOv0L/\nKmz/BS5sIg5QvtkavDPlO/Am+FzOBCBqgU8veEJA9LCBDRjQznIw3/lJEIBs\n5gqhUIALN3rWR3QTh31IFwcUkAiV1QEOCH4ddw8LkAqpUH5cgAtnIGzikHgs\nxzSW1w3+Jgc0Bz32Rw8DoA3lQA8yIAP6xwoj4H//B4BJYAOjoAZqYIDWRn0J\nuIB1Z3fHQAGdgHeJQIEcxwwLQH5csIHEQARE4C9aRx49oAPw5ydyIHaANUPE\nwXwtmH/6Vw5iKIb/F4DaoAGisAIroIM7WG0MR3pDd3qoJwjVQAEUAAdvEGAG\nsHcUgITFgAtLmIFNiAtQeAInMAa+UGwiyAEW8QMc//AkgKUNx7EPkLOCLOiC\nNiADIzCDY0iDm2cHLxCKbNiGPueDcVh02McJ/GWHjfABxyUJdigEfUiB+pAL\ndVAHX1B+uPCERHAChSAw8QAOHMaIE6EF3MAKkjiJxlGJljgC+UcPm7iJnch8\nDJAHoRiKaqiDBRgK01d9LDB0QFiHdmiH1YACSDCE4ziLsscIdRCIGriLhfiL\naxAPOKAKtbARPFAFQKKMywg5XuiC9ACN0TiNOwAAAHCNL5CN2siN3QiHcYhq\nwCAD6WiHomAJEzmO4LcGueCOG4gLf2OIAjOPOHCPEEFT/KiMzKgNLigDABmN\nnKgL02aQB3mNCkmKB+iNCv+IBjI2Y+O4ihcZi063DcywkReYi04Yj/ewBmuA\nAyRYEbAAAVVwkv3oj9rwgizJks4okCMwCI+ACqgwCQaJkGq4hm3IjW8YakPn\nCWxmhzz5kxfJd3iwkUx4lL0ojw/QlAnxlG4glQYCOStplS8YkJuoCwnwCIY5\nCYgZljRJlqTYg9WnbTq3lm3plrGojrVWixuJgRpIDB95AgLTCCRYkjeVAXw5\nlfqXiVa5ks64QSVlmF8JljO5mAtplj4IdJE5YzpHmenYcXCwAHKJi7rIi74Y\nD7oQms1xU71QmpQ4AOVwmvoHmAH5ABcwna3pmompmAnJmDzIcGp5m2upmxMp\ni+f/Zg9AIJeCeJSG+ACHAH8OwWyzoJyUCIOnCYOAKQP4wATTeQElVZio8AiI\nCZtiSZbbuHAIUAXemZu5CZ4YyQ250KAXeJ6c2YsCYIUYwWyZUADK6QoEwAfO\nOZ8yoANSwAT4SZ37eZjXGZtjOZshoAFQ8HAHOo6TCZ5CgAfluYS4OIhPGA8C\n4AXBtxBP+WXvWZrZ4ClhYAkdmokzgAkhKqIjqp+GaaIyGaAL+XDOEAEueqC4\nGaNuKQTWAAQ1OpceCQktcAgcYFuHJQc+wJfhADFpsAPhcJpewAZKKgVL2qTV\n2ZUnKptqMApJ8ADVZqVYKpkKaodwEAflaYvAuYFE4HIe/8CIEWGhchCkJ7kE\nJQQAHGoDZcYGckqnTGqnhWmiALqYS5AEdGCAVmqgBvqiMqagquANX3qe8cCo\njpqX1iQHsAALaWogx5FkEBMO7URCmjqnTJqfJQql2LkClpAEwNCGahABapmq\nqqqgjAAE3uCgTFgC6tEIZVoRzCYHckBpJ+kBJoQA+xcCqrOpdeqpT/qf2JkF\nSQAPOdiGLoqq0QqeVOCqDUp+RMBh+7atDgELX+atPJCPKOkAJmQJ7fRH54oJ\nc7qk+amfn+qfsAkAKqB5SeAFo7CGwBCo3smWlMkMQPaqyAAJi2AaKTBpECB5\nUdFlKJk6qoMK/McHVsSwdFqnxP9aUv3JrgRghhcbCCswqp0XmdAamTtJmXHg\nqjWaCmqCIwJwsg/RrSvLA6R5HDIAAyJAAJ3mKQQAAwxwC4Akp8Iqog9bna+5\nA2V4g+kUgM/HZlUwtB2rparwYzWKB/nzAG3QtBVaq1HxA5+wl8cBA1iABTCg\nCyGgsK7Af1lrReiariTKn6ggAmTIfDfIAJuntt7pth2bjnAABHKbC74ADi13\nByfLrQG7sp/AA8dBD4EruIILAy0ABboAA66ATMHKqcMKsZ/aCNMouWrbu2vb\nthw7kdUgt3VgP41WsinwEPzwb7NgqzzwA3xrCMYBuKu7ujBwvTBAAOYEtrbr\nqQkwg5z/GLmVa7GWy7EJmo7ccGB4gAxp8i3SMLoNEXnOywOf8AmwsA/aUL3V\ni726QELJtLi3W1ICWQ7SGLm+67tCi6UeSwGb8GOFkC1L+74uAbAq+7z1Sw0F\nwACXcAmBy8H6O7sLxb22O52k4IwD2Yk0SL69a763KWOJgAQLACnFBgl267Qy\nV8H0+wnUgAEb3MMbrL/a+1SaWrNMSgpYqZUEPIY1qMICyMJtCQSB4wv2czjw\nC3mla8E6nAzcEA4+jAU/HLiJG8IAbMRW6ZLgq8S8e8BOPGM4cDtSDLqboQD4\neMV8m8VXkAV47MMeDMJP9SmLiw82oAOpicThm8IHXL6BSgEn/4AHhbAsaRLH\nMSG/e3vBjojHWRADeowFg9DHEMO9DmADDjAK1ZCaLknAhZzGaoyl3IALXHAC\nMry0cjwR8juwz0sN1OBs3HDJlpwFl8DLvMrJnqKpUADKIUoKD1DGpVzAZ3vI\nWKoIxNDKr0yysRy/dKzDP3BTChADunzJlxAOygDMJkQANlAGmMCk+CDI0KiV\nBYzGh9zEOmcDRPCEjEwlI3IACtARkmzB1JBRs9AN3KDN2mzJZQDOJRQGNmAH\nDSuiyhCYL2jGKIzKCMxmdwCFRMDIb9xo07y8V1y/14wXVxADIA3QWRDEBF0t\nBi0CAOwKgDkCmmjGpzy+anwPvbjIJ//gyBitvLNswRmVVewQ0iL9yyVt0PVA\nAIsLBfVJytK4zuXQzknADIZoiIVABNEsx8vWvN/6vJRmU6vw0T4tsyWtOvxn\nA+EABQCgpID8gqh5lQ6dxGR4yIrgi78o01MdyVY9sJ+QCd+ARlmVzT490F8N\nMTEQ1gwQDiGwPh260i2dzJ3Yu8eAO/fw2BVwD408w7UAEv9mqyubQBe1Q/98\nCCA9A38NMSLAf4JtAyFw2Gnd0Il9wmKotm0Q10o5j41svFQtc/M7CwmU1/ZU\nC559CLrwC6FdLSFA2sR9pB5anw4dvlUZDyE5j/SINKBb2RRx2ZldHUxyFxwQ\nA70d3NUCBa7/QtyljdrIvdZj6AFKGQ/oTY84YA8PnCb3ON11PQv0dN0QgA1X\noAuH4Fvc7SkIwABcC97hfdiIvdrgSwnOrd72QAkGDsHSnRDD57wS0g4NcAVb\ncN1bkAKHcAh+vd95cL3+DeABPp+pjcybeAnojQMobg8JTgmqQAlSrAjSHb8q\nOwvT0QDocOMTQAJ6UARk4M+HANr77SnY6+Egrn/tdKTjHY2LkOIqruCq8OR2\n8MYk6ScqSyiGQAI3fuNRsOVRMAEKcAjAHeT+cARD/t8g3k5HLuJHLQMMYA/r\nreAsbhv48QCUYD8NDnmSR+MF0At/YARGoOXoEAW8QAscMARhHNwh/1DmHm7m\nxZ3mxw2Y1rDicY4ft/EAlp4tlS3LkndD3ODnfp7lW14EW7AHYu4pg9C6Zc5/\njE7a+4fkad3iTy7nlW4KtC4N9hAAU47nR1IAwtAMno4Of77labQHrVDqYWC9\nis61qx7i83kIsU7plk7rppAI1G4K0UCSDp4JbgAdJNAMvv7pOL4YViAPpe4P\n+pvsy87qrT6ftQHtiUPr1K4M+9EC9nDnlOYDg+EDf+Dt3/7n6EALi0EL+VDu\nD4DsqI69ql7kjo4F7r4IpiAN8T7vjdAIdmDv74DvPsAN/O7tv14EiUECUQAC\npV4G+ovsqf7hAH6a1jDr8E7tLaAbE+8FMv//3n6S79MwBDuw7xzv6e2gGBMQ\nBadQ6gSABQ5AAA4gAodg8kOe8GduCu8O8S7/8jHfH5/HDiWRDH6QA9hwK4PB\nDfbyBLRAAtPxDbaw5X0g5mlwCXzsMwgABUdw8Aif7ocg7fEu9VP/eUPwCmDw\nAzPxA+TgBxgQ+BBgMpUjKNQR6FEwB6WuDJdw6AAQuMnO9KQNI3UP8x0DQHoP\nBmBABnuxEH4f+KAP+LitPNNRDFq+DCN/CSQt3Psb+fyXBZU/8ZevA5mv+Zqf\nAz/AED+gBeQA+r4f+DkAAShTBKAu8kFOAOFQDQV97oqu6o0g8TFP+7Vv+5Ug\nC9+q+1PQ+7//+1n/DwFF4O/osAFiDgB4DNT+UPDWC/lljgV23zF5b/vwXwny\njw3f+hE/kP1TsP36/wxNABBNeEVBp87fQYQJFS5k2NBOjGoEwvxKSOASFowZ\nscDgyHFIo0ZehrwCU9JkyUopK8nKlIkHP379+P2YMoUcBpw5deZ8RohQE6Cn\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n"
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the description of a smart collection / Hide a published smart collection / Update a smart collection by setting a new collection image alternative text / Update a smart collection by clearing the collection image / Publish a hidden collection / Update a smart collection by setting a new collection image

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if smart_collection_id is None:
            raise ValueError("Missing required parameter 'smart_collection_id'")
        request_body = {
            'smart_collection': smart_collection,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_asmart_collection(self, api_version, smart_collection_id) -> dict[str, Any]:
        """
        Deletes the specified smart collection and returns a successful response upon completion.

        Args:
            api_version (string): api_version
            smart_collection_id (string): smart_collection_id

        Returns:
            dict[str, Any]: Remove a smart collection

        Tags:
            Products, SmartCollection
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if smart_collection_id is None:
            raise ValueError("Missing required parameter 'smart_collection_id'")
        url = f"{self.base_url}/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acheckout(self, api_version, token) -> dict[str, Any]:
        """
        Checks the status of a checkout using a provided token via the GET method.

        Args:
            api_version (string): api_version
            token (string): token

        Returns:
            dict[str, Any]: Retrieve a completed checkout

        Tags:
            Sales channels, Checkout
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modifies_an_existing_checkout(self, api_version, token, checkout=None) -> dict[str, Any]:
        """
        Updates a checkout using the provided token, supporting HTTP responses for successful updates (200), successful processing without immediate completion (202), and invalid request data (422).

        Args:
            api_version (string): api_version
            token (string): token
            checkout (object): checkout
                Example:
                ```json
                {
                  "checkout": {
                    "shipping_address": {
                      "address1": "126 York St.",
                      "city": "Beverly Hills",
                      "country_code": "US",
                      "first_name": "John",
                      "last_name": "Smith",
                      "phone": "(123)456-7890",
                      "province_code": "CA",
                      "zip": "1234"
                    },
                    "token": "exuw7apwoycchjuwtiqg8nytfhphr62a"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Select a shipping rate

        Tags:
            Sales channels, Checkout
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        request_body = {
            'checkout': checkout,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_shipping_rates(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves shipping rates for a specified checkout token via the API, returning available options in JSON format.

        Args:
            api_version (string): api_version
            token (string): token

        Returns:
            dict[str, Any]: Retrieve available shipping rates / Retrieving shipping rates when none are available for the current shipping address or cart returns an empty array

        Tags:
            Sales channels, Checkout
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}/shipping_rates.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_collection_listings_that_are_published_to_your_app(self, api_version, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of collection listings in JSON format using the "GET" method, optionally limited by a specified number of entries.

        Args:
            api_version (string): api_version
            limit (string): Amount of results(default: 50)(maximum: 1000)

        Returns:
            dict[str, Any]: Retrieve collection listings that are published to your app

        Tags:
            Sales channels, CollectionListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/collection_listings.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code(self, api_version, collection_listing_id, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of product IDs for a specified collection listing, optionally limited by a query parameter, using the GET method.

        Args:
            api_version (string): api_version
            collection_listing_id (string): collection_listing_id
            limit (string): Amount of results(default: 50)(maximum: 1000)

        Returns:
            dict[str, Any]: Retrieve <code>product_ids</code> that are published to a <code>collection_id</code>

        Tags:
            Sales channels, CollectionListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_listing_id is None:
            raise ValueError("Missing required parameter 'collection_listing_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collection_listings/{collection_listing_id}/product_ids.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_aspecific_collection_listing_that_is_published_to_your_app(self, api_version, collection_listing_id) -> dict[str, Any]:
        """
        Retrieves details of a specific collection listing in the admin API.

        Args:
            api_version (string): api_version
            collection_listing_id (string): collection_listing_id

        Returns:
            dict[str, Any]: Retrieve a specific collection listing that is published to your app

        Tags:
            Sales channels, CollectionListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_listing_id is None:
            raise ValueError("Missing required parameter 'collection_listing_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_acollection_listing_to_publish_acollection_to_your_app(self, api_version, collection_listing_id, collection_listing=None) -> dict[str, Any]:
        """
        Updates the specified collection listing resource by replacing its entire representation at the specified ID, returning a success response upon completion.

        Args:
            api_version (string): api_version
            collection_listing_id (string): collection_listing_id
            collection_listing (object): collection_listing
                Example:
                ```json
                {
                  "collection_listing": {
                    "collection_id": 482865238
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a collection listing to publish a collection to your app

        Tags:
            Sales channels, CollectionListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_listing_id is None:
            raise ValueError("Missing required parameter 'collection_listing_id'")
        request_body = {
            'collection_listing': collection_listing,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_acollection_listing_to_unpublish_acollection_from_your_app(self, api_version, collection_listing_id) -> Any:
        """
        Deletes a collection listing with the specified ID using the DELETE method.

        Args:
            api_version (string): api_version
            collection_listing_id (string): collection_listing_id

        Returns:
            Any: Delete a collection listing to unpublish a collection from your app

        Tags:
            Sales channels, CollectionListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if collection_listing_id is None:
            raise ValueError("Missing required parameter 'collection_listing_id'")
        url = f"{self.base_url}/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def stores_acredit_card_in_the_card_vault(self, credit_card=None) -> dict[str, Any]:
        """
        Creates a new user session using the Shopify API at the specified path, enabling secure interactions between the client and server.

        Args:
            credit_card (object): credit_card
                Example:
                ```json
                {
                  "credit_card": {
                    "first_name": "John",
                    "last_name": "Smith",
                    "month": "5",
                    "number": "1",
                    "verification_value": "123",
                    "year": "15"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a payment session with the specified billing details.

        Tags:
            Sales channels, Payment
        """
        request_body = {
            'credit_card': credit_card,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/https:/elb.deposit.shopifycs.com/sessions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_payments_on_aparticular_checkout(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves payment details from a specific checkout session using the provided token, returning relevant payment information in JSON format.

        Args:
            api_version (string): api_version
            token (string): token

        Returns:
            dict[str, Any]: Retrieve all the payments on a checkout

        Tags:
            Sales channels, Payment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}/payments.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_anew_payment(self, api_version, token, payment=None) -> dict[str, Any]:
        """
        Creates a payment for a checkout session using the provided token, returning a status response upon completion.

        Args:
            api_version (string): api_version
            token (string): token
            payment (object): payment
                Example:
                ```json
                {
                  "payment": {
                    "amount": "430.48",
                    "request_details": {
                      "accept_language": "en-US,en;q=0.8,fr;q=0.6",
                      "ip_address": "123.1.1.1",
                      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                    },
                    "session_id": "global-an_invalid_session_id",
                    "unique_token": "client-side-idempotency-token"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create an authorization using a valid <code>session_id</code> stored in the vault

        Tags:
            Sales channels, Payment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        request_body = {
            'payment': payment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}/payments.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_payment(self, api_version, token, payment_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific payment associated with a checkout using the Checkout.com API.

        Args:
            api_version (string): api_version
            token (string): token
            payment_id (string): payment_id

        Returns:
            dict[str, Any]: Retrieve a payment with a succesful transaction / Retrieve a payment with a failed transaction

        Tags:
            Sales channels, Payment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        if payment_id is None:
            raise ValueError("Missing required parameter 'payment_id'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}/payments/{payment_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def counts_the_number_of_payments_attempted_on_acheckout(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves the count of payments for a specified checkout using the "GET" method, returning the result in JSON format.

        Args:
            api_version (string): api_version
            token (string): token

        Returns:
            dict[str, Any]: Retrieve the number of payments on a checkout

        Tags:
            Sales channels, Payment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if token is None:
            raise ValueError("Missing required parameter 'token'")
        url = f"{self.base_url}/admin/api/{api_version}/checkouts/{token}/payments/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_product_listings_that_are_published_to_your_app(self, api_version, product_ids=None, limit=None, page=None, collection_id=None, updated_at_min=None, handle=None) -> dict[str, Any]:
        """
        Retrieves a list of product listings with filtering options such as product identifiers, collection, update timestamps, and handles.

        Args:
            api_version (string): api_version
            product_ids (string): A comma-separated list of product ids
            limit (string): Amount of results(default: 50)(maximum: 1000)
            page (string): Page to show(default: 1)
            collection_id (string): Filter by products belonging to a particular collection
            updated_at_min (string): Filter by products last updated after a certain date and time (formatted in ISO 8601)
            handle (string): Filter by product handle

        Returns:
            dict[str, Any]: Retrieve product listings that are published to your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/product_listings.json"
        query_params = {k: v for k, v in [('product_ids', product_ids), ('limit', limit), ('page', page), ('collection_id', collection_id), ('updated_at_min', updated_at_min), ('handle', handle)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_code_product_ids_code_that_are_published_to_your_app(self, api_version, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of product IDs from product listings with optional limit parameter.

        Args:
            api_version (string): api_version
            limit (string): Amount of results(default: 50)(maximum: 1000)

        Returns:
            dict[str, Any]: Retrieve <code>product_ids</code> that are published to your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/product_listings/product_ids.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_acount_of_products_that_are_published_to_your_app(self, api_version) -> dict[str, Any]:
        """
        Retrieves the total count of product listings available in the system.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a count of products that are published to your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/product_listings/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_aspecific_product_listing_that_is_published_to_your_app(self, api_version, product_listing_id) -> dict[str, Any]:
        """
        Retrieves a specific product listing by ID using the GET method, returning details about the product listing.

        Args:
            api_version (string): api_version
            product_listing_id (string): product_listing_id

        Returns:
            dict[str, Any]: Retrieve a specific product listing that is published to your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_listing_id is None:
            raise ValueError("Missing required parameter 'product_listing_id'")
        url = f"{self.base_url}/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproduct_listing_to_publish_aproduct_to_your_app(self, api_version, product_listing_id, product_listing=None) -> dict[str, Any]:
        """
        Updates a product listing by fully replacing its data at the specified path, using the PUT method.

        Args:
            api_version (string): api_version
            product_listing_id (string): product_listing_id
            product_listing (object): product_listing
                Example:
                ```json
                {
                  "product_listing": {
                    "product_id": 921728736
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a product listing to publish a product to your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_listing_id is None:
            raise ValueError("Missing required parameter 'product_listing_id'")
        request_body = {
            'product_listing': product_listing,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproduct_listing_to_unpublish_aproduct_from_your_app(self, api_version, product_listing_id) -> Any:
        """
        Deletes a specific product listing by ID using the specified API version.

        Args:
            api_version (string): api_version
            product_listing_id (string): product_listing_id

        Returns:
            Any: Delete a product listing to unpublish a product from your app

        Tags:
            Sales channels, ProductListing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if product_listing_id is None:
            raise ValueError("Missing required parameter 'product_listing_id'")
        url = f"{self.base_url}/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_alist_of_all_resourcefeedbacks(self, api_version) -> dict[str, Any]:
        """
        Retrieves feedback data for a specific resource via the Admin API.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Get a list of resource feedback records for a specific shop

        Tags:
            Sales channels, ResourceFeedback
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/resource_feedback.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_resourcefeedback(self, api_version, resource_feedback=None) -> dict[str, Any]:
        """
        Submits resource feedback for review and processing, returning status codes for success, conflicts, or validation errors.

        Args:
            api_version (string): api_version
            resource_feedback (object): resource_feedback
                Example:
                ```json
                {
                  "resource_feedback": {
                    "feedback_generated_at": "2020-01-14T15:44:54.744363Z",
                    "state": "success"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a shop feedback record indicating the Shop is usable by your app / Create a shop feedback record indicating a problem specific to your app

        Tags:
            Sales channels, ResourceFeedback
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'resource_feedback': resource_feedback,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/resource_feedback.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app(self, api_version, assignment_status=None, location_ids=None) -> dict[str, Any]:
        """
        Retrieves fulfillment orders assigned to specific locations and filtered by assignment status using query parameters.

        Args:
            api_version (string): api_version
            assignment_status (string): The assigment status of the fulfillment orders that should be returned:
            location_ids (string): The IDs of the assigned locations of the fulfillment orders that should be returned.

        Returns:
            dict[str, Any]: Retrieve a list of fulfillment orders in cancellation_requested state at a location for an app

        Tags:
            Shipping and fulfillment, AssignedFulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/assigned_fulfillment_orders.json"
        query_params = {k: v for k, v in [('assignment_status', assignment_status), ('location_ids', location_ids)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def sends_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request=None) -> dict[str, Any]:
        """
        Sends a cancellation request to the fulfillment service for a specific fulfillment order, allowing the cancellation process to be initiated.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            cancellation_request (object): cancellation_request
                Example:
                ```json
                {
                  "cancellation_request": {
                    "message": "The customer changed his mind."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Sends a cancellation request to the fulfillment service of a fulfillment order and updates the fulfillment order

        Tags:
            Shipping and fulfillment, CancellationRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'cancellation_request': cancellation_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def accepts_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request=None) -> dict[str, Any]:
        """
        Accepts a cancellation request for a fulfillment order via a POST request to the specified endpoint.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            cancellation_request (object): cancellation_request
                Example:
                ```json
                {
                  "cancellation_request": {
                    "message": "We had not started any processing yet."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Accepts a cancellation request sent to a fulfillment service and updates the fulfillment order

        Tags:
            Shipping and fulfillment, CancellationRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'cancellation_request': cancellation_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request/accept.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def rejects_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request=None) -> dict[str, Any]:
        """
        Rejects a cancellation request for a Shopify fulfillment order and returns the updated fulfillment order details.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            cancellation_request (object): cancellation_request
                Example:
                ```json
                {
                  "cancellation_request": {
                    "message": "We have already send the shipment out."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Rejects a cancellation request sent to a fulfillment service and updates the fulfillment order

        Tags:
            Shipping and fulfillment, CancellationRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'cancellation_request': cancellation_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request/reject.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_carrier_services(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of carrier services from a Shopify store, providing access to shipping options and real-time shipping rates for integration with third-party shipping providers.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of carrier services

        Tags:
            Shipping and fulfillment, CarrierService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/carrier_services.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acarrier_service(self, api_version, carrier_service=None) -> dict[str, Any]:
        """
        Creates a custom carrier service in Shopify, enabling third-party shipping rate integration via a callback URL.

        Args:
            api_version (string): api_version
            carrier_service (object): carrier_service
                Example:
                ```json
                {
                  "carrier_service": {
                    "callback_url": "http://shippingrateprovider.com",
                    "name": "Shipping Rate Provider",
                    "service_discovery": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a carrier service

        Tags:
            Shipping and fulfillment, CarrierService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'carrier_service': carrier_service,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/carrier_services.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_carrier_service(self, api_version, carrier_service_id) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific carrier service configured to provide real-time shipping rates via Shopify's shipping API.

        Args:
            api_version (string): api_version
            carrier_service_id (string): carrier_service_id

        Returns:
            dict[str, Any]: Retrieve a single carrier service

        Tags:
            Shipping and fulfillment, CarrierService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if carrier_service_id is None:
            raise ValueError("Missing required parameter 'carrier_service_id'")
        url = f"{self.base_url}/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_acarrier_service(self, api_version, carrier_service_id, carrier_service=None) -> dict[str, Any]:
        """
        Updates a specific carrier service with the provided ID using the "PUT" method in the Shopify API.

        Args:
            api_version (string): api_version
            carrier_service_id (string): carrier_service_id
            carrier_service (object): carrier_service
                Example:
                ```json
                {
                  "carrier_service": {
                    "active": false,
                    "id": 1036894957,
                    "name": "Some new name"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a carrier service

        Tags:
            Shipping and fulfillment, CarrierService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if carrier_service_id is None:
            raise ValueError("Missing required parameter 'carrier_service_id'")
        request_body = {
            'carrier_service': carrier_service,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_acarrier_service(self, api_version, carrier_service_id) -> dict[str, Any]:
        """
        Deletes an existing carrier service by ID and returns a success status upon completion.

        Args:
            api_version (string): api_version
            carrier_service_id (string): carrier_service_id

        Returns:
            dict[str, Any]: Delete a carrier service

        Tags:
            Shipping and fulfillment, CarrierService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if carrier_service_id is None:
            raise ValueError("Missing required parameter 'carrier_service_id'")
        url = f"{self.base_url}/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_fulfillments_associated_with_an_order(self, api_version, order_id, created_at_max=None, created_at_min=None, fields=None, limit=None, since_id=None, updated_at_max=None, updated_at_min=None) -> dict[str, Any]:
        """
        Retrieves a list of fulfillments for a specific order with optional filtering by creation/update timestamps and pagination parameters.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            created_at_max (string): Show fulfillments created before date (format: 2014-04-25T16:15:47-04:00).
            created_at_min (string): Show fulfillments created after date (format: 2014-04-25T16:15:47-04:00).
            fields (string): A comma-separated list of fields to include in the response.
            limit (string): Limit the amount of results.(default: 50)(maximum: 250)
            since_id (string): Restrict results to after the specified ID.
            updated_at_max (string): Show fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Show fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00).

        Returns:
            dict[str, Any]: Retrieve a list of all fulfillments for an order / Retrieve all fulfillments after the specified ID

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments.json"
        query_params = {k: v for k, v in [('created_at_max', created_at_max), ('created_at_min', created_at_min), ('fields', fields), ('limit', limit), ('since_id', since_id), ('updated_at_max', updated_at_max), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_fulfillment(self, api_version, order_id, fulfillment=None) -> dict[str, Any]:
        """
        Creates a new fulfillment for an order, typically used to confirm shipment or pickup of items to complete the order process.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment (object): fulfillment
                Example:
                ```json
                {
                  "fulfillment": {
                    "line_items": [
                      {
                        "id": 466157049
                      },
                      {
                        "id": 518995019
                      },
                      {
                        "id": 703073504
                      }
                    ],
                    "location_id": 905684977,
                    "tracking_company": "fed ex",
                    "tracking_number": "123456789010"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Partially fulfill a single line item by specifying a line item and quantity to be fulfilled / Fulfill all line items for an order with multiple tracking numbers / Fulfill all line items for an order and send the shipping confirmation email. Not specifying line item IDs causes all unfulfilled and partially fulfilled line items for the order to be fulfilled. / Fulfill line items without a tracking number / Fulfill a single line item by explicitly specifying the line items to be fulfilled / Fulfill all line items for an order and use a custom tracking URL and company / Fulfill an order using a supported tracking company (generates tracking URL) / Fulfill an order using a supported tracking company in an incorrect format and custom tracking URL (respects sent URL) / Fulfill an order using only a tracking number and a custom tracking URL (respects tracking URL but attempts to generate tracking company if number matches recognizable pattern) / Fulfill an order using a non-supported tracking company without a tracking URL. Does not generate a URL if tracking number does not match a recognizable pattern. / Fulfill an order using a non-supported tracking company without a tracking URL (generates best guess URL if number matches recognizable pattern) / Fulfill an order using a supported tracking company in an incorrect format (uses fuzzy matches to generate tracking URL, but respects tracking company supplied)

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        request_body = {
            'fulfillment': fulfillment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_fulfillments_associated_with_afulfillment_order(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves fulfillment information for a specific fulfillment order by its ID using the Shopify API.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id

        Returns:
            dict[str, Any]: Retrieve a list of all fulfillments for a fulfillment order

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillments.json"
        query_params = {k: v for k, v in [('fulfillment_order_id', fulfillment_order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_fulfillments_associated_with_aspecific_order(self, api_version, order_id, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None) -> dict[str, Any]:
        """
        Retrieves the count of fulfillments for a specific order based on optional date filters for creation and update times using the GET method.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            created_at_min (string): Count fulfillments created after date (format: 2014-04-25T16:15:47-04:00).
            created_at_max (string): Count fulfillments created before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min (string): Count fulfillments last updated after date (format: 2014-04-25T16:15:47-04:00).
            updated_at_max (string): Count fulfillments last updated before date (format: 2014-04-25T16:15:47-04:00).

        Returns:
            dict[str, Any]: Count the total number of fulfillments for an order

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_fulfillment(self, api_version, order_id, fulfillment_id, fields=None) -> dict[str, Any]:
        """
        Retrieves a specific fulfillment for an order using the Shopify Admin API, returning fulfillment details in the response.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id
            fields (string): Comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve a specific fulfillment

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_fulfillment(self, api_version, order_id, fulfillment_id, fulfillment=None) -> dict[str, Any]:
        """
        Updates a specific fulfillment order in Shopify's admin API for order processing.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id
            fulfillment (object): fulfillment
                Example:
                ```json
                {
                  "fulfillment": {
                    "id": 255858046,
                    "tracking_number": "987654321"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the tracking number for a fulfillment

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        request_body = {
            'fulfillment': fulfillment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_afulfillment_for_one_or_many_fulfillment_orders(self, api_version, fulfillment=None) -> dict[str, Any]:
        """
        Creates a new fulfillment record for an order using the Shopify API, allowing for the inclusion of details such as tracking numbers and shipment status updates.

        Args:
            api_version (string): api_version
            fulfillment (object): fulfillment
                Example:
                ```json
                {
                  "fulfillment": {
                    "line_items_by_fulfillment_order": [
                      {
                        "fulfillment_order_id": 1025578621
                      }
                    ],
                    "message": "The package was shipped this morning.",
                    "notify_customer": false,
                    "tracking_info": {
                      "company": "my-shipping-company",
                      "number": 1562678,
                      "url": "https://www.my-shipping-company.com"
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a fulfillment for the fulfillment order line items specified / Creates a fulfillment for all fulfillment order line items if `fulfillment_order_line_items` is left blank

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'fulfillment': fulfillment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillments.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_the_tracking_information_for_afulfillment(self, api_version, fulfillment_id, fulfillment=None) -> dict[str, Any]:
        """
        Updates tracking information for a fulfillment using the provided tracking details via a POST request.

        Args:
            api_version (string): api_version
            fulfillment_id (string): fulfillment_id
            fulfillment (object): fulfillment
                Example:
                ```json
                {
                  "fulfillment": {
                    "notify_customer": true,
                    "tracking_info": {
                      "company": "my-company",
                      "number": "1111",
                      "url": "http://www.my-url.com"
                    }
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update the tracking information for a fulfillment

        Tags:
            Shipping and fulfillment, Fulfillment
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        request_body = {
            'fulfillment': fulfillment,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillments/{fulfillment_id}/update_tracking.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment(self, api_version, order_id, fulfillment_id) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment events associated with a specific fulfillment ID within an order using the Shopify API.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id

        Returns:
            dict[str, Any]: Retrieve a list of all the fulfillment events that are associated with a specific fulfillment

        Tags:
            Shipping and fulfillment, FulfillmentEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events.json"
        query_params = {k: v for k, v in [('fulfillment_id', fulfillment_id), ('order_id', order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_afulfillment_event(self, api_version, order_id, fulfillment_id, event=None) -> dict[str, Any]:
        """
        Creates a new fulfillment event for a specified order and fulfillment, allowing tracking and updating of the fulfillment status.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id
            event (object): event
                Example:
                ```json
                {
                  "event": {
                    "status": "in_transit"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a fulfillment event

        Tags:
            Shipping and fulfillment, FulfillmentEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        request_body = {
            'event': event,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_fulfillment_event(self, api_version, order_id, fulfillment_id, event_id) -> dict[str, Any]:
        """
        Retrieves a specific event by ID for a fulfillment within an order using the "GET" method.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id
            event_id (string): event_id

        Returns:
            dict[str, Any]: Retrieve a specific fulfillment event

        Tags:
            Shipping and fulfillment, FulfillmentEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json"
        query_params = {k: v for k, v in [('event_id', event_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_afulfillment_event(self, api_version, order_id, fulfillment_id, event_id) -> dict[str, Any]:
        """
        Deletes a specific fulfillment event associated with a fulfillment in an order using the Shopify API, removing its tracking information.

        Args:
            api_version (string): api_version
            order_id (string): order_id
            fulfillment_id (string): fulfillment_id
            event_id (string): event_id

        Returns:
            dict[str, Any]: Delete a fulfillment event

        Tags:
            Shipping and fulfillment, FulfillmentEvent
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        if fulfillment_id is None:
            raise ValueError("Missing required parameter 'fulfillment_id'")
        if event_id is None:
            raise ValueError("Missing required parameter 'event_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_fulfillment_orders_for_aspecific_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment orders associated with a specific order, including fulfillment details and status.

        Args:
            api_version (string): api_version
            order_id (string): order_id

        Returns:
            dict[str, Any]: Retrieve a list of all fulfillment orders for an order

        Tags:
            Shipping and fulfillment, FulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if order_id is None:
            raise ValueError("Missing required parameter 'order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/orders/{order_id}/fulfillment_orders.json"
        query_params = {k: v for k, v in [('order_id', order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_fulfillment_order(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific fulfillment order in Shopify, including its status and associated order items.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id

        Returns:
            dict[str, Any]: Get a single fulfillment order by its ID

        Tags:
            Shipping and fulfillment, FulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancel_afulfillment_order(self, api_version, fulfillment_order_id, fulfillment_order=None) -> dict[str, Any]:
        """
        Cancels a fulfillment order using the "POST" method at the specified endpoint, allowing for the termination of fulfillment attempts for the associated order.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_order (object): fulfillment_order
                Example:
                ```json
                {
                  "fulfillment_order": {
                    "assigned_location": {
                      "address1": null,
                      "address2": null,
                      "city": null,
                      "country_code": "DE",
                      "location_id": 48752903,
                      "name": "Apple Api Shipwire",
                      "phone": null,
                      "province": null,
                      "zip": null
                    },
                    "assigned_location_id": 48752903,
                    "destination": {
                      "address1": "Chestnut Street 92",
                      "address2": "",
                      "city": "Louisville",
                      "company": null,
                      "country": "United States",
                      "email": "bob.norman@hostmail.com",
                      "first_name": "Bob",
                      "id": 1025578634,
                      "last_name": "Norman",
                      "phone": "555-625-1199",
                      "province": "Kentucky",
                      "zip": "40202"
                    },
                    "fulfillment_service_handle": "mars-fulfillment",
                    "id": 1025578640,
                    "line_items": [
                      {
                        "fulfillable_quantity": 1,
                        "fulfillment_order_id": 1025578640,
                        "id": 1025578653,
                        "inventory_item_id": 49148385,
                        "line_item_id": 518995019,
                        "quantity": 1,
                        "shop_id": 690933842,
                        "variant_id": 49148385
                      }
                    ],
                    "merchant_requests": [],
                    "order_id": 450789469,
                    "request_status": "submitted",
                    "shop_id": 690933842,
                    "status": "open",
                    "supported_actions": [
                      "cancel_fulfillment_order"
                    ]
                  }
                }
                ```

        Returns:
            dict[str, Any]: Cancel a fulfillment order

        Tags:
            Shipping and fulfillment, FulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_order': fulfillment_order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancel.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def marks_afulfillment_order_as_incomplete(self, api_version, fulfillment_order_id, fulfillment_order=None) -> dict[str, Any]:
        """
        Closes a fulfillment order via the Shopify Admin API and returns a success status upon completion.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_order (object): fulfillment_order
                Example:
                ```json
                {
                  "fulfillment_order": {
                    "message": "Not enough inventory to complete this work."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Transition a fulfillment order from in progress to incomplete

        Tags:
            Shipping and fulfillment, FulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_order': fulfillment_order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/close.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def moves_afulfillment_order_to_anew_location(self, api_version, fulfillment_order_id, fulfillment_order=None) -> dict[str, Any]:
        """
        Moves fulfillment order line items to a new location and returns the updated fulfillment order details.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_order (object): fulfillment_order
                Example:
                ```json
                {
                  "fulfillment_order": {
                    "new_location_id": 905684977
                  }
                }
                ```

        Returns:
            dict[str, Any]: Move a fulfillment order to a new location

        Tags:
            Shipping and fulfillment, FulfillmentOrder
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_order': fulfillment_order,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/move.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sends_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request=None) -> dict[str, Any]:
        """
        Submits a fulfillment request for a specified fulfillment order, allowing for the management and processing of order line items through a fulfillment service.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_request (object): fulfillment_request
                Example:
                ```json
                {
                  "fulfillment_request": {
                    "message": "Fulfill this ASAP please."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Sends a fulfillment request to the fulfillment service of a fulfillment order for the specified line items / Sends a fulfillment request to the fulfillment service for all line items on the fulfillment order if fulfillment_order_line_items is left blank

        Tags:
            Shipping and fulfillment, FulfillmentRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_request': fulfillment_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def accepts_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request=None) -> dict[str, Any]:
        """
        Accepts a fulfillment request for a specific fulfillment order, transitioning the order status to processing.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_request (object): fulfillment_request
                Example:
                ```json
                {
                  "fulfillment_request": {
                    "message": "We will start processing your fulfillment on the next business day."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Accepts a fulfillment request sent to a fulfillment service and updates the fulfillment order

        Tags:
            Shipping and fulfillment, FulfillmentRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_request': fulfillment_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/accept.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def rejects_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request=None) -> dict[str, Any]:
        """
        Rejects a fulfillment request for a specified fulfillment order, preventing any associated line items from being fulfilled.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id
            fulfillment_request (object): fulfillment_request
                Example:
                ```json
                {
                  "fulfillment_request": {
                    "message": "Not enough inventory on hand to complete the work."
                  }
                }
                ```

        Returns:
            dict[str, Any]: Rejects a fulfillment request sent to a fulfillment service and updates the fulfillment order

        Tags:
            Shipping and fulfillment, FulfillmentRequest
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        request_body = {
            'fulfillment_request': fulfillment_request,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/reject.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_alist_of_all_fulfillmentservices(self, api_version, scope=None) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment services available to a merchant using the Shopify API.

        Args:
            api_version (string): api_version
            scope (string): Defines the specific actions or data access allowed for the fulfillment services API request, enabling control over what operations can be performed or what data can be accessed.

        Returns:
            dict[str, Any]: List your app's fulfillment services / List all of the shop's fulfillment services

        Tags:
            Shipping and fulfillment, FulfillmentService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_services.json"
        query_params = {k: v for k, v in [('scope', scope)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_anew_fulfillmentservice(self, api_version, fulfillment_service=None) -> dict[str, Any]:
        """
        Registers a new fulfillment service using the Shopify API, allowing third-party warehouses to prepare and ship orders on behalf of store owners.

        Args:
            api_version (string): api_version
            fulfillment_service (object): fulfillment_service
                Example:
                ```json
                {
                  "fulfillment_service": {
                    "callback_url": "http://google.com",
                    "format": "json",
                    "inventory_management": true,
                    "name": "Jupiter Fulfillment",
                    "requires_shipping_method": true,
                    "tracking_support": true
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a fulfillment service

        Tags:
            Shipping and fulfillment, FulfillmentService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'fulfillment_service': fulfillment_service,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_services.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_asingle_fulfillmentservice(self, api_version, fulfillment_service_id) -> dict[str, Any]:
        """
        Retrieves details of a specific fulfillment service, including its configuration and operational settings, within the Shopify admin API.

        Args:
            api_version (string): api_version
            fulfillment_service_id (string): fulfillment_service_id

        Returns:
            dict[str, Any]: Get a single fulfillment service by its ID

        Tags:
            Shipping and fulfillment, FulfillmentService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_service_id is None:
            raise ValueError("Missing required parameter 'fulfillment_service_id'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def modify_an_existing_fulfillmentservice(self, api_version, fulfillment_service_id, fulfillment_service=None) -> dict[str, Any]:
        """
        Updates a Shopify fulfillment service's configuration, including tracking support and inventory management settings.

        Args:
            api_version (string): api_version
            fulfillment_service_id (string): fulfillment_service_id
            fulfillment_service (object): fulfillment_service
                Example:
                ```json
                {
                  "fulfillment_service": {
                    "id": 755357713,
                    "name": "New Fulfillment Service Name"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a fulfillment service

        Tags:
            Shipping and fulfillment, FulfillmentService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_service_id is None:
            raise ValueError("Missing required parameter 'fulfillment_service_id'")
        request_body = {
            'fulfillment_service': fulfillment_service,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_fulfillmentservice(self, api_version, fulfillment_service_id) -> dict[str, Any]:
        """
        Deletes a specified fulfillment service from the Shopify admin and returns a success status upon removal.

        Args:
            api_version (string): api_version
            fulfillment_service_id (string): fulfillment_service_id

        Returns:
            dict[str, Any]: Destroy a fulfillment service

        Tags:
            Shipping and fulfillment, FulfillmentService
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_service_id is None:
            raise ValueError("Missing required parameter 'fulfillment_service_id'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves a list of eligible locations where fulfillment order items can be moved for potential fulfillment, sorted alphabetically by location name.

        Args:
            api_version (string): api_version
            fulfillment_order_id (string): fulfillment_order_id

        Returns:
            dict[str, Any]: Retrieve a list of locations that a fulfillment order can potentially move to.

        Tags:
            Shipping and fulfillment, LocationsForMove
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if fulfillment_order_id is None:
            raise ValueError("Missing required parameter 'fulfillment_order_id'")
        url = f"{self.base_url}/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/locations_for_move.json"
        query_params = {k: v for k, v in [('fulfillment_order_id', fulfillment_order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_the_current_balance(self, api_version) -> dict[str, Any]:
        """
        Retrieves the current account balance for Shopify Payments, reflecting transactions not yet included in a payout.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieves the account's current balance.

        Tags:
            Shopify Payments, Balance
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/balance.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_alist_of_all_disputes(self, api_version, since_id=None, last_id=None, status=None, initiated_at=None) -> dict[str, Any]:
        """
        Retrieves a list of Shopify Payments disputes based on specified parameters, such as ID, status, and initiation date, using the GET method at the "/admin/api/{api_version}/shopify_payments/disputes.json" endpoint.

        Args:
            api_version (string): api_version
            since_id (string): Return only disputes after the specified ID.
            last_id (string): Return only disputes before the specified ID.
            status (string): Return only disputes with the specified status.
            initiated_at (string): Return only disputes with the specified `initiated_at` date ([ISO 8601][1] format). [1]:

        Returns:
            dict[str, Any]: Retrieve all disputes ordered newest to oldest / Retrieve all won disputes / Retrieve all disputes initiated on 2013-05-03

        Tags:
            Shopify Payments, Dispute
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/disputes.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('status', status), ('initiated_at', initiated_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_asingle_dispute(self, api_version, dispute_id) -> dict[str, Any]:
        """
        Retrieves information about a specific dispute related to Shopify Payments using the provided dispute ID.

        Args:
            api_version (string): api_version
            dispute_id (string): dispute_id

        Returns:
            dict[str, Any]: Retrieves a single dispute by ID

        Tags:
            Shopify Payments, Dispute
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if dispute_id is None:
            raise ValueError("Missing required parameter 'dispute_id'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/disputes/{dispute_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_alist_of_all_payouts(self, api_version, since_id=None, last_id=None, date_min=None, date_max=None, date=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of Shopify Payments payouts, which represent the movement of money from a merchant's Shopify Payments balance to their bank account, based on specified parameters like date range and payout status.

        Args:
            api_version (string): api_version
            since_id (string): Filter response to payouts exclusively after the specified ID.
            last_id (string): Filter response to payouts exclusively before the specified ID
            date_min (string): Filter response to payouts inclusively after the specified date.
            date_max (string): Filter response to payouts inclusively before the specified date.
            date (string): Filter response to payouts on the specified date.
            status (string): Filter response to payouts with the specified status

        Returns:
            dict[str, Any]: List all payouts up to a specific date / List all payouts ordered newest to oldest

        Tags:
            Shopify Payments, Payouts
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/payouts.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('date_min', date_min), ('date_max', date_max), ('date', date), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_asingle_payout(self, api_version, payout_id) -> dict[str, Any]:
        """
        Retrieves details of a specific Shopify Payments payout using the payout ID and API version.

        Args:
            api_version (string): api_version
            payout_id (string): payout_id

        Returns:
            dict[str, Any]: Retrieves a single payout by id.

        Tags:
            Shopify Payments, Payouts
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if payout_id is None:
            raise ValueError("Missing required parameter 'payout_id'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/payouts/{payout_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def return_alist_of_all_balance_transactions(self, api_version, since_id=None, last_id=None, test=None, payout_id=None, payout_status=None) -> dict[str, Any]:
        """
        Retrieves Shopify Payments balance transactions associated with payouts, filtered by parameters like payout ID, status, or test mode.

        Args:
            api_version (string): api_version
            since_id (string): Filter response to transactions exclusively after the specified ID.
            last_id (string): Filter response to transactions exclusively before the specified ID
            test (string): Filter response to transactions placed in test mode.
            payout_id (string): Filter response to transactions paid out in the specified payout.
            payout_status (string): Filter response to transactions with the specified payout status

        Returns:
            dict[str, Any]: List all transactions associated with a payout.

        Tags:
            Shopify Payments, Transactions
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/shopify_payments/balance/transactions.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('test', test), ('payout_id', payout_id), ('payout_status', payout_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def receive_alist_of_all_countries(self, api_version, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves country data based on specified parameters such as since_id and fields, returning details in JSON format.

        Args:
            api_version (string): api_version
            since_id (string): Restrict results to after the specified ID.
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve all countries after the specified ID / Retrieve all countries

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/countries.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def creates_acountry(self, api_version, country=None) -> dict[str, Any]:
        """
        Creates a new country entry via the Shopify Admin REST API and returns a success status upon creation.

        Args:
            api_version (string): api_version
            country (object): country
                Example:
                ```json
                {
                  "country": {
                    "code": "FR"
                  }
                }
                ```

        Returns:
            dict[str, Any]: Create a country using a custom tax rate  / Create a country using Shopify's tax rate for it

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        request_body = {
            'country': country,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/countries.json"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_countries(self, api_version) -> dict[str, Any]:
        """
        Retrieves country list data in JSON format using a GET request.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Count all countries

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_aspecific_county(self, api_version, country_id, fields=None) -> dict[str, Any]:
        """
        Retrieves country details by ID with optional field filtering.

        Args:
            api_version (string): api_version
            country_id (string): country_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a specific country by its ID

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_country(self, api_version, country_id, country=None) -> dict[str, Any]:
        """
        Updates or creates a country resource at a specified ID using the "PUT" method, allowing for full replacement or creation of the country data.

        Args:
            api_version (string): api_version
            country_id (string): country_id
            country (object): country
                Example:
                ```json
                {
                  "country": {
                    "id": 879921427,
                    "tax": 0.1
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a country's tax rate

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        request_body = {
            'country': country,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_an_existing_country(self, api_version, country_id) -> dict[str, Any]:
        """
        Deletes a specified country from the system using the DELETE method at the "/admin/api/{api_version}/countries/{country_id}.json" endpoint.

        Args:
            api_version (string): api_version
            country_id (string): country_id

        Returns:
            dict[str, Any]: Delete a country

        Tags:
            Store properties, Country
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_currencies_enabled_on_ashop(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of supported currencies with their metadata using the specified API version.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of currencies enabled on a shop

        Tags:
            Store properties, Currency
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/currencies.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_the_shop_spolicies(self, api_version) -> dict[str, Any]:
        """
        Retrieves policy configurations in JSON format from the specified API version path using a GET request.

        Args:
            api_version (string): api_version

        Returns:
            dict[str, Any]: Retrieve a list of the shop's policies

        Tags:
            Store properties, Policy
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/policies.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_provinces_for_acountry(self, api_version, country_id, since_id=None, fields=None) -> dict[str, Any]:
        """
        Retrieves a list of provinces for a specific country using query parameters like `since_id` and `fields` to filter or format the response.

        Args:
            api_version (string): api_version
            country_id (string): country_id
            since_id (string): Restrict results to after the specified ID.
            fields (string): Show only certain fields, specified by a comma-separated list of fields names.

        Returns:
            dict[str, Any]: Retrieve all provinces for a country / Retrieve all provinces for a country after the specified ID

        Tags:
            Store properties, Province
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}/provinces.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_acount_of_provinces_for_acountry(self, api_version, country_id) -> dict[str, Any]:
        """
        Retrieves the total count of provinces for a specified country using the GET method.

        Args:
            api_version (string): api_version
            country_id (string): country_id

        Returns:
            dict[str, Any]: Count all provinces

        Tags:
            Store properties, Province
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}/provinces/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_asingle_province_for_acountry(self, api_version, country_id, province_id, fields=None) -> dict[str, Any]:
        """
        Retrieves province details for a specific country using the specified API version and includes optional field selection.

        Args:
            api_version (string): api_version
            country_id (string): country_id
            province_id (string): province_id
            fields (string): Show only certain fields, specified by a comma-separated list of field names.

        Returns:
            dict[str, Any]: Retrieve a single province

        Tags:
            Store properties, Province
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        if province_id is None:
            raise ValueError("Missing required parameter 'province_id'")
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}/provinces/{province_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_an_existing_province_for_acountry(self, api_version, country_id, province_id, province=None) -> dict[str, Any]:
        """
        Updates a specific province's details for a given country via the Shopify Admin REST API and returns a success status upon completion.

        Args:
            api_version (string): api_version
            country_id (string): country_id
            province_id (string): province_id
            province (object): province
                Example:
                ```json
                {
                  "province": {
                    "id": 224293623,
                    "tax": 0.15
                  }
                }
                ```

        Returns:
            dict[str, Any]: Update a province's tax rate

        Tags:
            Store properties, Province
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        if country_id is None:
            raise ValueError("Missing required parameter 'country_id'")
        if province_id is None:
            raise ValueError("Missing required parameter 'province_id'")
        request_body = {
            'province': province,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/admin/api/{api_version}/countries/{country_id}/provinces/{province_id}.json"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_the_shop_sconfiguration(self, api_version, fields=None) -> dict[str, Any]:
        """
        Retrieves shop information in JSON format using the specified API version via the "GET" method at the "/admin/api/{api_version}/shop.json" endpoint, allowing optional specification of fields to include in the response.

        Args:
            api_version (string): api_version
            fields (string): A comma-separated list of fields to include in the response.

        Returns:
            dict[str, Any]: Retrieve the shop's configuration

        Tags:
            Store properties, Shop
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/shop.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieves_alist_of_tender_transactions(self, api_version, limit=None, since_id=None, processed_at_min=None, processed_at_max=None, processed_at=None, order=None) -> dict[str, Any]:
        """
        Retrieves a list of tender transactions with optional filtering by processing time, order, and pagination parameters.

        Args:
            api_version (string): api_version
            limit (string): The maximum number of results to retrieve.(default: 50)(maximum: 250)
            since_id (string): Retrieve only transactions after the specified ID.
            processed_at_min (string): Show tender transactions processed\_at or after the specified date.
            processed_at_max (string): Show tender transactions processed\_at or before the specified date.
            processed_at (string): Show tender transactions processed at the specified date.
            order (string): Show tender transactions ordered by processed\_at in ascending or descending order.

        Returns:
            dict[str, Any]: Retrieve tender transactions processed_at the specified date / Retrieve tender transactions after the specified ID / Retrieve tender transactions ordered by <code>processed_at</code> / Retrieve tender transactions processed_at or after the specified date / Retrieve all tender transactions / Retrieve tender transactions processed_at or before the specified date

        Tags:
            Tendertransaction, TenderTransaction
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api_version'")
        url = f"{self.base_url}/admin/api/{api_version}/tender_transactions.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('processed_at_min', processed_at_min), ('processed_at_max', processed_at_max), ('processed_at', processed_at), ('order', order)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.retrieves_alist_of_access_scopes_associated_to_the_access_token,
            self.retrieves_alist_of_storefront_access_tokens_that_have_been_issued,
            self.creates_anew_storefrontaccesstoken,
            self.deletes_an_existing_storefront_access_token,
            self.retrieves_alist_of_reports,
            self.creates_anew_report,
            self.retrieves_asingle_report,
            self.updates_areport,
            self.deletes_areport,
            self.retrieves_alist_of_application_charges,
            self.creates_an_application_charge,
            self.retrieves_an_application_charge,
            self.activates_an_application_charge,
            self.retrieves_all_application_credits,
            self.creates_an_application_credit,
            self.retrieves_asingle_application_credit,
            self.retrieves_alist_of_recurring_application_charges,
            self.creates_arecurring_application_charge,
            self.retrieves_asingle_charge,
            self.cancels_arecurring_application_charge,
            self.activates_arecurring_application_charge,
            self.retrieves_alist_of_usage_charges,
            self.creates_ausage_charge,
            self.retrieves_asingle_charge1,
            self.retrieves_alist_of_addresses_for_acustomer,
            self.creates_anew_address_for_acustomer,
            self.retrieves_details_for_asingle_customer_address,
            self.updates_an_existing_customer_address,
            self.removes_an_address_from_acustomer_saddress_list,
            self.retrieves_alist_of_customers,
            self.creates_acustomer,
            self.searches_for_customers_that_match_asupplied_query,
            self.retrieves_asingle_customer,
            self.updates_acustomer,
            self.deletes_acustomer,
            self.sends_an_account_invite_to_acustomer,
            self.retrieves_acount_of_customers,
            self.retrieves_all_orders_belonging_to_acustomer,
            self.retrieves_alist_of_customer_saved_searches,
            self.creates_acustomer_saved_search,
            self.retrieves_acount_of_all_customer_saved_searches,
            self.retrieves_asingle_customer_saved_search,
            self.updates_acustomer_saved_search,
            self.deletes_acustomer_saved_search,
            self.retrieves_all_customers_returned_by_acustomer_saved_search,
            self.retrieves_alist_of_discount_codes,
            self.creates_adiscount_code,
            self.retrieves_asingle_discount_code,
            self.updates_an_existing_discount_code,
            self.deletes_adiscount_code,
            self.retrieves_the_location_of_adiscount_code,
            self.creates_adiscount_code_creation_job,
            self.retrieves_adiscount_code_creation_job,
            self.retrieves_alist_of_discount_codes_for_adiscount_code_creation_job,
            self.retrieves_alist_of_price_rules,
            self.creates_aprice_rule,
            self.retrieves_asingle_price_rule,
            self.updates_an_existing_aprice_rule,
            self.remove_an_existing_pricerule,
            self.retrieves_acount_of_all_price_rules,
            self.retrieves_alist_of_events,
            self.retrieves_asingle_event,
            self.retrieves_acount_of_events,
            self.retrieves_alist_of_webhooks,
            self.create_anew_webhook,
            self.receive_acount_of_all_webhooks,
            self.receive_asingle_webhook,
            self.modify_an_existing_webhook,
            self.remove_an_existing_webhook,
            self.retrieves_alist_of_inventory_items,
            self.retrieves_asingle_inventory_item_by_id,
            self.updates_an_existing_inventory_item,
            self.retrieves_alist_of_inventory_levels,
            self.deletes_an_inventory_level_from_alocation,
            self.adjusts_the_inventory_level_of_an_inventory_item_at_alocation,
            self.connects_an_inventory_item_to_alocation,
            self.sets_the_inventory_level_for_an_inventory_item_at_alocation,
            self.retrieves_alist_of_locations,
            self.retrieves_asingle_location_by_its_id,
            self.retrieves_acount_of_locations,
            self.retrieves_alist_of_inventory_levels_for_alocation,
            self.retrieves_alist_of_all_marketing_events,
            self.creates_amarketing_event,
            self.retrieves_acount_of_all_marketing_events,
            self.retrieves_asingle_marketing_event,
            self.updates_amarketing_event,
            self.deletes_amarketing_event,
            self.creates_marketing_engagements_on_amarketing_event,
            self.retrieves_alist_of_metafields_that_belong_to_aresource,
            self.creates_anew_metafield_for_aresource,
            self.retrieves_acount_of_aresource_smetafields,
            self.retrieves_asingle_metafield_from_aresource_by_its_id,
            self.updates_ametafield,
            self.deletes_ametafield_by_its_id,
            self.retrieves_alist_of_all_articles_from_ablog,
            self.creates_an_article_for_ablog,
            self.retrieves_acount_of_all_articles_from_ablog,
            self.receive_asingle_article,
            self.updates_an_article,
            self.deletes_an_article,
            self.retrieves_alist_of_all_article_authors,
            self.retrieves_alist_of_all_article_tags,
            self.retrieves_alist_of_assets_for_atheme,
            self.creates_or_updates_an_asset_for_atheme,
            self.deletes_an_asset_from_atheme,
            self.retrieve_alist_of_all_blogs,
            self.create_anew_blog,
            self.receive_acount_of_all_blogs,
            self.receive_asingle_blog,
            self.modify_an_existing_blog,
            self.remove_an_existing_blog,
            self.retrieves_alist_of_comments,
            self.creates_acomment_for_an_article,
            self.retrieves_acount_of_comments,
            self.retrieves_asingle_comment_by_its_id,
            self.updates_acomment_of_an_article,
            self.retrieves_alist_of_pages,
            self.create_anew_page,
            self.retrieves_apage_count,
            self.retrieves_asingle_page_by_its_id,
            self.updates_apage,
            self.deletes_apage,
            self.retrieves_alist_of_url_redirects,
            self.creates_aredirect,
            self.retrieves_acount_of_url_redirects,
            self.retrieves_asingle_redirect,
            self.updates_an_existing_redirect,
            self.deletes_aredirect,
            self.retrieves_alist_of_all_script_tags,
            self.creates_anew_script_tag,
            self.retrieves_acount_of_all_script_tags,
            self.retrieves_asingle_script_tag,
            self.updates_ascript_tag,
            self.deletes_ascript_tag,
            self.retrieves_alist_of_themes,
            self.creates_atheme,
            self.retrieves_asingle_theme,
            self.modify_an_existing_theme,
            self.remove_an_existing_theme,
            self.retrieves_acount_of_checkouts,
            self.retrieves_alist_of_abandoned_checkouts,
            self.creates_acheckout,
            self.retrieves_alist_of_draft_orders,
            self.create_anew_draftorder,
            self.receive_asingle_draftorder,
            self.modify_an_existing_draftorder,
            self.remove_an_existing_draftorder,
            self.receive_acount_of_all_draftorders,
            self.send_an_invoice,
            self.retrieves_alist_of_all_order_risks_for_an_order,
            self.creates_an_order_risk_for_an_order,
            self.retrieves_asingle_order_risk_by_its_id,
            self.updates_an_order_risk,
            self.deletes_an_order_risk_for_an_order,
            self.retrieves_alist_of_orders,
            self.creates_an_order,
            self.retrieves_aspecific_order,
            self.updates_an_order,
            self.deletes_an_order,
            self.retrieves_an_order_count,
            self.cancels_an_order,
            self.retrieves_alist_of_refunds_for_an_order,
            self.creates_arefund,
            self.retrieves_aspecific_refund,
            self.calculates_arefund,
            self.retrieves_alist_of_transactions,
            self.creates_atransaction_for_an_order,
            self.retrieves_acount_of_an_order_stransactions,
            self.retrieves_aspecific_transaction,
            self.retrieves_alist_of_gift_cards,
            self.creates_agift_card,
            self.retrieves_asingle_gift_card,
            self.updates_an_existing_gift_card,
            self.retrieves_acount_of_gift_cards,
            self.disables_agift_card,
            self.searches_for_gift_cards,
            self.retrieves_alist_of_all_users,
            self.retrieves_asingle_user,
            self.retrieves_the_currently_logged_in_user,
            self.retrieves_alist_of_collects,
            self.adds_aproduct_to_acustom_collection,
            self.retrieves_aspecific_collect_by_its_id,
            self.removes_aproduct_from_acollection,
            self.retrieves_acount_of_collects,
            self.retrieves_asingle_collection,
            self.retrieve_alist_of_products_belonging_to_acollection,
            self.retrieves_alist_of_custom_collections,
            self.creates_acustom_collection,
            self.retrieves_acount_of_custom_collections,
            self.retrieves_asingle_custom_collection,
            self.updates_an_existing_custom_collection,
            self.deletes_acustom_collection,
            self.receive_alist_of_all_product_images,
            self.create_anew_product_image,
            self.receive_acount_of_all_product_images,
            self.receive_asingle_product_image,
            self.modify_an_existing_product_image,
            self.remove_an_existing_product_image,
            self.retrieves_alist_of_product_variants,
            self.create_anew_product_variant,
            self.receive_acount_of_all_product_variants,
            self.receive_asingle_product_variant,
            self.modify_an_existing_product_variant,
            self.remove_an_existing_product_variant,
            self.retrieves_alist_of_products,
            self.creates_anew_product,
            self.retrieves_acount_of_products,
            self.retrieves_asingle_product,
            self.updates_aproduct,
            self.deletes_aproduct,
            self.retrieves_alist_of_smart_collections,
            self.creates_asmart_collection,
            self.retrieves_acount_of_smart_collections,
            self.retrieves_asingle_smart_collection,
            self.updates_an_existing_smart_collection,
            self.removes_asmart_collection,
            self.retrieves_acheckout,
            self.modifies_an_existing_checkout,
            self.retrieves_alist_of_shipping_rates,
            self.retrieve_collection_listings_that_are_published_to_your_app,
            self.retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code,
            self.retrieve_aspecific_collection_listing_that_is_published_to_your_app,
            self.create_acollection_listing_to_publish_acollection_to_your_app,
            self.delete_acollection_listing_to_unpublish_acollection_from_your_app,
            self.stores_acredit_card_in_the_card_vault,
            self.retrieves_alist_of_payments_on_aparticular_checkout,
            self.creates_anew_payment,
            self.retrieves_asingle_payment,
            self.counts_the_number_of_payments_attempted_on_acheckout,
            self.retrieve_product_listings_that_are_published_to_your_app,
            self.retrieve_code_product_ids_code_that_are_published_to_your_app,
            self.retrieve_acount_of_products_that_are_published_to_your_app,
            self.retrieve_aspecific_product_listing_that_is_published_to_your_app,
            self.create_aproduct_listing_to_publish_aproduct_to_your_app,
            self.delete_aproduct_listing_to_unpublish_aproduct_from_your_app,
            self.receive_alist_of_all_resourcefeedbacks,
            self.create_anew_resourcefeedback,
            self.retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app,
            self.sends_acancellation_request,
            self.accepts_acancellation_request,
            self.rejects_acancellation_request,
            self.retrieves_alist_of_carrier_services,
            self.creates_acarrier_service,
            self.retrieves_asingle_carrier_service,
            self.updates_acarrier_service,
            self.deletes_acarrier_service,
            self.retrieves_fulfillments_associated_with_an_order,
            self.create_anew_fulfillment,
            self.retrieves_fulfillments_associated_with_afulfillment_order,
            self.retrieves_acount_of_fulfillments_associated_with_aspecific_order,
            self.receive_asingle_fulfillment,
            self.modify_an_existing_fulfillment,
            self.creates_afulfillment_for_one_or_many_fulfillment_orders,
            self.updates_the_tracking_information_for_afulfillment,
            self.retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment,
            self.creates_afulfillment_event,
            self.retrieves_aspecific_fulfillment_event,
            self.deletes_afulfillment_event,
            self.retrieves_alist_of_fulfillment_orders_for_aspecific_order,
            self.retrieves_aspecific_fulfillment_order,
            self.cancel_afulfillment_order,
            self.marks_afulfillment_order_as_incomplete,
            self.moves_afulfillment_order_to_anew_location,
            self.sends_afulfillment_request,
            self.accepts_afulfillment_request,
            self.rejects_afulfillment_request,
            self.receive_alist_of_all_fulfillmentservices,
            self.create_anew_fulfillmentservice,
            self.receive_asingle_fulfillmentservice,
            self.modify_an_existing_fulfillmentservice,
            self.remove_an_existing_fulfillmentservice,
            self.retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to,
            self.return_the_current_balance,
            self.return_alist_of_all_disputes,
            self.return_asingle_dispute,
            self.return_alist_of_all_payouts,
            self.return_asingle_payout,
            self.return_alist_of_all_balance_transactions,
            self.receive_alist_of_all_countries,
            self.creates_acountry,
            self.retrieves_acount_of_countries,
            self.retrieves_aspecific_county,
            self.updates_an_existing_country,
            self.remove_an_existing_country,
            self.retrieves_alist_of_currencies_enabled_on_ashop,
            self.retrieves_alist_of_the_shop_spolicies,
            self.retrieves_alist_of_provinces_for_acountry,
            self.retrieves_acount_of_provinces_for_acountry,
            self.retrieves_asingle_province_for_acountry,
            self.updates_an_existing_province_for_acountry,
            self.retrieves_the_shop_sconfiguration,
            self.retrieves_alist_of_tender_transactions
        ]
