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
mcp dev src/universal mcp shopify/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Shopify API.


| Tool | Description |
|------|-------------|
| `retrieves_alist_of_access_scopes_associated_to_the_access_token` | Retrieves a list of access scopes associated to the access token.. Retrieves a list of access scopes associated to the access token. |
| `retrieves_alist_of_storefront_access_tokens_that_have_been_issued` | Retrieves a list of storefront access tokens that have been issued. Retrieves a list of storefront access tokens that have been issued |
| `creates_anew_storefrontaccesstoken` | Creates a new StorefrontAccessToken. Creates a new storefront access token |
| `deletes_an_existing_storefront_access_token` | Deletes an existing storefront access token. Deletes an existing storefront access token |
| `retrieves_alist_of_reports` | Retrieves a list of reports. Retrieves a list of reports. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_anew_report` | Creates a new report. Creates a new report |
| `retrieves_asingle_report` | Retrieves a single report. Retrieves a single report created by your app |
| `updates_areport` | Updates a report. Updates a report |
| `deletes_areport` | Deletes a report. Deletes a report |
| `retrieves_alist_of_application_charges` | Retrieves a list of application charges. Retrieves a list of application charges |
| `creates_an_application_charge` | Creates an application charge. Creates an application charge |
| `retrieves_an_application_charge` | Retrieves an application charge. Retrieves an application charge |
| `activates_an_application_charge` | Activates an application charge. Activates an accepted application charge |
| `retrieves_all_application_credits` | Retrieves all application credits. Retrieves all application credits |
| `creates_an_application_credit` | Creates an application credit. Creates an application credit |
| `retrieves_asingle_application_credit` | Retrieves a single application credit. Retrieves a single application credit |
| `retrieves_alist_of_recurring_application_charges` | Retrieves a list of recurring application charges. Retrieves a list of recurring application charges |
| `creates_arecurring_application_charge` | Creates a recurring application charge. Creates a recurring application charge |
| `retrieves_asingle_charge` | Retrieves a single charge. Retrieves a single charge |
| `cancels_arecurring_application_charge` | Cancels a recurring application charge. Cancels a recurring application charge |
| `activates_arecurring_application_charge` | Activates a recurring application charge. Activates a previously accepted recurring application charge |
| `updates_the_capped_amount_of_arecurring_application_charge` | Updates the capped amount of a recurring application charge. Updates the capped amount of an active recurring application charge |
| `retrieves_alist_of_usage_charges` | Retrieves a list of usage charges. Retrieves a list of usage charges |
| `creates_ausage_charge` | Creates a usage charge. Creates a usage charge |
| `retrieves_asingle_charge1` | Retrieves a single charge. Retrieves a single charge |
| `retrieves_alist_of_addresses_for_acustomer` | Retrieves a list of addresses for a customer. Retrieves a list of addresses for a customer. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_anew_address_for_acustomer` | Creates a new address for a customer. Creates a new address for a customer. |
| `retrieves_details_for_asingle_customer_address` | Retrieves details for a single customer address. Retrieves details a single customer address. |
| `updates_an_existing_customer_address` | Updates an existing customer address. Updates an existing customer address. |
| `removes_an_address_from_acustomer_saddress_list` | Removes an address from a customer’s address list. Removes an address from a customer’s address list. |
| `performs_bulk_operations_for_multiple_customer_addresses` | Performs bulk operations for multiple customer addresses. Performs bulk operations for multiple customer addresses. |
| `sets_the_default_address_for_acustomer` | Sets the default address for a customer. Sets the default address for a customer. |
| `retrieves_alist_of_customers` | Retrieves a list of customers. Retrieves a list of customers. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_acustomer` | Creates a customer. Creates a customer. |
| `searches_for_customers_that_match_asupplied_query` | Searches for customers that match a supplied query. Searches for customers that match a supplied query. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieves_asingle_customer` | Retrieves a single customer. Retrieves a single customer. |
| `updates_acustomer` | Updates a customer. Updates a customer. |
| `deletes_acustomer` | Deletes a customer.. Deletes a customer. A customer can't be deleted if they have existing orders. |
| `creates_an_account_activation_url_for_acustomer` | Creates an account activation URL for a customer. <p>Generate an account activation URL for a customer whose account is not yet enabled. This is useful when you've imported a large number of customers and want to send them activation emails all at once. Using this approach, you'll need to generate and send the activation emails yourself.</p> <p>The account activation URL generated by this endpoint is for one-time use and will expire after 30 days. If you make a new POST request to this endpoint, then a new URL will be generated. The new URL will be again valid for 30 days, but the previous URL will no longer be valid.</p> |
| `sends_an_account_invite_to_acustomer` | Sends an account invite to a customer. Sends an account invite to a customer. |
| `retrieves_acount_of_customers` | Retrieves a count of customers. Retrieves a count of all customers. |
| `retrieves_all_orders_belonging_to_acustomer` | Retrieves all orders belonging to a customer. Retrieves all orders belonging to a customer. |
| `retrieves_alist_of_customer_saved_searches` | Retrieves a list of customer saved searches. Retrieves a list of customer saved searches. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_acustomer_saved_search` | Creates a customer saved search. Creates a customer saved search. |
| `retrieves_acount_of_all_customer_saved_searches` | Retrieves a count of all customer saved searches. Retrieves a count of all customer saved searches. |
| `retrieves_asingle_customer_saved_search` | Retrieves a single customer saved search. Retrieves a single customer saved search. |
| `updates_acustomer_saved_search` | Updates a customer saved search. Updates a customer saved search. |
| `deletes_acustomer_saved_search` | Deletes a customer saved search. Deletes a customer saved search. |
| `retrieves_all_customers_returned_by_acustomer_saved_search` | Retrieves all customers returned by a customer saved search. Retrieves all customers returned by a customer saved search. |
| `retrieves_alist_of_discount_codes` | Retrieves a list of discount codes. Retrieve a list of discount codes. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_adiscount_code` | Creates a discount code. Creates a discount code |
| `retrieves_asingle_discount_code` | Retrieves a single discount code. Retrieves a single discount code |
| `updates_an_existing_discount_code` | Updates an existing discount code. Updates an existing discount code |
| `deletes_adiscount_code` | Deletes a discount code. Deletes a discount code |
| `retrieves_the_location_of_adiscount_code` | Retrieves the location of a discount code. <p>Retrieves the location of a discount code.</p> <p>The discount code's location is returned in the location header, not in the DiscountCode object itself. Depending on your HTTP client, the location of the discount code might follow the location header automatically.</p> |
| `creates_adiscount_code_creation_job` | Creates a discount code creation job. <p>Creates a discount code creation job.</p> <p>The batch endpoint can be used to asynchronously create up to 100 discount codes in a single request. It enqueues and returns a <code>discount_code_creation</code> object that can be monitored for completion.</p> |
| `retrieves_adiscount_code_creation_job` | Retrieves a discount code creation job. <p>Retrieves a discount code creation job</p> |
| `retrieves_alist_of_discount_codes_for_adiscount_code_creation_job` | Retrieves a list of discount codes for a discount code creation job. <p>Retrieves a list of discount codes for a discount code creation job.</p> <p>Discount codes that have been successfully created include a populated <code>id</code> field. Discount codes that encountered errors during the creation process include a populated <code>errors</code> field.</p> |
| `retrieves_alist_of_price_rules` | Retrieves a list of price rules. Retrieves a list of price rules. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_aprice_rule` | Creates a price rule. Creates a price rule |
| `retrieves_asingle_price_rule` | Retrieves a single price rule. Retrieves a single price rule |
| `updates_an_existing_aprice_rule` | Updates an existing a price rule. Updates an existing a price rule |
| `remove_an_existing_pricerule` | Remove an existing PriceRule. Deletes a price rule |
| `retrieves_acount_of_all_price_rules` | Retrieves a count of all price rules. Retrieves a count of all price rules. |
| `retrieves_alist_of_events` | Retrieves a list of events. Retrieves a list of events. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieves_asingle_event` | Retrieves a single event. Retrieves a single event by its ID |
| `retrieves_acount_of_events` | Retrieves a count of events. Retrieves a count of events |
| `retrieves_alist_of_webhooks` | Retrieves a list of webhooks. Retrieves a list of webhooks. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_webhook` | Create a new Webhook. Create a new webhook subscription by specifying both an <code>address</code> and a <code>topic</code> |
| `receive_acount_of_all_webhooks` | Receive a count of all Webhooks. Retrieves a count of existing webhook subscriptions |
| `receive_asingle_webhook` | Receive a single Webhook. Retrieves a single webhook subscription |
| `modify_an_existing_webhook` | Modify an existing Webhook. Update a webhook subscription's topic or address URIs |
| `remove_an_existing_webhook` | Remove an existing Webhook. Delete a webhook subscription |
| `retrieves_alist_of_inventory_items` | Retrieves a list of inventory items. Retrieves a list of inventory items. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieves_asingle_inventory_item_by_id` | Retrieves a single inventory item by ID. Retrieves a single inventory item by ID |
| `updates_an_existing_inventory_item` | Updates an existing inventory item. Updates an existing inventory item |
| `retrieves_alist_of_inventory_levels` | Retrieves a list of inventory levels. <p>Retrieves a list of inventory levels.</p> <p>You must include <code>inventory_item_ids</code>, <code>location_ids</code>, or both as filter parameters.</p> <p><strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>.</p> |
| `deletes_an_inventory_level_from_alocation` | Deletes an inventory level from a location. Deletes an inventory level of an inventory item at a location. Deleting an inventory level for an inventory item removes that item from the specified location. Every inventory item must have at least one inventory level. To move inventory to another location, first connect the inventory item to another location, and then delete the previous inventory level. |
| `adjusts_the_inventory_level_of_an_inventory_item_at_alocation` | Adjusts the inventory level of an inventory item at a location. <p>Adjusts the inventory level of an inventory item at a single location</p> |
| `connects_an_inventory_item_to_alocation` | Connects an inventory item to a location. <p>Connects an inventory item to a location by creating an inventory level at that location.</p> <p>When connecting inventory items to locations, it's important to understand the rules around <a href="#inventory-levels-and-fulfillment-service-locations">fulfillment service locations</a>.</p> |
| `sets_the_inventory_level_for_an_inventory_item_at_alocation` | Sets the inventory level for an inventory item at a location. Sets the inventory level for an inventory item at a location. If the specified location is not connected, it will be automatically connected first. When connecting inventory items to locations, it's important to understand the rules around <a href="#inventory-levels-and-fulfillment-service-locations">fulfillment service locations</a>. |
| `retrieves_alist_of_locations` | Retrieves a list of locations. Retrieves a list of locations |
| `retrieves_asingle_location_by_its_id` | Retrieves a single location by its ID. Retrieves a single location by its ID |
| `retrieves_acount_of_locations` | Retrieves a count of locations. Retrieves a count of locations |
| `retrieves_alist_of_inventory_levels_for_alocation` | Retrieves a list of inventory levels for a location.. Retrieves a list of inventory levels for a location. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieves_alist_of_all_marketing_events` | Retrieves a list of all marketing events. Retrieves a list of all marketing events. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_amarketing_event` | Creates a marketing event. Creates a marketing event |
| `retrieves_acount_of_all_marketing_events` | Retrieves a count of all marketing events. Retrieves a count of all marketing events |
| `retrieves_asingle_marketing_event` | Retrieves a single marketing event. Retrieves a single marketing event |
| `updates_amarketing_event` | Updates a marketing event. Updates a marketing event |
| `deletes_amarketing_event` | Deletes a marketing event. Deletes a marketing event |
| `creates_marketing_engagements_on_amarketing_event` | Creates marketing engagements on a marketing event. <p>Engagements on marketing events represent customer activity taken on the marketing event before customers reach the shop’s website. Not all types of marketing events will necessarily have engagement, and most types of marketing events will only use a subset of the possible engagement types.</p> <br> <p>Engagements are aggregated on a daily basis. However, the data can be sent more often than once a day if the information is available. If you create an engagement with the same value for <code>occurred_on</code> as an existing engagement, then the new engagement will overwrite the previous one.</p> |
| `retrieves_alist_of_metafields_that_belong_to_aresource` | Retrieves a list of metafields that belong to a resource. Retrieves a list of metafields that belong to a resource. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_anew_metafield_for_aresource` | Creates a new metafield for a resource. Creates a new metafield for a resource. |
| `retrieves_acount_of_aresource_smetafields` | Retrieves a count of a resource's metafields. Retrieves a count of a resource's metafields. |
| `retrieves_asingle_metafield_from_aresource_by_its_id` | Retrieves a single metafield from a resource by its ID. Retrieves a single metafield from a resource by its ID. |
| `updates_ametafield` | Updates a metafield. Updates a metafield. |
| `deletes_ametafield_by_its_id` | Deletes a metafield by its ID. Deletes a metafield by its ID. |
| `retrieves_alist_of_all_articles_from_ablog` | Retrieves a list of all articles from a blog. Retrieves a list of all articles from a blog. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_an_article_for_ablog` | Creates an article for a blog. Creates an article for a blog |
| `retrieves_acount_of_all_articles_from_ablog` | Retrieves a count of all articles from a blog. Retrieves a count of all articles from a blog |
| `receive_asingle_article` | Receive a single Article. Retrieves a single article |
| `updates_an_article` | Updates an article. Updates an article |
| `deletes_an_article` | Deletes an article. Deletes an article |
| `retrieves_alist_of_all_article_authors` | Retrieves a list of all article authors. Retrieves a list all of article authors |
| `retrieves_alist_of_all_article_tags` | Retrieves a list of all article tags. Retrieves a list of all the tags |
| `retrieves_alist_of_assets_for_atheme` | Retrieves a list of assets for a theme. Retrieves a list of assets for a theme. Listing theme assets returns only metadata about each asset. To get an asset's contents, you need to <a href="#show">retrieve the asset individually</a>. |
| `creates_or_updates_an_asset_for_atheme` | Creates or updates an asset for a theme. <p>Creates or updates an asset for a theme.</p> <p>In the PUT request, you can include the <code>src</code> or <code>source_key</code> property to create the asset from an existing file.</p> |
| `deletes_an_asset_from_atheme` | Deletes an asset from a theme. Deletes an asset from a theme. |
| `retrieve_alist_of_all_blogs` | Retrieve a list of all blogs. Retrieve a list of all blogs. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_blog` | Create a new Blog. Create a new blog |
| `receive_acount_of_all_blogs` | Receive a count of all Blogs. Get a count of all blogs |
| `receive_asingle_blog` | Receive a single Blog. Get a single blog by its ID |
| `modify_an_existing_blog` | Modify an existing Blog. Update a blog |
| `remove_an_existing_blog` | Remove an existing Blog. Delete a blog |
| `retrieves_alist_of_comments` | Retrieves a list of comments. Retrieves a list of comments. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_acomment_for_an_article` | Creates a comment for an article. Creates a comment for an article |
| `retrieves_acount_of_comments` | Retrieves a count of comments. Retrieves a count of comments |
| `retrieves_asingle_comment_by_its_id` | Retrieves a single comment by its ID. Retrieves a single comment by its ID |
| `updates_acomment_of_an_article` | Updates a comment of an article. Updates a comment of an article |
| `marks_acomment_as_spam` | Marks a comment as spam. Marks a comment as spam |
| `marks_acomment_as_not_spam` | Marks a comment as not spam. Marks a comment as not spam |
| `approves_acomment` | Approves a comment. Approves a comment |
| `removes_acomment` | Removes a comment. Removes a comment |
| `restores_apreviously_removed_comment` | Restores a previously removed comment. Restores a previously removed comment |
| `retrieves_alist_of_pages` | Retrieves a list of pages. Retrieve a list of all pages. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_page` | Create a new Page. Creates a page. |
| `retrieves_apage_count` | Retrieves a page count. Retrieves a page count. |
| `retrieves_asingle_page_by_its_id` | Retrieves a single page by its ID. Retrieves a single page by its ID. |
| `updates_apage` | Updates a page. Updates a page. |
| `deletes_apage` | Deletes a page. Deletes a page. |
| `retrieves_alist_of_url_redirects` | Retrieves a list of URL redirects. Retrieves a list of URL redirects. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_aredirect` | Creates a redirect. Creates a redirect. When you provide a full URL as the value of the <code>path</code> property, it will be saved as an absolute path without the domain. For example, <code>"path": "http://www.johns-apparel.com/springwear"</code> will be saved as <code>"path": "springwear"</code>. |
| `retrieves_acount_of_url_redirects` | Retrieves a count of URL redirects. Retrieves a count of URL redirects |
| `retrieves_asingle_redirect` | Retrieves a single redirect. Retrieves a single redirect |
| `updates_an_existing_redirect` | Updates an existing redirect. Updates an existing redirect |
| `deletes_aredirect` | Deletes a redirect. Deletes a redirect |
| `retrieves_alist_of_all_script_tags` | Retrieves a list of all script tags. Retrieves a list of all script tags. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_anew_script_tag` | Creates a new script tag. Creates a new script tag |
| `retrieves_acount_of_all_script_tags` | Retrieves a count of all script tags. Retrieves a count of all script tags |
| `retrieves_asingle_script_tag` | Retrieves a single script tag. Retrieves a single script tag |
| `updates_ascript_tag` | Updates a script tag. Updates a script tag |
| `deletes_ascript_tag` | Deletes a script tag. Deletes a script tag |
| `retrieves_alist_of_themes` | Retrieves a list of themes. Retrieves a list of themes. |
| `creates_atheme` | Creates a theme. Creates a theme by providing the public URL of a ZIP file that contains the theme. <p>A new theme is always unpublished by default. To publish a theme when you create it, include <code>"role": "main"</code> in the POST request. The theme will be published only after all of its files have been extracted and stored by Shopify, which might take a couple of minutes.</p> |
| `retrieves_asingle_theme` | Retrieves a single theme. Retrieves a single theme. |
| `modify_an_existing_theme` | Modify an existing Theme. Updates an existing theme. |
| `remove_an_existing_theme` | Remove an existing Theme. Deletes a theme. |
| `retrieves_acount_of_checkouts` | Retrieves a count of checkouts. Retrieves a count of checkouts from the past 90 days |
| `retrieves_alist_of_abandoned_checkouts` | Retrieves a list of abandoned checkouts. Retrieves a list of abandoned checkouts. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_acheckout` | Creates a checkout. Creates a checkout |
| `retrieves_alist_of_draft_orders` | Retrieves a list of draft orders. Retrieves a list of draft orders. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_draftorder` | Create a new DraftOrder. <p>Creates a draft order.</p> <p>Using the DraftOrder resource you can create orders in draft state using product variant line items, or custom line items. To create a product variant draft order, provide the <code>variant_id</code>, <code>quantity</code> and <code>discount</code> properties. To create a custom line item, provide the <code>title</code>, <code>price</code>, <code>taxable</code>, and <code>quantity</code> properties.</p> <br/> <aside class="note"> <h4>Note</h4> <p>If you are using this endpoint with a Partner development store or a trial store, then you can only create five draft orders per minute.</p> </aside> <h3>Polling</h3> When you create and update draft orders some calculations are done asynchronously, such as calculating shipping and taxes. There might be times when a draft order is created but these calculations haven't completed. In these cases, you need to poll the draft order until the calculations are finished. <br> When a draft order requires polling, a <code>202 accepted</code> response code is returned along with <code>location</code> and <code>retry-after</code> response headers. The <code>location</code> header refers to the URL to be polled, and <code>retry-after</code> denotes the interval (in seconds) at which polling requests should be sent. When the draft order is ready, a <code>200 OK</code> response code will be returned. <h3>About custom shipping lines</h3> You can use the DraftOrder resource to send orders with custom shipping lines. A custom shipping line includes a <code>title</code> and <code>price</code> with <code>handle</code> set to <code>Nil</code>. A shipping line with a carrier provided shipping rate (currently set via the Shopify admin) includes the shipping rate handle. <h3>Applying discounts</h3> <p>A draft order and its line items can have one discount each. Calculations for discounts are based on the setting of the <code>value_type</code> property, which can be set to either <code>fixed_amount</code> or <code>percentage</code>. For example, you can apply a fixed amount discount to a draft order to reduce the price by the specified <code>value</code> property. When you use a percentage discount, the discount <code>amount</code> property is the price multiplied by the <code>value</code> property. For line item discounts, the <code>value</code> property is applied per individual unit of the item, based on the line item's quantity.</p> <br> <p><strong>Calculating line item discount amounts</strong></p> <p>For <code>fixed_amount</code> discounts, the total <code>amount</code> corresponds to the line item quantity times the value of the discount. For percentage discounts, the total amount corresponds to the following:</p> <br> <p><code>amount = floor(price * quantity * value) / 100</code>, where <code>floor()</code> is the usual round down function.</p> <br> <p>For non-fractional currencies, this formula needs to use round() instead of floor(), and the division by 100 takes place inside the rounding, resulting in a non-fractional value. Otherwise, an error is returned.</p> <br> <p><code>amount = round(price * quantity * value / 100)</code></p> <br> <strong>Line item examples</strong> <br> <p><i>Fixed amount discount</i></p> <p>For a $19.99 line item with quantity of 2 and with $5 dollars off, discount amount corresponds to $10 ($5 * 2):</p> <br> <p><code>applied_discount: { "value_type": "fixed_amount", "value": 5, "amount": 10 }</code></p> <br> <p>For a fixed amount example, see <a href="#create-a-draft-order-with-a-discount-"><i>Create a draft order with a discount</i></a>.</p> <br> <p><i>Percentage discount</i></p> <p>For a $19.99 line item with quantity of 2 and with 15% off, discount amount corresponds to $5.99 (floor ($19.99 * 2 * 15) / 100):</p> <br> <p><code>applied_discount: { "value_type": "percentage", "value": 15, "amount": 5.99 }</code></p> <br> <p>For a percentage example, see <a href="#create-a-percent-discount-on-a-line-item-"><i>Create a percent discount on a line item</i></a>.</p> <h3>Loading and removing customers</h3> <p>You can load a customer to a draft order by sending the <code>customer_id</code> as part of the draft order object. The recommended way to remove a customer from a draft order is to make a POST request with the Customer object set to null, without specifying an email, shipping address, or billing address. A customer may also be removed by setting <code>customer</code>, <code>email</code>, <code>shipping_address</code>, and <code>billing_address</code> to <code>null</code>. </p> |
| `receive_asingle_draftorder` | Receive a single DraftOrder. Retrieves a specific draft order |
| `modify_an_existing_draftorder` | Modify an existing DraftOrder. Updates a draft order |
| `remove_an_existing_draftorder` | Remove an existing DraftOrder. Deletes a draft order |
| `receive_acount_of_all_draftorders` | Receive a count of all DraftOrders. Retrieves a count of draft orders |
| `send_an_invoice` | Send an invoice. <p>Sends an invoice for the draft order.</p> <p>You can include the following parameters in the body of the request:</p> <ul> <li><strong>draft_order_invoice</strong>: The object to send in the body of the request. <ul> <li><strong>to</strong>: The email address that will populate the <strong>to</strong> field of the email.</li> <li><strong>from</strong>: The email address that will populate the <strong>from</strong> field of the email.</li> <li><strong>bcc</strong>: The list of email addresses to include in the <strong>bcc</strong> field of the email. Emails must be associated with staff accounts on the shop.</li> <li><strong>subject</strong>: The email subject.</li> <li><strong>custom_message</strong>: The custom message displayed in the email.</li> </ul> </li> </ul> |
| `complete_adraft_order` | Complete a draft order. Completes a draft order. <br> <p>Using the DraftOrder resource, you can create a draft order and transition it to an order.</p> <br> <p>The following flows are supported:</p> <br> <ul> <li>Create a draft order that calculates taxes and totals but accept payment from the customer outside of Shopify.</li> <li>Create a draft order and send an invoice to the customer.</li> </ul> |
| `retrieves_alist_of_all_order_risks_for_an_order` | Retrieves a list of all order risks for an order. Retrieves a list of all order risks for an order. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_an_order_risk_for_an_order` | Creates an order risk for an order. Creates an order risk for an order |
| `retrieves_asingle_order_risk_by_its_id` | Retrieves a single order risk by its ID. Retrieves a single order risk by its ID |
| `updates_an_order_risk` | Updates an order risk. <p>Updates an order risk</p> <br/> <aside class="note"> <h4>Note</h4> <p>You cannot modify an order risk that was created by another application.</p> </aside> |
| `deletes_an_order_risk_for_an_order` | Deletes an order risk for an order. <p>Deletes an order risk for an order</p> <br/> <aside class="note"> <h4>Note</h4> <p>You cannot delete an order risk that was created by another application.</p> </aside> |
| `retrieves_alist_of_orders` | Retrieves a list of orders. Retrieves a list of orders. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_an_order` | Creates an order. <p>Creates an order. By default, product inventory is not claimed.</p> <p>When you create an order, you can include the following option parameters in the body of the request:</p> <ul> <li><strong>inventory_behaviour</strong>: The behaviour to use when updating inventory. (default: <code>bypass</code>) <ul> <li><strong>bypass</strong>: Do not claim inventory.</li> <li><strong>decrement_ignoring_policy</strong>: Ignore the product's inventory policy and claim inventory.</li> <li><strong>decrement_obeying_policy</strong>: Follow the product's inventory policy and claim inventory, if possible.</li> </ul> </li> <li><strong>send_receipt</strong>: Whether to send an order confirmation to the customer.</li> </ul> <aside class="note"> <h4>Note</h4> <p>If you're working on a private app and order confirmations are still being sent to the customer when <code>send_receipt</code> is set to <code>false</code>, then you need to disable the Storefront API from the private app's page in the Shopify admin.</p> </aside> <ul> <li><strong>send_fulfillment_receipt</strong>: Whether to send a shipping confirmation to the customer.</li> </ul> <aside class="note"> <h4>Note</h4> <p>If you are including <strong>shipping_address</strong> or <strong>billing_address</strong>, make sure to pass both <strong>first_name</strong> and <strong>last_name</strong>. Otherwise both these addresses will be ignored.</p> <p>If you're using this endpoint with a trial or Partner development store, then you can create no more than 5 new orders per minute.</p> </aside> |
| `retrieves_aspecific_order` | Retrieves a specific order. Retrieves a specific order |
| `updates_an_order` | Updates an order. Updates an order |
| `deletes_an_order` | Deletes an order. Deletes an order. Orders that interact with an online gateway can't be deleted. |
| `retrieves_an_order_count` | Retrieves an order count. Retrieves an order count |
| `closes_an_order` | Closes an order. Closes an order |
| `re_opens_aclosed_order` | Re-opens a closed order. Re-opens a closed order |
| `cancels_an_order` | Cancels an order. <aside class="note caution"> <h4>Caution</h4> <p>For multi-currency orders, the <code>currency</code> property is required whenever the <code>amount</code> property is provided. For more information, see <a href="https://help.shopify.com/api/guides/multi-currency-migration-guide"><i>Migrating to support multiple currencies</i></a>.</p> </aside> Cancels an order. Orders that have a fulfillment object can't be canceled. |
| `retrieves_alist_of_refunds_for_an_order` | Retrieves a list of refunds for an order. Retrieves a list of refunds for an order. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_arefund` | Creates a refund. <aside class="note caution"> <h4>Caution</h4> <p>For multi-currency orders, the <code>currency</code> property is required whenever the <code>amount</code> property is provided. For more information, see <a href="https://help.shopify.com/api/guides/multi-currency-migration-guide"><i>Migrating to support multiple currencies</i></a>.</p> </aside> <p>Creates a refund. Use the <a href="#calculate">calculate</a> endpoint to produce the transactions to submit.</p> <br/> <aside class="note"> <h4>Note</h4> <p>When you use this endpoint with a Partner development store or a trial store, you can create only five refunds per minute.</p> </aside> |
| `retrieves_aspecific_refund` | Retrieves a specific refund. Retrieves a specific refund. |
| `calculates_arefund` | Calculates a refund. <aside class="note caution"> <h4>Caution</h4> <p>For multi-currency orders, the <code>currency</code> property is required whenever the <code>amount</code> property is provided. For more information, see <a href="https://help.shopify.com/api/guides/multi-currency-migration-guide"><i>Migrating to support multiple currencies</i></a>.</p> </aside> <p>Calculates refund transactions based on line items and shipping. When you want to create a refund, you should first use the calculate endpoint to generate accurate refund transactions. Specify the line items that are being refunded, their quantity and restock instructions, and whether you intend to refund shipping costs. If the restock instructions can't be met—for example, because you try to return more items than have been fulfilled—then the endpoint returns modified restock instructions. You can then use the response in the body of the request to create the actual refund.</p> <p>The response includes a <code>transactions</code> object with <code>"kind": "suggested_refund"</code>, which must to be changed to <code>"kind" : "refund"</code> for the refund to be accepted. |
| `retrieves_alist_of_transactions` | Retrieves a list of transactions. <p>Retrieves a list of transactions.</p> <p>Transactions attached to multi-currency orders are in the presentment currency by default. To retrieve transactions in the shop currency, include the URL parameter <code>in_shop_currency=true</code>.</p> |
| `creates_atransaction_for_an_order` | Creates a transaction for an order. <aside class="note caution"> <h4>Caution</h4> <p>For multi-currency orders, the <code>currency</code> property is required when creating refund and capture transactions. The value should be the presentment currency from the order. For more information, see <a href="https://help.shopify.com/api/guides/multi-currency-migration-guide"><i>Migrating to support multiple currencies</i></a>.</p> </aside> <p>Creates a transaction for an order.</p> |
| `retrieves_acount_of_an_order_stransactions` | Retrieves a count of an order's transactions. Retrieves a count of an order's transactions. |
| `retrieves_aspecific_transaction` | Retrieves a specific transaction. <p>Retrieves a specific transaction.</p> <p>Transactions attached to multi-currency orders are in the presentment currency by default. To retrieve transactions in the shop currency, include the URL parameter <code>in_shop_currency=true</code>.</p> |
| `retrieves_alist_of_gift_cards` | Retrieves a list of gift cards. Retrieves a list of gift cards. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_agift_card` | Creates a gift card. Creates a gift card |
| `retrieves_asingle_gift_card` | Retrieves a single gift card. Retrieves a single gift card by its ID |
| `updates_an_existing_gift_card` | Updates an existing gift card. <p>Updates an existing gift card.</p> <p>The gift card's balance can't be changed via the API. You can change only the expiry date, note, and template suffix.</p> |
| `retrieves_acount_of_gift_cards` | Retrieves a count of gift cards. Retrieves a count of gift cards |
| `disables_agift_card` | Disables a gift card. Disables a gift card. Disabling a gift card can't be undone. |
| `searches_for_gift_cards` | Searches for gift cards. <p>Searches for gift cards that match a supplied query. The following fields are indexed by search:</p> <ul> <li><code>created_at</code></li> <li><code>updated_at</code></li> <li><code>disabled_at</code></li> <li><code>balance</code></li> <li><code>initial_value</code></li> <li><code>amount_spent</code></li> <li><code>last_characters</code></li> </ul> <p><strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>.</p> |
| `retrieves_alist_of_all_users` | Retrieves a list of all users. Retrieves a list of all users |
| `retrieves_asingle_user` | Retrieves a single user. Retrieves a single user |
| `retrieves_the_currently_logged_in_user` | Retrieves the currently logged-in user. Retrieves information about the user account associated with the access token used to make this API request. This request works only when the access token was created for a specific user of the shop. |
| `retrieves_alist_of_collects` | Retrieves a list of collects. Retrieves a list of collects. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `adds_aproduct_to_acustom_collection` | Adds a product to a custom collection. Adds a product to a custom collection. |
| `retrieves_aspecific_collect_by_its_id` | Retrieves a specific collect by its ID. Retrieves a specific collect by its ID. |
| `removes_aproduct_from_acollection` | Removes a product from a collection. Removes a product from a collection. |
| `retrieves_acount_of_collects` | Retrieves a count of collects. Retrieves a count of collects. |
| `retrieves_asingle_collection` | Retrieves a single collection. Retrieves a single collection |
| `retrieve_alist_of_products_belonging_to_acollection` | Retrieve a list of products belonging to a collection. Retrieve a list of products belonging to a collection. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>.. The products returned are sorted by the collection's sort order. |
| `retrieves_alist_of_custom_collections` | Retrieves a list of custom collections. Retrieves a list of custom collections. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_acustom_collection` | Creates a custom collection. Creates a custom collection |
| `retrieves_acount_of_custom_collections` | Retrieves a count of custom collections. Retrieves a count of custom collections |
| `retrieves_asingle_custom_collection` | Retrieves a single custom collection. Retrieves a single custom collection |
| `updates_an_existing_custom_collection` | Updates an existing custom collection. Updates an existing custom collection |
| `deletes_acustom_collection` | Deletes a custom collection. Deletes a custom collection |
| `receive_alist_of_all_product_images` | Receive a list of all Product Images. Get all product images |
| `create_anew_product_image` | Create a new Product Image. Create a new product image |
| `receive_acount_of_all_product_images` | Receive a count of all Product Images. Get a count of all product images |
| `receive_asingle_product_image` | Receive a single Product Image. Get a single product image by id |
| `modify_an_existing_product_image` | Modify an existing Product Image. Modify an existing product image |
| `remove_an_existing_product_image` | Remove an existing Product Image. Remove an existing Product Image |
| `retrieves_alist_of_product_variants` | Retrieves a list of product variants. Retrieves a list of product variants. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_product_variant` | Create a new Product Variant. Creates a new product variant |
| `receive_acount_of_all_product_variants` | Receive a count of all Product Variants. Retrieves a count of product variants |
| `receive_asingle_product_variant` | Receive a single Product Variant. Retrieves a single product variant by ID |
| `modify_an_existing_product_variant` | Modify an existing Product Variant. Updates an existing product variant |
| `remove_an_existing_product_variant` | Remove an existing Product Variant. Remove an existing Product Variant |
| `retrieves_alist_of_products` | Retrieves a list of products. Retrieves a list of products. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_anew_product` | Creates a new product. <p>Creates a new product.</p><br/> <p>If you want to set the product's SEO information, then you can use the following properties:</p> <ul> <li>metafields_global_title_tag: The name of the product used for <a href='/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page' title='Page title SEO information'>SEO purposes</a>. Generally added to the <code>&lt;meta name='title'&gt;</code> tag.</li> <li>metafields_global_description_tag: A description of the product used for <a href='/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page' title='Page title SEO information'>SEO purposes</a>. Generally added to the <code>&lt;meta name='description'&gt;</code> tag.</li> </ul><br/> |
| `retrieves_acount_of_products` | Retrieves a count of products. Retrieves a count of products. |
| `retrieves_asingle_product` | Retrieves a single product. Retrieves a single product. |
| `updates_aproduct` | Updates a product. <p>Updates a product and its variants and images.</p><br/> <p>If you want to update the product's SEO information, then you can use the following properties:</p> <ul> <li>metafields_global_title_tag: The name of the product used for <a href='/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page' title='Page SEO information'>SEO purposes</a>. Generally added to the <code>&lt;meta name='title'&gt;</code> tag.</li> <li>metafields_global_description_tag: A description of the product used for <a href='/manual/promoting-marketing/seo/adding-keywords#edit-the-title-and-meta-description-for-a-page' title='Page SEO information'>SEO purposes</a>. Generally added to the <code>&lt;meta name='description'&gt;</code> tag.</li> </ul> |
| `deletes_aproduct` | Deletes a product. Deletes a product. |
| `retrieves_alist_of_smart_collections` | Retrieves a list of smart collections. Retrieves a list of smart collections. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `creates_asmart_collection` | Creates a smart collection. Creates a new smart collection using the specified rules. |
| `retrieves_acount_of_smart_collections` | Retrieves a count of smart collections. Retrieves a count of smart collections |
| `retrieves_asingle_smart_collection` | Retrieves a single smart collection. Retrieves a single smart collection |
| `updates_an_existing_smart_collection` | Updates an existing smart collection. Updates an existing smart collection |
| `removes_asmart_collection` | Removes a smart collection. Removes a smart collection |
| `updates_the_ordering_type_of_products_in_asmart_collection` | Updates the ordering type of products in a smart collection. Updates the ordering type of products in a smart collection |
| `completes_acheckout` | Completes a checkout. Completes a checkout |
| `retrieves_acheckout` | Retrieves a checkout. Retrieves a checkout |
| `modifies_an_existing_checkout` | Modifies an existing checkout. Modifies an existing checkout |
| `retrieves_alist_of_shipping_rates` | Retrieves a list of shipping rates. Retrieves a list of available shipping rates for the specified checkout. Implementers need to poll this endpoint until rates become available. Each shipping rate contains the checkout's new subtotal price, total tax, and total price in the event that this shipping rate is selected. This can be used to update the UI without performing further API requests.</p> To apply a shipping rate, update the checkout's shipping line with the handle of the selected rate. |
| `retrieve_collection_listings_that_are_published_to_your_app` | Retrieve collection listings that are published to your app. Retrieve collection listings that are published to your app. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieve_code_product_ids_code_that_are_published_to_acode_collection_id_code` | Retrieve <code>product_ids</code> that are published to a <code>collection_id</code>. Retrieve <code>product_ids</code> that are published to a <code>collection_id</code>. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieve_aspecific_collection_listing_that_is_published_to_your_app` | Retrieve a specific collection listing that is published to your app. Retrieve a specific collection listing that is published to your app |
| `create_acollection_listing_to_publish_acollection_to_your_app` | Create a collection listing to publish a collection to your app. Create a collection listing to publish a collection to your app |
| `delete_acollection_listing_to_unpublish_acollection_from_your_app` | Delete a collection listing to unpublish a collection from your app. Delete a collection listing to unpublish a collection from your app |
| `stores_acredit_card_in_the_card_vault` | Stores a credit card in the card vault. Stores a credit card in the card vault. Credit cards cannot be sent to the Checkout API directly. They must be sent to the card vault, which in response will return a session ID. This session ID can then be used when calling the POST #{token}/payments.json endpoint. A session ID is valid only for a single call to the endpoint. The card vault has a static URL and is located at https://elb.deposit.shopifycs.com/sessions. It is also provided via the <code>payment_url</code> property on the <a href=/api/reference/sales-channels/checkout>Checkout</a> resource. |
| `retrieves_alist_of_payments_on_aparticular_checkout` | Retrieves a list of payments on a particular checkout. Retrieves a list of payments on a particular checkout |
| `creates_anew_payment` | Creates a new payment. Creates a payment on a checkout using the session ID returned by the card vault |
| `retrieves_asingle_payment` | Retrieves a single payment. Retrieves the payment information for an existing payment |
| `counts_the_number_of_payments_attempted_on_acheckout` | Counts the number of payments attempted on a checkout. Counts the number of payments attempted on a checkout |
| `retrieve_product_listings_that_are_published_to_your_app` | Retrieve product listings that are published to your app. Retrieve product listings that are published to your app. <strong>Note:</strong> As of version 2019-07, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieve_code_product_ids_code_that_are_published_to_your_app` | Retrieve <code>product_ids</code> that are published to your app. Retrieve <code>product_ids</code> that are published to your app. Maximum 1,000 results per page. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `retrieve_acount_of_products_that_are_published_to_your_app` | Retrieve a count of products that are published to your app. Retrieve a count of products that are published to your app |
| `retrieve_aspecific_product_listing_that_is_published_to_your_app` | Retrieve a specific product listing that is published to your app. Retrieve a specific product listing that is published to your app |
| `create_aproduct_listing_to_publish_aproduct_to_your_app` | Create a product listing to publish a product to your app. Create a product listing to publish a product to your app |
| `delete_aproduct_listing_to_unpublish_aproduct_from_your_app` | Delete a product listing to unpublish a product from your app. Delete a product listing to unpublish a product from your app |
| `receive_alist_of_all_resourcefeedbacks` | Receive a list of all ResourceFeedbacks. Returns a list (zero or one) of resource feedback objects. <div class="note"> <h4>Important</h4> <p>Note that ids are not returned as part of this request. Records are immutable except when POST replaces them.</p> </div> |
| `create_anew_resourcefeedback` | Create a new ResourceFeedback. Creates shop resource feedback. |
| `retrieves_alist_of_fulfillment_orders_on_ashop_for_aspecific_app` | Retrieves a list of fulfillment orders on a shop for a specific app. Retrieves a list of fulfillment orders on a shop for a specific app. |
| `sends_acancellation_request` | Sends a cancellation request. Sends a cancellation request to the fulfillment service of a fulfillment order. |
| `accepts_acancellation_request` | Accepts a cancellation request. Accepts a cancellation request sent to a fulfillment service for a fulfillment order. |
| `rejects_acancellation_request` | Rejects a cancellation request. Rejects a cancellation request sent to a fulfillment service for a fulfillment order. |
| `retrieves_alist_of_carrier_services` | Retrieves a list of carrier services. Retrieves a list of carrier services |
| `creates_acarrier_service` | Creates a carrier service. Creates a carrier service |
| `retrieves_asingle_carrier_service` | Retrieves a single carrier service. <p>Retrieves a single carrier service by its ID</p> |
| `updates_acarrier_service` | Updates a carrier service. <p>Updates a carrier service. Only the app that creates a carrier service can update it.</p> |
| `deletes_acarrier_service` | Deletes a carrier service. <p>Deletes a carrier service</p> |
| `retrieves_fulfillments_associated_with_an_order` | Retrieves fulfillments associated with an order. Retrieves fulfillments associated with an order. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `create_anew_fulfillment` | Create a new Fulfillment. <p>Create a fulfillment for the specified order and line items.</p> <p>The fulfillment's status depends on the line items in the order: <ul> <li>If the line items in the fulfillment use a manual or custom fulfillment service, then the status of the returned fulfillment will be set immediately.</li> <li>If the line items use an external fulfillment service, then they will be queued for fulfillment and the status will be set to <strong>pending</strong> until the external fulfillment service has been invoked.</li> </ul></p> <br/> <p>A fulfillment might then transition to <strong>open</strong>, which implies it is being processed by the service, before transitioning to <strong>success</strong> when the items have shipped. If you don't specify line item IDs, then all unfulfilled and partially fulfilled line items for the order will be fulfilled. However, if an order is refunded or if any of its individual line items are refunded, then the order can't be fulfilled.</p> <br/> <p>All line items being fulfilled must have the same fulfillment service.</p> <br/> <aside class="note"> <h4>Note</h4> <p>If you are using this endpoint with a Partner development store or a trial store, then you can create no more than 5 new fulfillments per minute.</p> </aside> <h3>About tracking urls</h3> <p>If you're creating a fulfillment for a supported carrier, then you can send the <code>tracking_company</code> and <code>tracking_numbers</code> fields, and Shopify will generate the <code>tracking_url</code> for you. If you're creating a fulfillment for an unsupported carrier (not in the <code>tracking_company</code> list), then send the <code>tracking_company</code>, <code>tracking_numbers</code>, and <code>tracking_urls</code> fields.</p> <br/> <aside class="note"> <h4>Note</h4> <p>If you send an unsupported carrier without a tracking URL, then Shopify will still try to generate a valid tracking URL by using pattern matching on the tracking number.</p> </aside> |
| `retrieves_fulfillments_associated_with_afulfillment_order` | Retrieves fulfillments associated with a fulfillment order. Retrieves fulfillments associated with a fulfillment order. |
| `retrieves_acount_of_fulfillments_associated_with_aspecific_order` | Retrieves a count of fulfillments associated with a specific order |
| `receive_asingle_fulfillment` | Receive a single Fulfillment. Retrieve a specific fulfillment |
| `modify_an_existing_fulfillment` | Modify an existing Fulfillment. Update information associated with a fulfillment |
| `creates_afulfillment_for_one_or_many_fulfillment_orders` | Creates a fulfillment for one or many fulfillment orders. Creates a fulfillment for one or many fulfillment orders. The fulfillment orders are associated with the same order and are assigned to the same location. |
| `updates_the_tracking_information_for_afulfillment` | Updates the tracking information for a fulfillment. Updates the tracking information for a fulfillment. |
| `complete_afulfillment` | Complete a fulfillment. Mark a fulfillment as complete |
| `transition_afulfillment_from_pending_to_open` | Transition a fulfillment from pending to open.. Mark a fulfillment as open |
| `cancel_afulfillment_for_aspecific_order_id` | Cancel a fulfillment for a specific order ID. Cancel a fulfillment for a specific order ID |
| `cancels_afulfillment` | Cancels a fulfillment. Cancels a fulfillment. |
| `retrieves_alist_of_fulfillment_events_for_aspecific_fulfillment` | Retrieves a list of fulfillment events for a specific fulfillment. Retrieves a list of fulfillment events for a specific fulfillment |
| `creates_afulfillment_event` | Creates a fulfillment event. Creates a fulfillment event |
| `retrieves_aspecific_fulfillment_event` | Retrieves a specific fulfillment event. Retrieves a specific fulfillment event |
| `deletes_afulfillment_event` | Deletes a fulfillment event. Deletes a fulfillment event |
| `retrieves_alist_of_fulfillment_orders_for_aspecific_order` | Retrieves a list of fulfillment orders for a specific order. Retrieves a list of fulfillment orders for a specific order. |
| `retrieves_aspecific_fulfillment_order` | Retrieves a specific fulfillment order. Retrieves a specific fulfillment order. |
| `cancel_afulfillment_order` | Cancel a fulfillment order. Marks a fulfillment order as cancelled. |
| `marks_afulfillment_order_as_incomplete` | Marks a fulfillment order as incomplete. Marks an in progress fulfillment order as incomplete, indicating the fulfillment service is unable to ship any remaining items and intends to close the fulfillment order. |
| `moves_afulfillment_order_to_anew_location` | Moves a fulfillment order to a new location. Moves a fulfillment order from one merchant managed location to another merchant managed location. |
| `sends_afulfillment_request` | Sends a fulfillment request. Sends a fulfillment request to the fulfillment service of a fulfillment order. |
| `accepts_afulfillment_request` | Accepts a fulfillment request. Accepts a fulfillment request sent to a fulfillment service for a fulfillment order. |
| `rejects_afulfillment_request` | Rejects a fulfillment request. Rejects a fulfillment request sent to a fulfillment service for a fulfillment order. |
| `receive_alist_of_all_fulfillmentservices` | Receive a list of all FulfillmentServices. Receive a list of all FulfillmentServices |
| `create_anew_fulfillmentservice` | Create a new FulfillmentService. <p>To create a fulfillment service, you can also use a cURL request that uses that <code>fulfillment_service.json</code> payload:</p> curl -X POST -d @fulfillment_service.json -H"Accept:application/json" -H"Content-Type:application/json" -H"X-Shopify-Access-Token:THE_TOKEN_GOES_HERE" https://AUTHORIZED_SHOP.myshopify.com/admin/fulfillment_services <p>Where <code>THE_TOKEN_GOES_HERE</code> is replaced by the OAuth token given to you by Shopify and <code>https://AUTHORIZED_SHOP.myshopify.com/admin/fulfillment_services</code> is replaced by the authorized shop's URL.</p> |
| `receive_asingle_fulfillmentservice` | Receive a single FulfillmentService. Receive a single FulfillmentService |
| `modify_an_existing_fulfillmentservice` | Modify an existing FulfillmentService. Modify an existing FulfillmentService |
| `remove_an_existing_fulfillmentservice` | Remove an existing FulfillmentService. Remove an existing FulfillmentService |
| `retrieves_alist_of_locations_that_afulfillment_order_can_potentially_move_to` | Retrieves a list of locations that a fulfillment order can potentially move to.. Retrieves a list of locations that a fulfillment order can potentially move to. The resulting list is sorted alphabetically in ascending order by location name. |
| `return_the_current_balance` | Return the current balance. Retrieves the account's current balance. |
| `return_alist_of_all_disputes` | Return a list of all disputes. Retrieve all disputes ordered by <code>initiated_at</code> date and time (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format), with the most recent being first. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `return_asingle_dispute` | Return a single dispute. Retrieves a single dispute by ID. |
| `return_alist_of_all_payouts` | Return a list of all payouts. Retrieves a list of all payouts ordered by payout date, with the most recent being first. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `return_asingle_payout` | Return a single payout. Retrieves a single payout by id. |
| `return_alist_of_all_balance_transactions` | Return a list of all balance transactions. Retrieves a list of all balance transactions ordered by processing time, with the most recent being first. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. Sending the <code>page</code> parameter will return an error. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |
| `receive_alist_of_all_countries` | Receive a list of all Countries. Retrieves a list of countries. |
| `creates_acountry` | Creates a country. Creates a country. |
| `retrieves_acount_of_countries` | Retrieves a count of countries. Retrieves a count of countries. |
| `retrieves_aspecific_county` | Retrieves a specific county. Retrieves a specific county. |
| `updates_an_existing_country` | Updates an existing country. Updates an existing country. |
| `remove_an_existing_country` | Remove an existing Country. Deletes a country. |
| `retrieves_alist_of_currencies_enabled_on_ashop` | Retrieves a list of currencies enabled on a shop. Retrieves a list of currencies enabled on a shop |
| `retrieves_alist_of_the_shop_spolicies` | Retrieves a list of the shop's policies. Retrieves a list of the shop's policies |
| `retrieves_alist_of_provinces_for_acountry` | Retrieves a list of provinces for a country. Retrieves a list of provinces |
| `retrieves_acount_of_provinces_for_acountry` | Retrieves a count of provinces for a country. Retrieves a count of provinces for a country |
| `retrieves_asingle_province_for_acountry` | Retrieves a single province for a country. Retrieves a single province for a country |
| `updates_an_existing_province_for_acountry` | Updates an existing province for a country. Updates an existing province for a country |
| `retrieves_the_shop_sconfiguration` | Retrieves the shop's configuration. Retrieves the shop's configuration |
| `retrieves_alist_of_tender_transactions` | Retrieves a list of tender transactions. Retrieves a list of tender transactions. <strong>Note:</strong> As of version 2019-10, this endpoint implements pagination by using links that are provided in the response header. To learn more, see <a href="https://help.shopify.com/api/guides/paginated-rest-results"><em>Making requests to paginated REST Admin API endpoints</em></a>. |


## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal mcp shopify/
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