# Universal Mcp Shopify MCP Server

An MCP Server for the Universal Mcp Shopify API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_shopify/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Shopify API.


Here is the markdown table summarizing the tools in the `ShopifyApp` class:

| Tool                                                                      | Description                                                                                                                               |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `retrieves_alist_of_access_scopes_associated_to_the_access_token`         | Retrieves access scopes associated with the current authentication token.                                                                 |
| `retrieves_alist_of_storefront_access_tokens_that_have_been_issued`       | Retrieves a list of issued storefront access tokens.                                                                                      |
| `creates_anew_storefrontaccesstoken`                                      | Creates a new Storefront Access Token.                                                                                                    |
| `deletes_an_existing_storefront_access_token`                             | Deletes an existing storefront access token.                                                                                              |
| `retrieves_alist_of_reports`                                              | Retrieves a list of reports based on the specified filters and parameters.                                                                |
| `creates_anew_report`                                                     | Creates a new report by sending a POST request with the provided report data to a specific URL.                                           |
| `retrieves_asingle_report`                                                | Retrieves a single report from the application.                                                                                           |
| `updates_areport`                                                         | Updates an existing report by sending a PUT request to the API endpoint with the provided report data.                                  |
| `deletes_areport`                                                         | Deletes a report by making a DELETE request to the API endpoint.                                                                          |
| `retrieves_alist_of_application_charges`                                  | Retrieves a list of application charges from the API, filtered by specified criteria.                                                     |
| `creates_an_application_charge`                                           | Creates a new application charge for billing purposes.                                                                                    |
| `retrieves_an_application_charge`                                         | Retrieves application charge details from the billing system.                                                                             |
| `activates_an_application_charge`                                         | Activates an accepted application charge.                                                                                                 |
| `retrieves_all_application_credits`                                       | Retrieves all application credits from the server.                                                                                        |
| `creates_an_application_credit`                                           | Creates an application credit by sending a POST request to the API endpoint.                                                              |
| `retrieves_asingle_application_credit`                                    | Retrieves a single application credit from the API, including specified fields.                                                           |
| `retrieves_alist_of_recurring_application_charges`                        | Retrieves a list of recurring application charges with optional filtering parameters.                                                     |
| `creates_arecurring_application_charge`                                   | Creates a recurring application charge.                                                                                                   |
| `retrieves_asingle_charge`                                                | Retrieves a single charge's data from the API, including specified fields.                                                                |
| `cancels_arecurring_application_charge`                                   | Cancels a recurring application charge, typically used in billing systems to stop periodic charges.                                       |
| `activates_arecurring_application_charge`                                 | Activates a previously accepted recurring application charge.                                                                             |
| `updates_the_capped_amount_of_arecurring_application_charge`              | Updates the capped amount of an active recurring application charge.                                                                      |
| `retrieves_alist_of_usage_charges`                                        | Retrieves a list of usage charges from a specified endpoint.                                                                              |
| `creates_ausage_charge`                                                   | Creates a usage charge for a billing resource, typically in a SaaS or subscription-based system.                                          |
| `retrieves_asingle_charge1`                                               | Retrieves a single charge including specified fields from the API.                                                                        |
| `retrieves_alist_of_addresses_for_acustomer`                              | Retrieves a list of addresses for a customer.                                                                                             |
| `creates_anew_address_for_acustomer`                                      | Creates a new address for a customer by sending a POST request with the provided address details.                                         |
| `retrieves_details_for_asingle_customer_address`                          | Retrieves details for a customer's address by making a GET request to the specified API endpoint.                                       |
| `updates_an_existing_customer_address`                                    | Updates an existing customer address by sending a PUT request with the new address details.                                               |
| `removes_an_address_from_acustomer_saddress_list`                         | Removes a specified address from a customer's address list by sending a DELETE request.                                                   |
| `performs_bulk_operations_for_multiple_customer_addresses`                | Performs bulk operations on multiple customer addresses using a provided request body.                                                    |
| `sets_the_default_address_for_acustomer`                                  | Sets the default address for a customer.                                                                                                  |
| `retrieves_alist_of_customers`                                            | Retrieves a list of customers based on specified criteria, including creation and update dates, customer IDs, and select fields.          |
| `creates_acustomer`                                                       | Creates a new customer record by sending customer data to the API endpoint.                                                               |
| `searches_for_customers_that_match_asupplied_query`                       | Searches for customers that match a supplied query, allowing filtering by fields, limit, ordering, and query text.                        |
| `retrieves_asingle_customer`                                              | Retrieves information about a single customer, allowing specification of which fields to include.                                         |
| `updates_acustomer`                                                       | Updates a customer by sending a PUT request with the provided customer data.                                                              |
| `deletes_acustomer`                                                       | Deletes a customer from the system if they have no existing orders.                                                                       |
| `creates_an_account_activation_url_for_acustomer`                         | Generates a one-time-use account activation URL for a customer with an inactive account.                                                  |
| `sends_an_account_invite_to_acustomer`                                    | Sends an account invitation to a customer via API request.                                                                                |
| `retrieves_acount_of_customers`                                           | Retrieves a count of all customers from the API endpoint.                                                                                 |
| `retrieves_all_orders_belonging_to_acustomer`                             | Retrieves all orders belonging to a customer.                                                                                             |
| `retrieves_alist_of_customer_saved_searches`                              | Retrieves a list of customer saved searches with pagination support via response headers.                                                 |
| `creates_acustomer_saved_search`                                          | Creates a customer saved search using the provided data.                                                                                  |
| `retrieves_acount_of_all_customer_saved_searches`                         | Retrieves a count of all customer saved searches, optionally filtering results to after a specified ID.                                   |
| `retrieves_asingle_customer_saved_search`                                 | Retrieves a single customer saved search.                                                                                                 |
| `updates_acustomer_saved_search`                                          | Updates a customer saved search by sending a PUT request to the specified URL.                                                            |
| `deletes_acustomer_saved_search`                                          | Deletes a customer saved search from the system.                                                                                          |
| `retrieves_all_customers_returned_by_acustomer_saved_search`              | Retrieves all customers associated with a customer saved search using specified filters and ordering.                                     |
| `retrieves_alist_of_discount_codes`                                       | Retrieves a paginated list of discount codes from the Shopify REST Admin API, adhering to API version 2019-10 pagination rules.           |
| `creates_adiscount_code`                                                  | Creates a discount code by sending a POST request with the specified parameters.                                                          |
| `retrieves_asingle_discount_code`                                         | Retrieves a single discount code.                                                                                                         |
| `updates_an_existing_discount_code`                                       | Updates an existing discount code with new data via a PUT request.                                                                        |
| `deletes_adiscount_code`                                                  | Deletes a discount code by sending a DELETE request to the API endpoint.                                                                  |
| `retrieves_the_location_of_adiscount_code`                                | Retrieves the location of a discount code via HTTP response headers.                                                                      |
| `creates_adiscount_code_creation_job`                                     | Creates an asynchronous batch job to generate discount codes, enqueuing the request for background processing.                          |
| `retrieves_adiscount_code_creation_job`                                   | Retrieves details of a discount code creation job from the API.                                                                           |
| `retrieves_alist_of_discount_codes_for_adiscount_code_creation_job`       | Retrieves a list of discount codes for a discount code creation job.                                                                      |
| `retrieves_alist_of_price_rules`                                          | Retrieves a list of price rules with optional filters for creation, update, start/end dates, and usage history, following Shopify's... |
| `creates_aprice_rule`                                                     | Creates a new price rule based on the provided parameters.                                                                                |
| `retrieves_asingle_price_rule`                                            | Retrieves a single price rule from the server.                                                                                            |
| `updates_an_existing_aprice_rule`                                         | Updates an existing price rule with new parameters.                                                                                       |
| `remove_an_existing_pricerule`                                            | Delete an existing PriceRule using the provided request body to specify which rule to remove.                                             |
| `retrieves_acount_of_all_price_rules`                                     | Retrieves a count of all price rules from the API endpoint.                                                                               |
| `retrieves_alist_of_events`                                               | Retrieves a list of events with optional pagination and filtering capabilities.                                                           |
| `retrieves_asingle_event`                                                 | Retrieves a single event by its ID, optionally specifying which fields to include.                                                        |
| `retrieves_acount_of_events`                                              | Retrieves a count of events based on the specified creation time range.                                                                   |
| `retrieves_alist_of_webhooks`                                             | Retrieves a paginated list of webhook subscriptions filtered by specified criteria such as date ranges, address, topic, and ID.             |
| `create_anew_webhook`                                                     | Creates a new webhook subscription by sending a POST request with a webhook configuration.                                              |
| `receive_acount_of_all_webhooks`                                          | Retrieves a count of existing webhook subscriptions based on specified filters.                                                           |
| `receive_asingle_webhook`                                                 | Retrieves a single webhook subscription from the API endpoint.                                                                            |
| `modify_an_existing_webhook`                                              | Modify an existing webhook by updating its subscription's topic or address URIs.                                                          |
| `remove_an_existing_webhook`                                              | Deletes an existing webhook subscription by sending a delete request to the API endpoint.                                                 |
| `retrieves_alist_of_inventory_items`                                      | Retrieves a list of inventory items based on provided IDs and a specified limit.                                                          |
| `retrieves_asingle_inventory_item_by_id`                                  | Retrieves a single inventory item by ID from a specified inventory source.                                                                |
| `updates_an_existing_inventory_item`                                      | Updates an existing inventory item by sending a PUT request with the provided item details.                                               |
| `retrieves_alist_of_inventory_levels`                                     | Retrieves a list of inventory levels based on specified parameters                                                                        |
| `deletes_an_inventory_level_from_alocation`                               | Deletes an inventory level of an inventory item at a specified location.                                                                  |
| `adjusts_the_inventory_level_of_an_inventory_item_at_alocation`             | Adjusts inventory levels for a specific item at a given location.                                                                         |
| `connects_an_inventory_item_to_alocation`                                 | Connects an inventory item to a specific location by creating an inventory level at that location.                                        |
| `sets_the_inventory_level_for_an_inventory_item_at_alocation`             | Updates the available inventory quantity for a specific item at a designated location, automatically connecting the location if not... |
| `retrieves_alist_of_locations`                                            | Retrieves a list of locations from the API endpoint.                                                                                      |
| `retrieves_asingle_location_by_its_id`                                    | Retrieves a single location by its unique identifier from the inventory system.                                                           |
| `retrieves_acount_of_locations`                                           | Retrieves the count of locations from the API.                                                                                            |
| `retrieves_alist_of_inventory_levels_for_alocation`                       | Retrieves a dictionary of inventory levels for a location.                                                                                |
| `retrieves_alist_of_all_marketing_events`                                 | Retrieves a list of all marketing events with pagination based on provided limit and offset.                                              |
| `creates_amarketing_event`                                                | Creates a marketing event by sending a POST request with the provided marketing event data.                                               |
| `retrieves_acount_of_all_marketing_events`                                | Retrieves a count of all marketing events.                                                                                                |
| `retrieves_asingle_marketing_event`                                       | Retrieves a single marketing event's details from the API endpoint.                                                                       |
| `updates_amarketing_event`                                                | Updates an existing marketing event by sending the provided data to the API endpoint.                                                     |
| `deletes_amarketing_event`                                                | Deletes a marketing event by sending a DELETE request to the specified base URL.                                                          |
| `creates_marketing_engagements_on_amarketing_event`                       | Creates or updates marketing engagements for a marketing event, with daily aggregation and overwrites for existing entries on the same date. |
| `retrieves_alist_of_metafields_that_belong_to_aresource`                  | Retrieves a list of metafields belonging to a resource using pagination via response headers (note: explicit pagination parameters are... |
| `creates_anew_metafield_for_aresource`                                    | Creates a new metafield for a resource by sending a POST request with the provided metafield details.                                     |
| `retrieves_acount_of_aresource_smetafields`                               | Retrieves the count of a resource's metafields.                                                                                           |
| `retrieves_asingle_metafield_from_aresource_by_its_id`                    | Retrieves a single metafield from a specified resource by its ID.                                                                         |
| `updates_ametafield`                                                      | Updates a metafield by sending a PUT request with the provided metafield data.                                                            |
| `deletes_ametafield_by_its_id`                                            | Deletes a metafield by its ID.                                                                                                            |
| `retrieves_alist_of_all_articles_from_ablog`                              | Retrieve a paginated list of blog articles with filtering options via Shopify's REST Admin API.                                           |
| `creates_an_article_for_ablog`                                            | Creates an article entry for a blog by sending a POST request to the API endpoint.                                                        |
| `retrieves_acount_of_all_articles_from_ablog`                             | Retrieves a count of articles from a blog based on specified creation, publication, and update dates, as well as publication status.      |
| `receive_asingle_article`                                                 | Retrieve a single article from an online source.                                                                                          |
| `updates_an_article`                                                      | Updates an article by sending a PUT request with the provided article data.                                                               |
| `deletes_an_article`                                                      | Deletes an article by sending a DELETE request to the specified URL.                                                                      |
| `retrieves_alist_of_all_article_authors`                                  | Retrieves a list of all article authors.                                                                                                  |
| `retrieves_alist_of_all_article_tags`                                     | Retrieves a list of all article tags with optional filtering by popularity and limit.                                                     |
| `retrieves_alist_of_assets_for_atheme`                                    | Retrieves a list of assets for a theme, returning metadata about each asset.                                                              |
| `creates_or_updates_an_asset_for_atheme`                                  | Creates or updates an asset for a theme by sending a PUT request.                                                                         |
| `deletes_an_asset_from_atheme`                                            | Deletes an asset from a theme by sending a DELETE request to a specified URL.                                                             |
| `retrieve_alist_of_all_blogs`                                             | Retrieve a paginated list of blogs from the Shopify REST Admin API, supporting field selection, filtering, and result limiting.             |
| `create_anew_blog`                                                        | Create a new blog with the provided blog details.                                                                                         |
| `receive_acount_of_all_blogs`                                             | Retrieve a count of all blogs from a remote endpoint.                                                                                     |
| `receive_asingle_blog`                                                    | Retrieves a single Blog by its ID, optionally specifying fields to include in the response.                                               |
| `modify_an_existing_blog`                                                 | Modifies an existing blog by sending a PUT request with the provided blog data.                                                           |
| `remove_an_existing_blog`                                                 | Removes an existing blog by sending a delete request to the specified endpoint.                                                           |
| `retrieves_alist_of_comments`                                             | Retrieves a list of comments based on various filter criteria, including creation and publication dates, fields, limit, and status.       |
| `creates_acomment_for_an_article`                                         | Creates a new comment for an article by sending a POST request to the API endpoint.                                                       |
| `retrieves_acount_of_comments`                                            | Retrieves the count of comments filtered by creation, update, publication dates, and statuses.                                          |
| `retrieves_asingle_comment_by_its_id`                                     | Retrieves a single comment by its unique identifier from the API.                                                                         |
| `updates_acomment_of_an_article`                                          | Updates a specific comment on an article by sending a PUT request with the updated comment details.                                       |
| `marks_acomment_as_spam`                                                  | Marks a comment as spam by sending a POST request to the target URL with provided request body                                            |
| `marks_acomment_as_not_spam`                                              | Marks a comment as not spam by sending a POST request to the server.                                                                      |
| `approves_acomment`                                                       | Approves a comment in an online store system.                                                                                             |
| `removes_acomment`                                                        | Removes a comment by sending a POST request to the specified URL endpoint.                                                                |
| `restores_apreviously_removed_comment`                                    | Restores a previously removed comment.                                                                                                    |
| `retrieves_alist_of_pages`                                                | Retrieves a list of pages from the Shopify REST Admin API with pagination support via response header links.                              |
| `create_anew_page`                                                        | Creates a new page with the provided data.                                                                                                |
| `retrieves_apage_count`                                                   | Retrieves a page count based on specified filters like creation, publication, and update dates, page title, and publication status.     |
| `retrieves_asingle_page_by_its_id`                                        | Retrieves a single page by its ID, optionally selecting specific fields.                                                                  |
| `updates_apage`                                                           | Updates a specific page with the provided data.                                                                                           |
| `deletes_apage`                                                           | Deletes a page based on the provided request body.                                                                                        |
| `retrieves_alist_of_url_redirects`                                        | Retrieves a list of URL redirects with optional filtering parameters. Results are paginated through response headers (page parameters... |
| `creates_aredirect`                                                       | Creates a redirect by sending a POST request to the server with the redirect details.                                                     |
| `retrieves_acount_of_url_redirects`                                       | Retrieves a count of URL redirects matching specified path and/or target parameters.                                                      |
| `retrieves_asingle_redirect`                                              | Retrieves details of a single redirect entry from the API.                                                                                |
| `updates_an_existing_redirect`                                            | Updates an existing redirect by sending a PUT request with the specified redirect details.                                                |
| `deletes_aredirect`                                                       | Deletes a redirect from the system using provided request data.                                                                           |
| `retrieves_alist_of_all_script_tags`                                      | Retrieves a list of all script tags with optional filters such as creation date, update date, and source URL.                          |
| `creates_anew_script_tag`                                                 | Creates a new script tag resource by making a POST request to the API endpoint.                                                           |
| `retrieves_acount_of_all_script_tags`                                     | Retrieves a count of script tags from an online store, optionally filtered by source URL.                                                 |
| `retrieves_asingle_script_tag`                                            | Retrieves a single script tag from the online store with specified response fields.                                                       |
| `updates_ascript_tag`                                                     | Updates a script tag in an online store by sending a PUT request with the provided script tag details.                                    |
| `deletes_ascript_tag`                                                     | Deletes a script tag from the system.                                                                                                     |
| `retrieves_alist_of_themes`                                               | Retrieves a list of themes from the online store with optional field filtering.                                                           |
| `creates_atheme`                                                          | Creates a theme for an online store using a provided configuration. The theme is created as unpublished by default unless explicitly... |
| `retrieves_asingle_theme`                                                 | Retrieves a single theme from the server.                                                                                                 |
| `modify_an_existing_theme`                                                | Updates an existing theme by sending a modified theme configuration to the API.                                                           |
| `remove_an_existing_theme`                                                | Remove an existing theme by deleting it from the specified system.                                                                        |
| `retrieves_acount_of_checkouts`                                           | Retrieves a count of checkouts based on specified filters like creation date, status, and update date.                                  |
| `retrieves_alist_of_abandoned_checkouts`                                  | Retrieves a paginated list of abandoned checkouts with optional filtering based on creation/update timestamps, status, and ID ranges.   |
| `creates_acheckout`                                                       | Creates a checkout object via API request with the specified parameters.                                                                  |
| `retrieves_alist_of_draft_orders`                                         | Retrieves paginated draft orders from the REST Admin API with optional filtering parameters.                                              |
| `create_anew_draftorder`                                                  | Creates a new draft order in Shopify with product variant line items, custom line items, and discount configurations, supporting...         |
| `receive_asingle_draftorder`                                              | Retrieves a single DraftOrder based on the specified criteria.                                                                            |
| `modify_an_existing_draftorder`                                           | Modifies an existing draft order by updating its details via REST API request.                                                            |
| `remove_an_existing_draftorder`                                           | Removes an existing DraftOrder by sending a DELETE request to the specified URL.                                                          |
| `receive_acount_of_all_draftorders`                                       | Retrieve the count of draft orders based on optional filtering criteria.                                                                  |
| `send_an_invoice`                                                         | Sends an invoice for a draft order via email with customizable recipient, sender, and message details.                                    |
| `complete_adraft_order`                                                   | Completes a draft order by transitioning it to a regular order, supporting flows like external payment acceptance or sending invoices.    |
| `retrieves_alist_of_all_order_risks_for_an_order`                         | Retrieves a list of all order risks for an order.                                                                                         |
| `creates_an_order_risk_for_an_order`                                      | Creates an order risk for an order by sending a POST request with the provided risk details.                                              |
| `retrieves_asingle_order_risk_by_its_id`                                  | Retrieves a single order risk by its ID.                                                                                                  |
| `updates_an_order_risk`                                                   | Updates an order risk by sending a risk update request to the API.                                                                        |
| `deletes_an_order_risk_for_an_order`                                      | Deletes an order risk associated with an order, typically used to remove risk assessments that were manually created by the current...     |
| `retrieves_alist_of_orders`                                               | Retrieves a list of orders with optional filtering and pagination support. Note: Uses response header links for pagination (page...         |
| `creates_an_order`                                                        | Creates a new order, allowing control over inventory behavior and receipt settings.                                                       |
| `retrieves_aspecific_order`                                               | Retrieves a specific order from a remote source.                                                                                          |
| `updates_an_order`                                                        | Updates an existing order with the provided order data                                                                                    |
| `deletes_an_order`                                                        | Deletes an order by sending a DELETE request to the designated URL. Note that orders interacting with an online gateway cannot be deleted. |
| `retrieves_an_order_count`                                                | Retrieves the count of orders filtered by the specified date ranges, financial status, fulfillment status, or order status.             |
| `closes_an_order`                                                         | Closes an order via API request and returns the response data.                                                                            |
| `re_opens_aclosed_order`                                                  | Re-opens a previously closed order by submitting a request to the API.                                                                    |
| `cancels_an_order`                                                        | Cancels an order and returns the result. For multi-currency orders, the currency parameter is required when amount is provided.             |
| `retrieves_alist_of_refunds_for_an_order`                                 | Retrieves a list of refunds for an order, allowing customization of returned fields and currency.                                         |
| `creates_arefund`                                                         | Creates a refund based on the provided refund details.                                                                                    |
| `retrieves_aspecific_refund`                                              | Retrieves details of a specific refund including specified fields and currency preferences.                                               |
| `calculates_arefund`                                                      | Calculates refund transactions for an order based on line items and shipping, optionally handling multi-currency constraints.             |
| `retrieves_alist_of_transactions`                                         | Retrieves a list of transactions, optionally filtered by specified fields, in-shop currency display preference, and transaction ID...     |
| `creates_atransaction_for_an_order`                                       | Creates a new transaction for an order, handling the request body and API communication.                                                  |
| `retrieves_acount_of_an_order_stransactions`                              | Retrieves the count of an order's transactions.                                                                                           |
| `retrieves_aspecific_transaction`                                         | Retrieves a specific transaction from an API endpoint, allowing field selection and currency format control.                              |
| `retrieves_alist_of_gift_cards`                                           | Retrieves a paginated list of gift cards with optional filters, using Shopify's paginated REST Admin API.                                 |
| `creates_agift_card`                                                      | Creates a new gift card with the provided details.                                                                                        |
| `retrieves_asingle_gift_card`                                             | Retrieves a single gift card by its ID.                                                                                                   |
| `updates_an_existing_gift_card`                                           | Updates an existing gift card, modifying its expiry date, note, and template suffix while preserving the balance.                         |
| `retrieves_acount_of_gift_cards`                                          | Retrieves a count of gift cards filtered by status if provided.                                                                           |
| `disables_agift_card`                                                     | Disables a gift card irreversibly.                                                                                                        |
| `searches_for_gift_cards`                                                 | Searches for gift cards based on specified criteria, including indexed fields like creation time, balance, and last characters.             |
| `retrieves_alist_of_all_users`                                            | Retrieves a list of all users from the API endpoint and returns their data.                                                               |
| `retrieves_asingle_user`                                                  | Retrieves a single user's data via API request.                                                                                           |
| `retrieves_the_currently_logged_in_user`                                  | Retrieves information about the currently authenticated user account using the access token.                                              |
| `retrieves_alist_of_collects`                                             | Retrieves a paginated list of collects (product-collection relationships) from the Shopify API, supporting field filtering and result...  |
| `adds_aproduct_to_acustom_collection`                                     | Adds a product to a custom collection by sending a POST request with the specified collection details.                                  |
| `retrieves_aspecific_collect_by_its_id`                                   | Retrieves a specific collect entry from the API by its ID, allowing field selection.                                                      |
| `removes_aproduct_from_acollection`                                       | Initiates the removal of a product from a collection via a DELETE request to the API endpoint.                                            |
| `retrieves_acount_of_collects`                                            | Retrieves a count of collects from the server.                                                                                            |
| `retrieves_asingle_collection`                                            | Retrieves a single collection from the API, with optional field filtering.                                                                |
| `retrieve_alist_of_products_belonging_to_acollection`                     | Retrieves a paginated list of products associated with a collection, sorted by the collection's configured order.                         |
| `retrieves_alist_of_custom_collections`                                   | Retrieves a list of custom collections based on specified criteria.                                                                       |
| `creates_acustom_collection`                                              | Creates a custom collection with the provided specification.                                                                              |
| `retrieves_acount_of_custom_collections`                                  | Retrieves a count of custom collections based on various filters like product ID, published date, updated date, published status, and... |
| `retrieves_asingle_custom_collection`                                     | Retrieves a specific custom collection with optional field filtering.                                                                     |
| `updates_an_existing_custom_collection`                                   | Updates an existing custom collection using the provided data.                                                                            |
| `deletes_acustom_collection`                                              | Deletes a custom collection by sending a DELETE request to the API endpoint.                                                              |
| `receive_alist_of_all_product_images`                                     | Retrieve a list of product images, optionally filtering by specified fields and IDs.                                                      |
| `create_anew_product_image`                                               | Creates a new product image by sending a POST request to the server with the provided image details.                                      |
| `receive_acount_of_all_product_images`                                    | Retrieves a count of all product images optionally filtered by a since ID.                                                                |
| `receive_asingle_product_image`                                           | Retrieves a single product image by ID with optional field filtering.                                                                     |
| `modify_an_existing_product_image`                                        | Modify an existing product image by updating its details.                                                                                 |
| `remove_an_existing_product_image`                                        | Remove an existing product image by sending a delete request to the product management API.                                               |
| `retrieves_alist_of_product_variants`                                     | Retrieves a paginated list of product variants from Shopify's REST Admin API, including fields, currencies, and pagination controls.    |
| `create_anew_product_variant`                                             | Creates a new product variant by sending a POST request to the API.                                                                       |
| `receive_acount_of_all_product_variants`                                  | Retrieves a count of all product variants.                                                                                                |
| `receive_asingle_product_variant`                                         | Retrieves a single product variant by ID.                                                                                                 |
| `modify_an_existing_product_variant`                                      | Modifies an existing product variant by sending updated details to the API.                                                               |
| `remove_an_existing_product_variant`                                      | Remove an existing Product Variant from the system.                                                                                       |
| `retrieves_alist_of_products`                                             | Retrieves a paginated list of products with filtering options, implementing Shopify's REST Admin API pagination via response headers.       |
| `creates_anew_product`                                                    | Creates a new product by sending a POST request with the product details                                                                  |
| `retrieves_acount_of_products`                                            | Retrieve the count of products matching specified filter criteria, including collection ID, publication status, date ranges, and vendor... |
| `retrieves_asingle_product`                                               | Retrieves a single product's data from the API.                                                                                           |
| `updates_aproduct`                                                        | Updates a product and its associated variants, images, and SEO metadata.                                                                  |
| `deletes_aproduct`                                                        | Deletes a product from the system by making an HTTP DELETE request to the specified endpoint.                                             |
| `retrieves_alist_of_smart_collections`                                    | Retrieves a list of smart collections with optional filtering by various criteria.                                                        |
| `creates_asmart_collection`                                               | Creates a new smart collection using specified rules and configuration.                                                                   |
| `retrieves_acount_of_smart_collections`                                   | Retrieves a count of smart collections filtered by specified criteria including product association, publication/update timestamps,...   |
| `retrieves_asingle_smart_collection`                                      | Retrieves a single smart collection, optionally specifying fields to include.                                                             |
| `updates_an_existing_smart_collection`                                    | Updates an existing smart collection with provided parameters.                                                                            |
| `removes_asmart_collection`                                               | Removes a smart collection using the provided request data.                                                                               |
| `updates_the_ordering_type_of_products_in_asmart_collection`              | Updates the ordering type of products in a smart collection via API request.                                                              |
| `completes_acheckout`                                                     | Completes a checkout by sending a POST request to the checkout endpoint.                                                                  |
| `retrieves_acheckout`                                                     | Retrieves checkout details from the specified API endpoint.                                                                               |
| `modifies_an_existing_checkout`                                           | Modifies an existing checkout via HTTP PUT request with provided checkout data.                                                           |
| `retrieves_alist_of_shipping_rates`                                       | Retrieves a list of available shipping rates for a checkout                                                                               |
| `retrieve_collection_listings_that_are_published_to_your_app`             | Retrieve published collection listings available to your app, implementing pagination via response header links.                          |
| `retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code` | Retrieve product IDs published to a specified collection ID from the Shopify REST Admin API, supporting pagination via response headers.    |
| `retrieve_aspecific_collection_listing_that_is_published_to_your_app`     | Retrieves a specific collection listing published to your app.                                                                            |
| `create_acollection_listing_to_publish_acollection_to_your_app`             | Creates or updates a collection listing to publish a specific collection to the application.                                              |
| `delete_acollection_listing_to_unpublish_acollection_from_your_app`       | Deletes a collection listing to unpublish it from the app by sending a DELETE request to the API endpoint.                                |
| `stores_acredit_card_in_the_card_vault`                                   | Stores credit card details in a secure vault and returns a session ID for payment processing.                                             |
| `retrieves_alist_of_payments_on_aparticular_checkout`                     | Retrieves a list of payments for a specific checkout.                                                                                     |
| `creates_anew_payment`                                                    | Creates a new payment on a checkout using the provided payment details.                                                                   |
| `retrieves_asingle_payment`                                               | Retrieves a single payment by fetching payment information for an existing payment.                                                       |
| `counts_the_number_of_payments_attempted_on_acheckout`                    | Counts the number of payments attempted on a checkout                                                                                     |
| `retrieve_product_listings_that_are_published_to_your_app`                | Retrieve product listings that are published to your app.                                                                                 |
| `retrieve_code_product_ids_code_that_are_published_to_your_app`           | Retrieves product IDs published to the associated app, supporting pagination through response headers.                                    |
| `retrieve_acount_of_products_that_are_published_to_your_app`              | Retrieves the count of products published to the associated app.                                                                          |
| `retrieve_aspecific_product_listing_that_is_published_to_your_app`        | Retrieve a specific published product listing for your app.                                                                               |
| `create_aproduct_listing_to_publish_aproduct_to_your_app`                 | Creates a product listing to publish a product to your app.                                                                               |
| `delete_aproduct_listing_to_unpublish_aproduct_from_your_app`             | Deletes a product listing to remove it from public view in your app's sales channels.                                                     |
| `receive_alist_of_all_resourcefeedbacks`                                  | Retrieve a list of all ResourceFeedbacks as a dictionary.                                                                                 |
| `create_anew_resourcefeedback`                                            | Creates a new resource feedback entry for a Shopify shop resource.                                                                        |
| `retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app`        | Retrieves a list of fulfillment orders on a shop for a specific app, filtered by assignment status and location IDs.                      |
| `sends_acancellation_request`                                             | Sends a cancellation request to the fulfillment service for a fulfillment order.                                                          |
| `accepts_acancellation_request`                                           | Accepts a cancellation request sent to a fulfillment service for a fulfillment order.                                                     |
| `rejects_acancellation_request`                                           | Rejects a cancellation request sent to a fulfillment service for a fulfillment order.                                                     |
| `retrieves_alist_of_carrier_services`                                     | Retrieves a list of carrier services available through the API.                                                                           |
| `creates_acarrier_service`                                                | Creates a carrier service by sending a request with the specified carrier service details.                                                |
| `retrieves_asingle_carrier_service`                                       | Retrieves a single carrier service by its ID.                                                                                             |
| `updates_acarrier_service`                                                | Updates a carrier service. Only the app that creates a carrier service can update it.                                                     |
| `deletes_acarrier_service`                                                | Deletes a carrier service by issuing a DELETE request.                                                                                    |
| `retrieves_fulfillments_associated_with_an_order`                         | Retrieves fulfillments associated with an order based on specified criteria.                                                              |
| `create_anew_fulfillment`                                                 | Create a new fulfillment for an order, specifying line items and fulfillment details.                                                     |
| `retrieves_fulfillments_associated_with_afulfillment_order`             | Retrieves all fulfillments associated with a specified fulfillment order.                                                                 |
| `retrieves_acount_of_fulfillments_associated_with_aspecific_order`        | Retrieves a count of fulfillments associated with a specific order based on date filters.                                                 |
| `receive_asingle_fulfillment`                                             | Retrieves a specific fulfillment entry from the API by making a GET request.                                                              |
| `modify_an_existing_fulfillment`                                          | Updates an existing fulfillment by modifying its details and returns the updated fulfillment data.                                       |
| `creates_afulfillment_for_one_or_many_fulfillment_orders`                 | Creates a fulfillment for one or multiple fulfillment orders associated with the same order at the same location.                       |
| `updates_the_tracking_information_for_afulfillment`                       | Updates the tracking information for a fulfillment by sending a POST request with the provided fulfillment data.                          |
| `complete_afulfillment`                                                   | Complete a fulfillment by marking it as complete and processing the request.                                                              |
| `transition_afulfillment_from_pending_to_open`                            | Transition a fulfillment from pending to open, marking it as open.                                                                        |
| `cancel_afulfillment_for_aspecific_order_id`                              | Cancels a fulfillment for a specific order ID by sending a POST request to the fulfillment service.                                       |
| `cancels_afulfillment`                                                    | Cancels a fulfillment.                                                                                                                    |
| `retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment`         | Retrieves a list of fulfillment events associated with a specific fulfillment.                                                            |
| `creates_afulfillment_event`                                              | Creates a fulfillment event by sending a payload to a configured endpoint.                                                                |
| `retrieves_aspecific_fulfillment_event`                                   | Retrieves a specific fulfillment event from the server.                                                                                   |
| `deletes_afulfillment_event`                                              | Deletes a fulfillment event.                                                                                                              |
| `retrieves_alist_of_fulfillment_orders_for_aspecific_order`               | Retrieves a list of fulfillment orders associated with a specific order ID.                                                               |
| `retrieves_aspecific_fulfillment_order`                                   | Retrieves a specific fulfillment order from a fulfillment service.                                                                        |
| `cancel_afulfillment_order`                                               | Cancel a fulfillment order by marking it as cancelled.                                                                                    |
| `marks_afulfillment_order_as_incomplete`                                  | Marks an in-progress fulfillment order as incomplete, signaling the fulfillment service cannot ship remaining items and intends to close... |
| `moves_afulfillment_order_to_anew_location`                               | Moves an in-progress fulfillment order to a new location, updating the fulfillment service warehouse or pick-up point from which the...     |
| `sends_afulfillment_request`                                              | Sends a fulfillment request to a fulfillment service.                                                                                     |
| `accepts_afulfillment_request`                                            | Accepts a fulfillment request sent to a fulfillment service for a fulfillment order.                                                      |
| `rejects_afulfillment_request`                                            | Rejects a fulfillment request sent to a fulfillment service for a fulfillment order.                                                      |
| `receive_alist_of_all_fulfillmentservices`                                | Retrieves a list of all FulfillmentServices based on the specified scope.                                                                 |
| `create_anew_fulfillmentservice`                                          | Create a new FulfillmentService by sending a POST request to Shopify.                                                                     |
| `receive_asingle_fulfillmentservice`                                      | Receive a single FulfillmentService.                                                                                                      |
| `modify_an_existing_fulfillmentservice`                                   | Modifies an existing FulfillmentService using a provided dictionary of fulfillment service details.                                       |
| `remove_an_existing_fulfillmentservice`                                   | Removes an existing FulfillmentService.                                                                                                   |
| `retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to` | Retrieves a list of locations to which a fulfillment order can potentially move.                                                            |
| `return_the_current_balance`                                              | Retrieve the current balance of an account.                                                                                               |
| `return_alist_of_all_disputes`                                            | Retrieve a list of all disputes, filtered by optional parameters for initiate date, IDs, and status.                                      |
| `return_asingle_dispute`                                                  | Retrieves a single dispute by ID via Shopify Payments.                                                                                    |
| `return_alist_of_all_payouts`                                             | Retrieve a paginated list of payouts ordered by date (most recent first) with filtering options.                                          |
| `return_asingle_payout`                                                   | Retrieves a single payout by ID from Shopify Payments.                                                                                    |
| `return_alist_of_all_balance_transactions`                                | Retrieves a list of balance transactions ordered by processing time, with the most recent first.                                          |
| `receive_alist_of_all_countries`                                          | Retrieves a list of all countries, optionally filtering by specific fields or since a specified ID.                                       |
| `creates_acountry`                                                        | Creates a new country entry in the system via API request.                                                                                |
| `retrieves_acount_of_countries`                                           | Retrieves a count of countries from a remote API.                                                                                         |
| `retrieves_aspecific_county`                                              | Retrieves detailed information about a specific county from an API endpoint, allowing field filtering.                                  |
| `updates_an_existing_country`                                             | Updates an existing country's data by sending a PUT request to the API endpoint.                                                          |
| `remove_an_existing_country`                                              | Removes an existing country by sending a DELETE request.                                                                                  |
| `retrieves_alist_of_currencies_enabled_on_ashop`                          | Retrieves a list of currencies enabled on a shop.                                                                                         |
| `retrieves_alist_of_the_shop_spolicies`                                   | Retrieves a list of the shop's policies including refunds, shipping, and other store-related terms.                                       |
| `retrieves_alist_of_provinces_for_acountry`                               | Retrieves a list of provinces for a country, optionally filtering by specific fields and IDs.                                             |
| `retrieves_acount_of_provinces_for_acountry`                              | Retrieves a count of provinces for a country through an API request.                                                                      |
| `retrieves_asingle_province_for_acountry`                                 | Retrieves a single province's details for a specified country from the API.                                                               |
| `updates_an_existing_province_for_acountry`                               | Updates an existing province for a country by sending a PUT request with the new province details.                                        |
| `retrieves_the_shop_sconfiguration`                                       | Retrieves the shop's configuration details including specified fields.                                                                    |
| `retrieves_alist_of_tender_transactions`                                  | Retrieves a paginated list of tender transactions, supporting filters by date ranges, order, and pagination markers.                      |

## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_shopify/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Shopify app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 