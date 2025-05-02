import json 
from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class ShopifyApp(APIApplication):
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name='shopify', integration=integration, **kwargs)
        self.base_url = "https://{{store_name}}.myshopify.com"
        
    def retrieves_alist_of_access_scopes_associated_to_the_access_token(self) -> dict[str, Any]:
        """
        Retrieves access scopes associated with the current authentication token.
        
        Args:
            None: This function does not require parameters.
        
        Returns:
            Dictionary containing access scopes and associated metadata.
        
        Raises:
            HTTPError: If the API request fails, typically due to invalid authentication credentials or server errors.
        
        Tags:
            access-scopes, authentication, metadata, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/oauth/access_scopes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_storefront_access_tokens_that_have_been_issued(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of issued storefront access tokens.
        
        Args:
            None: This function accepts no parameters.
        
        Returns:
            A dictionary containing the list of storefront access tokens and related metadata.
        
        Raises:
            HTTPError: If the API request fails, including invalid responses or network issues.
        
        Tags:
            retrieve, list, access-tokens, storefront, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/storefront_access_tokens.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_storefrontaccesstoken(self, api_version, storefront_access_token: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new Storefront Access Token.
        
        Args:
            storefront_access_token: A dictionary containing the Storefront Access Token configuration details.
        
        Returns:
            A dictionary containing the newly created Storefront Access Token data.
        
        Raises:
            HTTPError: Raised if the API request fails, typically due to invalid input data or authentication issues.
        
        Tags:
            storefront-access-token, create, management, access, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'storefront_access_token': storefront_access_token,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/storefront_access_tokens.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_existing_storefront_access_token(self, api_version, storefront_access_token_id, request_body: Any | None = None) -> Any:
        """
        Deletes an existing storefront access token.
        
        Args:
            request_body: Optional request body. Defaults to None.
        
        Returns:
            The JSON response from the delete operation.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, storefront, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/storefront_access_tokens/{storefront_access_token_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_reports(self, api_version, ids: str | None = None, limit: str | None = None, since_id: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of reports based on the specified filters and parameters.
        
        Args:
            fields: A comma-separated list of fields to include in the response.
            ids: A comma-separated list of report IDs.
            limit: The amount of results to return (default: 50, maximum: 250)
            since_id: Restrict results to after the specified ID.
            updated_at_max: Show reports last updated before the specified date (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Show reports last updated after the specified date (format: 2014-04-25T16:15:47-04:00)
        
        Returns:
            A dictionary containing the list of reports.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, reports, api-query, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/reports.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit), ('since_id', since_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_report(self, api_version, report: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new report by sending a POST request with the provided report data to a specific URL.
        
        Args:
            report: Optional dictionary with report details; default is None.
        
        Returns:
            A dictionary representing the response from the server.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, report, analytics, http, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'report': report,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/reports.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_report(self, api_version, report_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single report from the application.
        
        Args:
            fields: A comma-separated list of fields to include in the response.
        
        Returns:
            A dictionary containing the details of the single report.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, report, important, analytics, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_areport(self, api_version, report_id, report: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing report by sending a PUT request to the API endpoint with the provided report data.
        
        Args:
            report: A dictionary containing the report data to be updated. Must include all required fields for the report type.
        
        Returns:
            A dictionary containing the updated report details from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid request data, authentication failures, or server errors (4xx/5xx responses).
        
        Tags:
            update, report, api, async-job, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'report': report,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_areport(self, api_version, report_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a report by making a DELETE request to the API endpoint.
        
        Args:
            request_body: Optional request payload for the delete operation (if applicable), formatted as JSON-compatible data. Defaults to None.
        
        Returns:
            Dictionary containing the API's JSON response data.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails (non-2xx status code received).
        
        Tags:
            delete, report, api, important, analytics
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/reports/{report_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_application_charges(self, api_version, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of application charges from the API, filtered by specified criteria.
        
        Args:
            fields: A comma-separated list of fields to include in the response.
            since_id: Restrict results to charges created after the specified ID.
        
        Returns:
            Dictionary containing the API response data with application charges.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with an HTTP error status code.
        
        Tags:
            retrieve, list, billing, application-charge, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_charges.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_application_charge(self, api_version, application_charge: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new application charge for billing purposes.
        
        Args:
            application_charge: Dictionary containing application charge details (e.g., name, price, test status). Required fields depend on the API implementation.
        
        Returns:
            Dictionary containing the created application charge data as returned by the API, including charge ID and status.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (e.g., invalid parameters, authentication errors, or server issues).
        
        Tags:
            billing, application-charge, api, create, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'application_charge': application_charge,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_charges.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_an_application_charge(self, api_version, application_charge_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves application charge details from the billing system.
        
        Args:
            fields: A comma-separated list of fields to include in the response (optional).
        
        Returns:
            Dictionary containing the application charge data as key-value pairs.
        
        Raises:
            HTTPError: If the GET request fails due to network issues or invalid response status.
        
        Tags:
            retrieve, billing, application-charge, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_charges/{application_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def activates_an_application_charge(self, api_version, application_charge_id, application_charge: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Activates an accepted application charge.
        
        Args:
            application_charge: Optional dictionary containing application charge details (default is None).
        
        Returns:
            A dictionary containing the activation result.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            activate, billing, application-charge, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'application_charge': application_charge,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_charges/{application_charge_id}/activate.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_all_application_credits(self, api_version, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves all application credits from the server.
        
        Args:
            fields: A comma-separated list of fields to include in the response. Default is None, which means all fields are included.
        
        Returns:
            A dictionary containing all application credits.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, application-credits, billing, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_credits.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_application_credit(self, api_version, application_credit: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates an application credit by sending a POST request to the API endpoint.
        
        Args:
            application_credit: A dict containing the application credit details. Required fields should be included according to API specifications.
        
        Returns:
            A dict containing the created application credit details as returned by the API.
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            create, application-credit, billing, api-client, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'application_credit': application_credit,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_credits.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_application_credit(self, api_version, application_credit_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single application credit from the API, including specified fields.
        
        Args:
            fields: A comma-separated list of fields to include in the response. If None, returns all available fields.
        
        Returns:
            A dictionary containing the application credit data retrieved from the API.
        
        Raises:
            HTTPError: If the API request fails (4XX/5XX status code).
        
        Tags:
            retrieve, application-credit, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/application_credits/{application_credit_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_recurring_application_charges(self, api_version, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of recurring application charges with optional filtering parameters.
        
        Args:
            fields: A comma-separated list of fields to include in the response. If None, returns all fields.
            since_id: Restrict results to recurring charges created after the specified ID.
        
        Returns:
            Dictionary containing the API response with recurring application charge data.
        
        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid parameters.
        
        Tags:
            billing, recurring-application-charge, list, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_arecurring_application_charge(self, api_version, recurring_application_charge: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a recurring application charge.
        
        Args:
            recurring_application_charge: A dictionary containing details for the recurring application charge. Defaults to None.
        
        Returns:
            A dictionary containing the result of creating the recurring application charge.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            recurring, billing, charge, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'recurring_application_charge': recurring_application_charge,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_charge(self, api_version, recurring_application_charge_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single charge's data from the API, including specified fields.
        
        Args:
            fields: A comma-separated list of fields to include in the response (optional). If omitted, returns all available fields.
        
        Returns:
            Dictionary containing the charge data retrieved from the API.
        
        Raises:
            HTTPError: Raised when the API request fails (non-2xx status code).
        
        Tags:
            retrieve, billing, api, recurring-charge, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def cancels_arecurring_application_charge(self, api_version, recurring_application_charge_id, request_body: Any | None = None) -> Any:
        """
        Cancels a recurring application charge, typically used in billing systems to stop periodic charges.
        
        Args:
            request_body: Optional data (JSON-parsable object) to include in the DELETE request body. Contains charge details or identifiers (exact schema context-dependent).
        
        Returns:
            A JSON-parsable Python object containing the server's response to the cancellation request.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4XX/5XX status codes) during the cancellation attempt.
        
        Tags:
            cancel, recurring, billing, async-job, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def activates_arecurring_application_charge(self, api_version, recurring_application_charge_id, recurring_application_charge: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Activates a previously accepted recurring application charge.
        
        Args:
            recurring_application_charge: An optional dictionary containing details of the recurring application charge.
        
        Returns:
            A dictionary containing the response from the activation request.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            activate, recurring-charge, billing, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'recurring_application_charge': recurring_application_charge,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/activate.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_the_capped_amount_of_arecurring_application_charge(self, api_version, recurring_application_charge_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Updates the capped amount of an active recurring application charge.
        
        Args:
            request_body: Optional request body annotated with type Any. Defaults to None.
        
        Returns:
            A dictionary response as JSON from the server.
        
        Raises:
            HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, billing, recurring-application-charge, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/customize.json"
        query_params = {}
        response = self._put(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_usage_charges(self, api_version, recurring_application_charge_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of usage charges from a specified endpoint.
        
        Args:
            fields: A comma-separated list of fields to include in the response. Defaults to None.
        
        Returns:
            A dictionary containing the list of usage charges.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request.
        
        Tags:
            billing, usage-charge, api-call, important, async_job
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_ausage_charge(self, api_version, recurring_application_charge_id, usage_charge: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a usage charge for a billing resource, typically in a SaaS or subscription-based system.
        
        Args:
            usage_charge: Dictionary containing usage charge details (e.g., amount, description, billing cycle). Required fields depend on API implementation.
        
        Returns:
            Dictionary containing the created usage charge data from the API response, typically including ID, amount, and timestamp
        
        Raises:
            HTTPError: Raised when the API request fails, typically due to invalid data (4xx) or server errors (5xx)
        
        Tags:
            billing, usage-charge, create, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'usage_charge': usage_charge,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_charge1(self, api_version, recurring_application_charge_id, usage_charge_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single charge including specified fields from the API.
        
        Args:
            fields: A comma-separated list of fields to include in the response. Leave None to return all available fields.
        
        Returns:
            Dictionary containing the charge data from the API response.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (non-2xx status codes) from the API.
        
        Tags:
            retrieve, charge, billing, usage-charge, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/recurring_application_charges/{recurring_application_charge_id}/usage_charges/{usage_charge_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_addresses_for_acustomer(self, api_version, customer_id) -> dict[str, Any]:
        """
        Retrieves a list of addresses for a customer.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary containing the list of addresses for the customer.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
            requests.exceptions.RequestException: Raised for any other error related to the HTTP request.
        
        Tags:
            list, customer, address, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_address_for_acustomer(self, api_version, customer_id, address: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new address for a customer by sending a POST request with the provided address details.
        
        Args:
            address: Optional dictionary containing address data. If none is provided, it defaults to None.
        
        Returns:
            Dictionary containing the newly created address.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, customer_address, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'address': address,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_details_for_asingle_customer_address(self, api_version, customer_id, address_id) -> dict[str, Any]:
        """
        Retrieves details for a customer's address by making a GET request to the specified API endpoint.
        
        Args:
            None: This function does not require any parameters
        
        Returns:
            A dictionary containing details for the customer address
        
        Raises:
            HTTPError: Raised if the GET request to the API fails due to an HTTP error
        
        Tags:
            retrieve, customer, address, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_customer_address(self, api_version, customer_id, address_id, address: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing customer address by sending a PUT request with the new address details.
        
        Args:
            address: A dictionary containing the address details to update. Optional; defaults to None.
        
        Returns:
            A dictionary containing the updated address information.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, customer, address, api-call, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'address': address,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def removes_an_address_from_acustomer_saddress_list(self, api_version, customer_id, address_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes a specified address from a customer's address list by sending a DELETE request.
        
        Args:
            request_body: Data containing the address identifier(s) to remove. Expected structure depends on API requirements.
        
        Returns:
            JSON-formatted response data containing the result of the deletion operation.
        
        Raises:
            HTTPError: If the HTTP request fails, typically due to invalid input data, authentication issues, or server errors.
        
        Tags:
            customers, customer-address, delete, management, core-operation, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def performs_bulk_operations_for_multiple_customer_addresses(self, api_version, customer_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Performs bulk operations on multiple customer addresses using a provided request body.
        
        Args:
            request_body: An optional request body containing data for bulk operations on customer addresses.
        
        Returns:
            A dictionary containing the response data from the bulk operation.
        
        Raises:
            HTTPError: Raised if the HTTP request to the server fails.
        
        Tags:
            bulk-operations, customer-addresses, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses/set.json"
        query_params = {}
        response = self._put(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def sets_the_default_address_for_acustomer(self, api_version, customer_id, address_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Sets the default address for a customer.
        
        Args:
            request_body: Optional request body to update the default address. Defaults to None if not provided.
        
        Returns:
            A dictionary representing the response from setting the default customer address.
        
        Raises:
            HTTPError: Raised when the HTTP request fails, typically due to client or server errors.
        
        Tags:
            set, address, customers, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/addresses/{address_id}/default.json"
        query_params = {}
        response = self._put(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_customers(self, api_version, ids: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, limit: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of customers based on specified criteria, including creation and update dates, customer IDs, and select fields.
        
        Args:
            created_at_max: The maximum date to show customers created before, in the format '2014-04-25T16:15:47-04:00'.
            created_at_min: The minimum date to show customers created after, in the format '2014-04-25T16:15:47-04:00'.
            fields: A comma-separated list of fields to include in the response.
            ids: A comma-separated list of customer IDs to restrict results to.
            limit: The maximum number of results to return (default 50, maximum 250).
            since_id: Fetch results with IDs greater than the specified ID.
            updated_at_max: The maximum date to show customers updated before, in the format '2014-04-25T16:15:47-04:00'.
            updated_at_min: The minimum date to show customers updated after, in the format '2014-04-25T16:15:47-04:00'.
        
        Returns:
            A dictionary containing the list of customers.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            customer, list, paginate, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers.json"
        query_params = {k: v for k, v in [('ids', ids), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acustomer(self, api_version, customer: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new customer record by sending customer data to the API endpoint.
        
        Args:
            customer: Dictionary containing customer details (e.g., name, contact). Omitting results in empty record creation.
        
        Returns:
            Dictionary containing API response with newly created customer details.
        
        Raises:
            HTTPError: When the API request fails due to network issues, invalid input, or server errors.
        
        Tags:
            create, customer, management, api-client, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'customer': customer,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def searches_for_customers_that_match_asupplied_query(self, api_version, order: str | None = None, query: str | None = None, limit: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Searches for customers that match a supplied query, allowing filtering by fields, limit, ordering, and query text.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
            limit: The maximum number of results to show. Default is 50, with a maximum of 250.
            order: Set the field and direction by which to order results. Default is 'last_order_date DESC'.
            query: Text to search for in the shop's customer data.
        
        Returns:
            A dictionary containing customer data that matches the search query.
        
        Raises:
            requests.exceptions.HTTPError: Raised if there is an HTTP error, such as a non-successful status code returned from the server.
        
        Tags:
            search, customer, important, shopify-api
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/search.json"
        query_params = {k: v for k, v in [('order', order), ('query', query), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_customer(self, api_version, customer_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves information about a single customer, allowing specification of which fields to include.
        
        Args:
            fields: A comma-separated list of field names to retrieve; if None, all fields are returned.
        
        Returns:
            A dictionary containing the customer's details.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            customer, retrieve, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_acustomer(self, api_version, customer_id, customer: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a customer by sending a PUT request with the provided customer data.
        
        Args:
            customer: Optional dictionary containing customer data. If None, an empty dictionary is sent.
        
        Returns:
            Dictionary containing the updated customer data.
        
        Raises:
            requests.HTTPError: Raised if the request to update the customer fails.
        
        Tags:
            update, customer-management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'customer': customer,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_acustomer(self, api_version, customer_id, request_body: Any | None = None) -> Any:
        """
        Deletes a customer from the system if they have no existing orders.
        
        Args:
            request_body: Optional JSON payload containing deletion details. Defaults to None.
        
        Returns:
            JSON response from the server indicating the outcome of the deletion request.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, customer, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_account_activation_url_for_acustomer(self, api_version, customer_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Generates a one-time-use account activation URL for a customer with an inactive account.
        
        Args:
            request_body: Optional payload containing customer account details (type/format not explicitly specified).
        
        Returns:
            Dictionary containing the generated activation URL and associated metadata.
        
        Raises:
            HTTPError: If the POST request fails due to invalid input or server errors.
        
        Tags:
            activation-url-generation, customer-management, account-enablement, async-batch, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/account_activation_url.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def sends_an_account_invite_to_acustomer(self, api_version, customer_id, customer_invite: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Sends an account invitation to a customer via API request.
        
        Args:
            customer_invite: A dictionary containing customer invitation details (e.g., email, permissions). Must contain required fields for the API.
        
        Returns:
            Parsed JSON response from the API containing invitation details or status.
        
        Raises:
            requests.HTTPError: If the API request fails due to invalid input, network issues, or server errors.
        
        Tags:
            send, account-invite, customers, api, post, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'customer_invite': customer_invite,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/send_invite.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_customers(self, api_version) -> dict[str, Any]:
        """
        Retrieves a count of all customers from the API endpoint.
        
        Returns:
            A dictionary containing the customer count data as returned by the API.
        
        Raises:
            HTTPError: If the API request fails (non-2xx status code).
        
        Tags:
            retrieve, count, customers, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_all_orders_belonging_to_acustomer(self, api_version, customer_id) -> dict[str, Any]:
        """
        Retrieves all orders belonging to a customer.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary containing all orders belonging to the customer.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a network error or invalid response.
        
        Tags:
            retrieve, orders, customer, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customers/{customer_id}/orders.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_customer_saved_searches(self, api_version, limit: str | None = None, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of customer saved searches with pagination support via response headers.
        
        Args:
            fields: Comma-separated list of field names to include in the response.
            limit: Maximum number of results to return (default: 50, maximum: 250).
            since_id: Restrict results to those created after the specified ID.
        
        Returns:
            Dictionary containing the parsed JSON response data.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP requests, typically due to invalid parameters or authentication failures.
        
        Tags:
            customer-saved-searches, retrieve, list, pagination, customers, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acustomer_saved_search(self, api_version, customer_saved_search: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a customer saved search using the provided data.
        
        Args:
            customer_saved_search: Dictionary containing customer saved search configuration details. Must include required fields for creating a saved search.
        
        Returns:
            Dictionary containing the created customer saved search details, including unique identifier and configuration.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to invalid input, authentication issues, or server errors.
        
        Tags:
            create, customer-saved-search, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'customer_saved_search': customer_saved_search,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_all_customer_saved_searches(self, api_version, since_id: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of all customer saved searches, optionally filtering results to after a specified ID.
        
        Args:
            since_id: Restrict results to after the specified ID (defaults to None for no restriction)
        
        Returns:
            A dictionary containing the count of customer saved searches.
        
        Raises:
            HTTPError: Raised if the HTTP request returns a status code indicating a problem, such as network errors or invalid responses.
        
        Tags:
            search, management, customers, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches/count.json"
        query_params = {k: v for k, v in [('since_id', since_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_customer_saved_search(self, api_version, customer_saved_search_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single customer saved search.
        
        Args:
            fields: A comma-separated list of field names to show; if None, all fields are returned.
        
        Returns:
            A dictionary containing the requested customer saved search data.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            search, customer-management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_acustomer_saved_search(self, api_version, customer_saved_search_id, customer_saved_search: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a customer saved search by sending a PUT request to the specified URL.
        
        Args:
            customer_saved_search: A dictionary containing the updated customer saved search parameters.
        
        Returns:
            A dictionary containing the response from the server after updating the customer saved search.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, customer-saved-search, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'customer_saved_search': customer_saved_search,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_acustomer_saved_search(self, api_version, customer_saved_search_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a customer saved search from the system.
        
        Args:
            request_body: The payload containing data required to delete the specific customer saved search (format unspecified)
        
        Returns:
            Dictionary containing the API response data after deletion
        
        Raises:
            HTTPError: Raised when the API request fails with a non-200 status code
        
        Tags:
            delete, customer, saved-search, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_all_customers_returned_by_acustomer_saved_search(self, api_version, customer_saved_search_id, order: str | None = None, limit: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves all customers associated with a customer saved search using specified filters and ordering.
        
        Args:
            fields: Show only certain fields (comma-separated list of field names)
            limit: Maximum number of results (default: 50, maximum: 250)
            order: Field and direction for ordering results (default: last_order_date DESC)
        
        Returns:
            Dictionary containing the retrieved customer data from the API response.
        
        Raises:
            requests.HTTPError: When the API request fails (non-2xx status code)
        
        Tags:
            retrieve, customers, saved-search, async-job, ai-management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/customer_saved_searches/{customer_saved_search_id}/customers.json"
        query_params = {k: v for k, v in [('order', order), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_discount_codes(self, api_version, price_rule_id) -> dict[str, Any]:
        """
        Retrieves a paginated list of discount codes from the Shopify REST Admin API, adhering to API version 2019-10 pagination rules.
        
        Args:
            None: This function does not accept explicit parameters. Pagination is handled via response headers.
        
        Returns:
            A dictionary containing the parsed JSON response with discount code data, including pagination links in the response header (accessible via the response object outside this function).
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes) during API communication.
        
        Tags:
            discounts, discount-code, pagination, rest-api, shopify, list, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_adiscount_code(self, api_version, price_rule_id, discount_code: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a discount code by sending a POST request with the specified parameters.
        
        Args:
            discount_code: Optional dictionary containing details for the discount code. Defaults to None.
        
        Returns:
            A dictionary representing the response from the server, typically including the created discount code details.
        
        Raises:
            requests.RequestException: Raised if there is a problem sending the request, such as a network error or invalid response.
            HTTPError: Raised if the server returns an unsuccessful status code.
        
        Tags:
            create, discount-code, post-request, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'discount_code': discount_code,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_discount_code(self, api_version, price_rule_id, discount_code_id) -> dict[str, Any]:
        """
        Retrieves a single discount code.
        
        Args:
            None: This function does not take any arguments.
        
        Returns:
            A dictionary containing a single discount code.
        
        Raises:
            requests.HTTPError: An HTTP error is raised if the request status code indicates an error.
        
        Tags:
            discount, discount-code, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_discount_code(self, api_version, price_rule_id, discount_code_id, discount_code: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing discount code with new data via a PUT request.
        
        Args:
            discount_code: Dictionary containing discount code attributes to update. Must include required fields for valid updates.
        
        Returns:
            Dictionary containing the updated discount code data returned by the API.
        
        Raises:
            HTTPError: Raised for HTTP request failures (e.g., invalid parameters, server errors, or authorization issues).
        
        Tags:
            update, discount, async-job, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'discount_code': discount_code,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_adiscount_code(self, api_version, price_rule_id, discount_code_id, request_body: Any | None = None) -> Any:
        """
        Deletes a discount code by sending a DELETE request to the API endpoint.
        
        Args:
            request_body: Optional data payload for the DELETE request. Typically includes identifiers for the discount code to be deleted or `None` if not required (default: `None`).
        
        Returns:
            Dictionary containing the parsed JSON response from the API after successful deletion.
        
        Raises:
            HTTPError: Raised if the API request fails (e.g., invalid credentials, resource not found, or server error).
        
        Tags:
            discounts, delete, management, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_the_location_of_adiscount_code(self, api_version) -> Any:
        """
        Retrieves the location of a discount code via HTTP response headers.
        
        Args:
            None: This function does not accept any parameters
        
        Returns:
            Any: Parsed JSON response containing discount code data. Note: The actual location URL is returned in the response's Location header, which may be automatically followed by some HTTP clients.
        
        Raises:
            HTTPError: Raised when the HTTP request fails (non-2xx status code)
        
        Tags:
            retrieve, discount-code, location-header, http-client, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/discount_codes/lookup.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_adiscount_code_creation_job(self, api_version, price_rule_id, discount_codes: list[Any] | None = None) -> dict[str, Any]:
        """
        Creates an asynchronous batch job to generate discount codes, enqueuing the request for background processing.
        
        Args:
            discount_codes: List of discount code data to be processed (format depends on API requirements)
        
        Returns:
            Dictionary containing the discount_code_creation job details including job ID and status
        
        Raises:
            HTTPError: If the HTTP request fails during job creation process
        
        Tags:
            discounts, batch-job, async-job, discount-code-creation, important
        """
        # Use discount_codes as the request body (assuming it's a list)
        request_body_payload = discount_codes
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/batch.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_adiscount_code_creation_job(self, api_version, price_rule_id, batch_id) -> dict[str, Any]:
        """
        Retrieves details of a discount code creation job from the API.
        
        Args:
            None: This function does not accept parameters.
        
        Returns:
            dict[str, Any]: A dictionary containing the discount code creation job details as returned by the API response.
        
        Raises:
            HTTPError: Raised if the API request fails (e.g., network issues, invalid response, or server errors).
        
        Tags:
            retrieve, discount-code, management, job-status, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/batch/{batch_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_discount_codes_for_adiscount_code_creation_job(self, api_version, price_rule_id, batch_id) -> dict[str, Any]:
        """
        Retrieves a list of discount codes for a discount code creation job.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary of discount codes where each code may include an 'id' if successfully created or 'errors' if creation encountered issues.
        
        Raises:
            HTTPError: Raised if the HTTP request to retrieve discount codes fails.
        
        Tags:
            retrieves, discounts, discount-codes, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_price_rules(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, starts_at_min: str | None = None, starts_at_max: str | None = None, ends_at_min: str | None = None, ends_at_max: str | None = None, times_used: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of price rules with optional filters for creation, update, start/end dates, and usage history, following Shopify's pagination guidelines.
        
        Args:
            created_at_max: Show price rules created before this ISO 8601 timestamp (format 2017-03-25T16:15:47-04:00)
            created_at_min: Show price rules created after this ISO 8601 timestamp
            ends_at_max: Show price rules ending before this ISO 8601 timestamp
            ends_at_min: Show price rules ending after this ISO 8601 timestamp
            limit: Maximum number of results to retrieve (default: 50, maximum: 250)
            since_id: Restrict results to after specified ID
            starts_at_max: Show price rules starting before this ISO 8601 timestamp
            starts_at_min: Show price rules starting after this ISO 8601 timestamp
            times_used: Filter by number of times price rules were used
            updated_at_max: Show price rules last updated before this ISO 8601 timestamp
            updated_at_min: Show price rules last updated after this ISO 8601 timestamp
        
        Returns:
            Dictionary containing price rules data from Shopify API response
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters or server errors
        
        Tags:
            retrieve, list, price-rules, discounts, pagination, shopify-api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('starts_at_min', starts_at_min), ('starts_at_max', starts_at_max), ('ends_at_min', ends_at_min), ('ends_at_max', ends_at_max), ('times_used', times_used)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_aprice_rule(self, api_version, price_rule: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new price rule based on the provided parameters.
        
        Args:
            price_rule: A dictionary containing details for the price rule. Default is None.
        
        Returns:
            A dictionary representing the created price rule as per the server's response.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, price-rule, management, ecommerce, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'price_rule': price_rule,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_price_rule(self, api_version, price_rule_id) -> dict[str, Any]:
        """
        Retrieves a single price rule from the server.
        
        Args:
            None: This function takes no arguments.
        
        Returns:
            A dictionary containing details of the price rule.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters a status error.
        
        Tags:
            price_rule, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_aprice_rule(self, api_version, price_rule_id, price_rule: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing price rule with new parameters.
        
        Args:
            price_rule: A dictionary containing parameters to update the existing price rule. Defaults to None.
        
        Returns:
            A dictionary containing the updated price rule data.
        
        Raises:
            HTTPError: Raised if the HTTP request fails (e.g., server error, unauthorized access).
        
        Tags:
            update, pricerule, important, management
        """
        # Build the request body from parameters
        request_body_payload = {
            'price_rule': price_rule,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_pricerule(self, api_version, price_rule_id, request_body: Any | None = None) -> Any:
        """
        Delete an existing PriceRule using the provided request body to specify which rule to remove.
        
        Args:
            request_body: Data specifying the PriceRule to delete, typically containing identifiers. Defaults to None.
        
        Returns:
            JSON response containing the deletion result or confirmation message.
        
        Raises:
            requests.HTTPError: Raised if the API request fails, such as when the PriceRule does not exist or the request is malformed.
        
        Tags:
            discounts, price-rule, delete, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/{price_rule_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_all_price_rules(self, api_version) -> dict[str, Any]:
        """
        Retrieves a count of all price rules from the API endpoint.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            Dictionary containing the count of price rules as returned by the API.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (non-2xx status code response).
        
        Tags:
            retrieve, count, discounts, price-rule, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/price_rules/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_events(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, filter: str | None = None, verb: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of events with optional pagination and filtering capabilities.
        
        Args:
            created_at_max: Show events created at or before this datetime (format: ISO 8601, e.g., 2014-04-25T16:15:47-04:00).
            created_at_min: Show events created at or after this datetime (format: ISO 8601, e.g., 2014-04-25T16:15:47-04:00).
            fields: Return comma-separated list specifying fields to include in response.
            filter: Filter events using custom criteria.
            limit: Limit results to maximum 250 items (default: 50).
            since_id: Show results after the specified sequential ID.
            verb: Filter events by specific action type.
        
        Returns:
            Dictionary containing parsed JSON response with event data and pagination headers.
        
        Raises:
            HTTPError: When the API request fails due to invalid parameters or server-side errors.
        
        Tags:
            events, retrieve, pagination, filtering, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/events.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('filter', filter), ('verb', verb), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_event(self, api_version, event_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single event by its ID, optionally specifying which fields to include.
        
        Args:
            fields: A comma-separated list of field names to show. If None, all fields are included.
        
        Returns:
            A dictionary containing the retrieved event data.
        
        Raises:
            requests.HTTPError: Raised if there is an HTTP error during the request.
        
        Tags:
            event, retrieve, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/events/{event_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_events(self, api_version, created_at_min: str | None = None, created_at_max: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of events based on the specified creation time range.
        
        Args:
            created_at_max: The maximum creation time (format: 2014-04-25T16:15:47-04:00) for counting events.
            created_at_min: The minimum creation time (format: 2014-04-25T16:15:47-04:00) for counting events.
        
        Returns:
            A dictionary containing the event count.
        
        Raises:
            HTTPError: If the HTTP request to retrieve events fails.
        
        Tags:
            events, event-counting, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/events/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_webhooks(self, api_version, address: str | None = None, created_at_max: str | None = None, created_at_min: str | None = None, fields: str | None = None, limit: str | None = None, since_id: str | None = None, topic: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of webhook subscriptions filtered by specified criteria such as date ranges, address, topic, and ID.
        
        Args:
            address: URI where webhook subscriptions send POST requests.
            created_at_max: Retrieve subscriptions created before this ISO 8601 datetime (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Retrieve subscriptions created after this ISO 8601 datetime.
            fields: Comma-separated list of properties to include in each result.
            limit: Maximum number of subscriptions to return (default: 50, maximum: 250).
            since_id: Retrieve subscriptions with IDs greater than this value.
            topic: Filter subscriptions by event topic (see `topic` property reference).
            updated_at_max: Retrieve subscriptions updated before this ISO 8601 datetime.
            updated_at_min: Retrieve subscriptions updated after this ISO 8601 datetime.
        
        Returns:
            Dictionary containing the API response data with webhook records.
        
        Raises:
            HTTPError: When the API request fails (e.g., invalid parameters or network issues).
        
        Tags:
            webhook, retrieve, list, pagination, subscription, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks.json"
        query_params = {k: v for k, v in [('address', address), ('created_at_max', created_at_max), ('created_at_min', created_at_min), ('fields', fields), ('limit', limit), ('since_id', since_id), ('topic', topic), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_webhook(self, api_version, webhook: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new webhook subscription by sending a POST request with a webhook configuration.
        
        Args:
            webhook: An optional dictionary containing the webhook configuration. It should include 'address' and 'topic'.
        
        Returns:
            A dictionary containing the response from the server after creating the webhook.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            webhook, create, important, management
        """
        # Build the request body from parameters
        request_body_payload = {
            'webhook': webhook,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_acount_of_all_webhooks(self, api_version, address: str | None = None, topic: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of existing webhook subscriptions based on specified filters.
        
        Args:
            address: Retrieve webhook subscriptions that send POST requests to this URI. If None, all addresses are included.
            topic: Show webhook subscriptions with the specified topic. Valid values reference the `topic` property documentation.
        
        Returns:
            A dictionary containing metadata and count data for matching webhook subscriptions.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails, typically due to invalid parameters or server errors.
        
        Tags:
            webhook, count, retrieve, subscriptions, events, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks/count.json"
        query_params = {k: v for k, v in [('address', address), ('topic', topic)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_webhook(self, api_version, webhook_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single webhook subscription from the API endpoint.
        
        Args:
            fields: Comma-separated list of properties to return (string or list-like). Limits response to only the specified fields.
        
        Returns:
            Dictionary containing webhook subscription data as key-value pairs.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4XX/5XX status codes) during API communication.
        
        Tags:
            webhook, retrieve, api-call, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_webhook(self, api_version, webhook_id, webhook: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modify an existing webhook by updating its subscription's topic or address URIs.
        
        Args:
            webhook: A dictionary containing the updated webhook details. Default is None.
        
        Returns:
            A dictionary representing the modified webhook response.
        
        Raises:
            requests.RequestException: Raised when there are issues with the HTTP request, such as network errors or invalid responses.
        
        Tags:
            modify, webhook, events, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'webhook': webhook,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_webhook(self, api_version, webhook_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes an existing webhook subscription by sending a delete request to the API endpoint.
        
        Args:
            request_body: Optional payload data for the delete request (typically unused in DELETE operations, included here for API consistency)
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API containing the deletion confirmation or status details
        
        Raises:
            HTTPError: Raised when the API request fails, typically due to invalid permissions, non-existent webhook, or network issues
        
        Tags:
            webhook, events, delete, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/webhooks/{webhook_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_inventory_items(self, api_version, ids: str | None = None, limit: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of inventory items based on provided IDs and a specified limit.
        
        Args:
            ids: A comma-separated list of IDs for inventory items to retrieve (maximum: 100).
            limit: The maximum number of results to show (default: 50, maximum: 250).
        
        Returns:
            A dictionary containing the retrieved inventory items.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            inventory, paginated, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_items.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_inventory_item_by_id(self, api_version, inventory_item_id) -> dict[str, Any]:
        """
        Retrieves a single inventory item by ID from a specified inventory source.
        
        Args:
            None: This function currently does not accept any parameters.
        
        Returns:
            A dictionary containing details of the inventory item.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, inventory, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_items/{inventory_item_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_inventory_item(self, api_version, inventory_item_id, inventory_item: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing inventory item by sending a PUT request with the provided item details.
        
        Args:
            inventory_item: A dictionary containing the updated details of the inventory item to update. If None, the function may not update any items.
        
        Returns:
            A dictionary containing the response from the server after updating the inventory item.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request failed, typically due to status code indicating an error.
        
        Tags:
            update, inventory, item, http-put, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'inventory_item': inventory_item,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_items/{inventory_item_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_inventory_levels(self, api_version, inventory_item_ids: str | None = None, location_ids: str | None = None, limit: str | None = None, updated_at_min: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of inventory levels based on specified parameters
        
        Args:
            inventory_item_ids: A comma-separated list of inventory item IDs (maximum: 50)
            limit: The maximum number of results to show (default: 50, maximum: 250)
            location_ids: A comma-separated list of location IDs (maximum: 50)
            updated_at_min: Show inventory levels updated at or after this date (format: 2019-03-19T01:21:44-04:00)
        
        Returns:
            A dictionary containing inventory levels
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request, such as invalid URL or parameters.
        
        Tags:
            inventory, inventory-levels, retrieve, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_levels.json"
        query_params = {k: v for k, v in [('inventory_item_ids', inventory_item_ids), ('location_ids', location_ids), ('limit', limit), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_inventory_level_from_alocation(self, api_version, request_body: Any | None = None) -> Any:
        """
        Deletes an inventory level of an inventory item at a specified location.
        
        Args:
            request_body: Optional request body containing additional information for deletion. Defaults to None.
        
        Returns:
            JSON response from the deletion operation.
        
        Raises:
            requests.RequestException: Raised if there's an issue with the HTTP request, such as network problems or invalid response.
        
        Tags:
            delete, inventory, important, location-management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_levels.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def adjusts_the_inventory_level_of_an_inventory_item_at_alocation(self, api_version, available_adjustment: float | None = None, inventory_item_id: float | None = None, location_id: float | None = None) -> dict[str, Any]:
        """
        Adjusts inventory levels for a specific item at a given location.
        
        Args:
            available_adjustment: The quantity adjustment to apply (positive or negative float)
            inventory_item_id: Unique identifier of the inventory item
            location_id: Unique identifier of the location
        
        Returns:
            Dictionary containing the updated inventory level details from the API response
        
        Raises:
            requests.HTTPError: Raised when the API request fails or returns a non-2XX status code
        
        Tags:
            inventory, inventory-level, adjustment, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'available_adjustment': available_adjustment,
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_levels/adjust.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def connects_an_inventory_item_to_alocation(self, api_version, inventory_item_id: float | None = None, location_id: float | None = None) -> dict[str, Any]:
        """
        Connects an inventory item to a specific location by creating an inventory level at that location.
        
        Args:
            inventory_item_id: The ID of the inventory item to connect (type: float)
            location_id: The ID of the location where the inventory level will be created (type: float)
        
        Returns:
            A dictionary containing the API response data from the inventory level creation operation.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails, typically due to invalid IDs or server errors
        
        Tags:
            inventory, inventory-level, connect, location, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_levels/connect.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def sets_the_inventory_level_for_an_inventory_item_at_alocation(self, api_version, available: float | None = None, inventory_item_id: float | None = None, location_id: float | None = None) -> dict[str, Any]:
        """
        Updates the available inventory quantity for a specific item at a designated location, automatically connecting the location if not already linked.
        
        Args:
            available: The updated quantity of the inventory item available at the specified location
            inventory_item_id: Identifier of the inventory item to be updated
            location_id: Identifier of the location where inventory is managed
        
        Returns:
            Dictionary containing the API response data with updated inventory details
        
        Raises:
            HTTPError: When the API request fails due to invalid parameters, authorization issues, or server errors
        
        Tags:
            inventory, inventory-level, update, management, async_job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'available': available,
            'inventory_item_id': inventory_item_id,
            'location_id': location_id,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/inventory_levels/set.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_locations(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of locations from the API endpoint.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            dict[str, Any]: A dictionary containing location data from the API response.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails (non-2xx status code).
        
        Tags:
            retrieve, list, inventory, location-management, api-interaction, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/locations.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_location_by_its_id(self, api_version, location_id) -> dict[str, Any]:
        """
        Retrieves a single location by its unique identifier from the inventory system.
        
        Args:
            location_id: Missing parameter - appears absent in implementation but implied by function purpose (added for correctness)
        
        Returns:
            A dictionary containing the location data as returned by the API
        
        Raises:
            HTTPError: When the API request fails with HTTP 4XX/5XX status codes, through response.raise_for_status()
        
        Tags:
            retrieve, location, inventory, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/locations/{location_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_locations(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of locations from the API.
        
        Args:
            None: This function does not accept parameters.
        
        Returns:
            A dictionary containing the location count data as returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: If the HTTP request to the API fails, indicating a client or server error (4xx or 5xx status code).
        
        Tags:
            retrieve, inventory, location, count, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/locations/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_inventory_levels_for_alocation(self, api_version, location_id) -> dict[str, Any]:
        """
        Retrieves a dictionary of inventory levels for a location.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary mapping inventory items to their levels.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            inventory, location, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/locations/{location_id}/inventory_levels.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_marketing_events(self, api_version, limit: str | None = None, offset: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of all marketing events with pagination based on provided limit and offset.
        
        Args:
            limit: The amount of results to return. Default: 50, Maximum: 250
            offset: The number of marketing events to skip.
        
        Returns:
            A dictionary containing the list of marketing events.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, marketing, event, important, api-call, pagination
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events.json"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_amarketing_event(self, api_version, marketing_event: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a marketing event by sending a POST request with the provided marketing event data.
        
        Args:
            marketing_event: Optional dictionary containing marketing event details (default: None)
        
        Returns:
            A dictionary containing the response from the server.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            create, marketing-event, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'marketing_event': marketing_event,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_all_marketing_events(self, api_version) -> dict[str, Any]:
        """
        Retrieves a count of all marketing events.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary containing the count of all marketing events.
        
        Raises:
            requests.RequestException: Raised when there is an issue with the HTTP request, such as a network problem or server error.
        
        Tags:
            retrieve, marketing, event, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_marketing_event(self, api_version, marketing_event_id) -> dict[str, Any]:
        """
        Retrieves a single marketing event's details from the API endpoint.
        
        Returns:
            dict[str, Any]: JSON response containing the marketing event data.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (e.g., invalid path, authentication issues, or server errors).
        
        Tags:
            retrieve, marketing-event, api, get, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_amarketing_event(self, api_version, marketing_event_id, marketing_event: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing marketing event by sending the provided data to the API endpoint.
        
        Args:
            marketing_event: A dictionary containing marketing event data to be updated. Must include all required fields for the event.
        
        Returns:
            A dictionary containing the updated marketing event details as returned by the API.
        
        Raises:
            HTTPError: If the API request fails due to invalid data, permissions, or server issues.
        
        Tags:
            update, marketing, management, api, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'marketing_event': marketing_event,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_amarketing_event(self, api_version, marketing_event_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a marketing event by sending a DELETE request to the specified base URL.
        
        Args:
            request_body: Optional request body for the DELETE request. Defaults to None.
        
        Returns:
            A dictionary containing the JSON response from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            delete, marketing-event, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events/{marketing_event_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_marketing_engagements_on_amarketing_event(self, api_version, marketing_event_id, engagements: list[Any] | None = None) -> dict[str, Any]:
        """
        Creates or updates marketing engagements for a marketing event, with daily aggregation and overwrites for existing entries on the same date.
        
        Args:
            engagements: List of marketing engagements to create/update. Engagements with matching `occurred_on` dates overwrite existing entries. Defaults to None.
        
        Returns:
            Dictionary containing the API response with details of created/updated engagements.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4XX/5XX status codes).
        
        Tags:
            create, marketing-engagements, marketing-event, async-job, api, overwrite, important
        """
        # Use engagements as the request body (assuming it's a list)
        request_body_payload = engagements
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/marketing_events/{marketing_event_id}/engagements.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_metafields_that_belong_to_aresource(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, namespace: str | None = None, key: str | None = None, value_type: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of metafields belonging to a resource using pagination via response headers (note: explicit pagination parameters are not supported).
        
        Args:
            created_at_max: Show metafields created before this timestamp (format: 2014-04-25T16:15:47-04:00)
            created_at_min: Show metafields created after this timestamp (format: 2014-04-25T16:15:47-04:00)
            fields: Comma-separated list of fields to include in response
            key: Filter metafields by key
            limit: Number of results to return (default: 50, max: 250)
            namespace: Filter metafields by namespace
            since_id: Restrict results to after specified ID
            updated_at_max: Show metafields last updated before this timestamp (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Show metafields last updated after this timestamp (format: 2014-04-25T16:15:47-04:00)
            value_type: Filter by metafield value type
        
        Returns:
            Dictionary containing the API response data including metafield information
        
        Raises:
            HTTPError: If the API request fails
        
        Tags:
            metafield, list, pagination, api, resource, retrieve, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('namespace', namespace), ('key', key), ('value_type', value_type), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_metafield_for_aresource(self, api_version, metafield: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new metafield for a resource by sending a POST request with the provided metafield details.
        
        Args:
            metafield: Optional dictionary containing metafield details for the resource. Defaults to None.
        
        Returns:
            A dictionary containing the newly created metafield in JSON format.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            metafield, resource, creates, api, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'metafield': metafield,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_aresource_smetafields(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of a resource's metafields.
        
        Args:
            None: This function does not require parameters.
        
        Returns:
            Dictionary containing the count of metafields from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails (e.g., authentication failure, invalid endpoint, or server error).
        
        Tags:
            metafield, retrieve, count, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_metafield_from_aresource_by_its_id(self, api_version, metafield_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single metafield from a specified resource by its ID.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
        
        Returns:
            A dictionary containing the requested metafield data from the resource.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns a status code indicating failure (4XX/5XX).
            ValueError: Raised when the response contains invalid JSON data.
        
        Tags:
            metafield, retrieve, resource, fields-filter, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_ametafield(self, api_version, metafield_id, metafield: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a metafield by sending a PUT request with the provided metafield data.
        
        Args:
            metafield: A dictionary where keys are metafield names and values are the corresponding metafield values to update. Default is None.
        
        Returns:
            A dictionary containing the updated metafield data as returned by the server.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, metafield, important, management
        """
        # Build the request body from parameters
        request_body_payload = {
            'metafield': metafield,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_ametafield_by_its_id(self, api_version, metafield_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a metafield by its ID.
        
        Args:
            request_body: An optional dictionary containing additional request data (defaults to None).
        
        Returns:
            A dictionary containing the result of the deletion operation.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            metafield, delete, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/metafields/{metafield_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_articles_from_ablog(self, api_version, blog_id, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None, handle: str | None = None, tag: str | None = None, author: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieve a paginated list of blog articles with filtering options via Shopify's REST Admin API.
        
        Args:
            author: Filter articles by author name.
            created_at_max: Show articles created before this ISO 8601 timestamp (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Show articles created after this ISO 8601 timestamp.
            fields: Specify fields to return using comma-separated field names.
            handle: Retrieve article by unique URL handle.
            limit: Maximum number of results (default: 50, max: 250).
            published_at_max: Show articles published before this timestamp.
            published_at_min: Show articles published after this timestamp.
            published_status: Filter by publication status ('published', 'unpublished', or 'any').
            since_id: Restrict results to articles after specified ID.
            tag: Filter articles containing specific tag.
            updated_at_max: Show articles updated before this timestamp.
            updated_at_min: Show articles updated after this timestamp.
        
        Returns:
            Dictionary containing article data from JSON API response.
        
        Raises:
            HTTPError: If API request fails due to invalid parameters or server errors.
        
        Tags:
            retrieve, list, articles, blog, paginated, rest-api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('handle', handle), ('tag', tag), ('author', author), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_article_for_ablog(self, api_version, blog_id, article: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates an article entry for a blog by sending a POST request to the API endpoint.
        
        Args:
            article: Dictionary containing article data to be created. Must be non-None to include in the request.
        
        Returns:
            Dictionary representing the newly created article from the API response.
        
        Raises:
            HTTPError: Raised when the API request fails (non-2xx status code).
        
        Tags:
            create, article, blog, api, post-request, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'article': article,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_all_articles_from_ablog(self, api_version, blog_id, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of articles from a blog based on specified creation, publication, and update dates, as well as publication status.
        
        Args:
            created_at_max: Maximum creation date for articles to count (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Minimum creation date for articles to count (format: 2014-04-25T16:15:47-04:00).
            published_at_max: Maximum publication date for articles to count (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Minimum publication date for articles to count (format: 2014-04-25T16:15:47-04:00).
            published_status: Count articles with a specific published status.
            updated_at_max: Maximum update date for articles to count (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Minimum update date for articles to count (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            A dictionary containing article counts based on the specified criteria.
        
        Raises:
            HTTPError: Raised if the HTTP request fails (e.g., server error, invalid request).
        
        Tags:
            search, blog, management, article, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_article(self, api_version, blog_id, article_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieve a single article from an online source.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
        
        Returns:
            A dictionary containing the article data.
        
        Raises:
            requests.RequestException: Raised when there is a problem with the HTTP request, such as network connection issues or HTTP errors.
        
        Tags:
            receive, article, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_article(self, api_version, blog_id, article_id, article: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an article by sending a PUT request with the provided article data.
        
        Args:
            article: (Optional) A dictionary containing article details; if not provided, an empty dictionary is sent.
        
        Returns:
            A JSON response from the server containing updated article information.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, article, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'article': article,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_article(self, api_version, blog_id, article_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes an article by sending a DELETE request to the specified URL.
        
        Args:
            request_body: Optional body of the request; may contain additional data for the deletion operation.
        
        Returns:
            A dictionary containing the response data from the server after deleting the article.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, article, important, online-store, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles/{article_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_article_authors(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of all article authors.
        
        Args:
            None: No arguments are accepted.
        
        Returns:
            A dictionary containing all article authors.
        
        Raises:
            requests.HTTPError: Raised if there is an issue with the HTTP request, such as a non-200 status code.
        
        Tags:
            list, article, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/articles/authors.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_article_tags(self, api_version, limit: str | None = None, popular: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of all article tags with optional filtering by popularity and limit.
        
        Args:
            limit: The maximum number of tags to retrieve.
            popular: A flag for ordering retrieved tags by popularity.
        
        Returns:
            A dictionary containing the list of all article tags.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request was unsuccessful.
        
        Tags:
            scrape, list, article, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/articles/tags.json"
        query_params = {k: v for k, v in [('limit', limit), ('popular', popular)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_assets_for_atheme(self, api_version, theme_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of assets for a theme, returning metadata about each asset.
        
        Args:
            fields: An optional comma-separated list of field names to include in the response.
        
        Returns:
            A dictionary containing metadata for each asset in the theme. Assets' contents are not included and must be retrieved individually.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, asset, metadata, theme, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_or_updates_an_asset_for_atheme(self, api_version, theme_id, asset: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates or updates an asset for a theme by sending a PUT request.
        
        Args:
            asset: Optional dictionary containing asset data; may include 'src' or 'source_key' for creating from existing files.
        
        Returns:
            A dictionary representing the created or updated asset's details in JSON format.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            asset, management, update, create, api-call, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'asset': asset,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_asset_from_atheme(self, api_version, theme_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes an asset from a theme by sending a DELETE request to a specified URL.
        
        Args:
            request_body: Optional body data to be sent with the request (default is None).
        
        Returns:
            A dictionary containing the response data from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, asset, theme, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}/assets.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_alist_of_all_blogs(self, api_version, limit: str | None = None, since_id: str | None = None, handle: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieve a paginated list of blogs from the Shopify REST Admin API, supporting field selection, filtering, and result limiting.
        
        Args:
            fields: comma-separated list of fields to include in the response
            handle: filter blogs by their unique handle identifier
            limit: maximum number of results to retrieve (default: 50, maximum: 250)
            since_id: restrict results to blogs with IDs greater than the specified value
        
        Returns:
            Dictionary containing the API response data and metadata, including blog entries and pagination links
        
        Raises:
            requests.HTTPError: raised for 4XX/5XX status codes from the Shopify API
        
        Tags:
            retrieve, list, blogs, shopify, rest-api, pagination, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('handle', handle), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_blog(self, api_version, blog: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Create a new blog with the provided blog details.
        
        Args:
            blog: A dictionary containing blog properties as key-value pairs. Required fields depend on API specifications.
        
        Returns:
            A dictionary representing the created blog with server-generated fields included
        
        Raises:
            HTTPError: If the POST request fails due to invalid input or server error.
        
        Tags:
            create, blog, management, api, important, async_job
        """
        # Build the request body from parameters
        request_body_payload = {
            'blog': blog,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_acount_of_all_blogs(self, api_version) -> dict[str, Any]:
        """
        Retrieve a count of all blogs from a remote endpoint.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing information about the count of all blogs.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            get, blog, data, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_blog(self, api_version, blog_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single Blog by its ID, optionally specifying fields to include in the response.
        
        Args:
            fields: comma-separated list of fields to include in the response (default: None)
        
        Returns:
            A dictionary containing the blog data with the specified fields.
        
        Raises:
            requests.HTTPError: If the HTTP request returns a bad status code.
        
        Tags:
            fetch, blog, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_blog(self, api_version, blog_id, blog: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modifies an existing blog by sending a PUT request with the provided blog data.
        
        Args:
            blog: A dictionary containing the blog data to modify (keys/values depend on API requirements)
        
        Returns:
            Dictionary containing the modified blog data as returned by the API
        
        Raises:
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP response status codes
        
        Tags:
            modify, update, blog, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'blog': blog,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_blog(self, api_version, blog_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes an existing blog by sending a delete request to the specified endpoint.
        
        Args:
            request_body: Optional request body to include with the delete request. Currently not utilized in the function's logic. Type: Annotated[Any, '']
        
        Returns:
            A dictionary containing the JSON response from the delete request.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a network problem or a server error.
        
        Tags:
            remove, delete, blog, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_comments(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, fields: str | None = None, published_status: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of comments based on various filter criteria, including creation and publication dates, fields, limit, and status.
        
        Args:
            created_at_max: Show comments created before this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
            created_at_min: Show comments created after this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
            fields: Show only certain fields, specified by a comma-separated list of field names
            limit: The maximum number of results to retrieve (default: 50; maximum: 250)
            published_at_max: Show comments published before this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
            published_at_min: Show comments published after this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
            published_status: Filter results by their published status
            since_id: Restrict results to after the specified ID
            status: Filter results by their status
            updated_at_max: Show comments last updated before this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
            updated_at_min: Show comments last updated after this date (format: YYYY-MM-DDTHH:MM:SS-YYYY)
        
        Returns:
            A dictionary containing the list of comments
        
        Raises:
            requests.HTTPError: If the request to the API endpoint fails
        
        Tags:
            retrieve, comments, filter, pagination, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('fields', fields), ('published_status', published_status), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acomment_for_an_article(self, api_version, comment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new comment for an article by sending a POST request to the API endpoint.
        
        Args:
            comment: Dictionary containing the comment data to be created. Keys and values should match the API's expected structure for comments.
        
        Returns:
            Dictionary containing the created comment details as returned by the API, typically including fields like ID, content, and metadata.
        
        Raises:
            HTTPError: If the API request fails due to client or server errors (4xx/5xx status codes).
        
        Tags:
            comment, create, api-integration, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'comment': comment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_comments(self, api_version, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves the count of comments filtered by creation, update, publication dates, and statuses.
        
        Args:
            created_at_max: Count comments created before this ISO 8601 datetime (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Count comments created after this ISO 8601 datetime.
            published_at_max: Count comments published before this ISO 8601 datetime.
            published_at_min: Count comments published after this ISO 8601 datetime.
            published_status: Filter by publication status (default: 'any').
            status: Filter by comment status.
            updated_at_max: Count comments last updated before this ISO 8601 datetime.
            updated_at_min: Count comments last updated after this ISO 8601 datetime.
        
        Returns:
            Dictionary containing comment count data from the API response.
        
        Raises:
            HTTPError: Raised for unsuccessful API requests (non-2xx status codes).
        
        Tags:
            comment, count, retrieve, filter, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_comment_by_its_id(self, api_version, comment_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single comment by its unique identifier from the API.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names. Defaults to None, which returns all available fields.
        
        Returns:
            Dictionary containing the comment data as returned by the API response.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, such as invalid comment ID or network errors.
        
        Tags:
            retrieve, comment, fetch, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_acomment_of_an_article(self, api_version, comment_id, comment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a specific comment on an article by sending a PUT request with the updated comment details.
        
        Args:
            comment: A dictionary containing the updated comment information; defaults to None if not provided.
        
        Returns:
            A dictionary containing the response from the server after updating the comment.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a network problem.
        
        Tags:
            update, comment, article, online-store, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'comment': comment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def marks_acomment_as_spam(self, api_version, comment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Marks a comment as spam by sending a POST request to the target URL with provided request body
        
        Args:
            request_body: (Any) Data payload to send with the request. Defaults to None
        
        Returns:
            (dict[str, Any]) Parsed JSON response from the POST request
        
        Raises:
            HTTPError: When the request fails with HTTP error status (4XX-5XX)
        
        Tags:
            comment, spam, moderation, post, api, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}/spam.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def marks_acomment_as_not_spam(self, api_version, comment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Marks a comment as not spam by sending a POST request to the server.
        
        Args:
            request_body: Request data for marking a comment as not spam (default: None).
        
        Returns:
            JSON response from the server indicating the result of marking the comment.
        
        Raises:
            requests.RequestException: Raised when a network problem or HTTP error occurs during the request.
        
        Tags:
            mark, comment, spam, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}/not_spam.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def approves_acomment(self, api_version, comment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Approves a comment in an online store system.
        
        Args:
            request_body: Optional request body used for approval, defaults to None.
        
        Returns:
            A dictionary containing the response data from the approval operation.
        
        Raises:
            HTTPError: Raised if the HTTP request fails, such as receiving a 4xx or 5xx status code.
        
        Tags:
            approve, async_job, ai, management, important, comments
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}/approve.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def removes_acomment(self, api_version, comment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes a comment by sending a POST request to the specified URL endpoint.
        
        Args:
            request_body: Data containing comment identifier(s) and removal parameters. Must be None or a valid dictionary matching the API's requirements.
        
        Returns:
            Dictionary containing the server's JSON response after comment removal.
        
        Raises:
            HTTPError: If the HTTP POST request fails due to client (4XX) or server (5XX) errors.
        
        Tags:
            remove, comment, post, api-call, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}/remove.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def restores_apreviously_removed_comment(self, api_version, comment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Restores a previously removed comment.
        
        Args:
            request_body: Optional request body data used for restoring the comment. Defaults to None.
        
        Returns:
            A dictionary containing the response from restoring the comment.
        
        Raises:
            HTTPError: Raised if the HTTP request to restore the comment fails.
        
        Tags:
            restore, comment, management, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/comments/{comment_id}/restore.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_pages(self, api_version, limit: str | None = None, since_id: str | None = None, title: str | None = None, handle: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, fields: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of pages from the Shopify REST Admin API with pagination support via response header links.
        
        Args:
            created_at_max: Show pages created before this date (format: 2008-12-31).
            created_at_min: Show pages created after this date (format: 2008-12-31).
            fields: Comma-separated list of field names to include in the response.
            handle: Retrieve a specific page by its unique handle.
            limit: Maximum number of results to return (default: 50, maximum: 250).
            published_at_max: Show pages published before this timestamp (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Show pages published after this timestamp (format: 2014-04-25T16:15:47-04:00).
            published_status: Filter pages by published status (default: any).
            since_id: Restrict results to pages with IDs greater than the specified ID.
            title: Filter pages by exact title match.
            updated_at_max: Show pages last updated before this date (format: 2008-12-31).
            updated_at_min: Show pages last updated after this date (format: 2008-12-31).
        
        Returns:
            Dictionary containing the paginated list of pages and their metadata.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests, authentication failures, or server errors (4XX/5XX status codes).
        
        Tags:
            retrieve, list, pages, shopify, rest-api, pagination, important, online-store
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('title', title), ('handle', handle), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('fields', fields), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_page(self, api_version, page: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new page with the provided data.
        
        Args:
            page: The page details to be created, as a dictionary, or None if no data is provided.
        
        Returns:
            A dictionary containing the newly created page's details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, page, important, management
        """
        # Build the request body from parameters
        request_body_payload = {
            'page': page,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_apage_count(self, api_version, title: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a page count based on specified filters like creation, publication, and update dates, page title, and publication status.
        
        Args:
            created_at_max: Count pages created before this date (format: YYYY-MM-DD).
            created_at_min: Count pages created after this date (format: YYYY-MM-DD).
            published_at_max: Show pages published before this date (format: YYYY-MM-DDTHH:MM:SS+HHMM).
            published_at_min: Show pages published after this date (format: YYYY-MM-DDTHH:MM:SS+HHMM).
            published_status: Count pages with a given published status (default: any).
            title: Count pages with a given title.
            updated_at_max: Count pages last updated before this date (format: YYYY-MM-DD).
            updated_at_min: Count pages last updated after this date (format: YYYY-MM-DD).
        
        Returns:
            A dictionary containing the page count based on the provided filters.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            search, list, important, page-management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages/count.json"
        query_params = {k: v for k, v in [('title', title), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_page_by_its_id(self, api_version, page_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single page by its ID, optionally selecting specific fields.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names. Defaults to None.
        
        Returns:
            A dict containing the page data.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            page, retrieve, important, online-store
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_apage(self, api_version, page_id, page: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a specific page with the provided data.
        
        Args:
            page: A dictionary containing the page data to update. Optional.
        
        Returns:
            A dictionary representing the updated page from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, page-management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'page': page,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_apage(self, api_version, page_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a page based on the provided request body.
        
        Args:
            request_body: Optional request body data of type Annotated[Any, ''] to delete a page. Defaults to None.
        
        Returns:
            A dictionary containing the response data from the deletion operation.
        
        Raises:
            requests.exceptions.RequestException: Raised if the HTTP request fails or if the response status code indicates an error.
        
        Tags:
            delete, page, management, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/pages/{page_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_url_redirects(self, api_version, limit: str | None = None, since_id: str | None = None, path: str | None = None, target: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of URL redirects with optional filtering parameters. Results are paginated through response headers (page parameters are not supported).
        
        Args:
            fields: Show only specified fields (comma-separated list of field names)
            limit: Maximum number of results to return (default: 50, max: 250)
            path: Filter redirects by source path
            since_id: Restrict results to entries after the specified ID
            target: Filter redirects by target URL
        
        Returns:
            Dictionary containing API response data with redirect information
        
        Raises:
            HTTPError: Raised for 4XX/5XX status code responses from the API
        
        Tags:
            retrieve, list, redirects, pagination, api, store-management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('path', path), ('target', target), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_aredirect(self, api_version, redirect: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a redirect by sending a POST request to the server with the redirect details.
        
        Args:
            redirect: Optional dictionary containing the redirect details (e.g., path).
        
        Returns:
            A dictionary containing the response from the server after creating the redirect.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, redirect, post, important, management, storage
        """
        # Build the request body from parameters
        request_body_payload = {
            'redirect': redirect,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_url_redirects(self, api_version, path: str | None = None, target: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of URL redirects matching specified path and/or target parameters.
        
        Args:
            path: Path to filter redirects (counts redirects originating from this path).
            target: Target URL to filter redirects (counts redirects pointing to this destination).
        
        Returns:
            Dictionary containing redirect count data from the API response.
        
        Raises:
            HTTPError: If the API request fails.
        
        Tags:
            redirect, count, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects/count.json"
        query_params = {k: v for k, v in [('path', path), ('target', target)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_redirect(self, api_version, redirect_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves details of a single redirect entry from the API.
        
        Args:
            fields: Show only specific fields, specified as a comma-separated list of field names (e.g., 'id,from_path,to_url')
        
        Returns:
            Dictionary containing the redirect's data as key-value pairs
        
        Raises:
            HTTPError: Raised when the API request fails, typically for invalid parameters or server errors
        
        Tags:
            retrieve, redirect, api, online-store, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_redirect(self, api_version, redirect_id, redirect: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing redirect by sending a PUT request with the specified redirect details.
        
        Args:
            redirect: An optional dictionary containing details for the redirect; if not provided, defaults to None.
        
        Returns:
            A dictionary containing the updated redirect details in JSON format.
        
        Raises:
            requests.HTTPError: Raised if there was an unsuccessful status code returned from the HTTP request.
        
        Tags:
            update, redirect, http-put, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'redirect': redirect,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_aredirect(self, api_version, redirect_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a redirect from the system using provided request data.
        
        Args:
            request_body: (Annotated[Any, '']) Data payload containing information needed to identify the redirect to delete. Defaults to None.
        
        Returns:
            dict[str, Any]: Response data parse from JSON after deleting the redirect.
        
        Raises:
            HTTPError: If the HTTP request fails (e.g., invalid credentials, network error, or server-side issues).
        
        Tags:
            delete, redirect, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/redirects/{redirect_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_script_tags(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, src: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of all script tags with optional filters such as creation date, update date, and source URL.
        
        Args:
            created_at_max: The maximum creation date to filter script tags. Format: 2014-04-25T16:15:47-04:00
            created_at_min: The minimum creation date to filter script tags. Format: 2014-04-25T16:15:47-04:00
            fields: A comma-separated list of fields to include in the response.
            limit: The number of results to return. Default: 50, Maximum: 250
            since_id: Restrict results to after the specified ID.
            src: Show script tags with this URL.
            updated_at_max: The maximum update date to filter script tags. Format: 2014-04-25T16:15:47-04:00
            updated_at_min: The minimum update date to filter script tags. Format: 2014-04-25T16:15:47-04:00
        
        Returns:
            A dictionary containing the list of script tags.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, script-tag, ecommerce, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('src', src), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_script_tag(self, api_version, script_tag: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new script tag resource by making a POST request to the API endpoint.
        
        Args:
            script_tag: Dictionary containing script tag configuration parameters (e.g., attributes like 'event', 'src', and 'display_scope'). Required fields depend on API specifications.
        
        Returns:
            Dictionary containing the created script tag's full configuration and metadata from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a 4XX/5XX status code.
        
        Tags:
            script, create, api, online-store, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'script_tag': script_tag,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_all_script_tags(self, api_version, src: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of script tags from an online store, optionally filtered by source URL.
        
        Args:
            src: Counts only script tags matching the specified URL (None for counting all script tags).
        
        Returns:
            Dictionary containing script tag count and metadata from the API response.
        
        Raises:
            HTTPError: Raised if the API request fails (e.g., network issues or invalid permissions).
        
        Tags:
            count, script-tag, online-store, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags/count.json"
        query_params = {k: v for k, v in [('src', src)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_script_tag(self, api_version, script_tag_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single script tag from the online store with specified response fields.
        
        Args:
            fields: A comma-separated list of fields to include in the response. If None, all fields are included.
        
        Returns:
            A dictionary containing the script tag data as returned by the API.
        
        Raises:
            HTTPError: Raised when the API request fails due to network errors, invalid URLs, or server-side issues (4XX/5XX status codes).
        
        Tags:
            script-tag-retrieval, online-store, api-integration, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_ascript_tag(self, api_version, script_tag_id, script_tag: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a script tag in an online store by sending a PUT request with the provided script tag details.
        
        Args:
            script_tag: A dictionary containing script tag information. Default is None.
        
        Returns:
            A dictionary containing the updated script tag response in JSON format.
        
        Raises:
            requests.RequestException: Raised if there is a problem with the HTTP request, such as network issues or invalid responses from the server.
        
        Tags:
            update, script-tag, online-store, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'script_tag': script_tag,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_ascript_tag(self, api_version, script_tag_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a script tag from the system.
        
        Args:
            request_body: Optional request body with data for the deletion operation. Defaults to None.
        
        Returns:
            A JSON response containing the outcome of the deletion operation.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request encounters an error status code.
        
        Tags:
            delete, scripttag, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/script_tags/{script_tag_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_themes(self, api_version, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of themes from the online store with optional field filtering.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names. If None, all available fields are returned.
        
        Returns:
            A dictionary containing the list of themes and their details, formatted according to the API response.
        
        Raises:
            HTTPError: Raised if the API request fails due to network issues, invalid permissions, or server-side errors.
        
        Tags:
            online-store, theme, retrieve, list, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_atheme(self, api_version, theme: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a theme for an online store using a provided configuration. The theme is created as unpublished by default unless explicitly specified as 'main' in the theme data.
        
        Args:
            theme: A dictionary containing theme configuration details, including the public URL of a ZIP file and optional 'role' key ('main' for immediate publication after processing).
        
        Returns:
            Dictionary containing the created theme's details, including its ID, name, and processing status.
        
        Raises:
            HTTPError: If the HTTP request fails due to network issues, invalid permissions, or malformed theme data.
        
        Tags:
            create, theme, online-store, async-job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'theme': theme,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_theme(self, api_version, theme_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single theme from the server.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
        
        Returns:
            A dictionary containing the theme details.
        
        Raises:
            HTTPError: Raised if the HTTP request fails (e.g., due to network errors or invalid status codes).
        
        Tags:
            retrieve, theme, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_theme(self, api_version, theme_id, theme: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing theme by sending a modified theme configuration to the API.
        
        Args:
            theme: Dictionary containing theme configuration data to update. Must include valid theme fields.
        
        Returns:
            Dictionary containing the updated theme configuration from the API response.
        
        Raises:
            requests.HTTPError: If the API request fails (non-2xx status code). Raised by response.raise_for_status().
        
        Tags:
            modify, theme, update, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'theme': theme,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_theme(self, api_version, theme_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Remove an existing theme by deleting it from the specified system.
        
        Args:
            request_body: Payload containing theme identifier and optional configuration (type may vary by implementation). If empty, system-specific defaults may apply.
        
        Returns:
            Dictionary containing deletion confirmation details (format varies by API implementation).
        
        Raises:
            HTTPError: If the DELETE request fails due to network issues, invalid permissions, or missing theme.
        
        Tags:
            delete, theme-management, online-store, http-delete, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/themes/{theme_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_checkouts(self, api_version, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of checkouts based on specified filters like creation date, status, and update date.
        
        Args:
            created_at_max: Maximum creation date for checkouts (format: 2014-04-25T16:15:47-04:00)
            created_at_min: Minimum creation date for checkouts (format: 2014-04-25T16:15:47-04:00)
            since_id: Restrict results to checkouts created after the specified ID
            status: Filter checkouts by status (default: 'open')
            updated_at_max: Maximum last updated date for checkouts (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Minimum last updated date for checkouts (format: 2014-04-25T16:15:47-04:00)
        
        Returns:
            A dictionary containing the count of checkouts
        
        Raises:
            RequestsException: Raised if an error occurs during the HTTP request (e.g., network issues, invalid response).
        
        Tags:
            checkouts, count, filter, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/count.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_abandoned_checkouts(self, api_version, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of abandoned checkouts with optional filtering based on creation/update timestamps, status, and ID ranges.
        
        Args:
            created_at_max: Show checkouts created before the specified date (format: 2014-04-25T16:15:47-04:00)
            created_at_min: Show checkouts created after the specified date (format: 2014-04-25T16:15:47-04:00)
            limit: Maximum number of results to return (default: 50, maximum: 250)
            since_id: Restrict results to checkouts created after the specified ID
            status: Filter results by checkout status (default: open)
            updated_at_max: Show checkouts last updated before the specified date (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Show checkouts last updated after the specified date (format: 2014-04-25T16:15:47-04:00)
        
        Returns:
            Dictionary containing the API response with checkout data and pagination links
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures or invalid API responses
        
        Tags:
            retrieve, list, abandoned-checkouts, orders, pagination, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acheckout(self, api_version, checkout: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a checkout object via API request with the specified parameters.
        
        Args:
            checkout: A dictionary containing checkout configuration details. If None, an empty checkout will be created.
        
        Returns:
            A dictionary containing the created checkout data from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails with a 4XX or 5XX status code.
        
        Tags:
            create, checkout, api, sales-channels, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'checkout': checkout,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_draft_orders(self, api_version, fields: str | None = None, limit: str | None = None, since_id: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, ids: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves paginated draft orders from the REST Admin API with optional filtering parameters.
        
        Args:
            fields: Comma-separated list of fields to include in the response
            ids: Filter by list of draft order IDs
            limit: Maximum number of results to retrieve (default: 50, max: 250)
            since_id: Restrict results to draft orders after specified ID
            status: Filter by draft order status
            updated_at_max: Show orders last updated before this timestamp (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Show orders last updated after this timestamp (format: 2014-04-25T16:15:47-04:00)
        
        Returns:
            Dictionary containing parsed JSON response with draft order data
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP requests (non-2xx status codes)
        
        Tags:
            retrieve, list, draft-orders, pagination, api-call, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders.json"
        query_params = {k: v for k, v in [('fields', fields), ('limit', limit), ('since_id', since_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('ids', ids), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_draftorder(self, api_version, draft_order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new draft order in Shopify with product variant line items, custom line items, and discount configurations, supporting asynchronous calculation workflows.
        
        Args:
            draft_order: Dictionary containing draft order details (product variants, quantities, discounts, customer_id, shipping lines). Must include either variant_id/quantity/discount for product line items or title/price/taxable/quantity for custom line items.
        
        Returns:
            Dictionary representing the created draft order with calculated shipping, taxes, and discounts. May include asynchronous response headers (location, retry-after) if calculations require polling.
        
        Raises:
            HTTPError: If API request fails due to rate limits (5/minute for trial/partner stores) or invalid input parameters.
        
        Tags:
            draft-order, shopify, ecommerce, async-job, order-management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'draft_order': draft_order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_draftorder(self, api_version, draft_order_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single DraftOrder based on the specified criteria.
        
        Args:
            fields: A comma-separated list of fields to include in the response.
        
        Returns:
            A dictionary containing the retrieved DraftOrder data.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            receive, draft, order, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_draftorder(self, api_version, draft_order_id, draft_order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modifies an existing draft order by updating its details via REST API request.
        
        Args:
            draft_order: Dictionary containing draft order details to be updated. Must include required fields for the draft order.
        
        Returns:
            Dictionary representing the updated draft order details as returned by the API.
        
        Raises:
            HTTPError: If the API request fails with a status code >= 400, indicating client or server errors.
        
        Tags:
            draft-order, modify, orders, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'draft_order': draft_order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_draftorder(self, api_version, draft_order_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes an existing DraftOrder by sending a DELETE request to the specified URL.
        
        Args:
            request_body: Optional body to be sent with the request; defaults to None if not provided.
        
        Returns:
            A dictionary containing the response from the server after deleting the draft order.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, draftorder, orders, delete, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/{draft_order_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_acount_of_all_draftorders(self, api_version, since_id: str | None = None, status: str | None = None, updated_at_max: str | None = None, updated_at_min: str | None = None) -> dict[str, Any]:
        """
        Retrieve the count of draft orders based on optional filtering criteria.
        
        Args:
            since_id: Count draft orders created after the specified ID.
            status: Filter draft orders by status (default: open).
            updated_at_max: Count draft orders last updated before this timestamp (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Count draft orders last updated after this timestamp (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            Dictionary containing the count of matching draft orders.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails.
        
        Tags:
            count, draft-orders, filter, orders, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/count.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('status', status), ('updated_at_max', updated_at_max), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def send_an_invoice(self, api_version, draft_order_id, draft_order_invoice: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Sends an invoice for a draft order via email with customizable recipient, sender, and message details.
        
        Args:
            draft_order_invoice: Dictionary containing email configuration (to, from, bcc, subject, custom_message) and invoice data. Required fields depend on API specifications.
        
        Returns:
            Dictionary containing the API response data after successful invoice submission.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures (4XX/5XX status codes) during invoice submission.
        
        Tags:
            orders, invoice, email, send, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'draft_order_invoice': draft_order_invoice,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/{draft_order_id}/send_invoice.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def complete_adraft_order(self, api_version, draft_order_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Completes a draft order by transitioning it to a regular order, supporting flows like external payment acceptance or sending invoices.
        
        Args:
            request_body: Optional request body containing draft order details (default is None).
        
        Returns:
            A dictionary containing the completed order details.
        
        Raises:
            HTTPError: Raised if the HTTP request to complete the draft order fails.
        
        Tags:
            orders, draft-order, complete, shopify, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/draft_orders/{draft_order_id}/complete.json"
        query_params = {}
        response = self._put(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_order_risks_for_an_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves a list of all order risks for an order.
        
        Args:
            None: No parameters required.
        
        Returns:
            A dictionary containing a list of all order risks for an order.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            order-risk, orders, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/risks.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_order_risk_for_an_order(self, api_version, order_id, risk: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates an order risk for an order by sending a POST request with the provided risk details.
        
        Args:
            risk: An optional dictionary containing the risk information for the order; defaults to None.
        
        Returns:
            A dictionary containing the result of creating an order risk.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, order-risk, orders, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'risk': risk,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/risks.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_order_risk_by_its_id(self, api_version, order_id, risk_id) -> dict[str, Any]:
        """
        Retrieves a single order risk by its ID.
        
        Args:
            None: This function does not take any arguments.
        
        Returns:
            A dictionary containing the order risk details.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
            ValueError: Raised if the response is not in JSON format.
        
        Tags:
            retrieves, order_risk, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_order_risk(self, api_version, order_id, risk_id, risk: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an order risk by sending a risk update request to the API.
        
        Args:
            risk: A dictionary containing the risk data to update. Must not be created by another application (as per API note).
        
        Returns:
            A dictionary containing the updated order risk data from the API response.
        
        Raises:
            requests.HTTPError: Raised for non-2xx HTTP responses from the API, typically due to invalid risk data, authorization issues, or attempts to modify risks created by other applications.
        
        Tags:
            update, orders, risk, management, api, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'risk': risk,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_order_risk_for_an_order(self, api_version, order_id, risk_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes an order risk associated with an order, typically used to remove risk assessments that were manually created by the current application.
        
        Args:
            request_body: Optional annotated payload containing order risk deletion parameters (type and structure dependent on API requirements)
        
        Returns:
            Dictionary containing the API response with deletion confirmation details
        
        Raises:
            requests.exceptions.HTTPError: Raised for 4XX/5XX status codes when deletion fails due to invalid permissions, non-existent order risks, or server errors
        
        Tags:
            delete, order-management, order-risk, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/risks/{risk_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_orders(self, api_version, ids: str | None = None, name: str | None = None, limit: str | None = None, since_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, processed_at_min: str | None = None, processed_at_max: str | None = None, attribution_app_id: str | None = None, status: str | None = None, financial_status: str | None = None, fulfillment_status: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of orders with optional filtering and pagination support. Note: Uses response header links for pagination (page parameter unsupported in v2019-10+).
        
        Args:
            attribution_app_id: Show orders attributed to a specific app ID. Use 'current' for the calling app.
            created_at_max: Filter orders created at or before this timestamp (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Filter orders created at or after this timestamp (format: 2014-04-25T16:15:47-04:00).
            fields: Comma-separated list of fields to include in response.
            financial_status: Filter by payment status (default: any).
            fulfillment_status: Filter by fulfillment status (default: any).
            ids: Comma-separated list of order IDs to retrieve.
            limit: Maximum results per page (50-250, default: 50).
            name: Order name filter.
            processed_at_max: Filter orders imported at or before this timestamp (format: 2014-04-25T16:15:47-04:00).
            processed_at_min: Filter orders imported at or after this timestamp (format: 2014-04-25T16:15:47-04:00).
            since_id: Show orders after this ID.
            status: Filter by order status (default: open).
            updated_at_max: Filter orders updated at or before this timestamp (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Filter orders updated at or after this timestamp (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            Dictionary containing order data and pagination details from the API response.
        
        Raises:
            HTTPError: Raised for failed API requests (non-2xx status codes).
        
        Tags:
            orders, retrieval, pagination, filtering, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders.json"
        query_params = {k: v for k, v in [('ids', ids), ('name', name), ('limit', limit), ('since_id', since_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('processed_at_min', processed_at_min), ('processed_at_max', processed_at_max), ('attribution_app_id', attribution_app_id), ('status', status), ('financial_status', financial_status), ('fulfillment_status', fulfillment_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_an_order(self, api_version, order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new order, allowing control over inventory behavior and receipt settings.
        
        Args:
            order: Dictionary containing order details. Must include address details with 'first_name' and 'last_name' if providing shipping/billing addresses.
        
        Returns:
            Dictionary containing the created order details, including order ID and status.
        
        Raises:
            HTTPError: If the API request fails, typically due to invalid parameters or server-side errors.
            ValueError: If required address fields ('first_name' and 'last_name') are missing when including addresses.
        
        Tags:
            orders, create, inventory-management, ecommerce, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'order': order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves a specific order from a remote source.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary containing information about the retrieved order.
        
        Raises:
            requests.RequestException: This exception may be raised if there is an issue with the HTTP request (e.g., network errors, invalid response).
        
        Tags:
            orders, order, retrieve, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_order(self, api_version, order_id, order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing order with the provided order data
        
        Args:
            order: Dict containing order details to update. If None, no update is made.
        
        Returns:
            Dictionary containing the updated order data
        
        Raises:
            HTTPError: Raised if the HTTP request to update the order fails
        
        Tags:
            update, orders, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'order': order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_an_order(self, api_version, order_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes an order by sending a DELETE request to the designated URL. Note that orders interacting with an online gateway cannot be deleted.
        
        Args:
            request_body: Optional request body. Defaults to None if not provided.
        
        Returns:
            A dictionary containing the response after the order has been deleted.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, order, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_an_order_count(self, api_version, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, status: str | None = None, financial_status: str | None = None, fulfillment_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves the count of orders filtered by the specified date ranges, financial status, fulfillment status, or order status.
        
        Args:
            created_at_max: Count orders created before this datetime (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Count orders created after this datetime (format: 2014-04-25T16:15:47-04:00).
            financial_status: Filter orders by financial status (e.g., paid, pending). Defaults to any status if unset.
            fulfillment_status: Filter orders by fulfillment status (e.g., fulfilled, unfulfilled). Defaults to any status if unset.
            status: Filter orders by order status (e.g., open, closed). Defaults to 'open' if unset.
            updated_at_max: Count orders last updated before this datetime (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Count orders last updated after this datetime (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            Dict containing the order count and metadata from the API response.
        
        Raises:
            requests.HTTPError: Raised if the API request fails (e.g., invalid parameters or server error).
        
        Tags:
            orders, count, retrieve, ecommerce, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('status', status), ('financial_status', financial_status), ('fulfillment_status', fulfillment_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def closes_an_order(self, api_version, order_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Closes an order via API request and returns the response data.
        
        Args:
            request_body: The data payload for closing the order, typically containing order-specific closure details.
        
        Returns:
            A dictionary containing the API response data after order closure.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a non-success HTTP status code.
        
        Tags:
            order, closure, api-request, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/close.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def re_opens_aclosed_order(self, api_version, order_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Re-opens a previously closed order by submitting a request to the API.
        
        Args:
            request_body: Payload containing order data for re-opening (structure depends on API requirements).
        
        Returns:
            Dict[str, Any]: Parsed JSON response from the API containing the re-opened order details.
        
        Raises:
            HTTPError: Raised when the API request fails (non-2xx status code).
        
        Tags:
            reopen, orders, management, api, important, async_job
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/open.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def cancels_an_order(self, api_version, order_id, amount: str | None = None, currency: str | None = None, note: str | None = None) -> dict[str, Any]:
        """
        Cancels an order and returns the result. For multi-currency orders, the currency parameter is required when amount is provided. Orders with existing fulfillments cannot be canceled.
        
        Args:
            amount: Optional amount to refund (required for multi-currency orders when currency is needed). Must be used with currency parameter if specified.
            currency: Currency code for the amount (required when amount is specified for multi-currency orders).
            note: Optional cancellation note or reason.
        
        Returns:
            Dictionary containing the API response data with cancellation details.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP requests (4XX/5XX status codes), indicating issues like invalid parameters or server errors.
        
        Tags:
            cancel, order, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'amount': amount,
            'currency': currency,
            'note': note,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/cancel.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_refunds_for_an_order(self, api_version, order_id, limit: str | None = None, fields: str | None = None, in_shop_currency: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of refunds for an order, allowing customization of returned fields and currency.
        
        Args:
            fields: A comma-separated list of field names to include in the response.
            in_shop_currency: Whether to show amounts in the shop currency (default: False).
            limit: The maximum number of results to retrieve (default: 50; maximum: 250).
        
        Returns:
            A dictionary containing the list of refunds for the order.
        
        Raises:
            HTTPError: Raised if the HTTP request fails, often due to invalid parameters or server errors.
        
        Tags:
            refund, orders, shopify-api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/refunds.json"
        query_params = {k: v for k, v in [('limit', limit), ('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_arefund(self, api_version, order_id, refund: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a refund based on the provided refund details.
        
        Args:
            refund: A dictionary containing refund information; required for multi-currency orders.
        
        Returns:
            A dictionary representing the created refund.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request to create the refund fails.
        
        Tags:
            refund, orders, ecommerce, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'refund': refund,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/refunds.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_refund(self, api_version, order_id, refund_id, fields: str | None = None, in_shop_currency: str | None = None) -> dict[str, Any]:
        """
        Retrieves details of a specific refund including specified fields and currency preferences.
        
        Args:
            fields: Comma-separated list of field names to include in the response. If None, returns all fields.
            in_shop_currency: If True, shows amounts in the shop currency for the underlying transaction. Defaults to False.
        
        Returns:
            A dictionary containing the refund details.
        
        Raises:
            HTTPError: If the HTTP request fails or returns a non-2xx status code.
        
        Tags:
            retrieve, refund, orders, http-client, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/refunds/{refund_id}.json"
        query_params = {k: v for k, v in [('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def calculates_arefund(self, api_version, order_id, refund: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Calculates refund transactions for an order based on line items and shipping, optionally handling multi-currency constraints.
        
        Args:
            refund: Dictionary containing refund details (line items, shipping, restock instructions). Must include 'currency' when specifying 'amount' in multi-currency orders.
        
        Returns:
            Dictionary containing suggested refund transactions (including 'kind': 'suggested_refund') and modified restock instructions if applicable.
        
        Raises:
            HTTPError: Raised for failed API requests (e.g., invalid parameters or server errors).
        
        Tags:
            calculate, refund, orders, important, async_job, multi-currency
        """
        # Build the request body from parameters
        request_body_payload = {
            'refund': refund,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/refunds/calculate.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_transactions(self, api_version, order_id, since_id: str | None = None, fields: str | None = None, in_shop_currency: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of transactions, optionally filtered by specified fields, in-shop currency display preference, and transaction ID boundaries.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
            in_shop_currency: Show amounts in the shop currency (default: false).
            since_id: Retrieve only transactions after the specified ID.
        
        Returns:
            Dictionary containing transaction data retrieved from the API.
        
        Raises:
            HTTPError: Raised when the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            retrieve, list, transactions, api, orders, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/transactions.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_atransaction_for_an_order(self, api_version, order_id, transaction: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new transaction for an order, handling the request body and API communication.
        
        Args:
            transaction: Dictionary containing transaction details (keys/values depend on API requirements). Required for multi-currency orders to specify currency.
        
        Returns:
            Dictionary containing the created transaction details as returned by the API.
        
        Raises:
            HTTPError: If the API request fails (e.g., invalid parameters, server error, or authentication issues).
        
        Tags:
            create, transaction, order, important, async_job, api
        """
        # Build the request body from parameters
        request_body_payload = {
            'transaction': transaction,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/transactions.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_an_order_stransactions(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves the count of an order's transactions.
        
        Args:
            None: This function does not require any parameters.
        
        Returns:
            A dictionary containing the transaction count data from the API response.
        
        Raises:
            HTTPError: If the API request fails or returns a non-2XX status code.
        
        Tags:
            orders, transactions, count, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/transactions/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_transaction(self, api_version, order_id, transaction_id, fields: str | None = None, in_shop_currency: str | None = None) -> dict[str, Any]:
        """
        Retrieves a specific transaction from an API endpoint, allowing field selection and currency format control.
        
        Args:
            fields: Show only specified fields (comma-separated list of field names)
            in_shop_currency: Show amounts in shop currency instead of presentment currency (default: false)
        
        Returns:
            Dictionary containing transaction details from the API response
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a 4XX or 5XX status code
        
        Tags:
            retrieve, transaction, orders, api-call, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/transactions/{transaction_id}.json"
        query_params = {k: v for k, v in [('fields', fields), ('in_shop_currency', in_shop_currency)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_gift_cards(self, api_version, status: str | None = None, limit: str | None = None, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of gift cards with optional filters, using Shopify's paginated REST Admin API.
        
        Args:
            fields: Show only specified fields (comma-separated list of field names).
            limit: Maximum number of results to return (default: 50, maximum: 250).
            since_id: Restrict results to those after the specified ID.
            status: Filter gift cards by status (valid status values required).
        
        Returns:
            Dictionary containing the API response data, including gift card details.
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters or server error.
        
        Tags:
            retrieve, list, gift-cards, api, pagination, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards.json"
        query_params = {k: v for k, v in [('status', status), ('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_agift_card(self, api_version, gift_card: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new gift card with the provided details.
        
        Args:
            gift_card: Dictionary containing gift card attributes (e.g., value, recipient, expiration). Required fields depend on API implementation.
        
        Returns:
            Dictionary containing the created gift card details from the API response.
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (e.g., 4xx/5xx status codes)
            ValueError: If required gift card fields are missing or invalid
        
        Tags:
            create, gift-card, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'gift_card': gift_card,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_gift_card(self, api_version, gift_card_id) -> dict[str, Any]:
        """
        Retrieves a single gift card by its ID.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary containing information about the gift card.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request to retrieve the gift card returns an unsuccessful status code.
        
        Tags:
            retrieve, gift-card, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards/{gift_card_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_gift_card(self, api_version, gift_card_id, gift_card: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing gift card, modifying its expiry date, note, and template suffix while preserving the balance.
        
        Args:
            gift_card: A dictionary containing updated gift card fields (excluding balance). Mandatory fields must be included as per API requirements.
        
        Returns:
            A dictionary representing the updated gift card object with current values from the server.
        
        Raises:
            HTTPError: Raised if the API request fails due to invalid data, authentication issues, or server errors.
        
        Tags:
            update, gift-card, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'gift_card': gift_card,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards/{gift_card_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_gift_cards(self, api_version, status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of gift cards filtered by status if provided.
        
        Args:
            status: Annotated[Any, 'Count gift cards with a given status. Valid values: '] (default None). Filters results to cards matching the specified status.
        
        Returns:
            dict[str, Any]: A dictionary containing the count of gift cards and associated metadata from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails or returns a non-2xx status code.
        
        Tags:
            retrieve, gift-cards, count, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards/count.json"
        query_params = {k: v for k, v in [('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def disables_agift_card(self, api_version, gift_card_id, gift_card: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Disables a gift card irreversibly.
        
        Args:
            gift_card: Optional dictionary containing gift card details; defaults to None.
        
        Returns:
            A dictionary containing the response from the server after disabling the gift card.
        
        Raises:
            requests.HTTPError: Raised if an HTTP error occurs while making the request to disable the gift card.
        
        Tags:
            disable, gift-card, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'gift_card': gift_card,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards/{gift_card_id}/disable.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def searches_for_gift_cards(self, api_version, order: str | None = None, query: str | None = None, limit: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Searches for gift cards based on specified criteria, including indexed fields like creation time, balance, and last characters.
        
        Args:
            fields: Comma-separated list of field names to include in the response.
            limit: Maximum number of results to retrieve (default: 50, maximum: 250).
            order: Field and direction to order results by (default: disabled_at DESC).
            query: Text to search for in indexed fields.
        
        Returns:
            Dictionary containing gift card data matching the query parameters.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails, typically due to invalid parameters or authorization issues.
        
        Tags:
            search, gift-cards, pagination, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/gift_cards/search.json"
        query_params = {k: v for k, v in [('order', order), ('query', query), ('limit', limit), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_all_users(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of all users from the API endpoint and returns their data.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing user data in JSON format, typically including user details such as IDs, names, and attributes.
        
        Raises:
            HTTPError: If the HTTP request fails due to network issues, invalid URL, or server-side errors (raised by `response.raise_for_status()`).
        
        Tags:
            list, retrieve, user-management, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/users.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_user(self, api_version, user_id) -> dict[str, Any]:
        """
        Retrieves a single user's data via API request.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            dict[str, Any]: A dictionary containing the retrieved user data.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request returns a status code indicating an HTTP error (4xx/5xx).
        
        Tags:
            retrieve, user, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/users/{user_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_the_currently_logged_in_user(self, api_version) -> dict[str, Any]:
        """
        Retrieves information about the currently authenticated user account using the access token.
        
        Returns:
            Dictionary containing user details from the API response
        
        Raises:
            requests.HTTPError: Raised for invalid requests, expired tokens, or server-side failures
        
        Tags:
            user, authentication, status, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/users/current.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_collects(self, api_version, limit: str | None = None, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of collects (product-collection relationships) from the Shopify API, supporting field filtering and result limitations.
        
        Args:
            fields: Comma-separated list of field names to include in response
            limit: Maximum number of results (1-250), defaults to 50
            since_id: Restrict results to records after the specified ID
        
        Returns:
            Dictionary containing list of collects and API response metadata
        
        Raises:
            requests.HTTPError: If API request fails due to invalid parameters or server error
        
        Tags:
            products, collect, list, shopify-api, pagination, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collects.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def adds_aproduct_to_acustom_collection(self, api_version, collect: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Adds a product to a custom collection by sending a POST request with the specified collection details.
        
        Args:
            collect: A dictionary containing custom collection information. Optional parameter that defaults to None if not provided.
        
        Returns:
            A JSON response from the server containing the result of the operation.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            add, collection, important, products, management
        """
        # Build the request body from parameters
        request_body_payload = {
            'collect': collect,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collects.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_collect_by_its_id(self, api_version, collect_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a specific collect entry from the API by its ID, allowing field selection.
        
        Args:
            fields: Show only specific fields as a comma-separated list of field names. Optional; defaults to None.
        
        Returns:
            Dictionary containing the retrieved collect data structure.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails (e.g., invalid collect ID or server error).
        
        Tags:
            retrieve, collect, api, single-record, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collects/{collect_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def removes_aproduct_from_acollection(self, api_version, collect_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Initiates the removal of a product from a collection via a DELETE request to the API endpoint.
        
        Args:
            request_body: Payload containing product/collection identifiers (format unspecified). Defaults to None.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API containing operation results.
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (non-2xx status codes).
        
        Tags:
            remove, product, collection, management, delete, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collects/{collect_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_collects(self, api_version) -> dict[str, Any]:
        """
        Retrieves a count of collects from the server.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing the count of collects.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            collect, retrieve, important, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collects/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_collection(self, api_version, collection_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single collection from the API, with optional field filtering.
        
        Args:
            fields: Show only certain fields, specified as a comma-separated list of field names. If None, returns all available fields.
        
        Returns:
            A dictionary containing the collection data.
        
        Raises:
            HTTPError: If the API request fails due to network issues or invalid response status
        
        Tags:
            retrieve, collection, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collections/{collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_alist_of_products_belonging_to_acollection(self, api_version, collection_id, limit: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of products associated with a collection, sorted by the collection's configured order.
        
        Args:
            limit: Number of products to retrieve. Default is 50, maximum allowed is 250. Pagination should be handled via response header links per Shopify's API guidelines.
        
        Returns:
            Dictionary containing the product list and metadata per Shopify API's JSON response format.
        
        Raises:
            requests.exceptions.HTTPError: Raised for 4XX/5XX status codes when the API request fails.
        
        Tags:
            retrieve, products, collection, pagination, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collections/{collection_id}/products.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_custom_collections(self, api_version, limit: str | None = None, ids: str | None = None, since_id: str | None = None, title: str | None = None, product_id: str | None = None, handle: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of custom collections based on specified criteria.
        
        Args:
            fields: A comma-separated list of field names to show.
            handle: Filter by custom collection handle.
            ids: A comma-separated list of collection IDs to show.
            limit: The maximum number of results to retrieve (default: 50, maximum: 250).
            product_id: Show custom collections including a given product.
            published_at_max: Show custom collections published before this date (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Show custom collections published after this date (format: 2014-04-25T16:15:47-04:00).
            published_status: Show custom collections with a given published status (default: any).
            since_id: Restrict results to after the specified ID.
            title: Show custom collections with a given title.
            updated_at_max: Show custom collections last updated before this date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Show custom collections last updated after this date (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            A dictionary containing the list of custom collections.
        
        Raises:
            requests.HTTPError: If the HTTP request fails.
        
        Tags:
            retrieve, list, custom, collections, ecommerce, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections.json"
        query_params = {k: v for k, v in [('limit', limit), ('ids', ids), ('since_id', since_id), ('title', title), ('product_id', product_id), ('handle', handle), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acustom_collection(self, api_version, custom_collection: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a custom collection with the provided specification.
        
        Args:
            custom_collection: Optional dictionary specifying the custom collection details (default is None)
        
        Returns:
            A dictionary containing the details of the newly created custom collection.
        
        Raises:
            RequestException: Raised if the HTTP request fails due to network issues or server errors.
        
        Tags:
            collections, custom-collection, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'custom_collection': custom_collection,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_custom_collections(self, api_version, title: str | None = None, product_id: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of custom collections based on various filters like product ID, published date, updated date, published status, and title.
        
        Args:
            product_id: The ID of the product to filter custom collections.
            published_at_max: Maximum published date to filter custom collections (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Minimum published date to filter custom collections (format: 2014-04-25T16:15:47-04:00).
            published_status: The published status of custom collections to filter.
            title: The title of custom collections to filter.
            updated_at_max: Maximum last updated date to filter custom collections (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Minimum last updated date to filter custom collections (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            A dictionary containing the count of custom collections based on the provided filters.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an error.
        
        Tags:
            search, products, custom-collection, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections/count.json"
        query_params = {k: v for k, v in [('title', title), ('product_id', product_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_custom_collection(self, api_version, custom_collection_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a specific custom collection with optional field filtering.
        
        Args:
            fields: A comma-separated list of field names to include in the response. If None, returns all available fields.
        
        Returns:
            A dictionary containing the retrieved custom collection data.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with an HTTP error status (4XX/5XX).
        
        Tags:
            retrieve, products, custom-collection, filtering, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_custom_collection(self, api_version, custom_collection_id, custom_collection: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing custom collection using the provided data.
        
        Args:
            custom_collection: Dictionary containing updated collection data (keys/values vary by implementation)
        
        Returns:
            Dictionary containing the updated custom collection data from the server response
        
        Raises:
            HTTPError: Raised when the API request fails (non-2xx status code)
        
        Tags:
            update, custom-collection, management, products, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'custom_collection': custom_collection,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_acustom_collection(self, api_version, custom_collection_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a custom collection by sending a DELETE request to the API endpoint.
        
        Args:
            request_body: Optional data for the DELETE request. Defaults to None.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API.
        
        Raises:
            requests.HTTPError: If the HTTP request fails. Raised by response.raise_for_status().
        
        Tags:
            delete, custom-collection, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/custom_collections/{custom_collection_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_alist_of_all_product_images(self, api_version, product_id, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieve a list of product images, optionally filtering by specified fields and IDs.
        
        Args:
            fields: A comma-separated list of fields to include in the response
            since_id: Restrict results to after the specified ID
        
        Returns:
            A dictionary containing product images as strings.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an unsuccessful status code.
        
        Tags:
            product, image, list, api-call, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_product_image(self, api_version, product_id, image: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new product image by sending a POST request to the server with the provided image details.
        
        Args:
            image: Optional dictionary containing image data; defaults to None if not provided.
        
        Returns:
            A dictionary containing the response data from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns a status code indicating a problem with the request (4xx or 5xx).
        
        Tags:
            create, image, product, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'image': image,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_acount_of_all_product_images(self, api_version, product_id, since_id: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of all product images optionally filtered by a since ID.
        
        Args:
            since_id: Restrict results to include only product images with IDs after the specified ID.
        
        Returns:
            A JSON response containing counts of product images.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            count, product-image, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images/count.json"
        query_params = {k: v for k, v in [('since_id', since_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_product_image(self, api_version, product_id, image_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single product image by ID with optional field filtering.
        
        Args:
            fields: Comma-separated list of fields to include in the response (None returns all fields)
        
        Returns:
            Dictionary containing product image data from the API response
        
        Raises:
            HTTPError: When the API request fails (non-2xx status code)
        
        Tags:
            retrieve, product-image, api-call, products, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_product_image(self, api_version, product_id, image_id, image: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modify an existing product image by updating its details.
        
        Args:
            image: A dictionary containing image details to be updated.
        
        Returns:
            A dictionary containing the response from the server after updating the image.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            modify, product-image, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'image': image,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_product_image(self, api_version, product_id, image_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Remove an existing product image by sending a delete request to the product management API.
        
        Args:
            request_body: Data containing identifying information for the product image to remove (exact structure depends on API requirements)
        
        Returns:
            dict[str, Any]: API response containing operation status or error details
        
        Raises:
            requests.HTTPError: Raised when the API returns an unsuccessful status code (4xx/5xx)
        
        Tags:
            delete, product-image, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/images/{image_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_product_variants(self, api_version, product_id, limit: str | None = None, presentment_currencies: str | None = None, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of product variants from Shopify's REST Admin API, including fields, currencies, and pagination controls.
        
        Args:
            fields: Comma-separated list of fields to include in response
            limit: Maximum number of results per page (default: 50, max: 250)
            presentment_currencies: Comma-separated list of ISO 4217 currency codes for price formatting
            since_id: Restrict results to variants with IDs greater than specified
        
        Returns:
            Dictionary containing product variant data from the API response
        
        Raises:
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes)
        
        Tags:
            products, product-variant, rest-api, paginated, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/variants.json"
        query_params = {k: v for k, v in [('limit', limit), ('presentment_currencies', presentment_currencies), ('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_product_variant(self, api_version, product_id, variant: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new product variant by sending a POST request to the API.
        
        Args:
            variant: A dictionary containing the product variant attributes (e.g., name, price, inventory). Required fields depend on API specifications.
        
        Returns:
            A dictionary containing the newly created product variant data from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails (e.g., invalid data, authentication errors, or server issues).
        
        Tags:
            create, product, variant, api, post, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'variant': variant,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/variants.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_acount_of_all_product_variants(self, api_version, product_id) -> dict[str, Any]:
        """
        Retrieves a count of all product variants.
        
        Args:
            None: No parameters.
        
        Returns:
            A dictionary containing the count of product variants.
        
        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP error occurs during the request.
        
        Tags:
            products, product-variant, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/variants/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_product_variant(self, api_version, variant_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single product variant by ID.
        
        Args:
            fields: A comma-separated list of fields to include in the response (optional).
        
        Returns:
            A dictionary containing the requested product variant details.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            get, product-variant, retail, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/variants/{variant_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_product_variant(self, api_version, variant_id, variant: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modifies an existing product variant by sending updated details to the API.
        
        Args:
            variant: Dictionary containing the updated product variant details to modify. Must include required fields for identification and updates.
        
        Returns:
            Dictionary containing the API response data with the modified product variant details.
        
        Raises:
            HTTPError: If the API request fails due to invalid data, authentication issues, or server errors.
        
        Tags:
            modify, products, product-variant, update, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'variant': variant,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/variants/{variant_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_product_variant(self, api_version, product_id, variant_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Remove an existing Product Variant from the system.
        
        Args:
            request_body: The data payload containing details of the Product Variant to be removed (typically includes variant identifiers). Defaults to None for empty payloads.
        
        Returns:
            A dictionary containing the API response, typically including success status and/or removed variant details.
        
        Raises:
            HTTPError: Raised when the API request fails, such as invalid variant identifiers, non-existent variants, or network issues.
        
        Tags:
            remove, product, product-variant, management, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}/variants/{variant_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_products(self, api_version, ids: str | None = None, limit: str | None = None, since_id: str | None = None, title: str | None = None, vendor: str | None = None, handle: str | None = None, product_type: str | None = None, collection_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None, fields: str | None = None, presentment_currencies: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of products with filtering options, implementing Shopify's REST Admin API pagination via response headers.
        
        Args:
            collection_id: Filter results by product collection ID.
            created_at_max: Show products created before date (format: 2014-04-25T16:15:47-04:00).
            created_at_min: Show products created after date (format: 2014-04-25T16:15:47-04:00).
            fields: Show only specified fields as comma-separated list.
            handle: Filter results by product handle.
            ids: Return products specified by comma-separated IDs.
            limit: Maximum number of results per page (50-250).
            presentment_currencies: Return prices in specified ISO 4217 currencies as comma-separated codes.
            product_type: Filter results by product type.
            published_at_max: Show products published before date (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Show products published after date (format: 2014-04-25T16:15:47-04:00).
            published_status: Filter by published status (default: any).
            since_id: Restrict results to after specified ID.
            title: Filter results by product title.
            updated_at_max: Show products updated before date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Show products updated after date (format: 2014-04-25T16:15:47-04:00).
            vendor: Filter results by product vendor.
        
        Returns:
            Dictionary containing product data and pagination details in API response format.
        
        Raises:
            HTTPError: When API request fails or returns non-2xx status code.
        
        Tags:
            products, list, retrieve, filter, pagination, api, important, shopify, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products.json"
        query_params = {k: v for k, v in [('ids', ids), ('limit', limit), ('since_id', since_id), ('title', title), ('vendor', vendor), ('handle', handle), ('product_type', product_type), ('collection_id', collection_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields), ('presentment_currencies', presentment_currencies)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_product(self, api_version, product: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new product by sending a POST request with the product details
        
        Args:
            product: An optional dictionary containing product data, including SEO information like metafields_global_title_tag and metafields_global_description_tag
        
        Returns:
            A dictionary with the newly created product details
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails for any reason, such as server errors or invalid responses
        
        Tags:
            create, product, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'product': product,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_products(self, api_version, vendor: str | None = None, product_type: str | None = None, collection_id: str | None = None, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieve the count of products matching specified filter criteria, including collection ID, publication status, date ranges, and vendor details.
        
        Args:
            collection_id: Filter results by collection ID
            created_at_max: Show products created before date (format: 2014-04-25T16:15:47-04:00)
            created_at_min: Show products created after date (format: 2014-04-25T16:15:47-04:00)
            product_type: Filter results by product type
            published_at_max: Show products published before date (format: 2014-04-25T16:15:47-04:00)
            published_at_min: Show products published after date (format: 2014-04-25T16:15:47-04:00)
            published_status: Return products by published status (default: any)
            updated_at_max: Show products last updated before date (format: 2014-04-25T16:15:47-04:00)
            updated_at_min: Show products last updated after date (format: 2014-04-25T16:15:47-04:00)
            vendor: Filter results by product vendor
        
        Returns:
            Dictionary containing the count of products matching the query parameters
        
        Raises:
            HTTPError: If the HTTP request fails due to server errors or invalid parameters
        
        Tags:
            products, search, count, retrieve, filter, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/count.json"
        query_params = {k: v for k, v in [('vendor', vendor), ('product_type', product_type), ('collection_id', collection_id), ('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_product(self, api_version, product_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single product's data from the API.
        
        Args:
            fields: A comma-separated list of fields to include in the response. If None, all available fields are returned by default (None).
        
        Returns:
            A dictionary containing the product's data as returned by the API.
        
        Raises:
            HTTPError: Raised when the API request fails due to an HTTP error (e.g., 404 Not Found if the product doesn't exist).
        
        Tags:
            retrieve, product, api, http-get, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_aproduct(self, api_version, product_id, product: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a product and its associated variants, images, and SEO metadata.
        
        Args:
            product: Dictionary containing product data including optional SEO fields (metafields_global_title_tag and metafields_global_description_tag). None if not provided.
        
        Returns:
            Dictionary containing the updated product details from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests, such as malformed input data or server-side errors, when the API returns a non-2xx status code.
        
        Tags:
            update, products, seo, async_job, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'product': product,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_aproduct(self, api_version, product_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a product from the system by making an HTTP DELETE request to the specified endpoint.
        
        Args:
            request_body: Optional payload data to send with the DELETE request. Typically includes product identifiers or deletion confirmation details.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API containing deletion confirmation or status details.
        
        Raises:
            HTTPError: Raised when the underlying HTTP request fails (non-2xx status code) - includes server error responses, invalid requests, or authorization failures.
        
        Tags:
            delete, products, management, http-client, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/products/{product_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_smart_collections(self, api_version, limit: str | None = None, ids: str | None = None, since_id: str | None = None, title: str | None = None, product_id: str | None = None, handle: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of smart collections with optional filtering by various criteria.
        
        Args:
            fields: Show only certain fields, specified by a comma-separated list of field names.
            handle: Filter results by smart collection handle.
            ids: Show only the smart collections specified by a comma-separated list of IDs.
            limit: The number of results to show. Default is 50, maximum is 250.
            product_id: Show smart collections that include the specified product.
            published_at_max: Show smart collections published before this date (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Show smart collections published after this date (format: 2014-04-25T16:15:47-04:00).
            published_status: Filter results based on the published status of smart collections. Default is any.
            since_id: Restrict results to after the specified ID.
            title: Show smart collections with the specified title.
            updated_at_max: Show smart collections last updated before this date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Show smart collections last updated after this date (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            A dictionary containing the list of smart collections.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request to retrieve smart collections fails.
        
        Tags:
            smart-collection, pagination, shopify-api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections.json"
        query_params = {k: v for k, v in [('limit', limit), ('ids', ids), ('since_id', since_id), ('title', title), ('product_id', product_id), ('handle', handle), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_asmart_collection(self, api_version, smart_collection: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new smart collection using specified rules and configuration.
        
        Args:
            smart_collection: Dictionary containing smart collection configuration including rules and metadata. Required.
        
        Returns:
            Dictionary containing the created smart collection details from the API response.
        
        Raises:
            HTTPError: Raised when the API request fails due to invalid input, network issues, or server errors.
        
        Tags:
            create, smart-collection, management, products, async-job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'smart_collection': smart_collection,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_smart_collections(self, api_version, title: str | None = None, product_id: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None, published_at_min: str | None = None, published_at_max: str | None = None, published_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of smart collections filtered by specified criteria including product association, publication/update timestamps, title, and status.
        
        Args:
            product_id: Show smart collections that include the specified product.
            published_at_max: Show collections published before this date (format: 2014-04-25T16:15:47-04:00).
            published_at_min: Show collections published after this date (format: 2014-04-25T16:15:47-04:00).
            published_status: Filter results by publication status (default: any).
            title: Show collections matching the specified title.
            updated_at_max: Show collections last updated before this date (format: 2014-04-25T16:15:47-04:00).
            updated_at_min: Show collections last updated after this date (format: 2014-04-25T16:15:47-04:00).
        
        Returns:
            Dictionary containing count-related data from the API response.
        
        Raises:
            HTTPError: Raised when the API request fails due to network issues or invalid server responses.
        
        Tags:
            retrieve, count, smart-collections, products, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections/count.json"
        query_params = {k: v for k, v in [('title', title), ('product_id', product_id), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max), ('published_at_min', published_at_min), ('published_at_max', published_at_max), ('published_status', published_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_smart_collection(self, api_version, smart_collection_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single smart collection, optionally specifying fields to include.
        
        Args:
            fields: A comma-separated list of field names to include in the response. Defaults to None, meaning all fields are returned.
        
        Returns:
            A dictionary containing the smart collection details
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails (e.g., due to network errors or invalid responses)
        
        Tags:
            retrieve, smart-collection, important, ecommerce
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_smart_collection(self, api_version, smart_collection_id, smart_collection: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing smart collection with provided parameters.
        
        Args:
            smart_collection: A dictionary containing details to update the smart collection. Defaults to None.
        
        Returns:
            A dictionary representing the updated smart collection.
        
        Raises:
            HTTPError: Raised if the HTTP request for updating the smart collection fails.
        
        Tags:
            update, smart-collection, important, products
        """
        # Build the request body from parameters
        request_body_payload = {
            'smart_collection': smart_collection,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def removes_asmart_collection(self, api_version, smart_collection_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes a smart collection using the provided request data.
        
        Args:
            request_body: Payload containing the smart collection data to remove. Typically includes identifiers like collection ID.
        
        Returns:
            Parsed JSON response from the API containing removal status or confirmation details.
        
        Raises:
            HTTPError: If the API request fails (e.g., invalid request data, authentication failure, or non-existent collection).
        
        Tags:
            remove, smart-collection, api-client, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections/{smart_collection_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_the_ordering_type_of_products_in_asmart_collection(self, api_version, smart_collection_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Updates the ordering type of products in a smart collection via API request.
        
        Args:
            request_body: Payload containing ordering type configuration for the smart collection. Must include required fields for update.
        
        Returns:
            Dictionary containing the API response data with updated collection details.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests, authentication failures, or server errors (4XX/5XX status codes).
        
        Tags:
            update, products, smart-collection, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/smart_collections/{smart_collection_id}/order.json"
        query_params = {}
        response = self._put(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def completes_acheckout(self, api_version, token, request_body: Any | None = None) -> dict[str, Any]:
        """
        Completes a checkout by sending a POST request to the checkout endpoint.
        
        Args:
            request_body: An optional request body for the checkout, annotated with any data type. Defaults to None.
        
        Returns:
            A dictionary containing the JSON response from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            checkout, payment, e-commerce, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/complete.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acheckout(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves checkout details from the specified API endpoint.
        
        Args:
            None: This function does not require arguments (operates on instance data).
        
        Returns:
            dict[str, Any]: A dictionary containing checkout details from the JSON response.
        
        Raises:
            requests.HTTPError: Raised if the API request returns a non-2xx status code.
        
        Tags:
            retrieve, checkout, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modifies_an_existing_checkout(self, api_version, token, checkout: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modifies an existing checkout via HTTP PUT request with provided checkout data.
        
        Args:
            checkout: Dictionary containing checkout data to be modified. Required fields depend on the API specifications.
        
        Returns:
            Dictionary containing the modified checkout details from the API response.
        
        Raises:
            requests.HTTPError: Raised if the API request fails due to client (4XX) or server (5XX) errors.
        
        Tags:
            modify-checkout, sales-channels, checkout-management, http-put, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'checkout': checkout,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_shipping_rates(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves a list of available shipping rates for a checkout
        
        Args:
            None: This function does not accept any parameters
        
        Returns:
            A dictionary containing shipping rates with details such as subtotal, tax, and total price
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request (e.g., network error, HTTP error)
            HTTPError: Raised if the server returns an unsuccessful status code
        
        Tags:
            retrieve, shipping, rates, checkout, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/shipping_rates.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_collection_listings_that_are_published_to_your_app(self, api_version, limit: str | None = None) -> dict[str, Any]:
        """
        Retrieve published collection listings available to your app, implementing pagination via response header links.
        
        Args:
            limit: Amount of results to return (default: 50, maximum: 1000). Note: Sending page parameters will error; pagination is handled through response headers.
        
        Returns:
            Dictionary containing the API response data with collection listings.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails with a non-2xx status code.
        
        Tags:
            retrieve, collection-listing, sales-channels, api-pagination, pagination-header, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collection_listings.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code(self, api_version, collection_listing_id, limit: str | None = None) -> dict[str, Any]:
        """
        Retrieve product IDs published to a specified collection ID from the Shopify REST Admin API, supporting pagination via response headers.
        
        Args:
            limit: Maximum number of product IDs to retrieve (default: 50, max: 1000). Pagination should use the API's header-based mechanism rather than explicit page parameters.
        
        Returns:
            Dictionary containing API response data with product IDs associated with the collection.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails, such as invalid collection ID or rate limiting.
        
        Tags:
            retrieve, product-ids, collection-listing, pagination, http-client, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collection_listings/{collection_listing_id}/product_ids.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_aspecific_collection_listing_that_is_published_to_your_app(self, api_version, collection_listing_id) -> dict[str, Any]:
        """
        Retrieves a specific collection listing published to your app.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary containing details of the collection listing.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            collection-listing, published, important, api-call
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_acollection_listing_to_publish_acollection_to_your_app(self, api_version, collection_listing_id, collection_listing: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates or updates a collection listing to publish a specific collection to the application.
        
        Args:
            collection_listing: A dictionary containing the collection listing data to publish. Represents the collection's configuration and metadata for app integration.
        
        Returns:
            A dictionary containing the API response data after publishing the collection listing, typically including confirmation details and identifiers.
        
        Raises:
            HTTPError: Indicates an API request failure, raised for non-2xx status codes during the HTTP PUT operation.
        
        Tags:
            create, publish, collection-listing, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'collection_listing': collection_listing,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def delete_acollection_listing_to_unpublish_acollection_from_your_app(self, api_version, collection_listing_id, request_body: Any | None = None) -> Any:
        """
        Deletes a collection listing to unpublish it from the app by sending a DELETE request to the API endpoint.
        
        Args:
            request_body: Optional data to include in the DELETE request (type not explicitly specified).
        
        Returns:
            Dictionary containing the JSON response from the API after successful deletion.
        
        Raises:
            HTTPError: Raised if the API request fails (non-2xx status code).
        
        Tags:
            delete, unpublish, collection-listing, api, http, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/collection_listings/{collection_listing_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def stores_acredit_card_in_the_card_vault(self, credit_card: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Stores credit card details in a secure vault and returns a session ID for payment processing.
        
        Args:
            credit_card: Dictionary containing credit card details to be stored in the vault (required for generating session ID)
        
        Returns:
            Dictionary containing the session ID and related vault response data for use in payment processing
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request to the card vault fails
        
        Tags:
            payment, store, vault, session-id, post, checkout, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'credit_card': credit_card,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/https:/elb.deposit.shopifycs.com/sessions"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_payments_on_aparticular_checkout(self, api_version, token) -> dict[str, Any]:
        """
        Retrieves a list of payments for a specific checkout.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing a list of payments for the checkout.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            retrieve, payment, checkout, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/payments.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_anew_payment(self, api_version, token, payment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new payment on a checkout using the provided payment details.
        
        Args:
            payment: An optional dictionary containing payment information.
        
        Returns:
            A dictionary containing the response data for the newly created payment.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            payment, checkout, sales-channel, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'payment': payment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/payments.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_payment(self, api_version, token, payment_id) -> dict[str, Any]:
        """
        Retrieves a single payment by fetching payment information for an existing payment.
        
        Args:
            None: No parameters.
        
        Returns:
            A dictionary containing the payment information.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request is unsuccessful, such as a 4xx or 5xx status code.
        
        Tags:
            payment, fetch, financial, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/payments/{payment_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def counts_the_number_of_payments_attempted_on_acheckout(self, api_version, token) -> dict[str, Any]:
        """
        Counts the number of payments attempted on a checkout
        
        Args:
            None: No parameters
        
        Returns:
            A dictionary containing payment attempt counts
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code
        
        Tags:
            payment, checkout, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/checkouts/{token}/payments/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_product_listings_that_are_published_to_your_app(self, api_version, product_ids: str | None = None, limit: str | None = None, page: str | None = None, collection_id: str | None = None, updated_at_min: str | None = None, handle: str | None = None) -> dict[str, Any]:
        """
        Retrieve product listings that are published to your app.
        
        Args:
            collection_id: Filter by products belonging to a particular collection.
            handle: Filter by product handle.
            limit: Amount of results (default: 50, maximum: 1000). Note: If using pagination, sending 'page' will result in an error.
            page: This parameter should not be used. As of version 2019-07, this endpoint implements pagination by using links in the response header.
            product_ids: A comma-separated list of product IDs.
            updated_at_min: Filter by products last updated after a certain date and time (formatted in ISO 8601).
        
        Returns:
            A dictionary containing product listings.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request, such as a non-200 status code.
        
        Tags:
            management, product-listing, scrape, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings.json"
        query_params = {k: v for k, v in [('product_ids', product_ids), ('limit', limit), ('page', page), ('collection_id', collection_id), ('updated_at_min', updated_at_min), ('handle', handle)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_code_product_ids_code_that_are_published_to_your_app(self, api_version, limit: str | None = None) -> dict[str, Any]:
        """
        Retrieves product IDs published to the associated app, supporting pagination through response headers.
        
        Args:
            limit: Amount of results to retrieve (default: 50, maximum: 1000). Note: Page parameters are not supported - pagination uses response headers per Shopify's 2019-10 API.
        
        Returns:
            Dictionary containing product data returned by Shopify REST Admin API.
        
        Raises:
            HTTPError: When the API request fails or returns invalid response status.
        
        Tags:
            retrieve, product-ids, api-pagination, important, shopify, rest-admin
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings/product_ids.json"
        query_params = {k: v for k, v in [('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_acount_of_products_that_are_published_to_your_app(self, api_version) -> dict[str, Any]:
        """
        Retrieves the count of products published to the associated app.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing the response data with the product count.
        
        Raises:
            HTTPError: If the HTTP request fails due to network issues, invalid authorization, or server-side errors.
        
        Tags:
            retrieve, count, products, app, sales-channels, product-listing, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieve_aspecific_product_listing_that_is_published_to_your_app(self, api_version, product_listing_id) -> dict[str, Any]:
        """
        Retrieve a specific published product listing for your app.
        
        Args:
            None: No parameters are accepted.
        
        Returns:
            A dictionary containing details of the product listing.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, product-listing, published, important, sales-channels
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_aproduct_listing_to_publish_aproduct_to_your_app(self, api_version, product_listing_id, product_listing: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a product listing to publish a product to your app.
        
        Args:
            product_listing: Optional dictionary containing product details. Defaults to None.
        
        Returns:
            A dictionary containing the result of publishing the product listing.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails, indicating an issue with the request or server response.
        
        Tags:
            publish, product-listing, sales-channels, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'product_listing': product_listing,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def delete_aproduct_listing_to_unpublish_aproduct_from_your_app(self, api_version, product_listing_id, request_body: Any | None = None) -> Any:
        """
        Deletes a product listing to remove it from public view in your app's sales channels.
        
        Args:
            request_body: Payload containing data required for product deletion. Typically includes product identifiers.
        
        Returns:
            Parsed JSON response from the API confirming deletion status or containing relevant error details.
        
        Raises:
            HTTPError: Raised if the API request fails, typically due to invalid product IDs, authentication issues, or server errors.
        
        Tags:
            delete, product-listing, sales-channels, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/product_listings/{product_listing_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_alist_of_all_resourcefeedbacks(self, api_version) -> dict[str, Any]:
        """
        Retrieve a list of all ResourceFeedbacks as a dictionary.
        
        Args:
            None: None
        
        Returns:
            A dictionary containing all resource feedbacks.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            resource-feedback, fetch, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/resource_feedback.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_resourcefeedback(self, api_version, resource_feedback: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new resource feedback entry for a Shopify shop resource.
        
        Args:
            resource_feedback: A dictionary containing feedback data for the resource. Must include required fields as per Shopify's API specifications.
        
        Returns:
            A dictionary containing the newly created resource feedback data returned by Shopify's API.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request fails, such as invalid input data or server-side errors.
        
        Tags:
            create, resource-feedback, shopify, sales-channels, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'resource_feedback': resource_feedback,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/resource_feedback.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app(self, api_version, assignment_status: str | None = None, location_ids: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment orders on a shop for a specific app, filtered by assignment status and location IDs.
        
        Args:
            assignment_status: The assignment status of the fulfillment orders that should be returned.
            location_ids: The IDs of the assigned locations of the fulfillment orders that should be returned.
        
        Returns:
            A dictionary containing the JSON response data with fulfillment order details.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails.
        
        Tags:
            shipping-fulfillment, fulfillment-orders, list-retrieval, important, async-job, management
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/assigned_fulfillment_orders.json"
        query_params = {k: v for k, v in [('assignment_status', assignment_status), ('location_ids', location_ids)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def sends_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Sends a cancellation request to the fulfillment service for a fulfillment order.
        
        Args:
            cancellation_request: A dictionary containing cancellation details (keys/values may include reason, fulfillment order ID, or other service-specific fields)
        
        Returns:
            Parsed JSON response from the fulfillment service containing cancellation confirmation or error details
        
        Raises:
            requests.HTTPError: Raised for 4XX/5XX status codes during the HTTP request to the fulfillment service
        
        Tags:
            cancellation, fulfillment, async-job, http-request, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'cancellation_request': cancellation_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def accepts_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Accepts a cancellation request sent to a fulfillment service for a fulfillment order.
        
        Args:
            cancellation_request: Optional dictionary containing details of the cancellation request.
        
        Returns:
            Dictionary containing the response from the fulfillment service.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            cancel, fulfillment, shipping, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'cancellation_request': cancellation_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request/accept.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def rejects_acancellation_request(self, api_version, fulfillment_order_id, cancellation_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Rejects a cancellation request sent to a fulfillment service for a fulfillment order.
        
        Args:
            cancellation_request: Optional cancellation request data as a dictionary (default is None).
        
        Returns:
            A dictionary containing the response from the fulfillment service.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns a status code indicating an error.
        
        Tags:
            shipping, fulfillment, cancel, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'cancellation_request': cancellation_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancellation_request/reject.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_carrier_services(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of carrier services available through the API.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary containing the list of carrier services and their details, typically including service names, IDs, and configurations.
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid permissions, or server errors.
        
        Tags:
            retrieve, list, carrier-services, shipping, fulfillment, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/carrier_services.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acarrier_service(self, api_version, carrier_service: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a carrier service by sending a request with the specified carrier service details.
        
        Args:
            carrier_service: Optional dictionary containing details for the carrier service (default is None).
        
        Returns:
            A dictionary containing the response from creating the carrier service.
        
        Raises:
            HTTPError: Raised when there is an HTTP request exception, such as when the status code is unsuccessful.
        
        Tags:
            management, shipping, fulfillment, carrier-service, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'carrier_service': carrier_service,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/carrier_services.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_carrier_service(self, api_version, carrier_service_id) -> dict[str, Any]:
        """
        Retrieves a single carrier service by its ID.
        
        Args:
            None: No parameters required.
        
        Returns:
            A dictionary containing details of the carrier service.
        
        Raises:
            HTTPError: Raised if the HTTP request fails with an undesirable status code.
        
        Tags:
            shipping, fulfillment, carrier-service, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_acarrier_service(self, api_version, carrier_service_id, carrier_service: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates a carrier service. Only the app that creates a carrier service can update it.
        
        Args:
            carrier_service: Dictionary of carrier service details. Optional; defaults to None.
        
        Returns:
            Dictionary of updated carrier service information.
        
        Raises:
            HTTPError: Raised if the HTTP request to update the carrier service fails.
        
        Tags:
            update, carrier-service, shipping, fulfillment, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'carrier_service': carrier_service,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_acarrier_service(self, api_version, carrier_service_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a carrier service by issuing a DELETE request.
        
        Args:
            request_body: Optional data to be sent in the request body. Type: Annotated[Any, ''], default=None.
        
        Returns:
            JSON response from the server as a dictionary.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, carrier-service, shipping, fulfillment, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/carrier_services/{carrier_service_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_fulfillments_associated_with_an_order(self, api_version, order_id, created_at_max: str | None = None, created_at_min: str | None = None, fields: str | None = None, limit: str | None = None, since_id: str | None = None, updated_at_max: str | None = None, updated_at_min: str | None = None) -> dict[str, Any]:
        """
        Retrieves fulfillments associated with an order based on specified criteria.
        
        Args:
            created_at_max: The maximum created_at date in ISO 8601 format to filter fulfillments. Ex: 2014-04-25T16:15:47-04:00
            created_at_min: The minimum created_at date in ISO 8601 format to filter fulfillments. Ex: 2014-04-25T16:15:47-04:00
            fields: A comma-separated list of fields to include in the response.
            limit: Limit the number of fulfillments returned (default: 50, max: 250).
            since_id: Restrict results to fulfillments with an ID greater than the specified ID.
            updated_at_max: The maximum updated_at date in ISO 8601 format to filter fulfillments. Ex: 2014-04-25T16:15:47-04:00
            updated_at_min: The minimum updated_at date in ISO 8601 format to filter fulfillments. Ex: 2014-04-25T16:15:47-04:00
        
        Returns:
            A dictionary containing the fulfillments associated with the order, following pagination rules.
        
        Raises:
            HTTPError: Raised if the request fails due to an HTTP error.
        
        Tags:
            fulfillment, pagination, shipping, async-job, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments.json"
        query_params = {k: v for k, v in [('created_at_max', created_at_max), ('created_at_min', created_at_min), ('fields', fields), ('limit', limit), ('since_id', since_id), ('updated_at_max', updated_at_max), ('updated_at_min', updated_at_min)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_fulfillment(self, api_version, order_id, fulfillment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Create a new fulfillment for an order, specifying line items and fulfillment details.
        
        Args:
            fulfillment (dict[str, Any]): Dictionary containing fulfillment details, such as line items and tracking information. Defaults to None.
        
        Returns:
            A dictionary representing the newly created fulfillment.
        
        Raises:
            requests.RequestException: Raised if there is an error with the HTTP request, such as a network issue or a non-200 status code.
        
        Tags:
            fulfillment, shipping, e-commerce, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment': fulfillment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_fulfillments_associated_with_afulfillment_order(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves all fulfillments associated with a specified fulfillment order.
        
        Args:
            fulfillment_order_id: The ID of the fulfillment order that is associated with the fulfillments (required).
        
        Returns:
            A dictionary containing fulfillment data in JSON format from the API response.
        
        Raises:
            requests.HTTPError: If the HTTP request fails (non-2xx status code) during API communication.
        
        Tags:
            retrieve, fulfillments, shipping, fulfillment-order, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillments.json"
        query_params = {k: v for k, v in [('fulfillment_order_id', fulfillment_order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_fulfillments_associated_with_aspecific_order(self, api_version, order_id, created_at_min: str | None = None, created_at_max: str | None = None, updated_at_min: str | None = None, updated_at_max: str | None = None) -> dict[str, Any]:
        """
        Retrieves a count of fulfillments associated with a specific order based on date filters.
        
        Args:
            created_at_max: Maximum date to count fulfillments created before (format: YYYY-MM-DDTHH:MM:SSZ).
            created_at_min: Minimum date to count fulfillments created after (format: YYYY-MM-DDTHH:MM:SSZ).
            updated_at_max: Maximum date to count fulfillments last updated before (format: YYYY-MM-DDTHH:MM:SSZ).
            updated_at_min: Minimum date to count fulfillments last updated after (format: YYYY-MM-DDTHH:MM:SSZ).
        
        Returns:
            A dictionary containing the count of fulfillments.
        
        Raises:
            HTTPError: Raised if the HTTP request to retrieve fulfillment count fails.
        
        Tags:
            shipping, fulfillment, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/count.json"
        query_params = {k: v for k, v in [('created_at_min', created_at_min), ('created_at_max', created_at_max), ('updated_at_min', updated_at_min), ('updated_at_max', updated_at_max)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_fulfillment(self, api_version, order_id, fulfillment_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a specific fulfillment entry from the API by making a GET request.
        
        Args:
            fields: Comma-separated list of fields to include in the response. If None, all available fields are returned.
        
        Returns:
            A dictionary containing the fulfillment data as returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with an HTTP error status code.
        
        Tags:
            fulfillment, retrieve, shipping, api, get, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_fulfillment(self, api_version, order_id, fulfillment_id, fulfillment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing fulfillment by modifying its details and returns the updated fulfillment data.
        
        Args:
            fulfillment: A dictionary containing fulfillment details to be updated (keys/values vary by implementation). Use None to skip updates.
        
        Returns:
            Dictionary containing the updated fulfillment data from the API response
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid data, or server errors
        
        Tags:
            fulfillment, update, shipping, management, put-request, api, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment': fulfillment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_afulfillment_for_one_or_many_fulfillment_orders(self, api_version, fulfillment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a fulfillment for one or multiple fulfillment orders associated with the same order at the same location.
        
        Args:
            fulfillment: Dictionary containing fulfillment details for one or more orders (keys/values depend on API requirements)
        
        Returns:
            Dictionary containing API response data with fulfillment creation results
        
        Raises:
            requests.HTTPError: Raised for unsuccessful API responses (4XX/5XX status codes)
            ValueError: Raised if required fulfillment data is missing or invalid
        
        Tags:
            fulfillment, shipping, create, batch, api-integration, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment': fulfillment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillments.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_the_tracking_information_for_afulfillment(self, api_version, fulfillment_id, fulfillment: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates the tracking information for a fulfillment by sending a POST request with the provided fulfillment data.
        
        Args:
            fulfillment: A dictionary containing fulfillment details, defaulting to None if not provided.
        
        Returns:
            A dictionary containing the response data after updating the tracking information.
        
        Raises:
            HTTPError: Raised if the HTTP request fails and no successful status code is returned.
        
        Tags:
            update, fulfillment, shipping, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment': fulfillment,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillments/{fulfillment_id}/update_tracking.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def complete_afulfillment(self, api_version, order_id, fulfillment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Complete a fulfillment by marking it as complete and processing the request.
        
        Args:
            request_body: Optional request body data to be sent with the request
        
        Returns:
            A dictionary containing the response from the fulfillment service
        
        Raises:
            HTTPError: Raised if the HTTP request returns a non-successful status code
        
        Tags:
            fulfillment, shipping, completion, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/complete.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def transition_afulfillment_from_pending_to_open(self, api_version, order_id, fulfillment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Transition a fulfillment from pending to open, marking it as open.
        
        Args:
            request_body: Optional body of the request, defaults to None.
        
        Returns:
            A dictionary containing the response from transitioning the fulfillment status.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            fulfillment, shipping, transition, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/open.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def cancel_afulfillment_for_aspecific_order_id(self, api_version, order_id, fulfillment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Cancels a fulfillment for a specific order ID by sending a POST request to the fulfillment service.
        
        Args:
            request_body: Payload containing details required for cancellation. Typically includes order and fulfillment identifiers.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the fulfillment service after cancellation.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests (4XX client errors) or server processing failures (5XX errors).
        
        Tags:
            cancel, fulfillment, shipping, async-job, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def cancels_afulfillment(self, api_version, fulfillment_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Cancels a fulfillment.
        
        Args:
            request_body: Optional body for the cancel fulfillment request.
        
        Returns:
            A dictionary containing the response from the fulfillment cancellation.
        
        Raises:
            HTTPError: Raised if the HTTP request for fulfillment cancellation fails.
        
        Tags:
            cancel, fulfillment, shipping-management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillments/{fulfillment_id}/cancel.json"
        query_params = {}
        response = self._post(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment(self, api_version, order_id, fulfillment_id) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment events associated with a specific fulfillment.
        
        Args:
            fulfillment_id: The ID of the fulfillment associated with the fulfillment events.
            order_id: The ID of the order associated with the fulfillment events.
        
        Returns:
            A dictionary containing a list of fulfillment events and associated metadata from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to an HTTP error (e.g., 4XX/5XX status codes).
        
        Tags:
            retrieve, list, fulfillment-events, shipping, api, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events.json"
        query_params = {k: v for k, v in [('fulfillment_id', fulfillment_id), ('order_id', order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_afulfillment_event(self, api_version, order_id, fulfillment_id, event: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a fulfillment event by sending a payload to a configured endpoint.
        
        Args:
            event: A dictionary containing the event details to be processed. Must include all required fields for fulfillment event creation.
        
        Returns:
            A dictionary containing the API response data from the fulfillment event creation.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request fails (e.g., network issues, invalid authentication, or server-side errors).
        
        Tags:
            create, fulfillment-event, shipping, api-call, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'event': event,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_fulfillment_event(self, api_version, order_id, fulfillment_id, event_id) -> dict[str, Any]:
        """
        Retrieves a specific fulfillment event from the server.
        
        Args:
            event_id (Any): The ID of the fulfillment event. If not provided, it defaults to None.
        
        Returns:
            A dictionary containing information about the fulfillment event.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the server returns a status code other than 200 OK.
        
        Tags:
            retrieves, fulfillment, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json"
        query_params = {k: v for k, v in [('event_id', event_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def deletes_afulfillment_event(self, api_version, order_id, fulfillment_id, event_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Deletes a fulfillment event.
        
        Args:
            request_body: Optional request body to customize the deletion. Defaults to None.
        
        Returns:
            A dictionary containing JSON data from the server response.
        
        Raises:
            requests.HTTPError: Raised if there is a problem with the HTTP request, such as a non-successful status code.
        
        Tags:
            delete, fulfillment, shipping, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_fulfillment_orders_for_aspecific_order(self, api_version, order_id) -> dict[str, Any]:
        """
        Retrieves a list of fulfillment orders associated with a specific order ID.
        
        Args:
            order_id: The ID of the order that is associated with the fulfillment orders.
        
        Returns:
            A dictionary containing fulfillment order data from the API response.
        
        Raises:
            HTTPError: If the API request fails (e.g., network issues, invalid order_id, or server errors).
        
        Tags:
            retrieve, fulfillment-orders, shipping, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/orders/{order_id}/fulfillment_orders.json"
        query_params = {k: v for k, v in [('order_id', order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_fulfillment_order(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves a specific fulfillment order from a fulfillment service.
        
        Args:
            None: This function does not require any parameters.
        
        Returns:
            A dictionary containing the specifics of the retrieved fulfillment order.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieval, fulfillment, shipping, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def cancel_afulfillment_order(self, api_version, fulfillment_order_id, fulfillment_order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Cancel a fulfillment order by marking it as cancelled.
        
        Args:
            fulfillment_order: An optional dict representing the fulfillment order, defaults to None.
        
        Returns:
            A dict containing the response from the cancellation request.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            cancel, fulfillment, shipping, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_order': fulfillment_order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/cancel.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def marks_afulfillment_order_as_incomplete(self, api_version, fulfillment_order_id, fulfillment_order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Marks an in-progress fulfillment order as incomplete, signaling the fulfillment service cannot ship remaining items and intends to close the order.
        
        Args:
            fulfillment_order: Dictionary containing fulfillment order details to mark as incomplete (default: None)
        
        Returns:
            Dictionary containing the API response data after processing the request
        
        Raises:
            HTTPError: Raised if the API request fails with an HTTP error status code
        
        Tags:
            fulfillment, order-management, shipping, api, async-job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_order': fulfillment_order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/close.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def moves_afulfillment_order_to_anew_location(self, api_version, fulfillment_order_id, fulfillment_order: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Moves an in-progress fulfillment order to a new location, updating the fulfillment service
        warehouse or pick-up point from which the order will be shipped.
        
        Args:
            fulfillment_order: Dictionary containing fulfillment order details, including the new
                location information to which the order should be moved (default: None)
        
        Returns:
            Dictionary containing the API response data after processing the request
        
        Raises:
            HTTPError: Raised if the API request fails with an HTTP error status code
        
        Tags:
            fulfillment, order-management, shipping, api, async-job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_order': fulfillment_order,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/move.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def sends_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Sends a fulfillment request to a fulfillment service.
        
        Args:
            fulfillment_request: A dictionary containing fulfillment request details (e.g., items, shipping preferences). Optional, defaults to None.
        
        Returns:
            A dictionary containing the fulfillment service's response data.
        
        Raises:
            HTTPError: If the HTTP request fails due to network issues, invalid credentials, or server-side errors (raised by response.raise_for_status()).
        
        Tags:
            send, fulfillment, shipping, http, async_job, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_request': fulfillment_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def accepts_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Accepts a fulfillment request sent to a fulfillment service for a fulfillment order.
        
        Args:
            fulfillment_request: A dictionary containing the fulfillment request details; defaults to None.
        
        Returns:
            A dictionary containing the response from the fulfillment service.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            fulfillment, shipping, accept, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_request': fulfillment_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/accept.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def rejects_afulfillment_request(self, api_version, fulfillment_order_id, fulfillment_request: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Rejects a fulfillment request sent to a fulfillment service for a fulfillment order.
        
        Args:
            fulfillment_request: A dictionary containing fulfillment request details (structure depends on service requirements)
        
        Returns:
            Dictionary containing the service response after rejecting the request
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures (4XX client errors or 5XX server errors)
        
        Tags:
            fulfillment, reject, shipping, async-job, management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_request': fulfillment_request,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/reject.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_alist_of_all_fulfillmentservices(self, api_version, scope: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of all FulfillmentServices based on the specified scope.
        
        Args:
            scope: The scope of FulfillmentServices to retrieve (optional).
        
        Returns:
            A dictionary containing all FulfillmentServices.
        
        Raises:
            HTTPError: Raised when the HTTP request to retrieve FulfillmentServices fails.
        
        Tags:
            fulfillment, shipping, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_services.json"
        query_params = {k: v for k, v in [('scope', scope)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def create_anew_fulfillmentservice(self, api_version, fulfillment_service: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Create a new FulfillmentService by sending a POST request to Shopify.
        
        Args:
            fulfillment_service: Optional dictionary containing data for the new fulfillment service.
        
        Returns:
            Dictionary representing the created fulfillment service.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, fulfillment, service, shopify, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_service': fulfillment_service,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_services.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_asingle_fulfillmentservice(self, api_version, fulfillment_service_id) -> dict[str, Any]:
        """
        Receive a single FulfillmentService.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            A dictionary containing information about a FulfillmentService.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request, such as a non-success status code.
        
        Tags:
            fulfillment, shipping, receive, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def modify_an_existing_fulfillmentservice(self, api_version, fulfillment_service_id, fulfillment_service: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Modifies an existing FulfillmentService using a provided dictionary of fulfillment service details.
        
        Args:
            fulfillment_service: A dictionary containing details for the FulfillmentService to be modified (default: None).
        
        Returns:
            A dictionary representing the modified FulfillmentService as returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request to the API fails with an error status code.
        
        Tags:
            modify, fulfillment, shipping, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'fulfillment_service': fulfillment_service,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_fulfillmentservice(self, api_version, fulfillment_service_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes an existing FulfillmentService.
        
        Args:
            request_body: An optional JSON body used in the request. Defaults to None if not provided.
        
        Returns:
            A dictionary response from the server after removing a FulfillmentService.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            fulfillment, shipping, management, important, delete-service
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_services/{fulfillment_service_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to(self, api_version, fulfillment_order_id) -> dict[str, Any]:
        """
        Retrieves a list of locations to which a fulfillment order can potentially move.
        
        Args:
            fulfillment_order_id: The ID of the fulfillment order.
        
        Returns:
            A dictionary containing a list of locations sorted alphabetically by name.
        
        Raises:
            RequestException: Raised if the HTTP request fails (e.g., network errors, server errors).
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            fulfillment, location-management, shipping, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/fulfillment_orders/{fulfillment_order_id}/locations_for_move.json"
        query_params = {k: v for k, v in [('fulfillment_order_id', fulfillment_order_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_the_current_balance(self, api_version) -> dict[str, Any]:
        """
        Retrieve the current balance of an account.
        
        Args:
            None: No parameters required
        
        Returns:
            A dictionary containing the current account balance.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an error (e.g., 4xx or 5xx status code).
        
        Tags:
            balance, shopify-payments, important, get-account-data
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/balance.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_alist_of_all_disputes(self, api_version, since_id: str | None = None, last_id: str | None = None, status: str | None = None, initiated_at: str | None = None) -> dict[str, Any]:
        """
        Retrieve a list of all disputes, filtered by optional parameters for initiate date, IDs, and status. The disputes are ordered by initiation date in descending order.
        
        Args:
            initiated_at: Return only disputes with the specified date (ISO 8601 format).
            last_id: Return only disputes before the specified ID.
            since_id: Return only disputes after the specified ID.
            status: Return only disputes with the specified status.
        
        Returns:
            A dictionary containing the list of disputes.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, dispute, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/disputes.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('status', status), ('initiated_at', initiated_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_asingle_dispute(self, api_version, dispute_id) -> dict[str, Any]:
        """
        Retrieves a single dispute by ID via Shopify Payments.
        
        Args:
            None: This function does not accept any parameters besides the implicit `self`.
        
        Returns:
            A dictionary containing details of the single dispute as retrieved from the API.
        
        Raises:
            HTTPError: Raised if there is an HTTP error (e.g., server response indicates an error).
        
        Tags:
            shopify, payments, dispute, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/disputes/{dispute_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_alist_of_all_payouts(self, api_version, since_id: str | None = None, last_id: str | None = None, date_min: str | None = None, date_max: str | None = None, date: str | None = None, status: str | None = None) -> dict[str, Any]:
        """
        Retrieve a paginated list of payouts ordered by date (most recent first) with filtering options.
        
        Args:
            date: Filter response to payouts on the specified date
            date_max: Filter response to payouts inclusively before the specified date
            date_min: Filter response to payouts inclusively after the specified date
            last_id: Filter response to payouts exclusively before the specified ID
            since_id: Filter response to payouts exclusively after the specified ID
            status: Filter response to payouts with the specified status
        
        Returns:
            Dictionary containing API response data with payout list and pagination metadata (typically JSON-decoded response)
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes)
        
        Tags:
            shopify-payments, payouts, list, filter, pagination, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/payouts.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('date_min', date_min), ('date_max', date_max), ('date', date), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_asingle_payout(self, api_version, payout_id) -> dict[str, Any]:
        """
        Retrieves a single payout by ID from Shopify Payments.
        
        Args:
            None: This method does not accept parameters directly; retrieves payout based on instance state (e.g., configured endpoint in the class).
        
        Returns:
            dict[str, Any]: A dictionary containing payout details (transaction data, timestamps, amount, etc.).
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP requests (4XX/5XX status codes).
        
        Tags:
            shopify-payments, payouts, retrieve, http, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/payouts/{payout_id}.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def return_alist_of_all_balance_transactions(self, api_version, since_id: str | None = None, last_id: str | None = None, test: str | None = None, payout_id: str | None = None, payout_status: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of balance transactions ordered by processing time, with the most recent first. Supports filtering by transaction IDs, payout status, and test mode.
        
        Args:
            last_id: Filter response to transactions exclusively before the specified ID
            payout_id: Filter response to transactions paid out in the specified payout
            payout_status: Filter response to transactions with the specified payout status
            since_id: Filter response to transactions exclusively after the specified ID
            test: Filter response to transactions placed in test mode
        
        Returns:
            A dictionary containing the API response with balance transaction data, typically including transaction details and pagination links in headers
        
        Raises:
            HTTPError: Raised if the API request fails due to network issues, invalid parameters, or authentication errors
        
        Tags:
            retrieve, list, transactions, shopify-payments, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shopify_payments/balance/transactions.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('last_id', last_id), ('test', test), ('payout_id', payout_id), ('payout_status', payout_status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def receive_alist_of_all_countries(self, api_version, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of all countries, optionally filtering by specific fields or since a specified ID.
        
        Args:
            fields: A comma-separated list of field names to include in the response.
            since_id: Restrict results to entries with IDs greater than the specified value.
        
        Returns:
            A dictionary containing the list of countries.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            receive, list, country, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def creates_acountry(self, api_version, country: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Creates a new country entry in the system via API request.
        
        Args:
            country: A dictionary containing country data (required fields depend on API specifications).
        
        Returns:
            Dictionary containing the created country's data from the API response.
        
        Raises:
            requests.HTTPError: Raised when the request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            create, country, api-call, important, data-management
        """
        # Build the request body from parameters
        request_body_payload = {
            'country': country,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries.json"
        query_params = {}
        response = self._post(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_countries(self, api_version) -> dict[str, Any]:
        """
        Retrieves a count of countries from a remote API.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary containing country count information, keyed by string and with values of any type.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, country, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_aspecific_county(self, api_version, country_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific county from an API endpoint, allowing field filtering.
        
        Args:
            fields: Show only specific fields, specified as a comma-separated list of field names. If None, returns all available fields.
        
        Returns:
            Dictionary containing county data structured as key-value pairs. Includes all requested fields or full dataset if no field filtering applied.
        
        Raises:
            requests.HTTPError: Raised when the API request fails due to client or server errors (4XX/5XX status codes).
        
        Tags:
            retrieve, county, api, fields, important, async-jobs
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_country(self, api_version, country_id, country: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing country's data by sending a PUT request to the API endpoint.
        
        Args:
            country: Dictionary containing country data to update. Fields must match API requirements.
        
        Returns:
            Dictionary containing the API response with updated country data.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails (non-2xx status code).
        
        Tags:
            update, country, management, api, put, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'country': country,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def remove_an_existing_country(self, api_version, country_id, request_body: Any | None = None) -> dict[str, Any]:
        """
        Removes an existing country by sending a DELETE request.
        
        Args:
            request_body: Optional request body data; defaults to None.
        
        Returns:
            A dictionary containing the JSON response after deleting the country.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            delete, country, management, api-call, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}.json"
        query_params = {}
        response = self._delete(url, json=request_body, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_currencies_enabled_on_ashop(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of currencies enabled on a shop.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A dictionary mapping currency identifiers to their details.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request to retrieve currency data.
        
        Tags:
            retrieve, currencies, store-properties, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/currencies.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_the_shop_spolicies(self, api_version) -> dict[str, Any]:
        """
        Retrieves a list of the shop's policies including refunds, shipping, and other store-related terms.
        
        Returns:
            dict[str, Any]: A dictionary containing the shop's policy information as parsed JSON data from the API response
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a 4XX/5XX status code
        
        Tags:
            retrieve, list, store-properties, policy, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/policies.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_provinces_for_acountry(self, api_version, country_id, since_id: str | None = None, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a list of provinces for a country, optionally filtering by specific fields and IDs.
        
        Args:
            fields: A comma-separated list of field names to include in the response, allowing selective data retrieval.
            since_id: Restricts results to entries with IDs greater than this value.
        
        Returns:
            A dictionary containing the list of provinces.
        
        Raises:
            requests.HTTPError: Raised when an HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, province, country, import, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}/provinces.json"
        query_params = {k: v for k, v in [('since_id', since_id), ('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_acount_of_provinces_for_acountry(self, api_version, country_id) -> dict[str, Any]:
        """
        Retrieves a count of provinces for a country through an API request.
        
        Args:
            None: This function does not require any parameters.
        
        Returns:
            Dictionary containing the parsed JSON response from the API with province count data.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to invalid authentication, network issues, or invalid endpoint configuration.
        
        Tags:
            retrieve, count, provinces, api, management, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}/provinces/count.json"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_asingle_province_for_acountry(self, api_version, country_id, province_id, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves a single province's details for a specified country from the API.
        
        Args:
            fields: Filters response to show only specified fields (comma-separated list of field names).
        
        Returns:
            Dictionary containing the province data with requested fields.
        
        Raises:
            HTTPException: If the API request fails due to invalid parameters, missing resources, or server errors.
        
        Tags:
            retrieve, province, api, store-properties, geodata, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}/provinces/{province_id}.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def updates_an_existing_province_for_acountry(self, api_version, country_id, province_id, province: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Updates an existing province for a country by sending a PUT request with the new province details.
        
        Args:
            province: A dictionary containing details for the province to be updated.
        
        Returns:
            A dictionary representing the response from the update operation.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request was unsuccessful.
        
        Tags:
            update, province, ai-management, important
        """
        # Build the request body from parameters
        request_body_payload = {
            'province': province,
        }
        request_body_payload = {k: v for k, v in request_body_payload.items() if v is not None}
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/countries/{country_id}/provinces/{province_id}.json"
        query_params = {}
        response = self._put(url, json=request_body_payload, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_the_shop_sconfiguration(self, api_version, fields: str | None = None) -> dict[str, Any]:
        """
        Retrieves the shop's configuration details including specified fields.
        
        Args:
            fields: A comma-separated list of fields to include in the response. If None, returns all available fields.
        
        Returns:
            A dictionary containing the shop's configuration details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails, such as network issues or invalid API responses.
        
        Tags:
            retrieve, shop-configuration, store-properties, shop, important
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/shop.json"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise

    def retrieves_alist_of_tender_transactions(self, api_version, limit: str | None = None, since_id: str | None = None, processed_at_min: str | None = None, processed_at_max: str | None = None, processed_at: str | None = None, order: str | None = None) -> dict[str, Any]:
        """
        Retrieves a paginated list of tender transactions, supporting filters by date ranges, order, and pagination markers. Implements Shopify API pagination via response headers as of version 2019-10.
        
        Args:
            limit: Maximum number of results to retrieve (default: 50, maximum: 250)
            order: Sort order for processed_at field (ascending/descending)
            processed_at: Exact processing date filter
            processed_at_max: Inclusive upper date bound for processing
            processed_at_min: Inclusive lower date bound for processing
            since_id: Retrieve transactions after specified ID
        
        Returns:
            Dictionary containing parsed JSON response with tender transaction data
        
        Raises:
            HTTPError: For non-2xx responses from Shopify API
            ValueError: If invalid date formats or ordering values are provided
        
        Tags:
            tender-transactions, pagination, shopify-api, retrieval, important, financial-transactions
        """
        url = "https://{{store_name}}.myshopify.com/admin/api/{api_version}/tender_transactions.json"
        query_params = {k: v for k, v in [('limit', limit), ('since_id', since_id), ('processed_at_min', processed_at_min), ('processed_at_max', processed_at_max), ('processed_at', processed_at), ('order', order)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
        except Exception as e:
            raise
    def list_tools(self):
        return [
            self.accepts_acancellation_request,
            self.accepts_afulfillment_request,
            self.activates_an_application_charge,
            self.activates_arecurring_application_charge,
            self.adds_aproduct_to_acustom_collection,
            self.adjusts_the_inventory_level_of_an_inventory_item_at_alocation,
            self.approves_acomment,
            self.calculates_arefund,
            self.cancel_afulfillment_for_aspecific_order_id,
            self.cancel_afulfillment_order,
            self.cancels_afulfillment,
            self.cancels_an_order,
            self.cancels_arecurring_application_charge,
            self.closes_an_order,
            self.complete_adraft_order,
            self.complete_afulfillment,
            self.completes_acheckout,
            self.connects_an_inventory_item_to_alocation,
            self.counts_the_number_of_payments_attempted_on_acheckout,
            self.create_acollection_listing_to_publish_acollection_to_your_app,
            self.create_anew_blog,
            self.create_anew_draftorder,
            self.create_anew_fulfillment,
            self.create_anew_fulfillmentservice,
            self.create_anew_page,
            self.create_anew_product_image,
            self.create_anew_product_variant,
            self.create_anew_resourcefeedback,
            self.create_anew_webhook,
            self.create_aproduct_listing_to_publish_aproduct_to_your_app,
            self.creates_acarrier_service,
            self.creates_acheckout,
            self.creates_acomment_for_an_article,
            self.creates_acountry,
            self.creates_acustom_collection,
            self.creates_acustomer,
            self.creates_acustomer_saved_search,
            self.creates_adiscount_code,
            self.creates_adiscount_code_creation_job,
            self.creates_afulfillment_event,
            self.creates_afulfillment_for_one_or_many_fulfillment_orders,
            self.creates_agift_card,
            self.creates_amarketing_event,
            self.creates_an_account_activation_url_for_acustomer,
            self.creates_an_application_charge,
            self.creates_an_application_credit,
            self.creates_an_article_for_ablog,
            self.creates_an_order,
            self.creates_an_order_risk_for_an_order,
            self.creates_anew_address_for_acustomer,
            self.creates_anew_metafield_for_aresource,
            self.creates_anew_payment,
            self.creates_anew_product,
            self.creates_anew_report,
            self.creates_anew_script_tag,
            self.creates_anew_storefrontaccesstoken,
            self.creates_aprice_rule,
            self.creates_arecurring_application_charge,
            self.creates_aredirect,
            self.creates_arefund,
            self.creates_asmart_collection,
            self.creates_atheme,
            self.creates_atransaction_for_an_order,
            self.creates_ausage_charge,
            self.creates_marketing_engagements_on_amarketing_event,
            self.creates_or_updates_an_asset_for_atheme,
            self.delete_acollection_listing_to_unpublish_acollection_from_your_app,
            self.delete_aproduct_listing_to_unpublish_aproduct_from_your_app,
            self.deletes_acarrier_service,
            self.deletes_acustom_collection,
            self.deletes_acustomer,
            self.deletes_acustomer_saved_search,
            self.deletes_adiscount_code,
            self.deletes_afulfillment_event,
            self.deletes_amarketing_event,
            self.deletes_ametafield_by_its_id,
            self.deletes_an_article,
            self.deletes_an_asset_from_atheme,
            self.deletes_an_existing_storefront_access_token,
            self.deletes_an_inventory_level_from_alocation,
            self.deletes_an_order,
            self.deletes_an_order_risk_for_an_order,
            self.deletes_apage,
            self.deletes_aproduct,
            self.deletes_aredirect,
            self.deletes_areport,
            self.deletes_ascript_tag,
            self.disables_agift_card,
            self.marks_acomment_as_not_spam,
            self.marks_acomment_as_spam,
            self.marks_afulfillment_order_as_incomplete,
            self.modifies_an_existing_checkout,
            self.modify_an_existing_blog,
            self.modify_an_existing_draftorder,
            self.modify_an_existing_fulfillment,
            self.modify_an_existing_fulfillmentservice,
            self.modify_an_existing_product_image,
            self.modify_an_existing_product_variant,
            self.modify_an_existing_theme,
            self.modify_an_existing_webhook,
            self.moves_afulfillment_order_to_anew_location,
            self.performs_bulk_operations_for_multiple_customer_addresses,
            self.re_opens_aclosed_order,
            self.receive_acount_of_all_blogs,
            self.receive_acount_of_all_draftorders,
            self.receive_acount_of_all_product_images,
            self.receive_acount_of_all_product_variants,
            self.receive_acount_of_all_webhooks,
            self.receive_alist_of_all_countries,
            self.receive_alist_of_all_fulfillmentservices,
            self.receive_alist_of_all_product_images,
            self.receive_alist_of_all_resourcefeedbacks,
            self.receive_asingle_article,
            self.receive_asingle_blog,
            self.receive_asingle_draftorder,
            self.receive_asingle_fulfillment,
            self.receive_asingle_fulfillmentservice,
            self.receive_asingle_product_image,
            self.receive_asingle_product_variant,
            self.receive_asingle_webhook,
            self.rejects_acancellation_request,
            self.rejects_afulfillment_request,
            self.remove_an_existing_blog,
            self.remove_an_existing_country,
            self.remove_an_existing_draftorder,
            self.remove_an_existing_fulfillmentservice,
            self.remove_an_existing_pricerule,
            self.remove_an_existing_product_image,
            self.remove_an_existing_product_variant,
            self.remove_an_existing_theme,
            self.remove_an_existing_webhook,
            self.removes_acomment,
            self.removes_an_address_from_acustomer_saddress_list,
            self.removes_aproduct_from_acollection,
            self.removes_asmart_collection,
            self.restores_apreviously_removed_comment,
            self.retrieve_acount_of_products_that_are_published_to_your_app,
            self.retrieve_alist_of_all_blogs,
            self.retrieve_alist_of_products_belonging_to_acollection,
            self.retrieve_aspecific_collection_listing_that_is_published_to_your_app,
            self.retrieve_aspecific_product_listing_that_is_published_to_your_app,
            self.retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code,
            self.retrieve_code_product_ids_code_that_are_published_to_your_app,
            self.retrieve_collection_listings_that_are_published_to_your_app,
            self.retrieve_product_listings_that_are_published_to_your_app,
            self.retrieves_acheckout,
            self.retrieves_acount_of_all_articles_from_ablog,
            self.retrieves_acount_of_all_customer_saved_searches,
            self.retrieves_acount_of_all_marketing_events,
            self.retrieves_acount_of_all_price_rules,
            self.retrieves_acount_of_all_script_tags,
            self.retrieves_acount_of_an_order_stransactions,
            self.retrieves_acount_of_aresource_smetafields,
            self.retrieves_acount_of_checkouts,
            self.retrieves_acount_of_collects,
            self.retrieves_acount_of_comments,
            self.retrieves_acount_of_countries,
            self.retrieves_acount_of_custom_collections,
            self.retrieves_acount_of_customers,
            self.retrieves_acount_of_events,
            self.retrieves_acount_of_fulfillments_associated_with_aspecific_order,
            self.retrieves_acount_of_gift_cards,
            self.retrieves_acount_of_locations,
            self.retrieves_acount_of_products,
            self.retrieves_acount_of_provinces_for_acountry,
            self.retrieves_acount_of_smart_collections,
            self.retrieves_acount_of_url_redirects,
            self.retrieves_adiscount_code_creation_job,
            self.retrieves_alist_of_abandoned_checkouts,
            self.retrieves_alist_of_access_scopes_associated_to_the_access_token,
            self.retrieves_alist_of_addresses_for_acustomer,
            self.retrieves_alist_of_all_article_authors,
            self.retrieves_alist_of_all_article_tags,
            self.retrieves_alist_of_all_articles_from_ablog,
            self.retrieves_alist_of_all_marketing_events,
            self.retrieves_alist_of_all_order_risks_for_an_order,
            self.retrieves_alist_of_all_script_tags,
            self.retrieves_alist_of_all_users,
            self.retrieves_alist_of_application_charges,
            self.retrieves_alist_of_assets_for_atheme,
            self.retrieves_alist_of_carrier_services,
            self.retrieves_alist_of_collects,
            self.retrieves_alist_of_comments,
            self.retrieves_alist_of_currencies_enabled_on_ashop,
            self.retrieves_alist_of_custom_collections,
            self.retrieves_alist_of_customer_saved_searches,
            self.retrieves_alist_of_customers,
            self.retrieves_alist_of_discount_codes,
            self.retrieves_alist_of_discount_codes_for_adiscount_code_creation_job,
            self.retrieves_alist_of_draft_orders,
            self.retrieves_alist_of_events,
            self.retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment,
            self.retrieves_alist_of_fulfillment_orders_for_aspecific_order,
            self.retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app,
            self.retrieves_alist_of_gift_cards,
            self.retrieves_alist_of_inventory_items,
            self.retrieves_alist_of_inventory_levels,
            self.retrieves_alist_of_inventory_levels_for_alocation,
            self.retrieves_alist_of_locations,
            self.retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to,
            self.retrieves_alist_of_metafields_that_belong_to_aresource,
            self.retrieves_alist_of_orders,
            self.retrieves_alist_of_pages,
            self.retrieves_alist_of_payments_on_aparticular_checkout,
            self.retrieves_alist_of_price_rules,
            self.retrieves_alist_of_product_variants,
            self.retrieves_alist_of_products,
            self.retrieves_alist_of_provinces_for_acountry,
            self.retrieves_alist_of_recurring_application_charges,
            self.retrieves_alist_of_refunds_for_an_order,
            self.retrieves_alist_of_reports,
            self.retrieves_alist_of_shipping_rates,
            self.retrieves_alist_of_smart_collections,
            self.retrieves_alist_of_storefront_access_tokens_that_have_been_issued,
            self.retrieves_alist_of_tender_transactions,
            self.retrieves_alist_of_the_shop_spolicies,
            self.retrieves_alist_of_themes,
            self.retrieves_alist_of_transactions,
            self.retrieves_alist_of_url_redirects,
            self.retrieves_alist_of_usage_charges,
            self.retrieves_alist_of_webhooks,
            self.retrieves_all_application_credits,
            self.retrieves_all_customers_returned_by_acustomer_saved_search,
            self.retrieves_all_orders_belonging_to_acustomer,
            self.retrieves_an_application_charge,
            self.retrieves_an_order_count,
            self.retrieves_apage_count,
            self.retrieves_asingle_application_credit,
            self.retrieves_asingle_carrier_service,
            self.retrieves_asingle_charge,
            self.retrieves_asingle_charge1,
            self.retrieves_asingle_collection,
            self.retrieves_asingle_comment_by_its_id,
            self.retrieves_asingle_custom_collection,
            self.retrieves_asingle_customer,
            self.retrieves_asingle_customer_saved_search,
            self.retrieves_asingle_discount_code,
            self.retrieves_asingle_event,
            self.retrieves_asingle_gift_card,
            self.retrieves_asingle_inventory_item_by_id,
            self.retrieves_asingle_location_by_its_id,
            self.retrieves_asingle_marketing_event,
            self.retrieves_asingle_metafield_from_aresource_by_its_id,
            self.retrieves_asingle_order_risk_by_its_id,
            self.retrieves_asingle_page_by_its_id,
            self.retrieves_asingle_payment,
            self.retrieves_asingle_price_rule,
            self.retrieves_asingle_product,
            self.retrieves_asingle_province_for_acountry,
            self.retrieves_asingle_redirect,
            self.retrieves_asingle_report,
            self.retrieves_asingle_script_tag,
            self.retrieves_asingle_smart_collection,
            self.retrieves_asingle_theme,
            self.retrieves_asingle_user,
            self.retrieves_aspecific_collect_by_its_id,
            self.retrieves_aspecific_county,
            self.retrieves_aspecific_fulfillment_event,
            self.retrieves_aspecific_fulfillment_order,
            self.retrieves_aspecific_order,
            self.retrieves_aspecific_refund,
            self.retrieves_aspecific_transaction,
            self.retrieves_details_for_asingle_customer_address,
            self.retrieves_fulfillments_associated_with_afulfillment_order,
            self.retrieves_fulfillments_associated_with_an_order,
            self.retrieves_the_currently_logged_in_user,
            self.retrieves_the_location_of_adiscount_code,
            self.retrieves_the_shop_sconfiguration,
            self.return_alist_of_all_balance_transactions,
            self.return_alist_of_all_disputes,
            self.return_alist_of_all_payouts,
            self.return_asingle_dispute,
            self.return_asingle_payout,
            self.return_the_current_balance,
            self.searches_for_customers_that_match_asupplied_query,
            self.searches_for_gift_cards,
            self.send_an_invoice,
            self.sends_acancellation_request,
            self.sends_afulfillment_request,
            self.sends_an_account_invite_to_acustomer,
            self.sets_the_default_address_for_acustomer,
            self.sets_the_inventory_level_for_an_inventory_item_at_alocation,
            self.stores_acredit_card_in_the_card_vault,
            self.transition_afulfillment_from_pending_to_open,
            self.updates_acarrier_service,
            self.updates_acomment_of_an_article,
            self.updates_acustomer,
            self.updates_acustomer_saved_search,
            self.updates_amarketing_event,
            self.updates_ametafield,
            self.updates_an_article,
            self.updates_an_existing_aprice_rule,
            self.updates_an_existing_country,
            self.updates_an_existing_custom_collection,
            self.updates_an_existing_customer_address,
            self.updates_an_existing_discount_code,
            self.updates_an_existing_gift_card,
            self.updates_an_existing_inventory_item,
            self.updates_an_existing_province_for_acountry,
            self.updates_an_existing_redirect,
            self.updates_an_existing_smart_collection,
            self.updates_an_order,
            self.updates_an_order_risk,
            self.updates_apage,
            self.updates_aproduct,
            self.updates_areport,
            self.updates_ascript_tag,
            self.updates_the_capped_amount_of_arecurring_application_charge,
            self.updates_the_ordering_type_of_products_in_asmart_collection,
            self.updates_the_tracking_information_for_afulfillment
        ]
